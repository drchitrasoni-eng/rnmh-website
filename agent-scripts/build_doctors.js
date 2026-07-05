const fs = require('fs');
const path = require('path');
const ejs = require('ejs');

const dirs = [
    {
        content: path.join(__dirname, '../content/doctors'),
        template: path.join(__dirname, '../templates/doctor.ejs'),
        output: path.join(__dirname, '../doctors'),
        prefix: 'https://rnmh.in/doctors/'
    },
    {
        content: path.join(__dirname, '../content/doctors-hi'),
        template: path.join(__dirname, '../templates/doctor-hi.ejs'),
        output: path.join(__dirname, '../hi/doctors'),
        prefix: 'https://rnmh.in/hi/doctors/'
    }
];

const sitemapPath = path.join(__dirname, '../sitemap.xml');
const sitemapUrls = [];

dirs.forEach(dirObj => {
    if (!fs.existsSync(dirObj.content)) return;
    
    if (!fs.existsSync(dirObj.output)) {
        fs.mkdirSync(dirObj.output, { recursive: true });
    }

    const templateStr = fs.readFileSync(dirObj.template, 'utf-8');

    fs.readdirSync(dirObj.content).forEach(file => {
        if (file.endsWith('.json')) {
            const filePath = path.join(dirObj.content, file);
            const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
            
            // 1. Generate Schema
            const schema = {
                "@context": "https://schema.org",
                "@graph": [
                    {
                        "@type": ["Physician", "Person"],
                        "@id": `${dirObj.prefix}${data.id}.html#physician`,
                        "name": data.hero.name,
                        "jobTitle": data.hero.title,
                        "image": `https://rnmh.in/${data.hero.image.replace('../', '')}`,
                        "description": data.biography,
                        "medicalSpecialty": {
                            "@type": "MedicalSpecialty",
                            "name": data.hero.specialty || data.areasOfExpertise[0]
                        },
                        "worksFor": {
                            "@type": "Hospital",
                            "@id": "https://rnmh.in/#hospital",
                            "name": "R N Multispeciality Hospital"
                        },
                        "knowsLanguage": data.languages || ["English", "Hindi"],
                        "sameAs": data.sameAs || []
                    }
                ]
            };

            if (data.faqs && data.faqs.length > 0) {
                schema["@graph"].push({
                    "@type": "FAQPage",
                    "mainEntity": data.faqs.map(faq => ({
                        "@type": "Question",
                        "name": faq.question,
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": faq.answer
                        }
                    }))
                });
            }
            
            if (data.reviews && data.reviews.rating) {
                schema["@graph"][0]["aggregateRating"] = {
                    "@type": "AggregateRating",
                    "ratingValue": data.reviews.rating,
                    "reviewCount": data.reviews.count
                };
            }

            data.schemaJson = JSON.stringify(schema, null, 2);

            // 2. Render HTML
            const html = ejs.render(templateStr, data);
            
            const finalHtml = html.replace('</body>', `\n<script type="application/ld+json">\n${data.schemaJson}\n</script>\n</body>`);

            // 3. Write HTML
            const outPath = path.join(dirObj.output, `${data.id}.html`);
            fs.writeFileSync(outPath, finalHtml);
            console.log(`Generated: ${outPath}`);
            
            sitemapUrls.push(`  <url>\n    <loc>${dirObj.prefix}${data.id}.html</loc>\n    <changefreq>monthly</changefreq>\n  </url>`);
        }
    });
});

// Update sitemap.xml
if (fs.existsSync(sitemapPath) && sitemapUrls.length > 0) {
    let sitemapStr = fs.readFileSync(sitemapPath, 'utf-8');
    const insertIndex = sitemapStr.lastIndexOf('</urlset>');
    if (insertIndex !== -1 && !sitemapStr.includes(sitemapUrls[0].match(/<loc>(.*?)<\/loc>/)[1])) {
        const newSitemapStr = sitemapStr.slice(0, insertIndex) + sitemapUrls.join('\n') + '\n' + sitemapStr.slice(insertIndex);
        fs.writeFileSync(sitemapPath, newSitemapStr);
        console.log("Updated sitemap.xml");
    }
}
