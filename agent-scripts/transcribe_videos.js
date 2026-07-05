const fs = require('fs');
const path = require('path');
const { YoutubeTranscript } = require('youtube-transcript');

// Example script to transcribe YouTube videos and append to HTML
// Usage: node transcribe_videos.js

const HTML_FILE = path.join(__dirname, '../doctors.html');

// Example video URLs to transcribe
const VIDEO_URLS = [
    { url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', doctorId: 'chitra-soni' } // Mock example
];

async function transcribeAndInject() {
    try {
        let htmlContent = fs.readFileSync(HTML_FILE, 'utf-8');

        for (const video of VIDEO_URLS) {
            console.log(`Fetching transcript for ${video.url}...`);
            try {
                const transcript = await YoutubeTranscript.fetchTranscript(video.url);
                
                // Combine the text of the transcript
                const fullText = transcript.map(t => t.text).join(' ');
                
                // Truncate or extract key insights (mock logic here)
                const insights = `<strong>Video Transcript Extract:</strong> ${fullText.substring(0, 500)}...`;
                
                // Inject into the HTML right after the doctor's description
                const regex = new RegExp(`(<div class="doc" id="${video.doctorId}">.*?<p>.*?</p>)`, 's');
                if (regex.test(htmlContent)) {
                    htmlContent = htmlContent.replace(regex, `$1\n    <div class="video-transcript" style="font-size: 0.85em; color: var(--muted); margin-top: 10px;">${insights}</div>`);
                    console.log(`Successfully injected transcript for ${video.doctorId}`);
                } else {
                    console.log(`Doctor ID ${video.doctorId} not found in HTML.`);
                }
            } catch (err) {
                console.error(`Error fetching transcript for ${video.url}:`, err.message);
            }
        }

        fs.writeFileSync(HTML_FILE, htmlContent, 'utf-8');
        console.log('Finished updating HTML.');

    } catch (e) {
        console.error("Error processing files:", e);
    }
}

transcribeAndInject();
