import os
import re

SITE_DIR = "/Users/jay/Documents/Claude/Projects/RNMH/site"

def update_footer(filepath, is_hindi=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if is_hindi:
        new_footer_col = """    <div>
      <a class="brand" href="index.html" style="color:#fff"><img src="../assets/img/logo.png" alt="R N Multispeciality Hospital logo" style="height:40px;background:#fff;border-radius:8px;padding:3px"><span style="color:#fff">R N Multispeciality Hospital</span></a>
      <p style="margin-top:12px">मेन किंग्स रोड, निर्माण नगर, जयपुर में 50-बेड मल्टीस्पेशलिटी हॉस्पिटल</p>
      <p><b>पता:</b><br>109-110, शिव शक्ति नगर, मेन किंग्स रोड, निर्माण नगर, जयपुर, राजस्थान 302019</p>
      <p><b>लैंडमार्क:</b><br>मानसरोवर मेट्रो स्टेशन के पास</p>
      <p><b>फोन:</b> <a href="tel:+911412390320" class="js-phone-link"><span class="js-phone-display">0141 239 0320</span></a></p>
      <p><b>उपलब्धता:</b><br>24x7 इमरजेंसी केयर</p>
      <p><b>सेवा क्षेत्र:</b><br>निर्माण नगर, मानसरोवर, किंग्स रोड, श्याम नगर, बृजलालपुरा, गोपालपुरा बाइपास और आसपास के जयपुर क्षेत्र</p>
    </div>"""
    else:
        # Check if assets is ../assets or assets
        assets_path = "assets" if not filepath.startswith(os.path.join(SITE_DIR, "treatments")) else "../assets"
        
        new_footer_col = f"""    <div>
      <a class="brand" href="index.html" style="color:#fff"><img src="{assets_path}/img/logo.png" alt="R N Multispeciality Hospital logo" style="height:40px;background:#fff;border-radius:8px;padding:3px"><span style="color:#fff">R N Multispeciality Hospital</span></a>
      <p style="margin-top:12px">50-bed multispeciality hospital on Main Kings Road, Nirman Nagar, Jaipur</p>
      <p><b>Address:</b><br>109-110, Shiv Shakti Nagar, Main Kings Road, Nirman Nagar, Jaipur, Rajasthan 302019</p>
      <p><b>Landmark:</b><br>Near Mansarovar Metro Station</p>
      <p><b>Phone:</b> <a href="tel:+911412390320" class="js-phone-link"><span class="js-phone-display">0141 239 0320</span></a></p>
      <p><b>Open:</b><br>24x7 emergency care</p>
      <p><b>Serving:</b><br>Nirman Nagar, Mansarovar, Kings Road, Shyam Nagar, Brijlalpura, Gopalpura Bypass and nearby Jaipur areas</p>
    </div>"""
    
    # Replace the first column of the footer
    # Using regex to find the first div inside .footer-grid
    pattern = re.compile(r'(<div class="grid footer-grid">\s*<div>\s*<a class="brand".*?</div>)', re.DOTALL)
    
    # Wait, the logo src might be different in hindi (../assets)
    # Let's adjust the regex to match up to the end of the first div
    
    match = pattern.search(content)
    if match:
        content = content[:match.start(1)] + '<div class="grid footer-grid">\n' + new_footer_col + content[match.end(1):]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for root, _, files in os.walk(SITE_DIR):
    for f in files:
        if f.endswith('.html') and 'node_modules' not in root:
            filepath = os.path.join(root, f)
            is_hindi = '/hi/' in filepath or filepath.endswith('/hi/index.html')
            update_footer(filepath, is_hindi)

print("Footer updated on all files.")
