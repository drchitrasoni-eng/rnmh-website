import os
import re

extra_links_en = [
    '<a href="{prefix}treatments/orthopedic-doctor-nirman-nagar-jaipur.html">Orthopedic Doctor Nirman Nagar</a>',
    '<a href="{prefix}treatments/knee-replacement-surgeon-kings-road-jaipur.html">Knee Replacement Kings Road</a>',
    '<a href="{prefix}treatments/urologist-nirman-nagar-jaipur.html">Urologist Nirman Nagar</a>',
    '<a href="{prefix}treatments/neurosurgeon-nirman-nagar-jaipur.html">Neurosurgeon Nirman Nagar</a>',
    '<a href="{prefix}treatments/ent-specialist-kings-road-jaipur.html">ENT Specialist Kings Road</a>',
    '<a href="{prefix}treatments/general-physician-nirman-nagar-jaipur.html">General Physician Nirman Nagar</a>',
    '<a href="{prefix}treatments/pathology-lab-nirman-nagar-jaipur.html">Pathology Lab Nirman Nagar</a>',
]

extra_links_hi = [
    '<a href="{prefix}hi/treatments/orthopedic-doctor-nirman-nagar-jaipur.html">निर्माण नगर ऑर्थोपेडिक डॉक्टर</a>',
    '<a href="{prefix}hi/treatments/knee-replacement-surgeon-kings-road-jaipur.html">किंग्स रोड नी रिप्लेसमेंट सर्जन</a>',
    '<a href="{prefix}hi/treatments/urologist-nirman-nagar-jaipur.html">निर्माण नगर यूरोलॉजिस्ट</a>',
    '<a href="{prefix}hi/treatments/neurosurgeon-nirman-nagar-jaipur.html">निर्माण नगर न्यूरोसर्जन</a>',
    '<a href="{prefix}hi/treatments/ent-specialist-kings-road-jaipur.html">किंग्स रोड ईएनटी विशेषज्ञ</a>',
    '<a href="{prefix}hi/treatments/general-physician-nirman-nagar-jaipur.html">निर्माण नगर जनरल फिजिशियन</a>',
    '<a href="{prefix}hi/treatments/pathology-lab-nirman-nagar-jaipur.html">निर्माण नगर पैथोलॉजी लैब</a>',
]

def update_html_files(base_dir):
    for root, _, files in os.walk(base_dir):
        if "node_modules" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                
                depth = filepath.replace(base_dir, "").count(os.sep) - 1
                prefix = ""
                if depth == 1:
                    prefix = "../"
                elif depth == 2:
                    prefix = "../../"
                
                is_hi = "/hi/" in filepath or filepath.endswith("/hi/index.html")
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Find the footer link block
                if is_hi:
                    en_prefix = prefix.replace("../../hi/", "../../").replace("../hi/", "../") if "/hi/" in prefix else prefix
                    # We just need the prefix, but in hindi links it's {prefix}treatments because I removed hi/ in add_footer_links
                    # Actually let's just append to the existing string.
                    # In hindi:
                    extra = " &middot; " + " &middot; ".join([l.format(prefix=prefix) for l in extra_links_hi]).replace(f"{prefix}hi/treatments", f"{prefix}treatments")
                else:
                    extra = " &middot; " + " &middot; ".join([l.format(prefix=prefix) for l in extra_links_en])

                # Use regex to append to the existing paragraph
                # <p style="font-size: 13px; line-height:1.6; color: rgba(255,255,255,0.7);">(.*?)<\/p>
                # But wait, there might be other paragraphs. We look for the one after <h4 style="margin-bottom:8px; font-size:14px;">(Local Searches:|स्थानीय खोज:)</h4>
                
                def replacer(match):
                    return match.group(1) + match.group(2) + extra + "</p>"

                pattern = re.compile(r'(<h4 style="margin-bottom:8px; font-size:14px;">(?:Local Searches:|स्थानीय खोज:)</h4>\s*<p style="font-size: 13px; line-height:1.6; color: rgba\(255,255,255,0.7\);">)(.*?)</p>', re.DOTALL)
                
                new_content = pattern.sub(replacer, content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)

update_html_files("site")
print("Footer SEO links appended to all pages.")
