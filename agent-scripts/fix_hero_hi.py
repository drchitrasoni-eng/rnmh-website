import re

with open('site/hi/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace H1
html = html.replace('<h1>किंग्स रोड, निर्माण नगर, जयपुर में भरोसेमंद मल्टीस्पेशलिटी केयर</h1>', '<h1>निर्माण नगर, जयपुर में विश्वसनीय मल्टीस्पेशलिटी केयर</h1>')

# Replace lead text
html = html.replace('<p class="lead">आर एन मल्टीस्पेशलिटी हॉस्पिटल 109-110, शिव शक्ति नगर, मेन किंग्स रोड, निर्माण नगर, जयपुर में स्थित 50-बेड मल्टीस्पेशलिटी हॉस्पिटल है, मानसरोवर मेट्रो स्टेशन के पास। यहाँ 24x7 इमरजेंसी केयर, विशेषज्ञ डॉक्टरों की सलाह, सर्जिकल सेवाएँ, डायग्नोस्टिक्स और कैशलेस इंश्योरेंस सहायता एक ही जगह उपलब्ध है。</p>', '<p class="lead">R N Multispeciality Hospital निर्माण नगर, जयपुर में एक 50-बेड मल्टीस्पेशलिटी हॉस्पिटल है। हम 24x7 इमरजेंसी केयर, विशेषज्ञ कंसल्टेशन, सर्जरी, डायग्नोस्टिक्स और कैशलेस इंश्योरेंस सहायता एक ही छत के नीचे प्रदान करते हैं।</p>')

# Remove extra paragraphs
html = re.sub(r'<p class="hero-locality-support".*?</p>\s*', '', html, flags=re.DOTALL)
html = re.sub(r'<p class="hero-specialties-text".*?</p>\s*', '', html, flags=re.DOTALL)

with open('site/hi/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Hindi hero section fixed.")
