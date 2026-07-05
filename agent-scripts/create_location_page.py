import os
import re

# 1. English Location Page
en_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Location | R N Multispeciality Hospital Jaipur</title>
<meta name="description" content="R N Multispeciality Hospital is located on Main Kings Road in Nirman Nagar, Jaipur, close to Mansarovar Metro Station.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css"><link rel="icon" href="assets/img/logo.png">
</head>
<body>

<div class="topbar"><div class="wrap">
  <span>Open 24x7 &middot; Near Mansarovar Metro Station, Nirman Nagar, Jaipur</span>
  <span>Call <a href="tel:+911412390320" class="js-phone-link"><span class="js-phone-display">0141 239 0320</span></a> &middot; <a href="#" class="js-wa">Book on WhatsApp</a></span>
</div></div>

<header class="nav"><div class="wrap">
  <a class="brand" href="index.html"><img src="assets/img/logo.png" alt="R N Multispeciality Hospital logo"><span>RNMH<small>inspiring better health</small></span></a>
  <nav class="menu"><a href="index.html">Home</a><a href="index.html#specialities">Specialities</a><a href="doctors.html">Doctors</a><a href="index.html#facilities">Facilities</a><a href="contact.html">Contact</a><a class="btn btn-primary js-wa" href="#">Book on WhatsApp</a></nav>
  <button class="burger" id="burger" aria-label="Menu">☰</button>
</div></header>

<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> / Location</div>
  <h1>Hospital near Mansarovar Metro Station, Kings Road and Nirman Nagar</h1>
  <p class="lead">R N Multispeciality Hospital is located on Main Kings Road in Nirman Nagar, Jaipur, close to Mansarovar Metro Station. The hospital is easily accessible for families from Nirman Nagar, Mansarovar, Shyam Nagar, Brijlalpura, Rail Nagar, Gopalpura Bypass, New Aatish Market and nearby Jaipur localities.</p>
</div></section>

<section><div class="wrap"><div class="grid-2">
  <div class="content-body">
    <p class="lead" style="margin-bottom: 24px;">Patients searching for a multispeciality hospital, gynaecologist, general surgeon, pain and spine specialist, diagnostic centre or 24x7 emergency hospital near Mansarovar Metro Station can visit RNMH for specialist-led care under one roof.</p>
    
    <div style="margin-top:30px; padding: 20px; background: var(--teal-soft); border-radius: 12px;">
      <h3 style="margin-top:0;">Book an Appointment</h3>
      <p style="margin-bottom:15px;">Get in touch to book your consultation.</p>
      <button class="btn btn-primary js-wa" style="width: 100%; justify-content:center;">Book on WhatsApp</button>
      <a href="tel:+911412390320" class="btn btn-ghost" style="width: 100%; justify-content:center; margin-top:8px;">Call 0141 239 0320</a>
    </div>
  </div>
  
  <div>
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3558.919280456184!2d75.7516773!3d26.8742881!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x396db4f61763aa87%3A0xc4eb04c7dfb91fdb!2sR%20N%20Multispeciality%20Hospital%20%7C%20General%20Physician%20%7C%20Gynecologist%20%7C%20Orthopedic%20%7C%20Pediatrician!5e0!3m2!1sen!2sin!4v1716383610217!5m2!1sen!2sin" width="100%" height="450" style="border:0; border-radius:12px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
  </div>
</div></div></section>

<footer class="site"><div class="wrap">
  <div class="grid footer-grid">
    <div>
      <a class="brand" href="index.html" style="color:#fff"><img src="assets/img/logo.png" alt="RNMH" style="height:40px;background:#fff;border-radius:8px;padding:3px"><span style="color:#fff">R N Multispeciality Hospital</span></a>
      <p style="margin-top:12px">50-bed multispeciality hospital on Main Kings Road, Nirman Nagar, Jaipur</p>
      <p><b>Address:</b><br>109-110, Shiv Shakti Nagar, Main Kings Road, Nirman Nagar, Jaipur, Rajasthan 302019</p>
      <p><b>Landmark:</b><br>Near Mansarovar Metro Station</p>
      <p><b>Phone:</b> <a href="tel:+911412390320" class="js-phone-link"><span class="js-phone-display">0141 239 0320</span></a></p>
      <p><b>Open:</b><br>24x7 emergency care</p>
      <p><b>Serving:</b><br>Nirman Nagar, Mansarovar, Kings Road, Shyam Nagar, Brijlalpura, Gopalpura Bypass and nearby Jaipur areas</p>
    </div>
    <div><h4>Departments</h4><p><a href="services/general-surgery.html">General &amp; Laparoscopic Surgery</a><br><a href="services/gynaecology.html">Obstetrics &amp; Gynaecology</a><br><a href="services/pain-spine.html">Pain Management &amp; Spine Care</a><br><a href="services/orthopaedics.html">Orthopaedics</a><br><a href="services/urology.html">Urology</a><br><a href="services/neurosurgery.html">Neurosurgery</a><br><a href="services/ent.html">ENT</a><br><a href="services/general-medicine.html">General Medicine</a><br><a href="services/pathology.html">Pathology</a></p></div>
    <div><h4>Important links</h4><p><a href="index.html">Home</a><br><a href="doctors.html">Doctors</a><br><a href="index.html#specialities">Services</a><br><a href="contact.html">Contact</a><br><a href="#" class="js-wa">Book Appointment</a></p></div>
  </div>
  
  <div class="footer-seo-links" style="border-top: 1px solid rgba(255,255,255,0.1); margin-top:30px; padding-top:20px;">
    <h4 style="margin-bottom:8px; font-size:14px;">Local Searches:</h4>
    <p style="font-size: 13px; line-height:1.6; color: rgba(255,255,255,0.7);"><a href="treatments/gynaecologist-near-nirman-nagar-jaipur.html">Gynaecologist near Nirman Nagar</a> &middot; <a href="treatments/gynaecologist-near-mansarovar-metro-station.html">Gynaecologist near Mansarovar Metro</a> &middot; <a href="treatments/pregnancy-care-hospital-near-mansarovar-metro.html">Pregnancy care near Mansarovar Metro</a> &middot; <a href="treatments/fertility-doctor-nirman-nagar-jaipur.html">Fertility Doctor Nirman Nagar</a> &middot; <a href="treatments/obgyn-kings-road-jaipur.html">OB-GYN Kings Road Jaipur</a> &middot; <a href="treatments/hospital-near-mansarovar-metro-station.html">Hospital near Mansarovar Metro</a> &middot; <a href="treatments/multispeciality-hospital-kings-road-jaipur.html">Multispeciality Hospital Kings Road</a> &middot; <a href="treatments/24x7-emergency-hospital-nirman-nagar-jaipur.html">24x7 Emergency Hospital in Nirman Nagar</a> &middot; <a href="treatments/cashless-hospital-near-mansarovar-jaipur.html">Cashless Hospital near Mansarovar</a> &middot; <a href="treatments/laparoscopic-surgeon-near-mansarovar-metro.html">Laparoscopic Surgeon near Mansarovar Metro</a> &middot; <a href="treatments/general-surgeon-nirman-nagar-jaipur.html">General Surgeon Nirman Nagar</a> &middot; <a href="treatments/laser-piles-treatment-kings-road-jaipur.html">Laser Piles Treatment Kings Road</a> &middot; <a href="treatments/hernia-surgery-nirman-nagar-jaipur.html">Hernia Surgery Nirman Nagar</a> &middot; <a href="treatments/back-pain-treatment-nirman-nagar-jaipur.html">Back Pain Treatment Nirman Nagar</a> &middot; <a href="treatments/spine-specialist-near-mansarovar-metro.html">Spine Specialist near Mansarovar Metro</a> &middot; <a href="treatments/pain-management-doctor-kings-road-jaipur.html">Pain Management Kings Road</a></p>
  </div>
  <div class="copy">© <span data-year></span> R N Multispeciality Hospital. All rights reserved.</div>
</div></footer>
<script src="assets/js/site.js"></script>
</body>
</html>
"""

with open("site/location.html", "w", encoding="utf-8") as f:
    f.write(en_html)

# 2. Hindi Location Page
hi_html = """<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>स्थान | R N Multispeciality Hospital Jaipur</title>
<meta name="description" content="R N Multispeciality Hospital मेन किंग्स रोड, निर्माण नगर, जयपुर में स्थित है, मानसरोवर मेट्रो स्टेशन के पास।">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/css/style.css"><link rel="icon" href="../assets/img/logo.png">
</head>
<body>

<div class="topbar"><div class="wrap">
  <span>24x7 उपलब्ध &middot; मानसरोवर मेट्रो स्टेशन के पास, निर्माण नगर, जयपुर</span>
  <span>कॉल करें <a href="tel:+911412390320" class="js-phone-link"><span class="js-phone-display">0141 239 0320</span></a> &middot; <a href="#" class="js-wa">WhatsApp पर बुक करें</a></span>
</div></div>

<header class="nav"><div class="wrap">
  <a class="brand" href="index.html"><img src="../assets/img/logo.png" alt="R N Multispeciality Hospital logo"><span>RNMH<small>inspiring better health</small></span></a>
  <nav class="menu"><a href="index.html">होम</a><a href="index.html#specialities">सेवाएँ</a><a href="doctors.html">डॉक्टर</a><a href="contact.html">संपर्क</a><a class="btn btn-primary js-wa" href="#">WhatsApp पर बुक करें</a></nav>
  <button class="burger" id="burger" aria-label="Menu">☰</button>
</div></header>

<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="index.html">होम</a> / स्थान</div>
  <h1>मानसरोवर मेट्रो स्टेशन, किंग्स रोड और निर्माण नगर के पास हॉस्पिटल</h1>
  <p class="lead">R N Multispeciality Hospital मेन किंग्स रोड, निर्माण नगर, जयपुर में स्थित है, मानसरोवर मेट्रो स्टेशन के पास। यह हॉस्पिटल निर्माण नगर, मानसरोवर, श्याम नगर, बृजलालपुरा, रेल नगर, गोपालपुरा बाइपास, न्यू आतिश मार्केट और आसपास के जयपुर इलाकों से आसानी से पहुँचा जा सकता है।</p>
</div></section>

<section><div class="wrap"><div class="grid-2">
  <div class="content-body">
    <p class="lead" style="margin-bottom: 24px;">मल्टीस्पेशलिटी हॉस्पिटल, गायनेकोलॉजिस्ट, जनरल सर्जन, पेन व स्पाइन स्पेशलिस्ट, डायग्नोस्टिक सेंटर या 24x7 इमरजेंसी हॉस्पिटल खोजने वाले मरीज एक ही जगह विशेषज्ञ-नेतृत्व वाली देखभाल के लिए RNMH में आ सकते हैं।</p>
    
    <div style="margin-top:30px; padding: 20px; background: var(--teal-soft); border-radius: 12px;">
      <h3 style="margin-top:0;">अपॉइंटमेंट बुक करें</h3>
      <p style="margin-bottom:15px;">कंसल्टेशन बुक करने के लिए संपर्क करें।</p>
      <button class="btn btn-primary js-wa" style="width: 100%; justify-content:center;">WhatsApp पर बुक करें</button>
      <a href="tel:+911412390320" class="btn btn-ghost" style="width: 100%; justify-content:center; margin-top:8px;">कॉल 0141 239 0320</a>
    </div>
  </div>
  
  <div>
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3558.919280456184!2d75.7516773!3d26.8742881!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x396db4f61763aa87%3A0xc4eb04c7dfb91fdb!2sR%20N%20Multispeciality%20Hospital!5e0!3m2!1sen!2sin!4v1716383610217!5m2!1sen!2sin" width="100%" height="450" style="border:0; border-radius:12px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
  </div>
</div></div></section>

<footer class="site"><div class="wrap">
  <div class="grid footer-grid">
    <div>
      <a class="brand" href="index.html" style="color:#fff"><img src="../assets/img/logo.png" alt="RNMH" style="height:40px;background:#fff;border-radius:8px;padding:3px"><span style="color:#fff">R N Multispeciality Hospital</span></a>
      <p style="margin-top:12px">मेन किंग्स रोड, निर्माण नगर, जयपुर में 50-बेड मल्टीस्पेशलिटी हॉस्पिटल</p>
      <p><b>पता:</b><br>109-110, शिव शक्ति नगर, मेन किंग्स रोड, निर्माण नगर, जयपुर, राजस्थान 302019</p>
      <p><b>लैंडमार्क:</b><br>मानसरोवर मेट्रो स्टेशन के पास</p>
      <p><b>फोन:</b> <a href="tel:+911412390320" class="js-phone-link"><span class="js-phone-display">0141 239 0320</span></a></p>
      <p><b>उपलब्धता:</b><br>24x7 इमरजेंसी केयर</p>
      <p><b>सेवा क्षेत्र:</b><br>निर्माण नगर, मानसरोवर, किंग्स रोड, श्याम नगर, बृजलालपुरा, गोपालपुरा बाइपास और आसपास के जयपुर क्षेत्र</p>
    </div>
    <div><h4>विभाग</h4><p><a href="index.html">सभी सेवाएँ देखें</a></p></div>
    <div><h4>महत्वपूर्ण लिंक</h4><p><a href="index.html">होम</a><br><a href="doctors.html">डॉक्टर</a><br><a href="contact.html">संपर्क</a><br><a href="#" class="js-wa">अपॉइंटमेंट बुक करें</a></p></div>
  </div>
  
  <div class="footer-seo-links" style="border-top: 1px solid rgba(255,255,255,0.1); margin-top:30px; padding-top:20px;">
    <h4 style="margin-bottom:8px; font-size:14px;">स्थानीय खोज:</h4>
    <p style="font-size: 13px; line-height:1.6; color: rgba(255,255,255,0.7);"><a href="treatments/gynaecologist-near-nirman-nagar-jaipur.html">निर्माण नगर के पास गायनेकोलॉजिस्ट</a> &middot; <a href="treatments/gynaecologist-near-mansarovar-metro-station.html">मानसरोवर मेट्रो के पास गायनेकोलॉजिस्ट</a> &middot; <a href="treatments/pregnancy-care-hospital-near-mansarovar-metro.html">मानसरोवर मेट्रो के पास प्रेगनेंसी केयर</a> &middot; <a href="treatments/fertility-doctor-nirman-nagar-jaipur.html">निर्माण नगर जयपुर फर्टिलिटी डॉक्टर</a> &middot; <a href="treatments/obgyn-kings-road-jaipur.html">किंग्स रोड जयपुर OB-GYN</a> &middot; <a href="treatments/hospital-near-mansarovar-metro-station.html">मानसरोवर मेट्रो के पास हॉस्पिटल</a> &middot; <a href="treatments/multispeciality-hospital-kings-road-jaipur.html">किंग्स रोड जयपुर मल्टीस्पेशलिटी हॉस्पिटल</a> &middot; <a href="treatments/24x7-emergency-hospital-nirman-nagar-jaipur.html">निर्माण नगर 24x7 इमरजेंसी हॉस्पिटल</a> &middot; <a href="treatments/cashless-hospital-near-mansarovar-jaipur.html">मानसरोवर के पास कैशलेस हॉस्पिटल</a> &middot; <a href="treatments/laparoscopic-surgeon-near-mansarovar-metro.html">मानसरोवर मेट्रो लेप्रोस्कोपिक सर्जन</a> &middot; <a href="treatments/general-surgeon-nirman-nagar-jaipur.html">निर्माण नगर जनरल सर्जन</a> &middot; <a href="treatments/laser-piles-treatment-kings-road-jaipur.html">किंग्स रोड लेजर पाइल्स ट्रीटमेंट</a> &middot; <a href="treatments/hernia-surgery-nirman-nagar-jaipur.html">निर्माण नगर हर्निया सर्जरी</a> &middot; <a href="treatments/back-pain-treatment-nirman-nagar-jaipur.html">निर्माण नगर बैक पेन ट्रीटमेंट</a> &middot; <a href="treatments/spine-specialist-near-mansarovar-metro.html">मानसरोवर मेट्रो के पास स्पाइन स्पेशलिस्ट</a> &middot; <a href="treatments/pain-management-doctor-kings-road-jaipur.html">किंग्स रोड पेन मैनेजमेंट डॉक्टर</a></p>
  </div>
  <div class="copy">© <span data-year></span> R N Multispeciality Hospital. All rights reserved.</div>
</div></footer>
<script src="../assets/js/site.js"></script>
</body>
</html>
"""

with open("site/hi/location.html", "w", encoding="utf-8") as f:
    f.write(hi_html)

# 3. Remove locality block from index.html
with open("site/index.html", "r", encoding="utf-8") as f:
    html = f.read()

locality_pattern = re.compile(r'<section id="locality" style="background:#F6F9F8; padding: 60px 0;">.*?</section>\s*', re.DOTALL)
html = locality_pattern.sub('', html)

# Add "View Location Details" button to At a Glance
btn_insert = '<tr><th>Appointment</th><td>WhatsApp or call <a href="tel:+911412390320" class="js-phone-link"><span class="js-phone-display">0141 239 0320</span></a></td></tr>\n    <tr><th>Location Info</th><td><a href="location.html" style="font-weight:600; color:var(--primary); text-decoration:underline;">View Location Details &rarr;</a></td></tr>'
html = html.replace('<tr><th>Appointment</th><td>WhatsApp or call <a href="tel:+911412390320" class="js-phone-link"><span class="js-phone-display">0141 239 0320</span></a></td></tr>', btn_insert)

with open("site/index.html", "w", encoding="utf-8") as f:
    f.write(html)

# 4. Remove locality block from hi/index.html
with open("site/hi/index.html", "r", encoding="utf-8") as f:
    hi_idx_html = f.read()

hi_idx_html = locality_pattern.sub('', hi_idx_html)

# Add "View Location Details" button to At a Glance (Hindi)
btn_insert_hi = '<tr><th>अपॉइंटमेंट</th><td>WhatsApp करें या कॉल करें: <a href="tel:+911412390320" class="js-phone-link"><span class="js-phone-display">0141 239 0320</span></a></td></tr>\n    <tr><th>स्थान विवरण</th><td><a href="location.html" style="font-weight:600; color:var(--primary); text-decoration:underline;">स्थान विवरण देखें &rarr;</a></td></tr>'
hi_idx_html = hi_idx_html.replace('<tr><th>अपॉइंटमेंट</th><td>WhatsApp करें या कॉल करें: <a href="tel:+911412390320" class="js-phone-link"><span class="js-phone-display">0141 239 0320</span></a></td></tr>', btn_insert_hi)

with open("site/hi/index.html", "w", encoding="utf-8") as f:
    f.write(hi_idx_html)

print("Location pages created and index updated.")
