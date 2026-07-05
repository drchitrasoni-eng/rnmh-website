import os

campaigns = [
    {
        "filename": "ivf-fertility.html",
        "title": "IVF & Fertility Treatments in Jaipur",
        "doc_name": "Dr Chitra Soni",
        "doc_title": "Senior Fertility & IVF Specialist",
        "doc_img": "../assets/img/docs/chitra-soni.jpg",
        "dept_id": "gynaecology",
        "hook": "Struggling to conceive? Get expert guidance from Dr Chitra Soni.",
        "desc": "Personalized IVF, IUI and advanced fertility treatments at R N Multispeciality Hospital, Jaipur. We combine state-of-the-art lab technology with compassionate care to help you build your family.",
        "benefits": ["High success rates", "Transparent pricing", "Advanced embryology lab", "EMI options available"]
    },
    {
        "filename": "spine-surgery.html",
        "title": "Minimally Invasive Spine Surgery in Jaipur",
        "doc_name": "Dr Naveen Soni",
        "doc_title": "Interventional Pain & Spine Specialist",
        "doc_img": "../assets/img/docs/naveen-soni.jpg",
        "dept_id": "pain-spine",
        "hook": "Severe back pain or sciatica? Avoid open surgery.",
        "desc": "Get advanced, minimally invasive treatments for slip disc and chronic spine pain. Faster recovery, smaller cuts, and rapid return to normal life under the expert care of Dr Naveen Soni.",
        "benefits": ["Day-care procedures", "No large incisions", "German-trained specialist", "Cashless insurance accepted"]
    },
    {
        "filename": "laparoscopic-surgery.html",
        "title": "Advanced Laparoscopic Surgery in Jaipur",
        "doc_name": "Dr Robin Bothra",
        "doc_title": "Senior Laparoscopic Surgeon",
        "doc_img": "../assets/img/docs/robin-bothra.jpg",
        "dept_id": "general-surgery",
        "hook": "Need gallbladder or hernia surgery? Choose keyhole surgery for a faster recovery.",
        "desc": "Dr Robin Bothra offers state-of-the-art laparoscopic (keyhole) surgeries for hernia, gallbladder stones, and appendix. Minimal pain, zero scars, and discharge within 24 hours.",
        "benefits": ["24-hour discharge", "Minimal pain & scarring", "RGHS & Cashless accepted", "Modular OT"]
    },
    {
        "filename": "joint-replacement.html",
        "title": "Knee & Joint Replacement in Jaipur",
        "doc_name": "Dr Chirag Jain",
        "doc_title": "Orthopaedic & Joint Replacement Surgeon",
        "doc_img": "../assets/img/docs/chirag-jain.jpg",
        "dept_id": "orthopaedics",
        "hook": "Severe knee pain stopping you from walking? Regain your mobility.",
        "desc": "Advanced computer-navigated knee and hip replacement surgery by Dr Chirag Jain. Get perfectly aligned joints that last longer, with advanced pain management protocols.",
        "benefits": ["Computer-navigated precision", "Rapid recovery protocols", "World-class implants", "0% EMI options"]
    }
]

template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | R N Multispeciality Hospital</title>
<meta name="robots" content="noindex, nofollow"> <!-- Marketing landing pages should not be indexed organically -->
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/css/style.css"><link rel="icon" href="../assets/img/logo.png">
<style>
  /* Funnel-specific styles */
  .funnel-hero {{ background: linear-gradient(150deg, var(--primary), var(--primary-deep)); color: #fff; padding: 80px 0; }}
  .funnel-hero h1 {{ color: #fff; font-size: clamp(32px, 5vw, 56px); margin-bottom: 16px; }}
  .funnel-hero .lead {{ color: #DCEFEC; font-size: 18px; max-width: 600px; }}
  .nav {{ display: none; }} /* Hide main nav to reduce exit paths */
  .funnel-header {{ padding: 16px 28px; background: #fff; display: flex; justify-content: space-between; align-items: center; max-width: 1180px; margin: 0 auto; }}
</style>
</head>
<body>

<div class="funnel-header">
  <a class="brand" href="../index.html"><img src="../assets/img/logo.png" alt="RNMH" style="height:46px;"></a>
  <a href="tel:+911412390320" class="btn btn-ghost" style="padding: 10px 16px;">Call 0141 239 0320</a>
</div>

<section class="funnel-hero"><div class="wrap grid-2" style="align-items:center;">
  <div>
    <span class="eyebrow" style="background: rgba(255,255,255,0.15); color: #fff;">Free Consultation Available</span>
    <h1>{hook}</h1>
    <p class="lead">{desc}</p>
    <ul class="ticks" style="margin-top:24px; color: #fff;">
      {benefits_html}
    </ul>
  </div>
  <div class="form-card" style="background: #fff; color: var(--ink);">
    <h3 style="margin-bottom:16px;">Book Your Consultation</h3>
    <form id="bookForm">
      <div class="field"><label>Your Name</label><input type="text" name="name" required></div>
      <div class="field"><label>Phone Number</label><input type="tel" name="phone" required></div>
      <input type="hidden" name="department" value="{dept_id}">
      <button class="btn btn-primary" type="submit" style="width:100%; margin-top:12px;">Get Started on WhatsApp</button>
      <p style="font-size:12px; color: var(--ink-faint); margin-top:12px; text-align:center;">Our team will reply within 15 minutes.</p>
    </form>
  </div>
</div></section>

<section><div class="wrap">
  <div class="sec-head center"><h2>Meet Your Expert</h2></div>
  <div class="grid-2" style="max-width: 800px; margin: 40px auto; align-items:center; background: var(--surface); padding: 24px; border-radius: var(--r-out); border: 1px solid var(--line);">
    <img src="{doc_img}" alt="{doc_name}" style="border-radius: var(--r-in); width: 100%;">
    <div>
      <h3 style="font-size: 28px; margin-bottom: 8px;">{doc_name}</h3>
      <p style="color: var(--primary); font-weight: 700; margin-bottom: 16px;">{doc_title}</p>
      <p>With thousands of successful cases, {doc_name} brings unparalleled expertise and a patient-first approach to ensure the best possible outcomes.</p>
      <p style="margin-top: 16px;"><span class="stars" style="color: var(--gold);">★★★★★</span><br><b>4.9/5</b> Patient Rating</p>
    </div>
  </div>
</div></section>

<footer style="text-align:center; padding: 40px 0; background: var(--bg); font-size: 14px; color: var(--ink-soft);">
  <p>© 2026 R N Multispeciality Hospital, Jaipur. All rights reserved.</p>
</footer>

<script src="../assets/js/site.js"></script>
</body>
</html>
"""

os.makedirs("site/campaigns", exist_ok=True)

for c in campaigns:
    benefits_html = "".join([f'<li>{b}</li>' for b in c["benefits"]])
    html = template.format(
        title=c["title"],
        hook=c["hook"],
        desc=c["desc"],
        doc_img=c["doc_img"],
        doc_name=c["doc_name"],
        doc_title=c["doc_title"],
        dept_id=c["dept_id"],
        benefits_html=benefits_html
    )
    filepath = os.path.join("site/campaigns", c["filename"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Marketing campaigns generated.")
