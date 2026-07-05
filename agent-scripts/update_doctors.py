import json
import re
import os

physicians = [
    {"id": "dr-robin-bothra", "name": "Dr Robin Bothra", "spec": ["General Surgery", "Laparoscopic Surgery"], "slug": "robin-bothra"},
    {"id": "dr-chitra-soni", "name": "Dr Chitra Soni", "spec": ["Obstetrics", "Gynaecology", "Fertility"], "slug": "chitra-soni"},
    {"id": "dr-naveen-soni", "name": "Dr Naveen Soni", "spec": ["Pain Management", "Spine Care"], "slug": "naveen-soni"},
    {"id": "dr-chirag-jain", "name": "Dr Chirag Jain", "spec": ["Orthopaedics", "Joint Replacement"], "slug": "chirag-jain"},
    {"id": "dr-rn-daga", "name": "Dr R N Daga", "spec": ["Urology", "Andrology"], "slug": "rn-daga"},
    {"id": "dr-pavan-jain", "name": "Dr Pavan Jain", "spec": ["Neurosurgery", "Spine Surgery"], "slug": "pavan-jain"},
    {"id": "dr-ns-rathore", "name": "Dr N S Rathore", "spec": ["ENT", "Otolaryngology"], "slug": "ns-rathore"},
    {"id": "dr-vishnu-gupta", "name": "Dr Vishnu Gupta", "spec": ["General Medicine", "Internal Medicine"], "slug": "vishnu-gupta"},
    {"id": "dr-vinita-jain", "name": "Dr Vinita Jain", "spec": ["Pathology", "Diagnostics"], "slug": "vinita-jain"}
]

schema_array = []
for p in physicians:
    schema_array.append({
        "@context": "https://schema.org",
        "@type": "Physician",
        "@id": f"https://rnmh.in/doctors.html#{p['id']}",
        "name": p["name"],
        "medicalSpecialty": p["spec"],
        "worksFor": {"@id": "https://rnmh.in/#hospital"},
        "hospitalAffiliation": {"@id": "https://rnmh.in/#hospital"},
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "109-110, Shiv Shakti Nagar, Main Kings Road, Nirman Nagar",
            "addressLocality": "Jaipur",
            "addressRegion": "Rajasthan",
            "postalCode": "302019",
            "addressCountry": "IN"
        },
        "areaServed": [
            "Nirman Nagar",
            "Kings Road",
            "Mansarovar Metro Station",
            "Mansarovar",
            "Shyam Nagar",
            "Jaipur"
        ],
        "url": f"https://rnmh.in/doctors.html#{p['slug']}"
    })

new_schema_str = '<script type="application/ld+json">\n' + json.dumps(schema_array, indent=2) + '\n</script>'

def update_html(filepath, is_hindi):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Replace Physician schema
    html = re.sub(
        r'<script type="application/ld\+json">\s*\[\s*{\s*"@context":\s*"https://schema\.org",\s*"@type":\s*"Physician".*?</script>',
        new_schema_str,
        html,
        flags=re.DOTALL
    )

    # 2. Add Locality paragraph to doctor cards
    for p in physicians:
        name = p['name']
        if is_hindi:
            phrase = f'<p class="doc-locality-support" style="font-weight: 500; margin-top: 12px; margin-bottom: 12px;">{name} से R N Multispeciality Hospital, मेन किंग्स रोड, निर्माण नगर, जयपुर में कंसल्ट करें, मानसरोवर मेट्रो स्टेशन के पास।</p>'
        else:
            phrase = f'<p class="doc-locality-support" style="font-weight: 500; margin-top: 12px; margin-bottom: 12px;">Consult {name} at R N Multispeciality Hospital, Main Kings Road, Nirman Nagar, Jaipur, near Mansarovar Metro Station.</p>'

        # We look for the button for this specific doctor and insert the phrase right before it
        # The button looks like: <button class="btn btn-teal js-wa" data-doc="Dr Robin Bothra"...
        # We need to make sure we don't insert it twice.
        
        button_pattern = re.compile(rf'(<button class="btn btn-teal js-wa" data-doc="{name}")')
        if "doc-locality-support" not in html or name not in html: # just basic check
            # wait, the name IS in html. We check if the phrase is already inserted
            if phrase not in html:
                html = button_pattern.sub(phrase + r'\n    \1', html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

update_html('site/doctors.html', False)
if os.path.exists('site/hi/doctors.html'):
    update_html('site/hi/doctors.html', True)
print("Doctors updated.")
