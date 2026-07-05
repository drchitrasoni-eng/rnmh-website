const fs = require('fs');
const path = require('path');
const https = require('https');

// Example script to fetch reviews from Google Places API and update the HTML schema
// Usage: PLACES_API_KEY=your_key node fetch_reviews.js

const PLACES_API_KEY = process.env.PLACES_API_KEY || null;
const PLACE_ID = 'ChIJYOdglaixabkR_5G5mwsbq_M'; // Example place ID
const HTML_FILE = path.join(__dirname, '../index.html');

async function fetchGoogleReviews() {
    return new Promise((resolve, reject) => {
        if (!PLACES_API_KEY) {
            console.log("No PLACES_API_KEY provided. Keeping static text for now.");
            return resolve(null);
        }

        const url = `https://maps.googleapis.com/maps/api/place/details/json?place_id=${PLACE_ID}&fields=rating,user_ratings_total,reviews&key=${PLACES_API_KEY}`;
        
        https.get(url, (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => {
                try {
                    const result = JSON.parse(data);
                    if (result.result) {
                        resolve(result.result);
                    } else {
                        reject(new Error("No result found in API response."));
                    }
                } catch (e) {
                    reject(e);
                }
            });
        }).on('error', (err) => {
            reject(err);
        });
    });
}

async function updateReviews() {
    try {
        const placeData = await fetchGoogleReviews();
        
        if (placeData && placeData.rating && placeData.user_ratings_total) {
            console.log(`Fetched new ratings: ${placeData.rating} from ${placeData.user_ratings_total} reviews.`);
            
            let htmlContent = fs.readFileSync(HTML_FILE, 'utf-8');
            
            // Build the AggregateRating schema
            const aggregateRatingSchema = {
                "@context": "https://schema.org",
                "@type": "MedicalClinic",
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": placeData.rating,
                    "reviewCount": placeData.user_ratings_total
                }
            };
            
            const schemaScript = `\n<script type="application/ld+json">\n${JSON.stringify(aggregateRatingSchema, null, 2)}\n</script>\n`;
            
            // Inject schema before </body>
            htmlContent = htmlContent.replace(/<\/body>/, `${schemaScript}</body>`);
            
            fs.writeFileSync(HTML_FILE, htmlContent, 'utf-8');
            console.log("HTML updated successfully with dynamic reviews schema.");
        }
    } catch (error) {
        console.error("Error fetching or updating reviews:", error);
    }
}

updateReviews();
