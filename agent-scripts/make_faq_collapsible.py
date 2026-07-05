import re
import os

css_addition = """

/* FAQ Accordion */
details.faq-card {
    background: #fff;
    border: 1px solid var(--line);
    border-radius: var(--r-out);
    margin-bottom: 16px;
    padding: 16px 20px;
    transition: all 0.2s ease;
}
details.faq-card[open] {
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
details.faq-card summary {
    font-family: 'Bricolage Grotesque', sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: var(--ink);
    cursor: pointer;
    list-style: none; /* remove default arrow */
    position: relative;
    padding-right: 24px;
}
details.faq-card summary::-webkit-details-marker {
    display: none;
}
details.faq-card summary::after {
    content: "+";
    position: absolute;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
    font-size: 24px;
    font-weight: 400;
    color: var(--primary);
    transition: transform 0.2s;
}
details.faq-card[open] summary::after {
    content: "\\2212"; /* minus sign */
}
details.faq-card .desc {
    margin-top: 12px;
    color: var(--ink-soft);
    line-height: 1.6;
}
"""

with open('site/assets/css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_addition)

def convert_faqs(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Regex to find the FAQ section grid
    # It looks like: <div class="grid-3" style="margin-top:32px;"> ... </div>
    # But wait, there might be other grid-3s. We know it's right after <h2>Patient questions answered</h2> or "अक्सर पूछे जाने वाले सवाल"
    
    # We replace the cards one by one
    def replacer(match):
        q = match.group(1)
        a = match.group(2)
        return f'<details class="faq-card"><summary>{q}</summary><p class="desc">{a}</p></details>'

    # find <div class="card"><div class="card-core"><h3>Question</h3><p class="desc" style="margin-top:10px;">Answer</p></div></div>
    pattern = re.compile(r'<div class="card">\s*<div class="card-core">\s*<h3.*?>(.*?)</h3>\s*<p class="desc".*?>(.*?)</p>\s*</div>\s*</div>', re.DOTALL)
    html = pattern.sub(replacer, html)

    # Change grid-3 to a single column wrapper for FAQs
    # Only the one right after the FAQ header
    faq_grid_pattern = re.compile(r'(<div class="sec-head">.*?<h2>.*?</h2>.*?</div>)\s*<div class="grid-3".*?>', re.DOTALL)
    html = faq_grid_pattern.sub(r'\1\n  <div style="max-width:800px; margin: 32px auto 0;">', html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

convert_faqs('site/index.html')
convert_faqs('site/hi/index.html')

print("FAQs made collapsible.")
