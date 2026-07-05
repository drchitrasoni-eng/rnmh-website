const fs = require('fs');
const path = require('path');
const ejs = require('ejs');

const contentDir = path.join(__dirname, '../content/doctors');
const templatePath = path.join(__dirname, '../templates/doctor.ejs');
const outputDir = path.join(__dirname, '../doctors');
const sitemapPath = path.join(__dirname, '../sitemap.xml');

// Ensure output directory exists
if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

const templateStr = fs.readFileSync(templatePath, 'utf-8');

const sitemapUrls = [];

fs.readdirSync(contentDir).forEach(file => {
    if (file.endsWith('.json')) {
        const filePath = path.join(contentDir, file);
        const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
        
        // 1. Generate Schema
        const schema = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": ["Physician", "Person"],
                    "@id": `https://rnmh.in/doctors/${data.id}.html#physician`,
                    "name": data.hero.name,
                    "jobTitle": data.hero.title,
                    "image": `https://rnmh.in/${data.hero.image.replace('../', '')}`,
                    "description": data.biography,
                    "medicalSpecialty": {
                        "@type": "MedicalSpecialty",
                        "name": data.hero.specialty
                    },
                    "worksFor": {
                        "@type": "Hospital",
                        "@id": "https://rnmh.in/#hospital",
                        "name": "R N Multispeciality Hospital"
                    },
                    "knowsLanguage": data.languages,
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

        // Add schema string to data
        data.schemaJson = JSON.stringify(schema, null, 2);

        // 2. Render HTML
        const html = ejs.render(templateStr, data);
        
        // Inject schema before closing body
        const finalHtml = html.replace('</body>', `\n<script type="application/ld+json">\n${data.schemaJson}\n</script>\n</body>`);

        // 3. Write HTML
        const outPath = path.join(outputDir, `${data.id}.html`);
        fs.writeFileSync(outPath, finalHtml);
        console.log(`Generated: ${outPath}`);
        
        // Prepare sitemap URL
        sitemapUrls.push(`  <url>\n    <loc>https://rnmh.in/doctors/${data.id}.html</loc>\n    <changefreq>monthly</changefreq>\n  </url>`);
    }
});

// Update sitemap.xml
if (fs.existsSync(sitemapPath) && sitemapUrls.length > 0) {
    let sitemapStr = fs.readFileSync(sitemapPath, 'utf-8');
    const insertIndex = sitemapStr.lastIndexOf('</urlset>');
    if (insertIndex !== -1 && !sitemapStr.includes(`https://rnmh.in/doctors/${sitemapUrls[0].match(/<loc>(.*?)<\/loc>/)[1].split('/').pop()}`)) {
        const newSitemapStr = sitemapStr.slice(0, insertIndex) + sitemapUrls.join('\n') + '\n' + sitemapStr.slice(insertIndex);
        fs.writeFileSync(sitemapPath, newSitemapStr);
        console.log("Updated sitemap.xml");
    }
}
