import json
import os

faq_en = [
    {
        "q": "Is R N Multispeciality Hospital open 24x7?",
        "a": "Yes, we are open 24x7, 365 days a year with an active emergency department, ICU, and round-the-clock ambulance services."
    },
    {
        "q": "Are government schemes like PM-JAY and RGHS accepted?",
        "a": "Yes, we are NABH accredited and accept cashless treatments under Ayushman Bharat (PM-JAY), RGHS, MAA Yojana, Chiranjeevi, and all major TPAs."
    },
    {
        "q": "How can I book an appointment with a specialist?",
        "a": "You can book an appointment instantly via WhatsApp by clicking any \"Book on WhatsApp\" button on our site, or by calling our reception directly at 0141 239 0320."
    }
]

faq_hi = [
    {
        "q": "क्या आर एन मल्टीस्पेशलिटी हॉस्पिटल 24x7 खुला रहता है?",
        "a": "हाँ, हम साल के 365 दिन, 24 घंटे खुले रहते हैं। हमारे पास एक सक्रिय इमरजेंसी विभाग, ICU और चौबीसों घंटे एम्बुलेंस सेवा उपलब्ध है।"
    },
    {
        "q": "क्या यहाँ PM-JAY और RGHS जैसी सरकारी योजनाएँ स्वीकार की जाती हैं?",
        "a": "हाँ, हम NABH मान्यता प्राप्त हैं और आयुष्मान भारत (PM-JAY), RGHS, MAA योजना, चिरंजीवी और सभी प्रमुख TPA के तहत कैशलेस इलाज की सुविधा देते हैं।"
    },
    {
        "q": "मैं किसी विशेषज्ञ डॉक्टर से अपॉइंटमेंट कैसे बुक कर सकता हूँ?",
        "a": "आप हमारी वेबसाइट पर किसी भी 'व्हाट्सएप पर बुक करें' बटन पर क्लिक करके तुरंत अपॉइंटमेंट बुक कर सकते हैं, या सीधे हमारे रिसेप्शन पर 0141 239 0320 पर कॉल कर सकते हैं।"
    }
]

def build_html_faq(faqs, title, is_hi):
    html = f'<!-- FAQ -->\n<section id="faq" style="background:var(--surface);"><div class="wrap">\n  <div class="sec-head"><span class="eyebrow">{"अक्सर पूछे जाने वाले प्रश्न" if is_hi else "Frequently Asked Questions"}</span><h2>{title}</h2></div>\n  <div class="grid-3" style="margin-top:32px;">\n'
    for f in faqs:
        html += f'    <div class="card"><div class="card-core"><h3>{f["q"]}</h3><p class="desc" style="margin-top:10px;">{f["a"]}</p></div></div>\n'
    html += '  </div>\n</div></section>\n\n'
    return html

def build_schema(faqs):
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": []
    }
    for f in faqs:
        schema["mainEntity"].append({
            "@type": "Question",
            "name": f["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": f["a"]
            }
        })
    return f'\n<script type="application/ld+json">\n{json.dumps(schema, ensure_ascii=False)}\n</script>\n'

for lang, filepath, faqs, title in [
    ('en', 'site/index.html', faq_en, "Patient questions answered"),
    ('hi', 'site/hi/index.html', faq_hi, "मरीज़ों के सवालों के जवाब")
]:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'id="faq"' not in content:
        # insert before <!-- REVIEWS --> or <section id="reviews">
        target = "<!-- REVIEWS -->"
        if target not in content:
            target = '<section id="reviews">'
        
        if target in content:
            content = content.replace(target, build_html_faq(faqs, title, lang=='hi') + target)
            
            # insert schema into head
            content = content.replace('</head>', build_schema(faqs) + '</head>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
