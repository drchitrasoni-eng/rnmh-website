import os
import glob
import re

# Mapping categories by keywords in filename
# Order matters (put more specific ones first if needed)
mapping = [
    (["laser-piles"], {
        "en": "Laser piles consultation and surgical care at R N Multispeciality Hospital, Nirman Nagar, near Mansarovar Metro Station.",
        "hi": "पाइल्स के लेजर इलाज की कंसल्टेशन और सर्जिकल केयर, R N Multispeciality Hospital, निर्माण नगर में, मानसरोवर मेट्रो स्टेशन के पास।"
    }),
    (["hernia-surgery"], {
        "en": "Hernia surgery consultation and care at R N Multispeciality Hospital, Main Kings Road, Nirman Nagar.",
        "hi": "हर्निया सर्जरी की कंसल्टेशन और इलाज, R N Multispeciality Hospital, मेन किंग्स रोड, निर्माण नगर में।"
    }),
    (["gall-bladder"], {
        "en": "Gall bladder stone surgery consultation and laparoscopic care at RNMH, Nirman Nagar, near Mansarovar Metro Station.",
        "hi": "पित्त की थैली की पथरी की सर्जरी और लैप्रोस्कोपिक केयर, RNMH निर्माण नगर में, मानसरोवर मेट्रो स्टेशन के पास।"
    }),
    (["appendix-surgery"], {
        "en": "Appendix surgery consultation and emergency surgical care at RNMH, Main Kings Road, Nirman Nagar.",
        "hi": "अपेंडिक्स सर्जरी की कंसल्टेशन और इमरजेंसी सर्जिकल केयर, RNMH मेन किंग्स रोड, निर्माण नगर में।"
    }),
    (["high-risk-pregnancy"], {
        "en": "High-risk pregnancy consultation and admission support at RNMH, near Mansarovar Metro Station.",
        "hi": "हाई-रिस्क प्रेगनेंसी कंसल्टेशन और एडमिशन सपोर्ट, RNMH में, मानसरोवर मेट्रो स्टेशन के पास।"
    }),
    (["pregnancy-care", "painless-delivery"], {
        "en": "Pregnancy care and delivery consultation with specialist doctors at RNMH, Nirman Nagar, Jaipur.",
        "hi": "प्रेगनेंसी केयर और डिलीवरी कंसल्टेशन, विशेषज्ञ डॉक्टरों के साथ RNMH निर्माण नगर, जयपुर में।"
    }),
    (["fertility"], {
        "en": "Fertility and women’s health consultation at RNMH, Main Kings Road, Nirman Nagar.",
        "hi": "फर्टिलिटी और महिला स्वास्थ्य कंसल्टेशन, RNMH मेन किंग्स रोड, निर्माण नगर में।"
    }),
    (["gynaecologist", "obgyn", "pcos"], {
        "en": "Consultation for PCOS, irregular periods and women’s health concerns at RNMH, Nirman Nagar.",
        "hi": "PCOS, अनियमित पीरियड्स और महिला स्वास्थ्य समस्याओं के लिए कंसल्टेशन, RNMH निर्माण नगर में।"
    }),
    (["back-pain"], {
        "en": "Back pain and spine consultation at RNMH, Nirman Nagar, near Mansarovar Metro Station.",
        "hi": "कमर दर्द और स्पाइन कंसल्टेशन, RNMH निर्माण नगर में, मानसरोवर मेट्रो स्टेशन के पास।"
    }),
    (["slip-disc"], {
        "en": "Slip disc consultation and pain management care at RNMH, Main Kings Road, Nirman Nagar.",
        "hi": "स्लिप डिस्क कंसल्टेशन और पेन मैनेजमेंट केयर, RNMH मेन किंग्स रोड, निर्माण नगर में।"
    }),
    (["sciatica"], {
        "en": "Sciatica pain consultation and spine care at RNMH, Nirman Nagar, Jaipur.",
        "hi": "सायटिका दर्द की कंसल्टेशन और स्पाइन केयर, RNMH निर्माण नगर, जयपुर में।"
    }),
    (["spine-specialist", "pain-management-doctor", "neurosurgeon"], {
        "en": "Slip disc consultation and pain management care at RNMH, Main Kings Road, Nirman Nagar.",
        "hi": "स्लिप डिस्क कंसल्टेशन और पेन मैनेजमेंट केयर, RNMH मेन किंग्स रोड, निर्माण नगर में।"
    }),
    (["kidney-stone"], {
        "en": "Kidney stone consultation and urology care at RNMH, near Mansarovar Metro Station.",
        "hi": "किडनी स्टोन कंसल्टेशन और यूरोलॉजी केयर, RNMH में, मानसरोवर मेट्रो स्टेशन के पास।"
    }),
    (["urologist"], {
        "en": "Urology consultation for kidney, urinary and prostate concerns at RNMH, Nirman Nagar.",
        "hi": "किडनी, यूरिनरी और प्रोस्टेट समस्याओं के लिए यूरोलॉजी कंसल्टेशन, RNMH निर्माण नगर में।"
    }),
    (["orthopaedic", "orthopedic", "fracture"], {
        "en": "Orthopaedic consultation for bone, joint and fracture care at RNMH, Main Kings Road, Nirman Nagar.",
        "hi": "हड्डी, जोड़ और फ्रैक्चर के इलाज के लिए ऑर्थोपेडिक कंसल्टेशन, RNMH मेन किंग्स रोड, निर्माण नगर में।"
    }),
    (["knee-pain", "knee-replacement"], {
        "en": "Knee pain consultation and orthopaedic care at RNMH, Nirman Nagar, Jaipur.",
        "hi": "घुटने के दर्द की कंसल्टेशन और ऑर्थोपेडिक केयर, RNMH निर्माण नगर, जयपुर में।"
    }),
    (["ent-specialist"], {
        "en": "ENT consultation for ear, nose and throat concerns at RNMH, near Mansarovar Metro Station.",
        "hi": "कान, नाक और गले की समस्याओं के लिए ENT कंसल्टेशन, RNMH में, मानसरोवर मेट्रो स्टेशन के पास।"
    }),
    (["general-physician", "general-medicine"], {
        "en": "General medicine consultation for fever, infections, diabetes and routine health concerns at RNMH, Nirman Nagar.",
        "hi": "बुखार, इंफेक्शन, डायबिटीज और सामान्य स्वास्थ्य समस्याओं के लिए जनरल मेडिसिन कंसल्टेशन, RNMH निर्माण नगर में।"
    }),
    (["pathology"], {
        "en": "Pathology tests and diagnostic support at RNMH, Main Kings Road, Nirman Nagar.",
        "hi": "पैथोलॉजी टेस्ट और डायग्नोस्टिक सपोर्ट, RNMH मेन किंग्स रोड, निर्माण नगर में।"
    }),
    (["emergency-hospital", "24x7-emergency", "multispeciality-hospital"], {
        "en": "24x7 emergency care at R N Multispeciality Hospital, Nirman Nagar, near Mansarovar Metro Station.",
        "hi": "24x7 इमरजेंसी केयर, R N Multispeciality Hospital निर्माण नगर में, मानसरोवर मेट्रो स्टेशन के पास।"
    }),
    (["cashless-hospital", "pm-jay", "maa-yojana", "rghs"], {
        "en": "Cashless insurance and TPA assistance available at RNMH, Main Kings Road, Nirman Nagar.",
        "hi": "कैशलेस इंश्योरेंस और TPA सहायता, RNMH मेन किंग्स रोड, निर्माण नगर में उपलब्ध।"
    }),
    (["laparoscopic-surgeon", "general-surgeon"], {
        "en": "Gall bladder stone surgery consultation and laparoscopic care at RNMH, Nirman Nagar, near Mansarovar Metro Station.",
        "hi": "पित्त की थैली की पथरी की सर्जरी और लैप्रोस्कोपिक केयर, RNMH निर्माण नगर में, मानसरोवर मेट्रो स्टेशन के पास।"
    })
]

def find_copy(filename, is_hi):
    for keywords, texts in mapping:
        for kw in keywords:
            if kw in filename:
                return texts["hi"] if is_hi else texts["en"]
    return None

def process_dir(directory, is_hi):
    for filepath in glob.glob(os.path.join(directory, "*.html")):
        filename = os.path.basename(filepath)
        new_copy = find_copy(filename, is_hi)
        if not new_copy:
            print(f"No match for {filename}")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        # We want to replace the first <p class="lead"> that comes after the <h1>
        # Using a regex that captures <h1>...</h1>\s*<p class="lead">...
        
        pattern = re.compile(r'(<h1>.*?</h1>\s*)<p class="lead">.*?</p>', re.DOTALL)
        
        if pattern.search(html):
            html = pattern.sub(r'\1<p class="lead">' + new_copy + '</p>', html, count=1)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
        else:
            print(f"Could not find h1 -> p.lead pattern in {filename}")

process_dir("site/treatments", False)
process_dir("site/hi/treatments", True)

print("Done updating treatment pages copy.")
