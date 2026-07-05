import os
import json

pages = [
    # Gynaecology
    {"slug": "gynaecologist-near-nirman-nagar-jaipur", "service": "Gynaecologist", "location": "Nirman Nagar, Jaipur", "doc": "Dr Chitra Soni", "dept": "Obstetrics, Gynaecology and Fertility", "type": "Physician"},
    {"slug": "gynaecologist-near-mansarovar-metro-station", "service": "Gynaecologist", "location": "Mansarovar Metro Station", "doc": "Dr Chitra Soni", "dept": "Obstetrics, Gynaecology and Fertility", "type": "Physician"},
    {"slug": "pregnancy-care-hospital-near-mansarovar-metro", "service": "Pregnancy Care", "location": "Mansarovar Metro", "doc": "Dr Chitra Soni", "dept": "Obstetrics and Gynaecology", "type": "Physician"},
    {"slug": "fertility-doctor-nirman-nagar-jaipur", "service": "Fertility Doctor", "location": "Nirman Nagar, Jaipur", "doc": "Dr Chitra Soni", "dept": "Obstetrics, Gynaecology and Fertility", "type": "Physician"},
    {"slug": "obgyn-kings-road-jaipur", "service": "OB-GYN", "location": "Kings Road, Jaipur", "doc": "Dr Chitra Soni", "dept": "Obstetrics, Gynaecology and Fertility", "type": "Physician"},

    # Hospital
    {"slug": "hospital-near-mansarovar-metro-station", "service": "Multispeciality Hospital", "location": "Mansarovar Metro Station", "doc": "our expert specialists", "dept": "all major departments", "type": "Hospital"},
    {"slug": "multispeciality-hospital-kings-road-jaipur", "service": "Multispeciality Hospital", "location": "Kings Road, Jaipur", "doc": "our expert specialists", "dept": "all major departments", "type": "Hospital"},
    {"slug": "24x7-emergency-hospital-nirman-nagar-jaipur", "service": "24x7 Emergency Hospital", "location": "Nirman Nagar, Jaipur", "doc": "our emergency team", "dept": "24x7 Emergency Care", "type": "Hospital"},
    {"slug": "cashless-hospital-near-mansarovar-jaipur", "service": "Cashless Hospital", "location": "Mansarovar, Jaipur", "doc": "our expert specialists", "dept": "all major departments", "type": "Hospital"},

    # Surgery
    {"slug": "laparoscopic-surgeon-near-mansarovar-metro", "service": "Laparoscopic Surgeon", "location": "Mansarovar Metro", "doc": "Dr Robin Bothra", "dept": "General and Laparoscopic Surgery", "type": "Physician"},
    {"slug": "general-surgeon-nirman-nagar-jaipur", "service": "General Surgeon", "location": "Nirman Nagar, Jaipur", "doc": "Dr Robin Bothra", "dept": "General and Laparoscopic Surgery", "type": "Physician"},
    {"slug": "laser-piles-treatment-kings-road-jaipur", "service": "Laser Piles Treatment", "location": "Kings Road, Jaipur", "doc": "Dr Robin Bothra", "dept": "General and Laparoscopic Surgery", "type": "Physician"},
    {"slug": "hernia-surgery-nirman-nagar-jaipur", "service": "Hernia Surgery", "location": "Nirman Nagar, Jaipur", "doc": "Dr Robin Bothra", "dept": "General and Laparoscopic Surgery", "type": "Physician"},

    # Pain & Spine
    {"slug": "back-pain-treatment-nirman-nagar-jaipur", "service": "Back Pain Treatment", "location": "Nirman Nagar, Jaipur", "doc": "Dr Naveen Soni", "dept": "Pain Management and Spine Care", "type": "Physician"},
    {"slug": "spine-specialist-near-mansarovar-metro", "service": "Spine Specialist", "location": "Mansarovar Metro", "doc": "Dr Naveen Soni", "dept": "Pain Management and Spine Care", "type": "Physician"},
    {"slug": "pain-management-doctor-kings-road-jaipur", "service": "Pain Management Doctor", "location": "Kings Road, Jaipur", "doc": "Dr Naveen Soni", "dept": "Pain Management and Spine Care", "type": "Physician"},
]

template = """<!DOCTYPE html>
<html lang="{lang_code}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{meta_title}</title>
<meta name="description" content="{meta_desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{assets_prefix}assets/css/style.css"><link rel="icon" href="{assets_prefix}assets/img/logo.png">
{schema}
</head>
<body>

<div class="topbar"><div class="wrap">
  <span>{topbar_text}</span>
  <span>{call_text} <a href="tel:+911412390320" class="js-phone-link"><span class="js-phone-display">0141 239 0320</span></a> &middot; <a href="#" class="js-wa">{book_wa_text}</a></span>
</div></div>

<header class="nav"><div class="wrap">
  <a class="brand" href="{assets_prefix}index.html"><img src="{assets_prefix}assets/img/logo.png" alt="R N Multispeciality Hospital logo"><span>RNMH<small>inspiring better health</small></span></a>
  <nav class="menu"><a href="{assets_prefix}index.html">Home</a><a href="{assets_prefix}index.html#specialities">Specialities</a><a href="{assets_prefix}doctors.html">Doctors</a><a href="{assets_prefix}index.html#facilities">Facilities</a><a href="{assets_prefix}contact.html">Contact</a><a class="btn btn-primary js-wa" href="#">{book_wa_text}</a></nav>
  <button class="burger" id="burger" aria-label="Menu">☰</button>
</div></header>

<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="{assets_prefix}index.html">Home</a> / {service}</div>
  <h1>{h1}</h1>
  <p class="lead">{intro}</p>
</div></section>

<section><div class="wrap"><div class="grid-2">
  <div class="content-body">
    <h2>{who_should_visit_h2}</h2>
    <p>{who_should_visit}</p>
    
    <h2>{doctor_dept_h2}</h2>
    <p>{doctor_dept}</p>
    
    <h2>{why_rnmh_h2}</h2>
    <p>{why_rnmh}</p>
    
    <div style="margin-top:30px; padding: 20px; background: var(--teal-soft); border-radius: 12px;">
      <h3 style="margin-top:0;">{cta_h3}</h3>
      <p style="margin-bottom:15px;">{cta_p}</p>
      <button class="btn btn-primary js-wa" style="width: 100%; justify-content:center;">{book_wa_text}</button>
      <a href="tel:+911412390320" class="btn btn-ghost" style="width: 100%; justify-content:center; margin-top:8px;">Call 0141 239 0320</a>
    </div>
  </div>
  
  <div>
    <div class="sec-head" style="margin-bottom: 20px;"><h2>FAQs</h2></div>
    {faq_html}
  </div>
</div></div></section>

<footer class="site"><div class="wrap">
  <div class="grid footer-grid">
    {footer_col1}
    {footer_col2}
    {footer_col3}
  </div>
  <div class="copy">© <span data-year></span> R N Multispeciality Hospital. All rights reserved.</div>
</div></footer>

<script src="{assets_prefix}assets/js/site.js"></script>
</body>
</html>"""

os.makedirs("site/treatments", exist_ok=True)
os.makedirs("site/hi/treatments", exist_ok=True)

for p in pages:
    # --- English ---
    lang_code = "en"
    assets_prefix = "../"
    meta_title = f"{p['service']} near {p['location']} | {p['doc']} at RNMH" if "Dr" in p['doc'] else f"{p['service']} near {p['location']} | RNMH Jaipur"
    meta_desc = f"Consult {p['doc']} for {p['service']} at R N Multispeciality Hospital, Main Kings Road, Nirman Nagar, Jaipur, near Mansarovar Metro Station." if "Dr" in p['doc'] else f"R N Multispeciality Hospital provides {p['service']} on Main Kings Road, Nirman Nagar, Jaipur, near Mansarovar Metro Station."
    h1 = f"{p['service']} near {p['location']}"
    intro = f"R N Multispeciality Hospital provides {p['service']} at its 50-bed hospital on Main Kings Road, Nirman Nagar, Jaipur, near Mansarovar Metro Station. The hospital is accessible from Mansarovar, Shyam Nagar, Brijlalpura, Gopalpura Bypass and nearby Jaipur areas."
    
    who_should_visit_h2 = "Who should visit"
    who_should_visit = f"Patients looking for a {p['service']} near {p['location']}, Kings Road, Mansarovar Metro Station, Mansarovar, Shyam Nagar, Brijlalpura or Gopalpura Bypass can visit RNMH."
    
    doctor_dept_h2 = "Doctor & Department"
    doctor_dept = f"You can consult {p['doc']} from the {p['dept']} department at RNMH."
    
    why_rnmh_h2 = "Why choose RNMH?"
    why_rnmh = "RNMH provides 24x7 emergency care, specialist consultations, diagnostics, admission support, operation theatre access, ICU/NICU support and cashless insurance assistance under one roof."
    
    cta_h3 = "Book an Appointment"
    cta_p = "Get in touch to book your consultation."
    book_wa_text = "Book on WhatsApp"
    topbar_text = "Open 24x7 &middot; Near Mansarovar Metro Station, Nirman Nagar, Jaipur"
    call_text = "Call"

    faqs = [
        {"q": f"Is {p['service']} available near {p['location']}?", "a": f"Yes. {p['service']} is available at R N Multispeciality Hospital on Main Kings Road, Nirman Nagar, Jaipur, near Mansarovar Metro Station."},
        {"q": f"Is there a {p['service']} near Mansarovar Metro Station?", "a": f"Yes. {p['service']} consultations are available at RNMH, located near Mansarovar Metro Station in Nirman Nagar, Jaipur."},
        {"q": f"Does RNMH provide {p['service']} in Nirman Nagar Jaipur?", "a": f"Yes. RNMH provides {p['service']} and related diagnostics in Nirman Nagar, Jaipur."},
        {"q": "How can I book an appointment?", "a": "You can book on WhatsApp or call 0141 239 0320."},
        {"q": "Is cashless insurance available?", "a": "Cashless insurance and TPA support may be available depending on the patient's insurance policy and provider approval."}
    ]
    
    faq_html = ""
    for faq in faqs:
        faq_html += f'<div class="card" style="margin-bottom:12px;"><div class="card-core"><h3 style="font-size:16px;">{faq["q"]}</h3><p class="desc" style="margin-top:6px; font-size:15px;">{faq["a"]}</p></div></div>\n'
        
    footer_col1 = """<div>
      <a class="brand" href="../index.html" style="color:#fff"><img src="../assets/img/logo.png" alt="RNMH" style="height:40px;background:#fff;border-radius:8px;padding:3px"><span style="color:#fff">R N Multispeciality Hospital</span></a>
      <p style="margin-top:12px">50-bed multispeciality hospital on Main Kings Road, Nirman Nagar, Jaipur</p>
      <p><b>Address:</b><br>109-110, Shiv Shakti Nagar, Main Kings Road, Nirman Nagar, Jaipur, Rajasthan 302019</p>
      <p><b>Landmark:</b><br>Near Mansarovar Metro Station</p>
      <p><b>Phone:</b> <a href="tel:+911412390320" class="js-phone-link"><span class="js-phone-display">0141 239 0320</span></a></p>
      <p><b>Open:</b><br>24x7 emergency care</p>
      <p><b>Serving:</b><br>Nirman Nagar, Mansarovar, Kings Road, Shyam Nagar, Brijlalpura, Gopalpura Bypass and nearby Jaipur areas</p>
    </div>"""
    footer_col2 = """<div><h4>Departments</h4><p><a href="../services/general-surgery.html">General &amp; Laparoscopic Surgery</a><br><a href="../services/gynaecology.html">Obstetrics &amp; Gynaecology</a><br><a href="../services/pain-spine.html">Pain Management &amp; Spine Care</a><br><a href="../services/orthopaedics.html">Orthopaedics</a><br><a href="../services/urology.html">Urology</a><br><a href="../services/neurosurgery.html">Neurosurgery</a><br><a href="../services/ent.html">ENT</a><br><a href="../services/general-medicine.html">General Medicine</a><br><a href="../services/pathology.html">Pathology</a></p></div>"""
    footer_col3 = """<div><h4>Important links</h4><p><a href="../index.html">Home</a><br><a href="../doctors.html">Doctors</a><br><a href="../index.html#specialities">Services</a><br><a href="../contact.html">Contact</a><br><a href="#" class="js-wa">Book Appointment</a></p></div>"""

    if p["type"] == "Physician":
        schema_json = {
          "@context": "https://schema.org",
          "@type": "Physician",
          "name": p["doc"],
          "medicalSpecialty": p["service"],
          "worksFor": {"@id": "https://rnmh.in/#hospital"},
          "hospitalAffiliation": {"@id": "https://rnmh.in/#hospital"},
          "address": {"@type": "PostalAddress", "streetAddress": "109-110, Shiv Shakti Nagar, Main Kings Road, Nirman Nagar", "addressLocality": "Jaipur", "addressRegion": "Rajasthan", "postalCode": "302019", "addressCountry": "IN"},
          "areaServed": ["Nirman Nagar", "Kings Road", "Mansarovar Metro Station", "Mansarovar", "Shyam Nagar", "Jaipur"]
        }
        schema = f'<script type="application/ld+json">\n{json.dumps(schema_json, indent=2)}\n</script>'
    else:
        schema = ""

    html = template.format(
        lang_code=lang_code, assets_prefix=assets_prefix, meta_title=meta_title, meta_desc=meta_desc,
        schema=schema, topbar_text=topbar_text, call_text=call_text, book_wa_text=book_wa_text,
        service=p["service"], h1=h1, intro=intro,
        who_should_visit_h2=who_should_visit_h2, who_should_visit=who_should_visit,
        doctor_dept_h2=doctor_dept_h2, doctor_dept=doctor_dept,
        why_rnmh_h2=why_rnmh_h2, why_rnmh=why_rnmh,
        cta_h3=cta_h3, cta_p=cta_p, faq_html=faq_html,
        footer_col1=footer_col1, footer_col2=footer_col2, footer_col3=footer_col3
    )

    with open(f"site/treatments/{p['slug']}.html", "w", encoding="utf-8") as f:
        f.write(html)


    # --- Hindi ---
    lang_code = "hi"
    assets_prefix = "../../"
    meta_title = f"{p['location']} के पास {p['service']} | RNMH जयपुर"
    meta_desc = f"आर एन मल्टीस्पेशलिटी हॉस्पिटल, मेन किंग्स रोड, निर्माण नगर, जयपुर में {p['location']} के पास {p['service']} उपलब्ध है।"
    h1 = f"{p['location']} के पास {p['service']}"
    intro = f"R N Multispeciality Hospital मेन किंग्स रोड, निर्माण नगर, जयपुर में स्थित 50-बेड हॉस्पिटल में {p['service']} उपलब्ध कराता है, मानसरोवर मेट्रो स्टेशन के पास। यह मानसरोवर, श्याम नगर, बृजलालपुरा, गोपालपुरा बाइपास और आसपास के जयपुर क्षेत्रों से आसानी से पहुँचा जा सकता है।"
    
    who_should_visit_h2 = "किसे संपर्क करना चाहिए"
    who_should_visit = f"{p['location']}, किंग्स रोड, मानसरोवर मेट्रो स्टेशन, मानसरोवर, श्याम नगर, बृजलालपुरा या गोपालपुरा बाइपास के पास {p['service']} खोज रहे मरीज RNMH में संपर्क कर सकते हैं।"
    
    doctor_dept_h2 = "डॉक्टर और विभाग"
    doctor_dept = f"आप RNMH में {p['dept']} विभाग के {p['doc']} से कंसल्ट कर सकते हैं।"
    
    why_rnmh_h2 = "RNMH क्यों चुनें?"
    why_rnmh = "RNMH में 24x7 इमरजेंसी केयर, विशेषज्ञ कंसल्टेशन, डायग्नोस्टिक्स, एडमिशन सपोर्ट, ऑपरेशन थियेटर, ICU/NICU सपोर्ट और कैशलेस इंश्योरेंस सहायता एक ही जगह उपलब्ध है।"
    
    cta_h3 = "अपॉइंटमेंट बुक करें"
    cta_p = "कंसल्टेशन बुक करने के लिए संपर्क करें।"
    book_wa_text = "WhatsApp पर बुक करें"
    topbar_text = "24x7 उपलब्ध &middot; मानसरोवर मेट्रो स्टेशन के पास, निर्माण नगर, जयपुर"
    call_text = "कॉल करें"

    faqs = [
        {"q": f"क्या {p['location']} के पास {p['service']} उपलब्ध है?", "a": f"हाँ। R N Multispeciality Hospital मेन किंग्स रोड, निर्माण नगर, जयपुर में {p['service']} उपलब्ध है, मानसरोवर मेट्रो स्टेशन के पास।"},
        {"q": f"क्या मानसरोवर मेट्रो स्टेशन के पास {p['service']} है?", "a": f"हाँ। RNMH में {p['service']} कंसल्टेशन उपलब्ध है, जो निर्माण नगर, जयपुर में मानसरोवर मेट्रो स्टेशन के पास स्थित है।"},
        {"q": f"क्या RNMH निर्माण नगर जयपुर में {p['service']} देता है?", "a": f"हाँ। RNMH निर्माण नगर, जयपुर में {p['service']} और संबंधित डायग्नोस्टिक्स उपलब्ध कराता है।"},
        {"q": "मैं अपॉइंटमेंट कैसे बुक कर सकता हूँ?", "a": "आप WhatsApp पर बुक कर सकते हैं या 0141 239 0320 पर कॉल कर सकते हैं।"},
        {"q": "क्या कैशलेस इंश्योरेंस उपलब्ध है?", "a": "मरीज की इंश्योरेंस पॉलिसी और प्रदाता की मंजूरी के आधार पर कैशलेस इंश्योरेंस और TPA सहायता उपलब्ध हो सकती है।"}
    ]
    
    faq_html = ""
    for faq in faqs:
        faq_html += f'<div class="card" style="margin-bottom:12px;"><div class="card-core"><h3 style="font-size:16px;">{faq["q"]}</h3><p class="desc" style="margin-top:6px; font-size:15px;">{faq["a"]}</p></div></div>\n'
        
    footer_col1 = """<div>
      <a class="brand" href="../../hi/index.html" style="color:#fff"><img src="../../assets/img/logo.png" alt="RNMH" style="height:40px;background:#fff;border-radius:8px;padding:3px"><span style="color:#fff">R N Multispeciality Hospital</span></a>
      <p style="margin-top:12px">मेन किंग्स रोड, निर्माण नगर, जयपुर में 50-बेड मल्टीस्पेशलिटी हॉस्पिटल</p>
      <p><b>पता:</b><br>109-110, शिव शक्ति नगर, मेन किंग्स रोड, निर्माण नगर, जयपुर, राजस्थान 302019</p>
      <p><b>लैंडमार्क:</b><br>मानसरोवर मेट्रो स्टेशन के पास</p>
      <p><b>फोन:</b> <a href="tel:+911412390320" class="js-phone-link"><span class="js-phone-display">0141 239 0320</span></a></p>
      <p><b>उपलब्धता:</b><br>24x7 इमरजेंसी केयर</p>
      <p><b>सेवा क्षेत्र:</b><br>निर्माण नगर, मानसरोवर, किंग्स रोड, श्याम नगर, बृजलालपुरा, गोपालपुरा बाइपास और आसपास के जयपुर क्षेत्र</p>
    </div>"""
    footer_col2 = """<div><h4>विभाग</h4><p><a href="../../hi/index.html">सभी सेवाएँ देखें</a></p></div>"""
    footer_col3 = """<div><h4>महत्वपूर्ण लिंक</h4><p><a href="../../hi/index.html">होम</a><br><a href="../../hi/doctors.html">डॉक्टर</a><br><a href="../../hi/contact.html">संपर्क</a><br><a href="#" class="js-wa">अपॉइंटमेंट बुक करें</a></p></div>"""

    if p["type"] == "Physician":
        schema_json = {
          "@context": "https://schema.org",
          "@type": "Physician",
          "name": p["doc"],
          "medicalSpecialty": p["service"],
          "worksFor": {"@id": "https://rnmh.in/#hospital"},
          "hospitalAffiliation": {"@id": "https://rnmh.in/#hospital"},
          "address": {"@type": "PostalAddress", "streetAddress": "109-110, Shiv Shakti Nagar, Main Kings Road, Nirman Nagar", "addressLocality": "Jaipur", "addressRegion": "Rajasthan", "postalCode": "302019", "addressCountry": "IN"},
          "areaServed": ["Nirman Nagar", "Kings Road", "Mansarovar Metro Station", "Mansarovar", "Shyam Nagar", "Jaipur"]
        }
        schema = f'<script type="application/ld+json">\n{json.dumps(schema_json, indent=2, ensure_ascii=False)}\n</script>'
    else:
        schema = ""

    html = template.format(
        lang_code=lang_code, assets_prefix=assets_prefix, meta_title=meta_title, meta_desc=meta_desc,
        schema=schema, topbar_text=topbar_text, call_text=call_text, book_wa_text=book_wa_text,
        service=p["service"], h1=h1, intro=intro,
        who_should_visit_h2=who_should_visit_h2, who_should_visit=who_should_visit,
        doctor_dept_h2=doctor_dept_h2, doctor_dept=doctor_dept,
        why_rnmh_h2=why_rnmh_h2, why_rnmh=why_rnmh,
        cta_h3=cta_h3, cta_p=cta_p, faq_html=faq_html,
        footer_col1=footer_col1, footer_col2=footer_col2, footer_col3=footer_col3
    )

    with open(f"site/hi/treatments/{p['slug']}.html", "w", encoding="utf-8") as f:
        f.write(html)

print("Local SEO pages generated successfully.")
