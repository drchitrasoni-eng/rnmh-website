import os
import re

en_specialities = "General and Laparoscopic Surgery, Obstetrics and Gynaecology, Pain Management and Spine, Orthopaedics, Urology, Neurosurgery, ENT, General Medicine, Pathology"
hi_specialities = "जनरल एवं लेप्रोस्कोपिक सर्जरी, स्त्री रोग एवं निःसंतानता, दर्द एवं रीढ़, हड्डी रोग, यूरोलॉजी, न्यूरोसर्जरी, ईएनटी, जनरल मेडिसिन, पैथोलॉजी"

def update_files():
    for root, dirs, files in os.walk('site'):
        if "node_modules" in root:
            continue
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                modified = False

                # Fix Metro Station
                if 'Mansarovar Metro' in content:
                    # Replace occurrences of "Mansarovar Metro Station" to a placeholder temporarily
                    # Or just do a regex replace
                    content = re.sub(r'Mansarovar Metro Station', 'MANSAROVAR_METRO_STATION_TEMP', content)
                    content = re.sub(r'Mansarovar Metro', 'Mansarovar Metro Station', content)
                    content = re.sub(r'MANSAROVAR_METRO_STATION_TEMP', 'Mansarovar Metro Station', content)
                    modified = True

                # Replace string in index.html and doctors.html for English
                if 'across pain and spine, gynaecology, surgery, orthopaedics, urology and more' in content:
                    content = content.replace('across pain and spine, gynaecology, surgery, orthopaedics, urology and more', 'across ' + en_specialities)
                    modified = True

                if "across surgery, women's health, pain and spine, orthopaedics, urology, neurosurgery, ENT, general medicine and pathology" in content:
                    content = content.replace("across surgery, women's health, pain and spine, orthopaedics, urology, neurosurgery, ENT, general medicine and pathology", 'across ' + en_specialities)
                    modified = True

                # Replace string in hi/index.html and hi/doctors.html for Hindi
                # hi/index.html lead paragraph translation of that list
                if 'दर्द एवं रीढ़, स्त्री रोग, सर्जरी, हड्डी रोग, यूरोलॉजी और अन्य विभागों में' in content:
                    content = content.replace('दर्द एवं रीढ़, स्त्री रोग, सर्जरी, हड्डी रोग, यूरोलॉजी और अन्य विभागों में', hi_specialities + ' और अन्य विभागों में')
                    modified = True

                if "सर्जरी, महिला स्वास्थ्य, दर्द और रीढ़, हड्डी रोग, यूरोलॉजी, न्यूरोसर्जरी, ईएनटी, सामान्य चिकित्सा और पैथोलॉजी" in content:
                    content = content.replace("सर्जरी, महिला स्वास्थ्य, दर्द और रीढ़, हड्डी रोग, यूरोलॉजी, न्यूरोसर्जरी, ईएनटी, सामान्य चिकित्सा और पैथोलॉजी", hi_specialities)
                    modified = True

                if modified:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)

    # Add .exp styling to css
    css_path = 'site/assets/css/style.css'
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            css = f.read()
        if '.exp{' not in css and '.exp {' not in css:
            css += '\n.exp{display:inline-block;padding:4px 8px;background:var(--teal-soft);border-radius:4px;font-weight:700;color:var(--teal-deep);margin:6px 0;font-size:0.9rem}\n'
            # Let's also reduce padding on doctors.html hero
            css += '.page-hero{padding:26px 0 !important;}\n' 
            with open(css_path, 'w', encoding='utf-8') as f:
                f.write(css)

if __name__ == '__main__':
    update_files()
    print("Content updated")
