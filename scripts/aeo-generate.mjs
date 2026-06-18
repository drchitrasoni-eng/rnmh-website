import fs from 'node:fs';
import path from 'node:path';

const outRoot = path.resolve('.');
const today = '2026-06-18';

const hospital = {
  name: 'R N Multispeciality Hospital',
  short: 'RNMH',
  phone: '0141 239 0320',
  tel: '+911412390320',
  schemaTel: '+91-141-239-0320',
  address: '109-110, Shiv Shakti Nagar, Kings Road, Nirman Nagar, Jaipur, Rajasthan 302019',
  street: '109-110, Shiv Shakti Nagar, Kings Road, Nirman Nagar',
  locality: 'Jaipur',
  region: 'Rajasthan',
  postal: '302019',
  map: 'https://maps.app.goo.gl/JJ4gArXVvhqm3ZyMA'
};

const departments = [
  ['General & Laparoscopic Surgery', '/services/general-surgery.html'],
  ['Obstetrics & Gynaecology', '/services/gynaecology.html'],
  ['Pain Management & Spine Care', '/services/pain-spine.html'],
  ['Orthopaedics', '/services/orthopaedics.html'],
  ['Urology', '/services/urology.html'],
  ['Neurosurgery', '/services/neurosurgery.html'],
  ['ENT', '/services/ent.html'],
  ['General Medicine', '/services/general-medicine.html'],
  ['Pathology', '/services/pathology.html']
];

const doctors = {
  surgery: { name: 'Dr Robin Bothra', anchor: 'robin-bothra', specialty: 'General & Laparoscopic Surgeon', qualification: 'MBBS, MS, FMAS', exp: '20+ years of experience', img: 'robin-bothra.jpg' },
  gyn: { name: 'Dr Chitra Soni', anchor: 'chitra-soni', specialty: 'Obstetrics, Gynaecology & Fertility', qualification: 'MBBS, MS (Obstetrics & Gynaecology)', exp: '15+ years of experience', img: 'chitra-soni.jpg' },
  pain: { name: 'Dr Naveen Soni', anchor: 'naveen-soni', specialty: 'Interventional Pain Physician - Spine & Pain', qualification: 'MBBS, MD, FIPM (Germany), MISS-EPP', exp: '15+ years of experience', img: 'naveen-soni.jpg' },
  ortho: { name: 'Dr Chirag Jain', anchor: 'chirag-jain', specialty: 'Orthopaedic, Joint Replacement & Trauma Surgeon', qualification: 'MBBS, MS (Orthopaedics)', exp: '10+ years of experience', img: 'chirag-jain.jpg' },
  uro: { name: 'Dr R N Daga', anchor: 'rn-daga', specialty: 'Urologist & Andrologist', qualification: 'MBBS, MS, M.Ch (Urology)', exp: '20+ years of experience', img: 'rn-daga.jpg' },
  neuro: { name: 'Dr Pavan Jain', anchor: 'pavan-jain', specialty: 'Neurosurgeon - Brain & Spine', qualification: 'MBBS, MS, M.Ch (Neurosurgery)', exp: '15+ years of experience', img: 'pavan-jain.jpg' },
  ent: { name: 'Dr N S Rathore', anchor: 'ns-rathore', specialty: 'ENT Surgeon', qualification: 'MBBS, MS (ENT)', exp: '10+ years of experience', img: 'ns-rathore.jpg' },
  med: { name: 'Dr Vishnu Gupta', anchor: 'vishnu-gupta', specialty: 'Consultant Physician - General Medicine', qualification: 'MBBS, MD (General Medicine)', exp: '10+ years of experience', img: 'vishnu-gupta.jpg' },
  path: { name: 'Dr Vinita Jain', anchor: 'vinita-jain', specialty: 'Consultant Pathologist', qualification: 'MBBS, MD (Pathology)', exp: '20+ years of experience', img: 'vinita-jain.jpg' }
};

const ownerDoctors = [doctors.surgery, doctors.gyn, doctors.pain, doctors.path];

const servicePages = [
  {
    slug: 'general-surgery', title: 'General & Laparoscopic Surgery in Jaipur | RNMH Nirman Nagar',
    meta: 'Consult experienced general and laparoscopic surgeons at R N Multispeciality Hospital, Jaipur, for piles, hernia, gall bladder, appendix and other surgical treatments. Book an appointment today.',
    h1: 'General & Laparoscopic Surgery in Jaipur', specialty: 'General & Laparoscopic Surgery', dept: 'general-surgery',
    img: 'general-surgery.jpg', doctor: doctors.surgery,
    intro: 'R N Multispeciality Hospital provides general and laparoscopic surgery in Nirman Nagar, Jaipur for conditions such as piles, hernia, gall bladder stones, appendix problems, fissure, fistula, varicose veins and diabetic foot concerns.',
    treats: ['Laparoscopic gall bladder, hernia and appendix surgery', 'Laser and stapler treatment for piles, fissure and fistula', 'Breast, thyroid and cancer surgery where indicated', 'ZSR circumcision and hypospadias surgery', 'Varicose veins and diabetic foot care'],
    treatmentLinks: ['laser-piles-treatment-jaipur', 'hernia-surgery-jaipur', 'gall-bladder-stone-surgery-jaipur', 'appendix-surgery-jaipur', 'laparoscopic-surgeon-jaipur'],
    procedure: 'General and Laparoscopic Surgery',
    faqs: [
      ['Is laparoscopic surgery available at RNMH Jaipur?', 'Yes. R N Multispeciality Hospital offers laparoscopic surgery in Jaipur for conditions such as hernia, gall bladder stones, appendix and other surgical needs. Suitability depends on doctor evaluation.'],
      ['Is laser piles treatment available at RNMH?', 'Yes. Laser treatment for piles is available at RNMH, subject to consultation, diagnosis and the grade of piles.'],
      ['Can I use cashless insurance for surgery?', 'Cashless insurance may be available depending on the patient\'s insurance provider, policy terms and TPA approval.'],
      ['How do I book an appointment with a surgeon?', 'You can book an appointment through WhatsApp or call 0141 239 0320.']
    ]
  },
  {
    slug: 'gynaecology', title: 'Gynaecology, Pregnancy & Fertility Care in Jaipur | RNMH',
    meta: 'Obstetrics, gynaecology, pregnancy care, high-risk pregnancy, delivery support, infertility and laparoscopic gynaecology at R N Multispeciality Hospital, Jaipur.',
    h1: 'Gynaecology & Pregnancy Care in Jaipur', specialty: 'Obstetrics & Gynaecology', dept: 'gynaecology',
    img: 'gynaecology.jpg', doctor: doctors.gyn,
    intro: 'R N Multispeciality Hospital provides women\'s health, pregnancy, delivery and fertility care in Nirman Nagar, Jaipur, supported by NICU, diagnostics, operation theatre and 24x7 hospital facilities.',
    treats: ['Normal, painless and caesarean delivery', 'High-risk pregnancy care', 'Laparoscopic gynaecology, hysteroscopy and infertility care', 'Fibroid, ovarian cyst and menstrual problem evaluation', 'Cosmetic gynaecology and laser procedures where suitable'],
    treatmentLinks: ['gynaecologist-nirman-nagar-jaipur', 'pregnancy-care-hospital-jaipur', 'high-risk-pregnancy-care-jaipur', 'painless-delivery-hospital-jaipur'],
    procedure: 'Obstetrics and Gynaecology',
    faqs: [
      ['Do you offer pregnancy care in Jaipur?', 'Yes. R N Multispeciality Hospital offers pregnancy care in Jaipur, including routine antenatal visits, high-risk pregnancy support and delivery planning.'],
      ['Is painless delivery available?', 'Epidural or painless delivery support may be available after assessment by the obstetrician and anaesthesia team. Suitability varies by patient condition.'],
      ['Is NICU available at RNMH?', 'Yes. NICU support is available for newborn care when needed.'],
      ['How can I book with a gynaecologist?', 'You can book on WhatsApp or call 0141 239 0320.']
    ]
  },
  {
    slug: 'pain-spine', title: 'Pain Management & Spine Treatment in Jaipur | RNMH Nirman Nagar',
    meta: 'Back pain, slip disc, sciatica, neck pain and joint pain treatment in Jaipur with interventional pain and spine care at R N Multispeciality Hospital.',
    h1: 'Pain Management & Spine Care in Jaipur', specialty: 'Pain Management & Spine Care', dept: 'pain-spine',
    img: 'pain-spine.jpg', doctor: doctors.pain,
    intro: 'R N Multispeciality Hospital provides pain management and spine care in Nirman Nagar, Jaipur for back pain, slip disc, sciatica, neck pain, joint pain, migraine and nerve-related pain.',
    treats: ['Back pain, neck pain and slip disc evaluation', 'Sciatica and nerve pain treatment', 'Knee, shoulder, hip and joint pain care', 'Nerve blocks and image-guided pain procedures', 'Minimally invasive spine procedures where suitable'],
    treatmentLinks: ['back-pain-treatment-jaipur', 'slip-disc-treatment-jaipur', 'sciatica-treatment-jaipur', 'spine-specialist-jaipur'],
    procedure: 'Pain Management and Spine Care',
    faqs: [
      ['Can slip disc and sciatica be treated without open surgery?', 'Many patients improve with medicines, physiotherapy, pain procedures or minimally invasive options. The right treatment depends on diagnosis and doctor evaluation.'],
      ['When should I see a spine specialist?', 'Consult a doctor if back pain travels to the leg, causes numbness or weakness, follows an injury, or does not improve with initial care.'],
      ['Who treats pain and spine conditions at RNMH?', 'Dr Naveen Soni leads pain management and spine care at R N Multispeciality Hospital.'],
      ['How do I book an appointment?', 'Book on WhatsApp or call 0141 239 0320.']
    ]
  },
  {
    slug: 'orthopaedics', title: 'Orthopaedic Doctor, Knee Pain & Fracture Care in Jaipur | RNMH',
    meta: 'Orthopaedic consultation, knee pain treatment, fracture care, arthroscopy and joint replacement services at R N Multispeciality Hospital, Jaipur.',
    h1: 'Orthopaedics & Joint Care in Jaipur', specialty: 'Orthopaedics', dept: 'orthopaedics',
    img: 'orthopaedics.jpg', doctor: doctors.ortho,
    intro: 'R N Multispeciality Hospital offers orthopaedic consultation, fracture care, arthroscopy, trauma care and joint replacement support in Nirman Nagar, Jaipur.',
    treats: ['Knee, hip, shoulder and joint pain', 'Fractures and trauma care', 'Arthroscopy and keyhole joint surgery', 'Knee and hip replacement evaluation', 'Sports injuries and ligament concerns'],
    treatmentLinks: ['orthopaedic-doctor-jaipur', 'knee-pain-treatment-jaipur', 'fracture-treatment-jaipur', 'knee-replacement-surgeon-jaipur'],
    procedure: 'Orthopaedic Care',
    faqs: [
      ['Do you treat fractures in Jaipur?', 'Yes. R N Multispeciality Hospital provides fracture and trauma care with orthopaedic consultation and hospital support.'],
      ['When should I see an orthopaedic doctor for knee pain?', 'See a doctor if knee pain persists, limits walking, follows an injury, causes swelling, or does not improve with basic care.'],
      ['Is knee replacement available?', 'Knee replacement evaluation and surgical planning are available when clinically indicated.'],
      ['Can I book on WhatsApp?', 'Yes. You can book on WhatsApp or call 0141 239 0320.']
    ]
  },
  {
    slug: 'urology', title: 'Kidney Stone, Prostate & Urology Treatment in Jaipur | RNMH',
    meta: 'Kidney stone treatment, laser stone surgery, prostate care and urology consultation in Nirman Nagar, Jaipur at R N Multispeciality Hospital.',
    h1: 'Urology & Kidney Stone Treatment in Jaipur', specialty: 'Urology', dept: 'urology',
    img: 'urology.jpg', doctor: doctors.uro,
    intro: 'R N Multispeciality Hospital provides urology consultation and treatment in Nirman Nagar, Jaipur for kidney stones, ureteric stones, prostate enlargement and other urinary problems.',
    treats: ['Kidney and ureteric stone treatment', 'Laser and keyhole urology procedures where suitable', 'Prostate enlargement evaluation and TURP', 'Urinary infection and urinary difficulty', 'Urological cancer evaluation and referral support'],
    treatmentLinks: ['kidney-stone-treatment-jaipur', 'laser-kidney-stone-surgery-jaipur', 'urologist-nirman-nagar-jaipur'],
    procedure: 'Urology Treatment',
    faqs: [
      ['Can kidney stones be treated with laser surgery?', 'Laser treatment may be suitable for many kidney or ureteric stones, depending on stone size, location and doctor evaluation.'],
      ['Who is the urologist at RNMH?', 'Dr R N Daga provides urology and andrology care at R N Multispeciality Hospital.'],
      ['Is cashless insurance available for urology procedures?', 'Cashless insurance may be available subject to policy terms, provider rules and TPA approval.'],
      ['How do I book a urology appointment?', 'Book on WhatsApp or call 0141 239 0320.']
    ]
  },
  {
    slug: 'neurosurgery', title: 'Neurosurgery & Brain-Spine Surgery in Jaipur | RNMH',
    meta: 'Neurosurgery and brain-spine consultation in Jaipur for brain tumours, spine surgery, spine fractures and neurological surgical conditions at RNMH.',
    h1: 'Neurosurgery in Jaipur', specialty: 'Neurosurgery', dept: 'neurosurgery',
    img: 'neurosurgery.jpg', doctor: doctors.neuro,
    intro: 'R N Multispeciality Hospital provides neurosurgery and brain-spine consultation in Nirman Nagar, Jaipur for selected brain and spine conditions.',
    treats: ['Brain tumour and head injury evaluation', 'Complex and minimally invasive spine surgery planning', 'Spinal tumour and traumatic spine fracture care', 'Degenerative spine disease', 'Non-surgical and surgical guidance based on diagnosis'],
    treatmentLinks: ['spine-specialist-jaipur', 'slip-disc-treatment-jaipur', 'back-pain-treatment-jaipur'],
    procedure: 'Neurosurgery',
    faqs: [
      ['When should I consult a neurosurgeon?', 'Consult a neurosurgeon for severe neurological symptoms, brain or spine injury, progressive weakness, spinal tumour concerns or conditions requiring surgical opinion.'],
      ['Is all spine surgery open surgery?', 'No. Some spine conditions may be managed with minimally invasive or motion-preserving techniques, while others may not need surgery.'],
      ['Who provides neurosurgery care at RNMH?', 'Dr Pavan Jain provides neurosurgery and brain-spine care at R N Multispeciality Hospital.'],
      ['How can I book?', 'Book on WhatsApp or call 0141 239 0320.']
    ]
  },
  {
    slug: 'ent', title: 'ENT Specialist & Ear Nose Throat Surgery in Jaipur | RNMH',
    meta: 'ENT consultation and surgery in Jaipur for ear, nose, throat, sinus, tonsil, hearing and paediatric ENT problems at R N Multispeciality Hospital.',
    h1: 'ENT Care in Jaipur', specialty: 'ENT', dept: 'ent',
    img: 'ent.jpg', doctor: doctors.ent,
    intro: 'R N Multispeciality Hospital provides ENT care in Nirman Nagar, Jaipur for adults and children with ear, nose and throat concerns.',
    treats: ['Ear infection, hearing and balance concerns', 'Sinus, nasal blockage and allergy-related problems', 'Tonsil, adenoid and throat conditions', 'ENT surgery where clinically indicated', 'Paediatric ENT consultation'],
    treatmentLinks: [],
    procedure: 'ENT Care',
    faqs: [
      ['What ENT problems are treated at RNMH?', 'Ear infections, hearing concerns, sinusitis, nasal blockage, tonsil problems, throat conditions and ENT surgical needs are evaluated.'],
      ['Do you treat children with ENT problems?', 'Yes. ENT consultation is available for children as well as adults.'],
      ['Who is the ENT specialist?', 'Dr N S Rathore provides ENT care at R N Multispeciality Hospital.'],
      ['How can I book an ENT appointment?', 'Book on WhatsApp or call 0141 239 0320.']
    ]
  },
  {
    slug: 'general-medicine', title: 'General Physician & Medicine Specialist in Jaipur | RNMH',
    meta: 'General medicine and physician consultation in Jaipur for diabetes, thyroid, blood pressure, fever, respiratory and seasonal illness at RNMH.',
    h1: 'General Medicine in Jaipur', specialty: 'General Medicine', dept: 'general-medicine',
    img: 'general-medicine.jpg', doctor: doctors.med,
    intro: 'R N Multispeciality Hospital provides general medicine and consultant physician care in Nirman Nagar, Jaipur for common, chronic and seasonal health concerns.',
    treats: ['Diabetes, thyroid and blood pressure management', 'Fever, infection and seasonal illness', 'Respiratory, gastric and migraine concerns', 'Preventive health checks and lab monitoring', 'Referral coordination with specialists when needed'],
    treatmentLinks: [],
    procedure: 'General Medicine Consultation',
    faqs: [
      ['What does a general physician treat?', 'A general physician evaluates common and chronic adult health concerns such as diabetes, thyroid, blood pressure, fever, respiratory symptoms and gastric problems.'],
      ['Are lab tests available in-house?', 'Yes. In-house laboratory and diagnostics support evaluation and follow-up.'],
      ['Who leads general medicine?', 'Dr Vishnu Gupta provides general medicine care at R N Multispeciality Hospital.'],
      ['How do I book?', 'Book on WhatsApp or call 0141 239 0320.']
    ]
  },
  {
    slug: 'pathology', title: 'Pathology Lab & Diagnostics in Jaipur | RNMH Nirman Nagar',
    meta: 'In-house pathology lab and diagnostics in Jaipur including blood tests, histopathology, X-ray, sonography, colour Doppler and ECG at RNMH.',
    h1: 'Pathology & Diagnostics in Jaipur', specialty: 'Pathology', dept: 'pathology',
    img: 'pathology.jpg', doctor: doctors.path,
    intro: 'R N Multispeciality Hospital provides in-house pathology and diagnostic support in Nirman Nagar, Jaipur for outpatient, emergency and admitted patients.',
    treats: ['Routine and specialised blood tests', 'Histopathology and diagnostic lab support', 'X-ray, sonography, colour Doppler and ECG', 'Health check-up packages', 'Timely reporting for admitted and urgent patients'],
    treatmentLinks: [],
    procedure: 'Pathology and Diagnostics',
    faqs: [
      ['What diagnostics are available at RNMH?', 'R N Multispeciality Hospital has an in-house laboratory, X-ray, sonography, colour Doppler and ECG.'],
      ['Who leads pathology?', 'Dr Vinita Jain leads pathology and diagnostic laboratory services.'],
      ['Are tests available for admitted patients?', 'Yes. Diagnostics support outpatient, emergency and admitted patients.'],
      ['How do I ask about test availability?', 'Call 0141 239 0320 or message on WhatsApp.']
    ]
  }
];

const treatmentPages = [
  ['laser-piles-treatment-jaipur', 'Laser Piles Treatment in Jaipur', 'surgery', 'Laser piles treatment consultation and surgical care in Jaipur at R N Multispeciality Hospital, Nirman Nagar.', doctors.surgery, 'general-surgery', ['Bleeding during stool', 'Pain or swelling near the anus', 'Itching or discomfort', 'Recurrent constipation with pain', 'Symptoms that do not improve with medication'], ['Clinical examination by a surgeon', 'Proctoscopy or related evaluation where needed', 'Assessment of grade and severity'], ['Medicines and lifestyle changes', 'Minimally invasive procedures', 'Laser treatment where suitable', 'Surgery when clinically indicated'], ['Is laser piles treatment available at RNMH Jaipur?', 'Yes. Laser treatment for piles is available after consultation and diagnosis.'], 'hi/laser-piles-treatment-jaipur'],
  ['hernia-surgery-jaipur', 'Hernia Surgery in Jaipur', 'surgery', 'Hernia surgery consultation and laparoscopic hernia repair options in Jaipur at RNMH.', doctors.surgery, 'general-surgery', ['Swelling in the groin, abdomen or near a previous surgery scar', 'Pain or heaviness while lifting or coughing', 'A hernia that is increasing in size', 'Sudden severe pain or vomiting'], ['Physical examination', 'Ultrasound or imaging when required', 'Fitness evaluation before surgery'], ['Open or laparoscopic hernia repair', 'Mesh repair where suitable', 'Emergency surgery if strangulation is suspected'], ['Is laparoscopic hernia surgery available?', 'Yes. Laparoscopic hernia surgery may be available depending on hernia type and doctor evaluation.'], 'hi/hernia-surgery-jaipur'],
  ['gall-bladder-stone-surgery-jaipur', 'Gall Bladder Stone Surgery in Jaipur', 'surgery', 'Laparoscopic gall bladder stone surgery consultation in Jaipur at R N Multispeciality Hospital.', doctors.surgery, 'general-surgery', ['Pain in the right upper abdomen', 'Pain after oily meals', 'Nausea, vomiting or fever', 'Jaundice or severe abdominal pain'], ['Ultrasound abdomen', 'Blood tests including liver function tests', 'Surgical and anaesthesia fitness'], ['Laparoscopic gall bladder removal where indicated', 'Medicines for symptoms before planned surgery', 'Emergency care for complications'], ['Is gall bladder stone surgery laparoscopic?', 'Many gall bladder surgeries are done laparoscopically, but suitability depends on the patient and diagnosis.'], 'hi/gall-bladder-stone-surgery-jaipur'],
  ['appendix-surgery-jaipur', 'Appendix Surgery in Jaipur', 'surgery', 'Appendix pain evaluation and appendicitis surgery care in Jaipur at RNMH Nirman Nagar.', doctors.surgery, 'general-surgery', ['Pain around the navel moving to the lower right abdomen', 'Fever, nausea or vomiting', 'Loss of appetite', 'Worsening abdominal pain'], ['Clinical examination', 'Blood tests', 'Ultrasound or CT scan when needed'], ['Antibiotics and observation in selected cases', 'Laparoscopic or open appendix surgery when indicated', 'Emergency surgery for complicated appendicitis'], ['Is appendix surgery available 24x7?', 'Emergency care is available 24x7, and the surgical team evaluates appendix cases promptly.'], null],
  ['laparoscopic-surgeon-jaipur', 'Laparoscopic Surgeon in Jaipur', 'surgery', 'Consult a laparoscopic surgeon in Jaipur for hernia, gall bladder, appendix, piles and other surgical concerns at RNMH.', doctors.surgery, 'general-surgery', ['A doctor has advised surgery', 'You want a keyhole surgery opinion', 'Repeated abdominal pain or diagnosed stones', 'Hernia, piles, appendix or gall bladder symptoms'], ['Clinical consultation', 'Imaging and lab tests as needed', 'Fitness evaluation before surgery'], ['Laparoscopic surgery where suitable', 'Open surgery where safer or clinically required', 'Post-operative follow-up and recovery guidance'], ['Who is the laparoscopic surgeon at RNMH?', 'Dr Robin Bothra provides general and laparoscopic surgery care at R N Multispeciality Hospital.'], null],
  ['gynaecologist-nirman-nagar-jaipur', 'Gynaecologist in Nirman Nagar Jaipur', 'gynaecology', 'Consult a gynaecologist in Nirman Nagar, Jaipur at R N Multispeciality Hospital.', doctors.gyn, 'gynaecology', ['Irregular periods or heavy bleeding', 'Pregnancy confirmation or antenatal care', 'Pelvic pain or discharge', 'Infertility concerns', 'Menopause symptoms'], ['History and examination', 'Ultrasound where needed', 'Blood tests and other investigations'], ['Medicines and follow-up', 'Pregnancy and delivery care', 'Laparoscopy or hysteroscopy where indicated', 'Infertility counselling and treatment planning'], ['Who is the gynaecologist at RNMH?', 'Dr Chitra Soni provides gynaecology, obstetrics and fertility care at R N Multispeciality Hospital.'], null],
  ['pregnancy-care-hospital-jaipur', 'Pregnancy Care Hospital in Jaipur', 'gynaecology', 'Pregnancy care and delivery support in Jaipur at RNMH, near Mansarovar Metro Station.', doctors.gyn, 'gynaecology', ['Missed period or confirmed pregnancy', 'Regular antenatal check-ups', 'High-risk pregnancy factors', 'Reduced baby movement or bleeding', 'Labour pain or fluid leakage'], ['Antenatal check-ups', 'Ultrasound and blood tests', 'Blood pressure, sugar and fetal monitoring'], ['Routine antenatal care', 'High-risk pregnancy monitoring', 'Normal, painless or caesarean delivery planning', 'NICU support when needed'], ['Is delivery care available at RNMH?', 'Yes. Pregnancy and delivery care is available with hospital, operation theatre and NICU support.'], 'hi/pregnancy-care-hospital-jaipur'],
  ['high-risk-pregnancy-care-jaipur', 'High-Risk Pregnancy Care in Jaipur', 'gynaecology', 'High-risk pregnancy monitoring and delivery planning in Jaipur at R N Multispeciality Hospital.', doctors.gyn, 'gynaecology', ['High blood pressure or diabetes in pregnancy', 'Previous miscarriage or caesarean', 'Twins or growth concerns', 'Bleeding, pain or reduced movement', 'Pregnancy with medical illness'], ['Regular obstetric review', 'Ultrasound and fetal monitoring', 'Blood and urine investigations', 'Physician or specialist coordination when needed'], ['Close antenatal monitoring', 'Medicines and lifestyle advice', 'Planned delivery timing', 'Emergency hospital support when required'], ['Can high-risk pregnancy be managed at RNMH?', 'Yes. The team evaluates and monitors high-risk pregnancies with obstetric, diagnostic and hospital support.'], null],
  ['painless-delivery-hospital-jaipur', 'Painless Delivery Hospital in Jaipur', 'gynaecology', 'Painless delivery and pregnancy care options in Jaipur at R N Multispeciality Hospital.', doctors.gyn, 'gynaecology', ['You are planning delivery options', 'You want to understand epidural analgesia', 'Labour pain has started', 'You have a high-risk pregnancy factor'], ['Antenatal assessment', 'Labour room monitoring', 'Anaesthesia review where needed'], ['Normal delivery support', 'Epidural analgesia where suitable', 'Caesarean section if clinically required', 'NICU support for newborn care'], ['Is painless delivery possible for everyone?', 'No. Suitability for epidural or painless delivery varies by patient condition and anaesthesia assessment.'], null],
  ['back-pain-treatment-jaipur', 'Back Pain Treatment in Jaipur', 'pain', 'Back pain diagnosis and treatment in Jaipur at RNMH, Nirman Nagar.', doctors.pain, 'pain-spine', ['Back pain lasting more than a few days', 'Pain travelling to the leg', 'Numbness, tingling or weakness', 'Pain after injury', 'Difficulty walking or standing'], ['Clinical spine and neurological examination', 'X-ray, MRI or other imaging when needed', 'Assessment of posture, movement and nerve symptoms'], ['Medicines and physiotherapy', 'Image-guided pain procedures', 'Minimally invasive options where suitable', 'Surgical referral if needed'], ['Can back pain be treated without surgery?', 'Many back pain cases improve without surgery, but treatment depends on the diagnosis.'], 'hi/back-pain-treatment-jaipur'],
  ['slip-disc-treatment-jaipur', 'Slip Disc Treatment in Jaipur', 'pain', 'Slip disc and sciatica treatment options in Jaipur at R N Multispeciality Hospital.', doctors.pain, 'pain-spine', ['Back pain spreading to the leg', 'Numbness or tingling', 'Weakness in foot or leg', 'Pain that worsens while sitting or bending'], ['Clinical examination', 'MRI when indicated', 'Nerve symptom assessment'], ['Medicines and guided exercises', 'Nerve root blocks or pain procedures', 'Ozone discectomy or endoscopic options where suitable', 'Surgery if urgently required'], ['Is slip disc always treated with surgery?', 'No. Many patients are treated without open surgery, depending on symptoms and MRI findings.'], 'hi/slip-disc-treatment-jaipur'],
  ['sciatica-treatment-jaipur', 'Sciatica Treatment in Jaipur', 'pain', 'Sciatica pain evaluation and treatment in Jaipur at RNMH near Mansarovar Metro Station.', doctors.pain, 'pain-spine', ['Pain from lower back to buttock or leg', 'Burning, electric or shooting pain', 'Numbness or tingling', 'Weakness or walking difficulty'], ['Neurological examination', 'MRI or imaging when needed', 'Evaluation of disc, nerve and spine causes'], ['Medicines and physiotherapy', 'Nerve blocks or epidural injections', 'Minimally invasive spine procedures where suitable'], ['What causes sciatica?', 'Sciatica is commonly caused by irritation or compression of a nerve in the lower spine, often due to a disc problem.'], null],
  ['spine-specialist-jaipur', 'Spine Specialist in Jaipur', 'pain', 'Consult a spine specialist in Jaipur for back pain, slip disc, sciatica and spine conditions at RNMH.', doctors.pain, 'pain-spine', ['Persistent back or neck pain', 'Pain spreading to arm or leg', 'Numbness, weakness or balance issues', 'Spine injury or fracture concern'], ['Spine examination', 'X-ray, MRI or CT when required', 'Pain and nerve assessment'], ['Non-surgical pain management', 'Minimally invasive spine procedures', 'Neurosurgical opinion when needed'], ['Which doctor should I see for spine pain?', 'An interventional pain physician or spine specialist can evaluate back pain, slip disc and sciatica, and guide treatment.'], null],
  ['kidney-stone-treatment-jaipur', 'Kidney Stone Treatment in Jaipur', 'urology', 'Kidney stone diagnosis and treatment in Jaipur at RNMH, Nirman Nagar.', doctors.uro, 'urology', ['Severe pain in side or back', 'Burning urination or blood in urine', 'Nausea, vomiting or fever', 'Repeated urinary infection'], ['Urine tests and blood tests', 'Ultrasound or CT KUB', 'Stone size and location assessment'], ['Medicines and hydration advice for small stones', 'URS, PCNL or laser procedures where suitable', 'Emergency care if infection or obstruction is present'], ['Is kidney stone treatment available at RNMH?', 'Yes. Kidney stone evaluation and treatment options are available with urology consultation.'], 'hi/kidney-stone-treatment-jaipur'],
  ['laser-kidney-stone-surgery-jaipur', 'Laser Kidney Stone Surgery in Jaipur', 'urology', 'Laser kidney stone surgery consultation in Jaipur at R N Multispeciality Hospital.', doctors.uro, 'urology', ['Stone pain that does not settle', 'Stone causing blockage', 'Recurrent stones', 'Blood in urine or infection with stone'], ['Ultrasound or CT scan', 'Urine and kidney function tests', 'Anaesthesia fitness if surgery is planned'], ['Laser stone surgery where suitable', 'URS or PCNL based on stone site and size', 'Stent placement when needed'], ['Is laser stone surgery suitable for every stone?', 'No. Suitability depends on stone size, location, kidney function and doctor evaluation.'], null],
  ['urologist-nirman-nagar-jaipur', 'Urologist in Nirman Nagar Jaipur', 'urology', 'Consult a urologist in Nirman Nagar Jaipur at R N Multispeciality Hospital.', doctors.uro, 'urology', ['Kidney stone symptoms', 'Difficulty or burning urination', 'Blood in urine', 'Prostate or male health concerns', 'Repeated urinary infections'], ['Clinical evaluation by urologist', 'Urine tests, ultrasound or CT where needed', 'Kidney function and prostate tests when indicated'], ['Medicines and follow-up', 'Laser or endoscopic procedures where suitable', 'Surgery when clinically required'], ['Who is the urologist at RNMH?', 'Dr R N Daga provides urology and andrology care at R N Multispeciality Hospital.'], null],
  ['orthopaedic-doctor-jaipur', 'Orthopaedic Doctor in Jaipur', 'orthopaedics', 'Consult an orthopaedic doctor in Jaipur for joint pain, fracture, trauma and sports injuries at RNMH.', doctors.ortho, 'orthopaedics', ['Joint pain or swelling', 'Fracture or injury', 'Difficulty walking', 'Sports injury', 'Long-standing knee, hip or shoulder pain'], ['Orthopaedic examination', 'X-ray or MRI when needed', 'Assessment of movement, stability and pain'], ['Medicines, rest and physiotherapy', 'Plaster, brace or fracture procedure', 'Arthroscopy or joint replacement where indicated'], ['Who is the orthopaedic doctor at RNMH?', 'Dr Chirag Jain provides orthopaedic, joint replacement and trauma care.'], null],
  ['knee-pain-treatment-jaipur', 'Knee Pain Treatment in Jaipur', 'orthopaedics', 'Knee pain diagnosis and treatment in Jaipur at R N Multispeciality Hospital.', doctors.ortho, 'orthopaedics', ['Knee pain while walking or climbing stairs', 'Swelling, locking or instability', 'Pain after injury', 'Pain that limits daily activity'], ['Clinical knee examination', 'X-ray or MRI when needed', 'Assessment for arthritis, ligament or meniscus injury'], ['Medicines and physiotherapy', 'Injections or arthroscopy where suitable', 'Knee replacement evaluation for advanced arthritis'], ['When should I see a doctor for knee pain?', 'See a doctor if pain persists, swelling is present, movement is limited or walking becomes difficult.'], null],
  ['fracture-treatment-jaipur', 'Fracture Treatment in Jaipur', 'orthopaedics', 'Fracture and trauma care in Jaipur at RNMH, a 24x7 hospital in Nirman Nagar.', doctors.ortho, 'orthopaedics', ['Pain, swelling or deformity after injury', 'Inability to move or bear weight', 'Open wound with suspected fracture', 'Numbness or severe pain'], ['X-ray and clinical examination', 'CT scan where needed', 'Assessment of blood supply and nerve function'], ['Splint, plaster or brace', 'Closed reduction where suitable', 'Surgery and fixation when required'], ['Is emergency fracture care available?', 'Yes. 24x7 emergency care is available, with orthopaedic evaluation arranged as needed.'], null],
  ['knee-replacement-surgeon-jaipur', 'Knee Replacement Surgeon in Jaipur', 'orthopaedics', 'Knee replacement evaluation and orthopaedic surgery planning in Jaipur at RNMH.', doctors.ortho, 'orthopaedics', ['Severe knee arthritis', 'Pain despite medicines and physiotherapy', 'Difficulty walking or climbing stairs', 'Bent or deformed knee'], ['X-ray and clinical assessment', 'Medical fitness evaluation', 'Discussion of benefits, risks and recovery'], ['Non-surgical care for early arthritis', 'Partial or total knee replacement where indicated', 'Physiotherapy-led recovery plan'], ['Is knee replacement right for every knee pain patient?', 'No. Knee replacement is considered when arthritis is advanced and non-surgical care is no longer helping.'], null],
  ['24x7-emergency-hospital-jaipur', '24x7 Emergency Hospital in Nirman Nagar Jaipur', 'emergency', '24x7 emergency hospital care in Nirman Nagar, Jaipur near Mansarovar Metro Station at RNMH.', doctors.surgery, 'general-surgery', ['Severe chest pain, breathing difficulty or fainting', 'Accident, fracture or head injury', 'Severe abdominal pain', 'High fever with danger signs', 'Pregnancy emergency'], ['Emergency triage and doctor assessment', 'Vitals, ECG, lab tests and imaging as needed', 'Specialist referral inside the hospital'], ['Emergency stabilisation', 'ICU/NICU support where needed', 'Surgery or admission if clinically required'], ['Is RNMH open 24x7?', 'Yes. R N Multispeciality Hospital provides 24x7 emergency care in Nirman Nagar, Jaipur.'], 'hi/24x7-emergency-hospital-jaipur'],
  ['emergency-hospital-near-mansarovar-metro-station', 'Emergency Hospital near Mansarovar Metro Station', 'emergency', 'Emergency hospital near Mansarovar Metro Station, Nirman Nagar Jaipur, open 24x7.', doctors.med, 'general-medicine', ['Sudden illness or injury near Mansarovar Metro Station', 'Road accident or fracture', 'Severe pain, fever or breathing symptoms', 'Pregnancy or surgical emergency'], ['Emergency evaluation', 'Lab, X-ray, ECG and sonography support', 'Specialist consultation where needed'], ['24x7 emergency care', 'ICU/NICU support', 'Admission, surgery or transfer decisions based on clinical need'], ['Where is RNMH located?', 'RNMH is located at 109-110, Shiv Shakti Nagar, Kings Road, Nirman Nagar, near Mansarovar Metro Station.'], null],
  ['cashless-hospital-jaipur', 'Cashless Hospital in Jaipur', 'insurance', 'Cashless insurance and TPA support in Jaipur at R N Multispeciality Hospital.', doctors.surgery, 'general-surgery', ['Planned surgery or admission with health insurance', 'Emergency admission needing insurance help', 'Questions about TPA approval', 'Government scheme eligibility'], ['Policy and card verification', 'TPA or insurer pre-authorisation', 'Estimate and document review'], ['Cashless admission support where approved', 'TPA coordination', 'Government scheme assistance where applicable'], ['Does RNMH offer cashless insurance?', 'Yes. Cashless insurance and TPA support are available subject to policy terms, insurer rules and approval.'], 'hi/cashless-hospital-jaipur'],
  ['rghs-hospital-jaipur', 'RGHS Hospital in Jaipur', 'insurance', 'RGHS support and government scheme assistance in Jaipur at R N Multispeciality Hospital.', doctors.med, 'general-medicine', ['You are covered under RGHS', 'Planned procedure or admission', 'Emergency care needing scheme help', 'Documents need verification'], ['RGHS eligibility and document check', 'Medical evaluation', 'Approval process as applicable'], ['RGHS support where applicable', 'Cashless or scheme-based treatment subject to approval', 'Admission and documentation assistance'], ['Is RGHS accepted at RNMH?', 'RGHS support is available where applicable and subject to scheme rules and approval.'], null],
  ['pm-jay-hospital-jaipur', 'PM-JAY Hospital in Jaipur', 'insurance', 'PM-JAY and Ayushman Bharat support in Jaipur at R N Multispeciality Hospital.', doctors.med, 'general-medicine', ['You have PM-JAY eligibility', 'Planned surgery or admission', 'Emergency care requiring scheme support', 'Need help checking documents'], ['Eligibility check', 'Doctor evaluation', 'Scheme approval process as applicable'], ['PM-JAY support where applicable', 'Covered procedure guidance', 'Admission assistance subject to approval'], ['Is PM-JAY available at RNMH?', 'PM-JAY support is available where applicable, subject to scheme rules and approval.'], null],
  ['maa-yojana-hospital-jaipur', 'MAA Yojana Hospital in Jaipur', 'insurance', 'MAA Yojana hospital support in Jaipur at R N Multispeciality Hospital.', doctors.med, 'general-medicine', ['You want to check MAA Yojana eligibility', 'Planned treatment or admission', 'Emergency hospital care', 'Need help with scheme documents'], ['Eligibility and document check', 'Doctor consultation', 'Scheme process and approval'], ['MAA Yojana support where applicable', 'Cashless or scheme support subject to approval', 'Hospital admission assistance'], ['Is MAA Yojana supported at RNMH?', 'MAA Yojana support is available where applicable, subject to scheme rules and approval.'], null]
];

const hiPages = {
  'laser-piles-treatment-jaipur': ['जयपुर में पाइल्स का लेजर इलाज', 'पाइल्स (Piles) के लिए जयपुर में परामर्श और लेजर इलाज की सुविधा R N Multispeciality Hospital में उपलब्ध है।', doctors.surgery, 'general-surgery'],
  'hernia-surgery-jaipur': ['जयपुर में हर्निया ऑपरेशन', 'हर्निया (Hernia) के ऑपरेशन और लेप्रोस्कोपिक सर्जरी के लिए RNMH, निर्माण नगर जयपुर में परामर्श उपलब्ध है।', doctors.surgery, 'general-surgery'],
  'gall-bladder-stone-surgery-jaipur': ['जयपुर में पित्त की थैली की पथरी का ऑपरेशन', 'पित्त की थैली की पथरी (Gall Bladder Stone) के लिए लेप्रोस्कोपिक सर्जरी परामर्श RNMH में उपलब्ध है।', doctors.surgery, 'general-surgery'],
  'pregnancy-care-hospital-jaipur': ['जयपुर में गर्भावस्था और डिलीवरी अस्पताल', 'गर्भावस्था, हाई-रिस्क प्रेग्नेंसी और डिलीवरी के लिए RNMH, निर्माण नगर जयपुर में देखभाल उपलब्ध है।', doctors.gyn, 'gynaecology'],
  'back-pain-treatment-jaipur': ['जयपुर में कमर दर्द और स्लिप डिस्क का इलाज', 'कमर दर्द, स्लिप डिस्क (Slip Disc) और साइटिका (Sciatica) के लिए RNMH में स्पाइन और पेन मैनेजमेंट परामर्श उपलब्ध है।', doctors.pain, 'pain-spine'],
  'slip-disc-treatment-jaipur': ['जयपुर में स्लिप डिस्क का इलाज', 'स्लिप डिस्क (Slip Disc) और नस दबने के दर्द के लिए RNMH में जांच और उपचार विकल्प उपलब्ध हैं।', doctors.pain, 'pain-spine'],
  'kidney-stone-treatment-jaipur': ['जयपुर में किडनी स्टोन का इलाज', 'किडनी स्टोन (Kidney Stone) के लिए यूरोलॉजी परामर्श और लेजर उपचार विकल्प RNMH में उपलब्ध हैं।', doctors.uro, 'urology'],
  '24x7-emergency-hospital-jaipur': ['निर्माण नगर जयपुर में 24 घंटे इमरजेंसी अस्पताल', 'R N Multispeciality Hospital निर्माण नगर, जयपुर में 24x7 इमरजेंसी केयर उपलब्ध कराता है।', doctors.surgery, 'general-surgery'],
  'cashless-hospital-jaipur': ['जयपुर में कैशलेस अस्पताल', 'RNMH में कैशलेस इंश्योरेंस, TPA, RGHS, PM-JAY और MAA Yojana सहायता नियमों और अप्रूवल के अनुसार उपलब्ध है।', doctors.surgery, 'general-surgery']
};

const treatmentBySlug = Object.fromEntries(treatmentPages.map((p) => [p[0], p]));
const serviceBySlug = Object.fromEntries(servicePages.map((p) => [p.slug, p]));

function esc(s) {
  return String(s).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
}

function jsonLd(data) {
  return `<script type="application/ld+json">\n${JSON.stringify(data, null, 2).replaceAll('</', '<\\/')}\n</script>`;
}

function languageRedirectScript() {
  return `<script>
(function(){
  try {
    var params = new URLSearchParams(window.location.search);
    var chosen = params.get('lang');
    if (chosen === 'en' || chosen === 'hi') localStorage.setItem('rnmhLang', chosen);
    if (chosen === 'en') return;
    if (localStorage.getItem('rnmhLang') === 'en') return;
    var path = window.location.pathname || '';
    var isHome = path === '/' || path.endsWith('/index.html') || path.endsWith('/site/index.html');
    if (!isHome) return;
    var langs = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || ''];
    var wantsHindi = langs.some(function(lang){ return /^hi\\b/i.test(lang); });
    if (!wantsHindi) return;
    localStorage.setItem('rnmhLang', 'hi');
    window.location.replace('hi/index.html' + (window.location.hash || ''));
  } catch (error) {}
})();
</script>`;
}

function relPrefix(kind) {
  if (kind === 'root') return '';
  if (kind === 'service' || kind === 'treatment') return '../';
  if (kind === 'hi-treatment') return '../../';
  return '';
}

function topbar(prefix) {
  return `<div class="topbar"><div class="wrap"><span>Open 24x7 · Near Mansarovar Metro Station, Nirman Nagar, Jaipur</span><span>Call <a href="tel:${hospital.tel}" class="js-phone-link"><span class="js-phone-display">${hospital.phone}</span></a> · <a href="#" class="js-wa">Book on WhatsApp</a></span></div></div>`;
}

function topbarHi(prefix) {
  return `<div class="topbar"><div class="wrap"><span>24x7 खुला · मानसरोवर मेट्रो स्टेशन के पास, निर्माण नगर, जयपुर</span><span>कॉल <a href="tel:${hospital.tel}" class="js-phone-link"><span class="js-phone-display">${hospital.phone}</span></a> · <a href="#" class="js-wa">WhatsApp पर बुक करें</a></span></div></div>`;
}

function header(prefix, langHref = '') {
  const lang = langHref ? `<a class="lang" href="${langHref}">हिन्दी</a>` : '';
  return `<header class="nav"><div class="wrap">
  <a class="brand" href="${prefix}index.html"><img src="${prefix}assets/img/logo.png" alt="R N Multispeciality Hospital logo"><span>RNMH<small>inspiring better health</small></span></a>
  <nav class="menu"><a href="${prefix}index.html">Home</a><a href="${prefix}index.html#specialities">Specialities</a><a href="${prefix}doctors.html">Doctors</a><a href="${prefix}index.html#facilities">Facilities</a><a href="${prefix}index.html#reviews">Reviews</a><a href="${prefix}contact.html">Contact</a>${lang}<a class="btn btn-primary js-wa" href="#">Book appointment</a></nav>
  <button class="burger" id="burger" aria-label="Menu">☰</button>
</div>
<div class="mobile-menu" id="mobileMenu"><a href="${prefix}index.html">Home</a><a href="${prefix}index.html#specialities">Specialities</a><a href="${prefix}doctors.html">Doctors</a><a href="${prefix}index.html#facilities">Facilities</a><a href="${prefix}index.html#reviews">Reviews</a><a href="${prefix}contact.html">Contact</a>${langHref ? `<a href="${langHref}">हिन्दी</a>` : ''}<a class="btn btn-primary js-wa" href="#" style="margin-top:8px; display:inline-block; text-align:center;">Book appointment</a></div>
</header>`;
}

function headerHi(prefix, langHref = '') {
  const lang = langHref ? `<a class="lang" href="${langHref}">English</a>` : '';
  return `<header class="nav"><div class="wrap">
  <a class="brand" href="${prefix}hi/index.html"><img src="${prefix}assets/img/logo.png" alt="आर एन मल्टीस्पेशलिटी हॉस्पिटल लोगो"><span>RNMH<small>inspiring better health</small></span></a>
  <nav class="menu"><a href="${prefix}hi/index.html">होम</a><a href="${prefix}hi/index.html#specialities">विभाग</a><a href="${prefix}hi/doctors.html">डॉक्टर</a><a href="${prefix}hi/index.html#facilities">सुविधाएँ</a><a href="${prefix}hi/index.html#reviews">समीक्षाएँ</a><a href="${prefix}hi/contact.html">संपर्क</a>${lang}<a class="btn btn-primary js-wa" href="#">अपॉइंटमेंट बुक करें</a></nav>
  <button class="burger" id="burger" aria-label="मेनू">☰</button>
</div>
<div class="mobile-menu" id="mobileMenu"><a href="${prefix}hi/index.html">होम</a><a href="${prefix}hi/index.html#specialities">विभाग</a><a href="${prefix}hi/doctors.html">डॉक्टर</a><a href="${prefix}hi/index.html#facilities">सुविधाएँ</a><a href="${prefix}hi/index.html#reviews">समीक्षाएँ</a><a href="${prefix}hi/contact.html">संपर्क</a>${langHref ? `<a href="${langHref}">English</a>` : ''}<a class="btn btn-primary js-wa" href="#" style="margin-top:8px; display:inline-block; text-align:center;">अपॉइंटमेंट बुक करें</a></div>
</header>`;
}

function footer(prefix) {
  const deptLinks = departments.map(([label, href]) => `<a href="${prefix}${href.slice(1)}">${esc(label)}</a>`).join('<br>');
  return `<footer class="site"><div class="wrap">
  <div class="grid footer-grid">
    <div>
      <a class="brand" href="${prefix}index.html" style="color:#fff"><img src="${prefix}assets/img/logo.png" alt="R N Multispeciality Hospital logo" style="height:40px;background:#fff;border-radius:8px;padding:3px"><span style="color:#fff">R N Multispeciality Hospital</span></a>
      <p style="margin-top:12px">50-bed multispeciality hospital in Nirman Nagar, Jaipur, near Mansarovar Metro Station.</p>
      <p><b>Address:</b><br>${hospital.address}</p>
      <p><b>Phone:</b> <a href="tel:${hospital.tel}" class="js-phone-link"><span class="js-phone-display">${hospital.phone}</span></a><br><b>Availability:</b> 24x7 emergency care</p>
    </div>
    <div><h4>Departments</h4><p>${deptLinks}</p></div>
    <div><h4>Important links</h4><p><a href="${prefix}index.html">Home</a><br><a href="${prefix}doctors.html">Doctors</a><br><a href="${prefix}index.html#specialities">Services</a><br><a href="${prefix}contact.html">Contact</a><br><a href="#" class="js-wa">Book Appointment</a></p></div>
  </div>
  <div class="copy">© <span data-year></span> R N Multispeciality Hospital. All rights reserved.</div>
</div></footer>`;
}

function footerHi(prefix) {
  return `<footer class="site"><div class="wrap">
  <div class="grid footer-grid">
    <div>
      <a class="brand" href="${prefix}hi/index.html" style="color:#fff"><img src="${prefix}assets/img/logo.png" alt="R N Multispeciality Hospital logo" style="height:40px;background:#fff;border-radius:8px;padding:3px"><span style="color:#fff">R N Multispeciality Hospital</span></a>
      <p style="margin-top:12px">निर्माण नगर, जयपुर में 50-bed multispeciality hospital, मानसरोवर मेट्रो स्टेशन के पास।</p>
      <p><b>पता:</b><br>109-110, शिव शक्ति नगर, किंग्स रोड, निर्माण नगर, जयपुर, राजस्थान 302019</p>
      <p><b>फोन:</b> <a href="tel:${hospital.tel}" class="js-phone-link"><span class="js-phone-display">${hospital.phone}</span></a><br><b>उपलब्धता:</b> 24x7 emergency care</p>
    </div>
    <div><h4>विभाग</h4><p><a href="${prefix}hi/services/general-surgery.html">जनरल एवं लेप्रोस्कोपिक सर्जरी</a><br><a href="${prefix}hi/services/gynaecology.html">स्त्री एवं प्रसूति रोग</a><br><a href="${prefix}hi/services/pain-spine.html">पेन मैनेजमेंट व स्पाइन केयर</a><br><a href="${prefix}hi/services/orthopaedics.html">हड्डी रोग</a><br><a href="${prefix}hi/services/urology.html">यूरोलॉजी</a><br><a href="${prefix}hi/services/neurosurgery.html">न्यूरोसर्जरी</a><br><a href="${prefix}hi/services/ent.html">ईएनटी</a><br><a href="${prefix}hi/services/general-medicine.html">जनरल मेडिसिन</a><br><a href="${prefix}hi/services/pathology.html">पैथोलॉजी</a></p></div>
    <div><h4>महत्वपूर्ण लिंक</h4><p><a href="${prefix}hi/index.html">होम</a><br><a href="${prefix}hi/doctors.html">डॉक्टर</a><br><a href="${prefix}hi/index.html#specialities">विभाग</a><br><a href="${prefix}hi/contact.html">संपर्क</a><br><a href="#" class="js-wa">अपॉइंटमेंट बुक करें</a></p></div>
  </div>
  <div class="copy">© <span data-year></span> R N Multispeciality Hospital. All rights reserved.</div>
</div></footer>`;
}

function layout({ kind, title, meta, canonical, alternates = '', schema = '', body, lang = 'en', langHref = '' }) {
  const prefix = relPrefix(kind);
  const isHindi = lang === 'hi';
  return `<!DOCTYPE html>
<html lang="${lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(title)}</title>
<meta name="description" content="${esc(meta)}">
<link rel="canonical" href="${canonical}">
${alternates}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="${prefix}assets/css/style.css"><link rel="icon" href="${prefix}assets/img/logo.png">
<meta property="og:title" content="${esc(title)}">
<meta property="og:description" content="${esc(meta)}">
<meta property="og:image" content="https://rnmh.in/assets/img/exterior.jpg">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
${schema}
</head>
<body>
${isHindi ? topbarHi(prefix) : topbar(prefix)}
${isHindi ? headerHi(prefix, langHref) : header(prefix, langHref)}
${body}
${isHindi ? footerHi(prefix) : footer(prefix)}
<div class="sticky-bar"><a class="btn btn-ghost js-phone-link" href="tel:${hospital.tel}">${isHindi ? 'कॉल' : 'Call'}</a><a class="btn btn-primary js-wa" href="#">${isHindi ? 'WhatsApp पर बुक करें' : 'Book on WhatsApp'}</a></div>
<script src="${prefix}assets/js/site.js"></script>
</body>
</html>
`;
}

function hospitalRef() {
  return { '@id': 'https://rnmh.in/#hospital' };
}

function postalAddress() {
  return { '@type': 'PostalAddress', streetAddress: hospital.street, addressLocality: hospital.locality, addressRegion: hospital.region, postalCode: hospital.postal, addressCountry: 'IN' };
}

function faqSchema(faqs) {
  return { '@context': 'https://schema.org', '@type': 'FAQPage', mainEntity: faqs.map(([q, a]) => ({ '@type': 'Question', name: q, acceptedAnswer: { '@type': 'Answer', text: a } })) };
}

function breadcrumbSchema(items) {
  return { '@context': 'https://schema.org', '@type': 'BreadcrumbList', itemListElement: items.map(([name, item], i) => ({ '@type': 'ListItem', position: i + 1, name, item })) };
}

function ctaBlock(prefix, dept, label) {
  return `<p style="margin-top:16px"><a class="btn btn-primary js-wa" href="#" data-dept="${dept}" data-deptlabel="${esc(label)}">Book on WhatsApp</a> <a class="btn btn-ghost js-phone-link" href="tel:${hospital.tel}">Call Now: <span class="js-phone-display">${hospital.phone}</span></a></p>`;
}

function ctaBlockHi(dept, label) {
  return `<p style="margin-top:16px"><a class="btn btn-primary js-wa" href="#" data-dept="${dept}" data-deptlabel="${esc(label)}">WhatsApp पर बुक करें</a> <a class="btn btn-ghost js-phone-link" href="tel:${hospital.tel}">अभी कॉल करें: <span class="js-phone-display">${hospital.phone}</span></a></p>`;
}

function doctorCard(prefix, doctor, dept, label) {
  return `<div class="doc doctor-summary"><div class="photo"><img loading="lazy" src="${prefix}assets/img/docs/${doctor.img}" alt="${esc(doctor.name)}, ${esc(doctor.specialty)} at RNMH Jaipur"></div><div class="body">
    <h3>${esc(doctor.name)}</h3><span class="spec">${esc(doctor.specialty)}</span><span class="qual">${esc(doctor.qualification)}</span><span class="exp">${esc(doctor.exp)}</span>
    <a class="btn btn-teal" href="${prefix}doctors.html#${doctor.anchor}">View profile</a><button class="btn btn-primary js-wa" data-doc="${esc(doctor.name)}" data-dept="${dept}" data-deptlabel="${esc(label)}">Book appointment</button>
  </div></div>`;
}

const hiDoctorMeta = {
  'robin-bothra': ['डॉ. रॉबिन बोथरा', 'जनरल एवं लेप्रोस्कोपिक सर्जन', '20+ वर्ष का अनुभव'],
  'chitra-soni': ['डॉ. चित्रा सोनी', 'स्त्री रोग, प्रसूति एवं फर्टिलिटी', '15+ वर्ष का अनुभव'],
  'naveen-soni': ['डॉ. नवीन सोनी', 'पेन मैनेजमेंट व स्पाइन केयर', '15+ वर्ष का अनुभव'],
  'chirag-jain': ['डॉ. चिराग जैन', 'हड्डी रोग एवं जोड़ प्रत्यारोपण', '10+ वर्ष का अनुभव'],
  'rn-daga': ['डॉ. आर एन डागा', 'यूरोलॉजिस्ट एवं एंड्रोलॉजिस्ट', '20+ वर्षों का अनुभव'],
  'pavan-jain': ['डॉ. पवन जैन', 'न्यूरोसर्जन — मस्तिष्क एवं रीढ़', '15+ वर्ष का अनुभव'],
  'ns-rathore': ['डॉ. एन एस राठौड़', 'ईएनटी सर्जन', '10+ वर्ष का अनुभव'],
  'vishnu-gupta': ['डॉ. विष्णु गुप्ता', 'जनरल मेडिसिन कंसल्टेंट', '10+ वर्ष का अनुभव'],
  'vinita-jain': ['डॉ. विनिता जैन', 'पैथोलॉजी एवं डायग्नोस्टिक्स', '20+ वर्षों का अनुभव']
};

function doctorCardHi(prefix, doctor, dept, label) {
  const [name, specialty, exp] = hiDoctorMeta[doctor.anchor] || [doctor.name, doctor.specialty, doctor.exp];
  return `<div class="doc doctor-summary"><div class="photo"><img loading="lazy" src="${prefix}assets/img/docs/${doctor.img}" alt="${esc(name)}, ${esc(specialty)}"></div><div class="body">
    <h3>${esc(name)}</h3><span class="spec">${esc(specialty)}</span><span class="qual">${esc(doctor.qualification)}</span><span class="exp">${esc(exp)}</span>
    <a class="btn btn-teal" href="${prefix}hi/doctors.html#${doctor.anchor}">प्रोफ़ाइल देखें</a><button class="btn btn-primary js-wa" data-doc="${esc(name)}" data-dept="${dept}" data-deptlabel="${esc(label)}">अपॉइंटमेंट बुक करें</button>
  </div></div>`;
}

function supportingFactsEnglish() {
  return `
<!-- RNMH SUPPORTING FACTS -->
<section id="hospital-profile" class="hospital-profile" style="background:var(--surface)"><div class="wrap">
  <div class="sec-head"><h2>Specialist-led care with personal continuity</h2><p class="lead">At R N Multispeciality Hospital, senior specialists remain closely involved in the patient journey, from consultation and diagnosis to admission, procedure planning and follow-up.</p></div>
  <div class="owner-grid">
    <a href="doctors.html#robin-bothra"><b>Dr Robin Bothra</b><span>General &amp; Laparoscopic Surgery</span></a>
    <a href="doctors.html#chitra-soni"><b>Dr Chitra Soni</b><span>Obstetrics, Gynaecology &amp; Fertility</span></a>
    <a href="doctors.html#naveen-soni"><b>Dr Naveen Soni</b><span>Pain Management &amp; Spine Care</span></a>
    <a href="doctors.html#vinita-jain"><b>Dr Vinita Jain</b><span>Pathology &amp; Diagnostics</span></a>
  </div>
  <p class="lead ownership-note">Women doctors lead key parts of the hospital's patient experience, including women's health, fertility, diagnostics and clinical governance. This helps families choose RNMH for privacy, continuity and direct specialist access.</p>
</div></section>

<section id="at-a-glance" style="background:var(--bg)"><div class="wrap">
  <div class="sec-head"><h2>R N Multispeciality Hospital at a glance</h2><p class="lead">A factual summary for patients, families and answer engines.</p></div>
  <table class="fact-table">
    <tr><th>Hospital type</th><td>50-bed multispeciality hospital</td></tr>
    <tr><th>Location</th><td>Nirman Nagar, Jaipur</td></tr>
    <tr><th>Landmark</th><td>Near Mansarovar Metro Station</td></tr>
    <tr><th>Open</th><td>24x7</td></tr>
    <tr><th>Emergency care</th><td>Available</td></tr>
    <tr><th>ICU/NICU</th><td>Available</td></tr>
    <tr><th>Insurance</th><td>Cashless, TPA, RGHS, PM-JAY, MAA Yojana</td></tr>
    <tr><th>Main departments</th><td>General &amp; Laparoscopic Surgery, Obstetrics &amp; Gynaecology, Pain &amp; Spine, Orthopaedics, Urology, Neurosurgery, ENT, General Medicine, Pathology</td></tr>
    <tr><th>Appointment</th><td>WhatsApp or call <a href="tel:+911412390320" class="js-phone-link"><span class="js-phone-display">0141 239 0320</span></a></td></tr>
  </table>
</div></section>

<section id="why-rnmh"><div class="wrap">
  <div class="sec-head"><h2>Why families choose RNMH</h2><p class="lead">Straightforward reasons to choose a specialist-led hospital near Mansarovar Metro Station.</p></div>
  <ul class="why-list">
    <li>24x7 emergency care and ambulance support</li>
    <li>50-bed multispeciality hospital in Nirman Nagar</li>
    <li>Senior specialists involved across consultation, admission and follow-up</li>
    <li>Women-led leadership across gynaecology, fertility and diagnostics</li>
    <li>ICU, NICU and modular operation theatre</li>
    <li>In-house diagnostics including lab, X-ray, sonography, colour Doppler and ECG</li>
    <li>Cashless insurance and TPA support</li>
    <li>RGHS, PM-JAY and MAA Yojana support where applicable</li>
    <li>Private, deluxe and family-friendly rooms for planned admissions</li>
  </ul>
</div></section>

<section class="link-band"><div class="wrap">
  <div class="sec-head"><h2>Treatment guides for common searches</h2><p class="lead">Useful local pages for patients comparing care options in Jaipur.</p></div>
  <div class="link-grid">
    <a href="treatments/laser-piles-treatment-jaipur.html">Laser Piles Treatment in Jaipur</a>
    <a href="treatments/hernia-surgery-jaipur.html">Hernia Surgery in Jaipur</a>
    <a href="treatments/gall-bladder-stone-surgery-jaipur.html">Gall Bladder Stone Surgery in Jaipur</a>
    <a href="treatments/pregnancy-care-hospital-jaipur.html">Pregnancy Care Hospital in Jaipur</a>
    <a href="treatments/back-pain-treatment-jaipur.html">Back Pain Treatment in Jaipur</a>
    <a href="treatments/kidney-stone-treatment-jaipur.html">Kidney Stone Treatment in Jaipur</a>
    <a href="treatments/24x7-emergency-hospital-jaipur.html">24x7 Emergency Hospital in Nirman Nagar Jaipur</a>
    <a href="treatments/cashless-hospital-jaipur.html">Cashless Hospital in Jaipur</a>
  </div>
</div></section>
<!-- END RNMH SUPPORTING FACTS -->`;
}

function supportingFactsHindi() {
  return `
<!-- RNMH SUPPORTING FACTS -->
<section id="hospital-profile" class="hospital-profile" style="background:var(--surface)"><div class="wrap">
  <div class="sec-head"><h2>विशेषज्ञों की देखरेख में इलाज, हर चरण पर निरंतर साथ</h2><p class="lead">आर एन मल्टीस्पेशलिटी हॉस्पिटल में वरिष्ठ विशेषज्ञ मरीज की पूरी इलाज यात्रा में करीब से जुड़े रहते हैं — कंसल्टेशन और डायग्नोसिस से लेकर एडमिशन, प्रोसीजर प्लानिंग और फॉलो-अप तक।</p></div>
  <h3 style="font-size:1.25rem;margin-bottom:12px">हमारे प्रमुख विशेषज्ञ</h3>
  <div class="owner-grid">
    <a href="doctors.html#robin-bothra"><b>Dr Robin Bothra</b><span>General &amp; Laparoscopic Surgery</span></a>
    <a href="doctors.html#chitra-soni"><b>Dr Chitra Soni</b><span>Obstetrics, Gynaecology &amp; Fertility</span></a>
    <a href="doctors.html#naveen-soni"><b>Dr Naveen Soni</b><span>Pain Management &amp; Spine Care</span></a>
    <a href="doctors.html#vinita-jain"><b>Dr Vinita Jain</b><span>Pathology &amp; Diagnostics</span></a>
  </div>
  <p class="lead ownership-note">महिला डॉक्टर हॉस्पिटल के मरीज अनुभव के महत्वपूर्ण हिस्सों का नेतृत्व करती हैं, जिनमें महिला स्वास्थ्य, फर्टिलिटी, डायग्नोस्टिक्स और क्लिनिकल गवर्नेंस शामिल हैं। इससे परिवार RNMH को प्राइवेसी, निरंतर देखभाल और सीधे विशेषज्ञों तक पहुँच के लिए भरोसेमंद विकल्प मानते हैं।</p>
</div></section>

<section id="at-a-glance" style="background:var(--bg)"><div class="wrap">
  <div class="sec-head"><h2>R N Multispeciality Hospital एक नज़र में</h2><p class="lead">मरीजों, परिवारों और आंसर इंजनों के लिए एक स्पष्ट तथ्यात्मक सारांश।</p></div>
  <table class="fact-table">
    <tr><th>हॉस्पिटल का प्रकार</th><td>50-बेड मल्टीस्पेशलिटी हॉस्पिटल</td></tr>
    <tr><th>स्थान</th><td>निर्माण नगर, जयपुर</td></tr>
    <tr><th>लैंडमार्क</th><td>मानसरोवर मेट्रो स्टेशन के पास</td></tr>
    <tr><th>उपलब्धता</th><td>24x7</td></tr>
    <tr><th>इमरजेंसी केयर</th><td>उपलब्ध</td></tr>
    <tr><th>ICU/NICU</th><td>उपलब्ध</td></tr>
    <tr><th>इंश्योरेंस</th><td>कैशलेस, TPA, RGHS, PM-JAY, MAA Yojana</td></tr>
    <tr><th>मुख्य विभाग</th><td>जनरल व लैप्रोस्कोपिक सर्जरी, स्त्री एवं प्रसूति रोग, पेन व स्पाइन, ऑर्थोपेडिक्स, यूरोलॉजी, न्यूरोसर्जरी, ईएनटी, जनरल मेडिसिन, पैथोलॉजी</td></tr>
    <tr><th>अपॉइंटमेंट</th><td>WhatsApp करें या कॉल करें: <a href="tel:+911412390320" class="js-phone-link"><span class="js-phone-display">0141 239 0320</span></a></td></tr>
  </table>
</div></section>

<section id="why-rnmh"><div class="wrap">
  <div class="sec-head"><h2>परिवार RNMH क्यों चुनते हैं</h2><p class="lead">मानसरोवर मेट्रो स्टेशन के पास एक विशेषज्ञ-नेतृत्व वाले हॉस्पिटल को चुनने के स्पष्ट कारण।</p></div>
  <ul class="why-list">
    <li>24x7 इमरजेंसी केयर और एम्बुलेंस सहायता</li>
    <li>निर्माण नगर में 50-बेड मल्टीस्पेशलिटी हॉस्पिटल</li>
    <li>कंसल्टेशन, एडमिशन और फॉलो-अप तक वरिष्ठ विशेषज्ञों की भागीदारी</li>
    <li>गाइनेकोलॉजी, फर्टिलिटी और डायग्नोस्टिक्स में महिला-नेतृत्व वाली देखभाल</li>
    <li>ICU, NICU और मॉड्यूलर ऑपरेशन थिएटर</li>
    <li>इन-हाउस डायग्नोस्टिक्स, जिनमें लैब, X-ray, सोनोग्राफी, कलर डॉप्लर और ECG शामिल हैं</li>
    <li>कैशलेस इंश्योरेंस और TPA सहायता</li>
    <li>RGHS, PM-JAY और MAA Yojana सहायता, जहाँ लागू हो</li>
    <li>प्लान्ड एडमिशन के लिए प्राइवेट, डीलक्स और परिवार-अनुकूल कमरे</li>
  </ul>
</div></section>

<section class="link-band"><div class="wrap">
  <div class="sec-head"><h2>आम सर्च के लिए ट्रीटमेंट गाइड्स</h2><p class="lead">जयपुर में इलाज के विकल्पों की तुलना कर रहे मरीजों के लिए उपयोगी स्थानीय पेज।</p></div>
  <div class="link-grid">
    <a href="treatments/laser-piles-treatment-jaipur.html">जयपुर में पाइल्स का लेजर इलाज</a>
    <a href="treatments/hernia-surgery-jaipur.html">जयपुर में हर्निया सर्जरी</a>
    <a href="treatments/gall-bladder-stone-surgery-jaipur.html">जयपुर में पित्त की थैली की पथरी का ऑपरेशन</a>
    <a href="treatments/pregnancy-care-hospital-jaipur.html">जयपुर में प्रेगनेंसी केयर हॉस्पिटल</a>
    <a href="treatments/back-pain-treatment-jaipur.html">जयपुर में कमर दर्द का इलाज</a>
    <a href="treatments/kidney-stone-treatment-jaipur.html">जयपुर में किडनी स्टोन का इलाज</a>
    <a href="treatments/24x7-emergency-hospital-jaipur.html">निर्माण नगर जयपुर में 24x7 इमरजेंसी हॉस्पिटल</a>
    <a href="treatments/cashless-hospital-jaipur.html">जयपुर में कैशलेस हॉस्पिटल</a>
  </div>
</div></section>
<!-- END RNMH SUPPORTING FACTS -->`;
}

function hindiHeroAndStats() {
  return `<section class="hero"><div class="wrap">
  <div>
    <span class="eyebrow">निर्माण नगर, जयपुर में 50-बेड मल्टीस्पेशलिटी हॉस्पिटल</span>
    <h1>अनुभवी विशेषज्ञों के साथ <span class="accent">24x7 भरोसेमंद इलाज</span></h1>
    <p class="lead">आर एन मल्टीस्पेशलिटी हॉस्पिटल, मानसरोवर मेट्रो स्टेशन के पास स्थित 50-बेड हॉस्पिटल है। यहाँ इमरजेंसी केयर, विशेषज्ञ डॉक्टरों की सलाह, सर्जरी, डायग्नोस्टिक्स और कैशलेस इंश्योरेंस सहायता एक ही जगह उपलब्ध है।</p>
    <p class="hero-specialties-text" style="color: var(--muted); font-size: 0.95rem; font-weight: 500; margin-bottom: 24px; line-height: 1.6;">जनरल व लैप्रोस्कोपिक सर्जरी &middot; स्त्री एवं प्रसूति रोग &middot; पेन मैनेजमेंट व स्पाइन केयर &middot; हड्डी रोग &middot; यूरोलॉजी &middot; न्यूरोसर्जरी &middot; ईएनटी &middot; जनरल मेडिसिन &middot; पैथोलॉजी</p>
    <div class="trust">
      <span class="rating-badge"><b>20+ वर्ष</b> डॉक्टर अनुभव</span>
      <span class="rating-badge"><b>1 लाख+</b> मरीजों का भरोसा</span>
      <span class="rating-badge"><span class="stars">4.9★</span> 3,814 Google Reviews</span>
      <span class="rating-badge"><b>24x7</b> इमरजेंसी केयर</span>
      <span class="rating-badge"><b>कैशलेस</b> इंश्योरेंस व TPA सहायता</span>
    </div>
    <div class="hero-cta"><a class="btn btn-primary js-wa" href="#book">WhatsApp पर बुक करें</a><a class="btn btn-ghost js-phone-link" href="tel:+911412390320">अभी कॉल करें: <span class="js-phone-display">0141 239 0320</span></a></div>
  </div>
  <div class="hero-media"><img src="../assets/img/exterior.jpg" alt="R N Multispeciality Hospital building exterior, Nirman Nagar, Jaipur"></div>
</div></section>

<section class="stats"><div class="wrap"><div class="grid">
  <div class="stat"><div class="num">10+</div><div class="lbl">वर्षों से जयपुर की सेवा</div></div>
  <div class="stat"><div class="num">1 लाख+</div><div class="lbl">मरीजों की देखभाल</div></div>
  <div class="stat"><div class="num">50</div><div class="lbl">बेड, ICU और NICU सहित</div></div>
  <div class="stat"><div class="num">4.9★</div><div class="lbl">3,814 समीक्षाओं में रेटेड</div></div>
</div></div></section>`;
}

function hindiFaqSection() {
  return `<div class="grid-3" style="margin-top:32px;">
    <div class="card"><div class="card-core"><h3>क्या R N Multispeciality Hospital 24x7 खुला रहता है?</h3><p class="desc" style="margin-top:10px;">हाँ। R N Multispeciality Hospital निर्माण नगर, जयपुर में 24x7 इमरजेंसी केयर उपलब्ध कराता है।</p></div></div>
    <div class="card"><div class="card-core"><h3>R N Multispeciality Hospital कहाँ स्थित है?</h3><p class="desc" style="margin-top:10px;">R N Multispeciality Hospital निर्माण नगर, जयपुर में स्थित है, मानसरोवर मेट्रो स्टेशन के पास।</p></div></div>
    <div class="card"><div class="card-core"><h3>क्या RNMH में कैशलेस इंश्योरेंस सुविधा उपलब्ध है?</h3><p class="desc" style="margin-top:10px;">हाँ। RNMH में कैशलेस इंश्योरेंस और TPA सेवाओं की सहायता उपलब्ध है। यह सुविधा मरीज की इंश्योरेंस पॉलिसी, इंश्योरेंस कंपनी और TPA अप्रूवल के अनुसार लागू होती है।</p></div></div>
    <div class="card"><div class="card-core"><h3>RNMH में कौन-कौन सी स्पेशलिटीज उपलब्ध हैं?</h3><p class="desc" style="margin-top:10px;">RNMH में जनरल व लैप्रोस्कोपिक सर्जरी, स्त्री एवं प्रसूति रोग, पेन मैनेजमेंट व स्पाइन केयर, ऑर्थोपेडिक्स, यूरोलॉजी, न्यूरोसर्जरी, ईएनटी, जनरल मेडिसिन और पैथोलॉजी जैसी स्पेशलिटीज उपलब्ध हैं।</p></div></div>
    <div class="card"><div class="card-core"><h3>अपॉइंटमेंट कैसे बुक करें?</h3><p class="desc" style="margin-top:10px;">मरीज WhatsApp के माध्यम से अपॉइंटमेंट बुक कर सकते हैं या <span class="js-phone-display">0141 239 0320</span> पर कॉल कर सकते हैं।</p></div></div>
  </div>`;
}

function replaceHindiHero(html) {
  return html.replace(/<section class="hero">[\s\S]*?<\/section>\s*<section class="stats">[\s\S]*?<\/section>/, hindiHeroAndStats());
}

function hindiFaqBlock() {
  return `<!-- FAQ -->
<section id="faq" style="background:var(--surface);"><div class="wrap">
  <div class="sec-head"><h2>अक्सर पूछे जाने वाले सवाल</h2><p class="lead">मरीजों के सामान्य सवालों के जवाब।</p></div>
  ${hindiFaqSection()}
</div></section>`;
}

function removeSupportingFacts(html) {
  html = html.replace(/\n?<!-- RNMH SUPPORTING FACTS -->[\s\S]*?<!-- END RNMH SUPPORTING FACTS -->\n?/g, '\n\n');
  html = html.replace(/\n?<!-- AT A GLANCE -->[\s\S]*?<\/div><\/section>\n?/g, '\n');
  html = html.replace(/\n?<!-- WHY CHOOSE -->[\s\S]*?<\/div><\/section>\n?/g, '\n');
  html = html.replace(/\n?<!-- HIGH-INTENT TREATMENT LINKS -->[\s\S]*?<\/div><\/section>\n?/g, '\n');
  return html;
}

function relatedTreatmentLinks(prefix, links) {
  if (!links || links.length === 0) return '';
  return `<section class="link-band"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Related treatment pages</span><h2>More patient guides</h2></div>
  <div class="link-grid">${links.map((slug) => {
    const page = treatmentBySlug[slug];
    return `<a href="${prefix}treatments/${slug}.html">${esc(page[1])}</a>`;
  }).join('')}</div>
</div></section>`;
}

function serviceHtml(page) {
  const prefix = '../';
  const canonical = `https://rnmh.in/services/${page.slug}.html`;
  const faqs = page.faqs;
  const schema = [
    jsonLd({
      '@context': 'https://schema.org',
      '@type': 'MedicalWebPage',
      '@id': `${canonical}#webpage`,
      url: canonical,
      name: page.h1,
      description: page.meta,
      about: { '@type': 'MedicalProcedure', name: page.procedure },
      publisher: hospitalRef()
    }),
    jsonLd(breadcrumbSchema([['Home', 'https://rnmh.in/'], ['Specialities', 'https://rnmh.in/#specialities'], [page.h1, canonical]])),
    jsonLd(faqSchema(faqs))
  ].join('\n');
  const body = `
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="../index.html">Home</a> / <a href="../index.html#specialities">Specialities</a> / ${esc(page.specialty)}</div>
  <h1>${esc(page.h1)}</h1>
  <p class="lead">${esc(page.intro)}</p>
  ${ctaBlock(prefix, page.dept, page.specialty)}
</div></section>
<section style="padding:24px 0 0"><div class="wrap"><img class="spec-banner" loading="lazy" src="../assets/img/spec/${page.img}" alt="${esc(page.specialty)} at R N Multispeciality Hospital, Jaipur"></div></section>
<section><div class="wrap grid-2" style="align-items:start">
  <div>
    <h2 style="font-size:1.5rem;margin-bottom:10px">What we treat</h2>
    <ul class="ticks">${page.treats.map((item) => `<li>${esc(item)}</li>`).join('')}</ul>
    <h2 style="font-size:1.5rem;margin:24px 0 10px">Why choose RNMH?</h2>
    <ul class="ticks"><li>50-bed multispeciality hospital in Nirman Nagar, Jaipur</li><li>Located near Mansarovar Metro Station</li><li>24x7 emergency care, ICU and NICU support</li><li>In-house diagnostics including lab, X-ray, sonography, colour Doppler and ECG</li><li>Cashless insurance and TPA support, subject to approval</li></ul>
  </div>
  ${doctorCard(prefix, page.doctor, page.dept, page.specialty)}
</div></section>
${relatedTreatmentLinks(prefix, page.treatmentLinks)}
<section style="background:var(--teal-soft)"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Common questions</span><h2>${esc(page.specialty)}: patient FAQs</h2></div>
  ${faqs.map(([q, a]) => `<div class="faq"><h3>${esc(q)}</h3><p>${esc(a)}</p></div>`).join('')}
</div></section>
<section class="band"><div class="wrap center">
  <h2 style="font-size:1.6rem;margin-bottom:10px">Book an appointment at RNMH</h2>
  <p class="lead center">Send a WhatsApp request or call ${hospital.phone}. Treatment suitability and insurance approval depend on doctor evaluation, policy terms and TPA rules.</p>
  ${ctaBlock(prefix, page.dept, page.specialty)}
</div></section>`;
  return layout({
    kind: 'service',
    title: page.title,
    meta: page.meta,
    canonical,
    alternates: `<link rel="alternate" hreflang="en" href="${canonical}">\n<link rel="alternate" hreflang="hi" href="https://rnmh.in/hi/services/${page.slug}.html">\n<link rel="alternate" hreflang="x-default" href="${canonical}">`,
    schema,
    body,
    langHref: `../hi/services/${page.slug}.html`
  });
}

function treatmentHtml(page) {
  const [slug, h1, category, meta, doctor, serviceSlug, symptoms, diagnosis, treatments, faqOne] = page;
  const service = serviceBySlug[serviceSlug] || serviceBySlug['general-medicine'];
  const canonical = `https://rnmh.in/treatments/${slug}.html`;
  const faqs = [
    faqOne,
    ['Where is R N Multispeciality Hospital located?', 'R N Multispeciality Hospital is located in Nirman Nagar, Jaipur, near Mansarovar Metro Station.'],
    ['Can I use cashless insurance?', 'Cashless insurance may be available depending on the patient\'s insurance provider, policy terms and TPA approval.'],
    ['How can I book an appointment?', 'Patients can book an appointment on WhatsApp or call 0141 239 0320.'],
    ['Is emergency care available?', 'Yes. RNMH provides 24x7 emergency care in Nirman Nagar, Jaipur.']
  ];
  const schema = [
    jsonLd({ '@context': 'https://schema.org', '@type': 'MedicalWebPage', '@id': `${canonical}#webpage`, url: canonical, name: h1, description: meta, about: { '@type': category === 'insurance' ? 'MedicalBusiness' : 'MedicalProcedure', name: h1.replace(' in Jaipur', '') }, publisher: hospitalRef() }),
    jsonLd(breadcrumbSchema([['Home', 'https://rnmh.in/'], ['Treatments', 'https://rnmh.in/treatments/'], [h1, canonical]])),
    jsonLd(faqSchema(faqs))
  ].join('\n');
  const hiSlug = Object.entries(hiPages).find(([key]) => key === slug)?.[0];
  const alternates = `<link rel="alternate" hreflang="en" href="${canonical}">${hiSlug ? `\n<link rel="alternate" hreflang="hi" href="https://rnmh.in/hi/treatments/${hiSlug}.html">` : ''}\n<link rel="alternate" hreflang="x-default" href="${canonical}">`;
  const body = `
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="../index.html">Home</a> / <a href="../services/${serviceSlug}.html">${esc(service.specialty)}</a> / ${esc(h1)}</div>
  <h1>${esc(h1)}</h1>
  <p class="lead">${esc(meta)} R N Multispeciality Hospital is a 50-bed multispeciality hospital near Mansarovar Metro Station with diagnostics, emergency support and cashless insurance assistance under one roof.</p>
  ${ctaBlock('../', service.dept, service.specialty)}
</div></section>
<section><div class="wrap grid-2" style="align-items:start">
  <div>
    <h2>When should you consult a doctor?</h2><ul class="ticks">${symptoms.map((x) => `<li>${esc(x)}</li>`).join('')}</ul>
    <h2 style="margin-top:24px">Diagnosis</h2><ul class="ticks">${diagnosis.map((x) => `<li>${esc(x)}</li>`).join('')}</ul>
    <h2 style="margin-top:24px">Treatment options</h2><p class="lead">Treatment depends on doctor evaluation. Suitability varies by condition, severity, age, medical history and investigation findings.</p><ul class="ticks">${treatments.map((x) => `<li>${esc(x)}</li>`).join('')}</ul>
    <h2 style="margin-top:24px">Insurance support</h2><p>RNMH supports cashless insurance, TPA, RGHS, PM-JAY and MAA Yojana where applicable. Approval depends on policy terms, scheme rules and TPA or government approval.</p>
  </div>
  <aside>
    ${doctorCard('../', doctor, service.dept, service.specialty)}
  </aside>
</div></section>
<section class="link-band"><div class="wrap"><div class="sec-head"><span class="eyebrow">Related care</span><h2>Helpful next pages</h2></div><div class="link-grid"><a href="../services/${serviceSlug}.html">${esc(service.specialty)}</a><a href="../doctors.html#${doctor.anchor}">${esc(doctor.name)}</a><a href="../contact.html">Contact and appointment</a><a href="cashless-hospital-jaipur.html">Cashless hospital in Jaipur</a><a href="24x7-emergency-hospital-jaipur.html">24x7 emergency hospital in Jaipur</a></div></div></section>
<section style="background:var(--teal-soft)"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Patient questions</span><h2>FAQs about ${esc(h1)}</h2></div>
  ${faqs.map(([q, a]) => `<div class="faq"><h3>${esc(q)}</h3><p>${esc(a)}</p></div>`).join('')}
</div></section>
<section class="band"><div class="wrap center"><h2>Book at R N Multispeciality Hospital</h2><p class="lead center">For appointments, message on WhatsApp or call ${hospital.phone}. For emergencies, call now or visit the hospital directly.</p>${ctaBlock('../', service.dept, service.specialty)}</div></section>`;
  return layout({ kind: 'treatment', title: `${h1} | R N Multispeciality Hospital`, meta, canonical, alternates, schema, body, langHref: hiSlug ? `../hi/treatments/${hiSlug}.html` : '' });
}

function hiTreatmentHtml(slug, data) {
  const [title, intro, doctor, serviceSlug] = data;
  const enSlug = slug;
  const service = serviceBySlug[serviceSlug];
  const deptHi = service.specialty
    .replace('General & Laparoscopic Surgery', 'जनरल एवं लेप्रोस्कोपिक सर्जरी')
    .replace('Obstetrics & Gynaecology', 'स्त्री एवं प्रसूति रोग')
    .replace('Pain Management & Spine Care', 'पेन मैनेजमेंट व स्पाइन केयर')
    .replace('Orthopaedics', 'हड्डी रोग')
    .replace('Urology', 'यूरोलॉजी')
    .replace('Neurosurgery', 'न्यूरोसर्जरी')
    .replace('ENT', 'ईएनटी')
    .replace('General Medicine', 'जनरल मेडिसिन')
    .replace('Pathology', 'पैथोलॉजी');
  const canonical = `https://rnmh.in/hi/treatments/${slug}.html`;
  const meta = `${title} - R N Multispeciality Hospital, निर्माण नगर जयपुर में 24x7 इमरजेंसी, विशेषज्ञ डॉक्टर और कैशलेस सहायता उपलब्ध।`;
  const faqs = [
    [`क्या RNMH में ${title.replace('जयपुर में ', '')} उपलब्ध है?`, `हाँ। ${intro} डॉक्टर की जांच के बाद सही उपचार तय किया जाता है।`],
    ['हॉस्पिटल कहाँ है?', 'R N Multispeciality Hospital निर्माण नगर, जयपुर में मानसरोवर मेट्रो स्टेशन के पास है।'],
    ['अपॉइंटमेंट कैसे बुक करें?', 'आप WhatsApp पर Book on WhatsApp कर सकते हैं या 0141 239 0320 पर कॉल कर सकते हैं।'],
    ['क्या कैशलेस इंश्योरेंस उपलब्ध है?', 'कैशलेस इंश्योरेंस, TPA, RGHS, PM-JAY और MAA Yojana सहायता नियमों और अप्रूवल के अनुसार उपलब्ध है।']
  ];
  const schema = [
    jsonLd({ '@context': 'https://schema.org', '@type': 'MedicalWebPage', '@id': `${canonical}#webpage`, url: canonical, name: title, description: meta, publisher: hospitalRef() }),
    jsonLd(breadcrumbSchema([['Home', 'https://rnmh.in/hi/'], ['Treatment', 'https://rnmh.in/hi/treatments/'], [title, canonical]])),
    jsonLd(faqSchema(faqs))
  ].join('\n');
  const body = `
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="../../hi/index.html">होम</a> / ${esc(title)}</div>
  <h1>${esc(title)}</h1>
  <p class="lead">${esc(intro)} RNMH 50-bed multispeciality hospital है, जो निर्माण नगर में मानसरोवर मेट्रो स्टेशन के पास स्थित है।</p>
  ${ctaBlockHi(service.dept, deptHi)}
</div></section>
<section><div class="wrap grid-2" style="align-items:start">
  <div>
    <h2>कब डॉक्टर से मिलें?</h2>
    <ul class="ticks"><li>दर्द, सूजन, बुखार या परेशानी लगातार रहे</li><li>लक्षण दवा से ठीक न हों</li><li>अचानक तेज दर्द या इमरजेंसी लक्षण हों</li><li>आपको सर्जरी या विशेषज्ञ राय की सलाह दी गई हो</li></ul>
    <h2 style="margin-top:24px">जांच और इलाज</h2>
    <p class="lead">इलाज डॉक्टर की जांच, रिपोर्ट और मरीज की स्थिति के अनुसार तय होता है। जरूरत के अनुसार lab test, X-ray, sonography, ECG या अन्य जांच कराई जा सकती है।</p>
    <h2 style="margin-top:24px">RNMH क्यों चुनें?</h2>
    <ul class="ticks"><li>निर्माण नगर, जयपुर में 50-bed multispeciality hospital</li><li>मानसरोवर मेट्रो स्टेशन के पास</li><li>24x7 emergency care, ICU और NICU</li><li>Cashless insurance, TPA, RGHS, PM-JAY और MAA Yojana सहायता नियमों के अनुसार</li></ul>
  </div>
  ${doctorCardHi('../../', doctor, service.dept, deptHi)}
</div></section>
<section class="link-band"><div class="wrap"><div class="sec-head"><h2>और जानकारी</h2></div><div class="link-grid"><a href="../../hi/services/${serviceSlug}.html">${esc(deptHi)}</a><a href="../../hi/doctors.html#${doctor.anchor}">${esc((hiDoctorMeta[doctor.anchor] || [doctor.name])[0])}</a><a href="../../hi/contact.html">संपर्क</a><a href="../../treatments/${enSlug}.html">Read in English</a></div></div></section>
<section style="background:var(--teal-soft)"><div class="wrap"><div class="sec-head"><span class="eyebrow">FAQ</span><h2>अक्सर पूछे जाने वाले सवाल</h2></div>${faqs.map(([q, a]) => `<div class="faq"><h3>${esc(q)}</h3><p>${esc(a)}</p></div>`).join('')}</div></section>
<section class="band"><div class="wrap center"><h2>अपॉइंटमेंट बुक करें</h2><p class="lead center">WhatsApp पर request भेजें या ${hospital.phone} पर कॉल करें।</p>${ctaBlockHi(service.dept, deptHi)}</div></section>`;
  return layout({
    kind: 'hi-treatment',
    lang: 'hi',
    title: `${title} | R N Multispeciality Hospital`,
    meta,
    canonical,
    alternates: `<link rel="alternate" hreflang="hi" href="${canonical}">\n<link rel="alternate" hreflang="en" href="https://rnmh.in/treatments/${enSlug}.html">\n<link rel="alternate" hreflang="x-default" href="https://rnmh.in/treatments/${enSlug}.html">`,
    schema,
    body,
    langHref: `../../treatments/${enSlug}.html`
  });
}

function updateCss() {
  const cssPath = path.join(outRoot, 'assets/css/style.css');
  let css = fs.readFileSync(cssPath, 'utf8');
  css = css.replace(/\.hero\{background:linear-gradient\(160deg,var\(--teal-soft\),#fff 60%\);position:relative;overflow:hidden(?:;padding:0)?\}/, '.hero{background:linear-gradient(160deg,var(--teal-soft),#fff 60%);position:relative;overflow:hidden;padding:0}');
  css = css.replace(/\.hero \.wrap\{grid-template-columns:1fr; padding-top: 24px;\}/, '.hero .wrap{grid-template-columns:1fr;padding-top:24px;padding-bottom:32px;gap:22px}');
  css = css.replace(/\n\/\* AEO fact tables and internal-link sections \*\/[\s\S]*?@media\(max-width:520px\)\{\.why-list,.link-grid(?:,.owner-grid)?\{grid-template-columns:1fr\}[\s\S]*?\}\n/g, '\n');
  const add = `

/* AEO fact tables and internal-link sections */
.fact-table{width:100%;border-collapse:separate;border-spacing:0;background:#fff;border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow-soft)}
.fact-table th,.fact-table td{padding:14px 16px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
.fact-table th{width:220px;color:var(--ink);font-weight:800;background:var(--teal-soft)}
.fact-table tr:last-child th,.fact-table tr:last-child td{border-bottom:0}
.why-list{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.why-list li{list-style:none;background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px;font-weight:600;box-shadow:var(--shadow-soft)}
.link-band{background:var(--surface)}
.link-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.link-grid a{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 16px;font-weight:700;color:var(--teal-deep);box-shadow:var(--shadow-soft)}
.link-grid a:hover{border-color:var(--teal);box-shadow:var(--shadow)}
.owner-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:22px 0}
.owner-grid a{background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px;box-shadow:var(--shadow-soft)}
.owner-grid b{display:block;color:var(--ink);font-family:var(--font-h);font-size:1.02rem}
.owner-grid span{display:block;color:var(--muted);font-size:.86rem;margin-top:4px}
.ownership-note{margin-top:8px}
.doctor-summary .btn{width:100%;justify-content:center}
.footer-grid p{margin-bottom:10px}
@media(max-width:900px){.why-list,.link-grid,.owner-grid{grid-template-columns:repeat(2,1fr)}.fact-table th{width:42%}}
@media(max-width:520px){.why-list,.link-grid,.owner-grid{grid-template-columns:1fr}.fact-table th,.fact-table td{display:block;width:100%}.fact-table th{border-bottom:0}.fact-table td{padding-top:6px}}
`;
  css += add;
  fs.writeFileSync(cssPath, css);
}

function updateHomepage() {
  const p = path.join(outRoot, 'index.html');
  let html = fs.readFileSync(p, 'utf8');
  html = removeSupportingFacts(html);
  html = html.replace(/<title>.*?<\/title>/, '<title>R N Multispeciality Hospital Jaipur | 24x7 Emergency Care in Nirman Nagar</title>');
  html = html.replace(/<meta name="description" content=".*?">/, '<meta name="description" content="R N Multispeciality Hospital is a 50-bed multispeciality hospital in Nirman Nagar, Jaipur, near Mansarovar Metro Station, offering 24x7 emergency care, specialist doctors, surgery, diagnostics, and cashless insurance support.">');
  html = html.replace(/<meta property="og:description" content=".*?">/, '<meta property="og:description" content="50-bed multispeciality hospital in Nirman Nagar, Jaipur, near Mansarovar Metro Station, with 24x7 emergency care, specialist doctors, surgery, diagnostics and cashless insurance support.">');
  if (!html.includes('rnmhLang')) {
    html = html.replace('<link rel="preconnect" href="https://fonts.googleapis.com">', `${languageRedirectScript()}\n<link rel="preconnect" href="https://fonts.googleapis.com">`);
  }
  html = html.replaceAll('href="hi/index.html"', 'href="hi/index.html?lang=hi"');
  html = html.replace(/"@type":"Hospital"/, '"@type":["Hospital","MedicalOrganization","LocalBusiness"]');
  html = html.replace(/"description":"[^"]+"/, '"description":"R N Multispeciality Hospital is a 50-bed multispeciality hospital in Nirman Nagar, Jaipur, near Mansarovar Metro Station, offering 24x7 emergency care, specialist consultations, surgical services, diagnostics, and cashless insurance support."');
  html = html.replace(/"telephone":"\+91-141-2390320"/g, '"telephone":"+91-141-239-0320"');
  html = html.replace(/,\n  "aggregateRating":\{"@type":"AggregateRating","ratingValue":"4\.9","reviewCount":"1289"\}/, '');
  html = html.replace(/<script type="application\/ld\+json">\n\{"@context": "https:\/\/schema\.org", "@type": "FAQPage"[\s\S]*?<\/script>/, `${jsonLd(faqSchema([
    ['Is R N Multispeciality Hospital open 24x7?', 'Yes. R N Multispeciality Hospital provides 24x7 emergency care in Nirman Nagar, Jaipur.'],
    ['Where is R N Multispeciality Hospital located?', 'R N Multispeciality Hospital is located in Nirman Nagar, Jaipur, near Mansarovar Metro Station.'],
    ['Does RNMH offer cashless insurance?', 'Yes. RNMH supports cashless insurance and TPA services, subject to policy and provider approval.'],
    ['What specialties are available at RNMH?', 'RNMH offers General & Laparoscopic Surgery, Obstetrics & Gynaecology, Pain Management & Spine Care, Orthopaedics, Urology, Neurosurgery, ENT, General Medicine, and Pathology.'],
    ['How can I book an appointment?', 'Patients can book an appointment on WhatsApp or call 0141 239 0320.']
  ]))}`);
  html = html.replace(/<div class="stat"><div class="num">20\+<\/div><div class="lbl">Years doctor experience<\/div><\/div>/, '<div class="stat"><div class="num">10+</div><div class="lbl">Years serving Jaipur</div></div>');
  html = html.replaceAll('<span class="exp"><span data-since="2003"></span>+ years</span>', '<span class="exp">20+ years of experience</span>');
  html = html.replaceAll('<span class="exp"><span data-since="2010"></span>+ years</span>', '<span class="exp">15+ years of experience</span>');
  html = html.replaceAll('<span class="exp"><span data-since="2015"></span>+ years</span>', '<span class="exp">10+ years of experience</span>');
  html = html.replaceAll('<span class="exp"><span data-since="2006"></span>+ years</span>', '<span class="exp">20+ years of experience</span>');
  html = html.replace(/<img loading="lazy" src="assets\/img\/lobby\.jpg" alt="Hospital lobby">/, '<img loading="lazy" src="assets/img/lobby.jpg" alt="Reception and lobby area at R N Multispeciality Hospital Jaipur">');
  html = html.replace(/<img loading="lazy" src="assets\/img\/ot\.jpg" alt="Operation theatre">/, '<img loading="lazy" src="assets/img/ot.jpg" alt="Operation theatre at R N Multispeciality Hospital Jaipur">');
  html = html.replace(/<img loading="lazy" src="assets\/img\/nicu\.jpg" alt="NICU">/, '<img loading="lazy" src="assets/img/nicu.jpg" alt="NICU facility at R N Multispeciality Hospital Jaipur">');
  html = html.replace(/<img loading="lazy" src="assets\/img\/ward\.jpg" alt="Patient ward">/, '<img loading="lazy" src="assets/img/ward.jpg" alt="Patient ward at R N Multispeciality Hospital Jaipur">');
  html = html.replace(/\n<!-- FAQ -->/, `${supportingFactsEnglish()}\n\n<!-- FAQ -->`);
  html = html.replace(/<div class="grid-3" style="margin-top:32px;">[\s\S]*?<\/div>\n<\/div><\/section>\n\n<!-- REVIEWS -->/, `<div class="grid-3" style="margin-top:32px;">
    <div class="card"><div class="card-core"><h3>Is R N Multispeciality Hospital open 24x7?</h3><p class="desc" style="margin-top:10px;">Yes. R N Multispeciality Hospital provides 24x7 emergency care in Nirman Nagar, Jaipur.</p></div></div>
    <div class="card"><div class="card-core"><h3>Where is R N Multispeciality Hospital located?</h3><p class="desc" style="margin-top:10px;">R N Multispeciality Hospital is located in Nirman Nagar, Jaipur, near Mansarovar Metro Station.</p></div></div>
    <div class="card"><div class="card-core"><h3>Does RNMH offer cashless insurance?</h3><p class="desc" style="margin-top:10px;">Yes. RNMH supports cashless insurance and TPA services, subject to policy and provider approval.</p></div></div>
    <div class="card"><div class="card-core"><h3>What specialties are available at RNMH?</h3><p class="desc" style="margin-top:10px;">RNMH offers General &amp; Laparoscopic Surgery, Obstetrics &amp; Gynaecology, Pain Management &amp; Spine Care, Orthopaedics, Urology, Neurosurgery, ENT, General Medicine, and Pathology.</p></div></div>
    <div class="card"><div class="card-core"><h3>How can I book an appointment?</h3><p class="desc" style="margin-top:10px;">Patients can book an appointment on WhatsApp or call <span class="js-phone-display">0141 239 0320</span>.</p></div></div>
  </div>
</div></section>

<!-- REVIEWS -->`);
  html = replaceFooter(html, '');
  fs.writeFileSync(p, html);
}

function replaceFooter(html, prefix) {
  return html.replace(/<footer class="site">[\s\S]*?<\/footer>/, footer(prefix));
}

function updateDoctors() {
  const p = path.join(outRoot, 'doctors.html');
  let html = fs.readFileSync(p, 'utf8');
  html = html.replace(/<title>.*?<\/title>/, '<title>Doctors at R N Multispeciality Hospital Jaipur | Specialist Consultants</title>');
  html = html.replace(/<meta name="description" content=".*?">/, '<meta name="description" content="Meet specialist doctors at R N Multispeciality Hospital, Jaipur, across surgery, gynaecology, orthopaedics, urology, neurosurgery, ENT, general medicine, pathology, pain and spine care.">');
  html = html.replace(/<meta property="og:title" content=".*?">/, '<meta property="og:title" content="Doctors at R N Multispeciality Hospital Jaipur | Specialist Consultants">');
  html = html.replace(/<meta property="og:description" content=".*?">/, '<meta property="og:description" content="Meet specialist doctors at R N Multispeciality Hospital, Jaipur, across surgery, gynaecology, orthopaedics, urology, neurosurgery, ENT, general medicine, pathology, pain and spine care.">');
  const physicianData = Object.values(doctors).map((d) => ({
    '@context': 'https://schema.org',
    '@type': 'Physician',
    '@id': `https://rnmh.in/doctors.html#${d.anchor}`,
    name: d.name,
    url: `https://rnmh.in/doctors.html#${d.anchor}`,
    image: `https://rnmh.in/assets/img/docs/${d.img}`,
    medicalSpecialty: d.specialty,
    worksFor: hospitalRef(),
    hospitalAffiliation: hospitalRef(),
    address: postalAddress()
  }));
  html = html.replace(/<script type="application\/ld\+json">\n\[[\s\S]*?\]\n<\/script>/, jsonLd(physicianData));
  html = html.replaceAll('<span class="exp"><span data-since="2003"></span>+ years of experience</span>', '<span class="exp">20+ years of experience</span>');
  html = html.replaceAll('<span class="exp"><span data-since="2010"></span>+ years of experience</span>', '<span class="exp">15+ years of experience</span>');
  html = html.replaceAll('<span class="exp"><span data-since="2015"></span>+ years of experience</span>', '<span class="exp">10+ years of experience</span>');
  html = html.replaceAll('<span class="exp"><span data-since="2006"></span>+ years of experience</span>', '<span class="exp">20+ years of experience</span>');
  html = html.replaceAll('<span class="exp"><span data-since="2013"></span>+ years of experience</span>', '<span class="exp">10+ years of experience</span>');
  html = html.replace(/<span class="exp">Over a d.cade of experience<\/span>/g, '<span class="exp">10+ years of experience</span>');
  html = replaceFooter(html, '');
  fs.writeFileSync(p, html);
}

function updateOtherRootPages() {
  for (const file of ['contact.html', 'accreditations.html']) {
    const p = path.join(outRoot, file);
    let html = fs.readFileSync(p, 'utf8');
    html = html.replace(/<meta name="description" content="[^"]*<span class="js-phone-display">0141 239 0320<\/span>[^"]*">/, '<meta name="description" content="Contact R N Multispeciality Hospital, Nirman Nagar, Jaipur. Call 0141 239 0320 or send a WhatsApp appointment request. Open 24x7, near Mansarovar Metro Station.">');
    html = html.replace(/<meta property="og:description" content="[^"]*<span class="js-phone-display">0141 239 0320<\/span>[^"]*">/, '<meta property="og:description" content="Contact R N Multispeciality Hospital, Nirman Nagar, Jaipur. Call 0141 239 0320 or send a WhatsApp appointment request. Open 24x7, near Mansarovar Metro Station.">');
    html = replaceFooter(html, '');
    fs.writeFileSync(p, html);
  }
}

function updateSharedJs() {
  const p = path.join(outRoot, 'assets/js/site.js');
  let js = fs.readFileSync(p, 'utf8');
  js = js.replace(/\n\/\/ ---- experience counters:[\s\S]*?\n\}\);\n/, '\n');
  fs.writeFileSync(p, js);
}

function replaceFooterAny(html, replacement) {
  if (/<footer class="site">[\s\S]*?<\/footer>/.test(html)) {
    return html.replace(/<footer class="site">[\s\S]*?<\/footer>/, replacement);
  }
  if (/<footer style="[\s\S]*?<\/footer>/.test(html)) {
    return html.replace(/<footer style="[\s\S]*?<\/footer>/, replacement);
  }
  return html;
}

function updateHindiExisting() {
  const replacements = [
    [/<span class="exp"><span data-since="2003"><\/span>\+ वर्ष(?: का अनुभव)?<\/span>/g, '<span class="exp">20+ वर्ष का अनुभव</span>'],
    [/<span class="exp"><span data-since="2010"><\/span>\+ वर्ष(?:ों का अनुभव| का अनुभव)?<\/span>/g, '<span class="exp">15+ वर्ष का अनुभव</span>'],
    [/<span class="exp"><span data-since="2015"><\/span>\+ वर्ष(?: का अनुभव)?<\/span>/g, '<span class="exp">10+ वर्ष का अनुभव</span>'],
    [/<span class="exp"><span data-since="2006"><\/span>\+ वर्ष(?:ों का अनुभव)?<\/span>/g, '<span class="exp">20+ वर्षों का अनुभव</span>'],
    [/<span class="exp"><span data-since="2013"><\/span>\+ वर्ष(?: का अनुभव)?<\/span>/g, '<span class="exp">10+ वर्ष का अनुभव</span>'],
    [/<span class="exp">एक दश. से अधिक का अनुभव<\/span>/g, '<span class="exp">10+ वर्ष का अनुभव</span>']
  ];
  for (const file of ['hi/index.html', 'hi/doctors.html', 'hi/contact.html', 'hi/accreditations.html']) {
    const p = path.join(outRoot, file);
    if (!fs.existsSync(p)) continue;
    let html = fs.readFileSync(p, 'utf8');
    html = removeSupportingFacts(html);
    for (const [from, to] of replacements) html = html.replace(from, to);
    html = html.replace(/"telephone":"\+91-141-2390320"/g, '"telephone":"+91-141-239-0320"');
    html = html.replace(/,"aggregateRating":\{"@type":"AggregateRating","ratingValue":"4\.9","reviewCount":"1289"\}/g, '');
    if (file === 'hi/index.html') {
      html = html.replace(/<meta name="description" content=".*?">/, '<meta name="description" content="R N Multispeciality Hospital निर्माण नगर, जयपुर में 50-bed multispeciality hospital है, मानसरोवर मेट्रो स्टेशन के पास, 24x7 emergency care, specialist doctors, surgery, diagnostics और cashless insurance support के साथ।">');
      html = html.replace(/<meta property="og:description" content=".*?">/, '<meta property="og:description" content="निर्माण नगर, जयपुर में 50-bed multispeciality hospital, 24x7 emergency care, specialist doctors, surgery, diagnostics और cashless insurance support के साथ।">');
      html = replaceHindiHero(html);
      html = html.replace(/\n<section id="book"/, `${supportingFactsHindi()}\n\n<section id="book"`);
      html = html.replace(/<script type="application\/ld\+json">\n\{"@context": "https:\/\/schema\.org", "@type": "FAQPage"[\s\S]*?<\/script>/, jsonLd(faqSchema([
        ['क्या R N Multispeciality Hospital 24x7 खुला रहता है?', 'हाँ। R N Multispeciality Hospital निर्माण नगर, जयपुर में 24x7 इमरजेंसी केयर उपलब्ध कराता है।'],
        ['R N Multispeciality Hospital कहाँ स्थित है?', 'R N Multispeciality Hospital निर्माण नगर, जयपुर में स्थित है, मानसरोवर मेट्रो स्टेशन के पास।'],
        ['क्या RNMH में कैशलेस इंश्योरेंस सुविधा उपलब्ध है?', 'हाँ। RNMH में कैशलेस इंश्योरेंस और TPA सेवाओं की सहायता उपलब्ध है। यह सुविधा मरीज की इंश्योरेंस पॉलिसी, इंश्योरेंस कंपनी और TPA अप्रूवल के अनुसार लागू होती है।'],
        ['RNMH में कौन-कौन सी स्पेशलिटीज उपलब्ध हैं?', 'RNMH में जनरल व लैप्रोस्कोपिक सर्जरी, स्त्री एवं प्रसूति रोग, पेन मैनेजमेंट व स्पाइन केयर, ऑर्थोपेडिक्स, यूरोलॉजी, न्यूरोसर्जरी, ईएनटी, जनरल मेडिसिन और पैथोलॉजी जैसी स्पेशलिटीज उपलब्ध हैं।'],
        ['अपॉइंटमेंट कैसे बुक करें?', 'मरीज WhatsApp के माध्यम से अपॉइंटमेंट बुक कर सकते हैं या 0141 239 0320 पर कॉल कर सकते हैं।']
      ])));
      html = html.replace(/<!-- FAQ -->\s*<section id="faq"[\s\S]*?<\/section>\s*(?=<section id="reviews")/, `${hindiFaqBlock()}\n\n`);
    }
    html = html.replaceAll('href="../index.html"', 'href="../index.html?lang=en"');
    html = html.replace(/<meta name="description" content="[^"]*<span class="js-phone-display">0141 239 0320<\/span>[^"]*">/, '<meta name="description" content="आर एन मल्टीस्पेशलिटी हॉस्पिटल, निर्माण नगर, जयपुर से संपर्क करें। कॉल 0141 239 0320 या WhatsApp appointment request भेजें। 24x7 खुला, मानसरोवर मेट्रो के पास।">');
    html = html.replace(/<meta property="og:description" content="[^"]*<span class="js-phone-display">0141 239 0320<\/span>[^"]*">/, '<meta property="og:description" content="आर एन मल्टीस्पेशलिटी हॉस्पिटल, निर्माण नगर, जयपुर से संपर्क करें। कॉल 0141 239 0320 या WhatsApp appointment request भेजें। 24x7 खुला, मानसरोवर मेट्रो के पास।">');
    html = replaceFooterAny(html, footerHi('../'));
    fs.writeFileSync(p, html);
  }
  const hiServices = fs.readdirSync(path.join(outRoot, 'hi/services')).filter((f) => f.endsWith('.html'));
  for (const file of hiServices) {
    const p = path.join(outRoot, 'hi/services', file);
    let html = fs.readFileSync(p, 'utf8');
    for (const [from, to] of replacements) html = html.replace(from, to);
    html = html.replace(/डॉ\. एन एस राठौड़, MBBS और MS \(ENT\) के साथ एक दश. से अधिक अनुभव वाले ENT सर्जन/g, 'डॉ. एन एस राठौड़, MBBS और MS (ENT) के साथ 10+ वर्ष के अनुभव वाले ENT सर्जन');
    html = html.replace(/डॉ\. विष्णु गुप्ता, MBBS और MD \(जनरल मेडिसिन\) के साथ एक दश. से अधिक अनुभव वाले कंसल्टेंट फिजिशियन/g, 'डॉ. विष्णु गुप्ता, MBBS और MD (जनरल मेडिसिन) के साथ 10+ वर्ष के अनुभव वाले कंसल्टेंट फिजिशियन');
    html = html.replace(/डॉ\. आर एन डागा, M\.Ch \(यूरोलॉजी\) और लगभग दो दश.ों के अनुभव वाले यूरोलॉजिस्ट/g, 'डॉ. आर एन डागा, M.Ch (यूरोलॉजी) और 20+ वर्षों के अनुभव वाले यूरोलॉजिस्ट');
    html = replaceFooterAny(html, footerHi('../../'));
    fs.writeFileSync(p, html);
  }
}

function updateCampaigns() {
  const campaignFixes = {
    'campaigns/ivf-fertility.html': [
      ['Free Consultation Available', 'Fertility Consultation Available'],
      ['Personalized IVF, IUI and advanced fertility treatments at R N Multispeciality Hospital, Jaipur. We combine state-of-the-art lab technology with compassionate care to help you build your family.', 'Personalised fertility evaluation, IUI/IVF guidance and women\'s health support at R N Multispeciality Hospital, Jaipur. Treatment planning depends on doctor evaluation and diagnostic findings.'],
      ['High success rates</li><li>Transparent pricing</li><li>Advanced embryology lab</li><li>EMI options available', 'Fertility work-up and counselling</li><li>Transparent treatment guidance</li><li>Diagnostics and ultrasound support</li><li>Insurance or payment guidance where applicable'],
      ['With thousands of successful cases, Dr Chitra Soni brings unparalleled expertise and a patient-first approach to ensure the best possible outcomes.', 'Dr Chitra Soni provides fertility, pregnancy and gynaecology care with a patient-first approach and clear treatment counselling.'],
      ['Our team will reply within 15 minutes.', 'Our team will reply as soon as possible.']
    ],
    'campaigns/joint-replacement.html': [
      ['Free Consultation Available', 'Orthopaedic Consultation Available'],
      ['Advanced computer-navigated knee and hip replacement surgery by Dr Chirag Jain. Get perfectly aligned joints that last longer, with advanced pain management protocols.', 'Knee, hip, fracture and joint replacement consultation with Dr Chirag Jain. Treatment planning depends on examination, imaging and medical fitness.'],
      ['Computer-navigated precision</li><li>Rapid recovery protocols</li><li>World-class implants</li><li>0% EMI options', 'Joint pain and arthritis evaluation</li><li>Fracture and trauma care</li><li>Modern implant options where suitable</li><li>Insurance guidance where applicable'],
      ['With thousands of successful cases, Dr Chirag Jain brings unparalleled expertise and a patient-first approach to ensure the best possible outcomes.', 'Dr Chirag Jain provides orthopaedic, trauma and joint replacement care with clear counselling and recovery guidance.'],
      ['Our team will reply within 15 minutes.', 'Our team will reply as soon as possible.']
    ],
    'campaigns/laparoscopic-surgery.html': [
      ['Free Consultation Available', 'Surgery Consultation Available'],
      ['Need gallbladder or hernia surgery? Choose keyhole surgery for a faster recovery.', 'Need gallbladder or hernia surgery? Ask about keyhole surgery options.'],
      ['Dr Robin Bothra offers state-of-the-art laparoscopic (keyhole) surgeries for hernia, gallbladder stones, and appendix. Minimal pain, zero scars, and discharge within 24 hours.', 'Dr Robin Bothra offers laparoscopic (keyhole) surgery consultation for hernia, gallbladder stones and appendix concerns. Recovery and hospital stay depend on the patient and procedure.'],
      ['24-hour discharge</li><li>Minimal pain & scarring</li><li>RGHS & Cashless accepted</li><li>Modular OT', 'Laparoscopic surgery where suitable</li><li>Smaller cuts than open surgery in selected cases</li><li>RGHS and cashless support where approved</li><li>Modular operation theatre'],
      ['With thousands of successful cases, Dr Robin Bothra brings unparalleled expertise and a patient-first approach to ensure the best possible outcomes.', 'Dr Robin Bothra provides general, laparoscopic and laser surgery care with clear counselling about benefits, risks and recovery.'],
      ['Our team will reply within 15 minutes.', 'Our team will reply as soon as possible.']
    ],
    'campaigns/spine-surgery.html': [
      ['Free Consultation Available', 'Spine Consultation Available'],
      ['Severe back pain or sciatica? Avoid open surgery.', 'Severe back pain or sciatica? Explore spine care options.'],
      ['Get advanced, minimally invasive treatments for slip disc and chronic spine pain. Faster recovery, smaller cuts, and rapid return to normal life under the expert care of Dr Naveen Soni.', 'Get evaluation for slip disc, sciatica and chronic spine pain. Non-surgical and minimally invasive options may be considered after diagnosis by Dr Naveen Soni.'],
      ['Day-care procedures</li><li>No large incisions</li><li>German-trained specialist</li><li>Cashless insurance accepted', 'Non-surgical options where suitable</li><li>Minimally invasive procedures where indicated</li><li>Fellowship-trained pain specialist</li><li>Cashless insurance support where approved'],
      ['With thousands of successful cases, Dr Naveen Soni brings unparalleled expertise and a patient-first approach to ensure the best possible outcomes.', 'Dr Naveen Soni provides pain and spine care with a conservative, diagnosis-led approach.'],
      ['Our team will reply within 15 minutes.', 'Our team will reply as soon as possible.']
    ]
  };
  for (const [file, fixes] of Object.entries(campaignFixes)) {
    const p = path.join(outRoot, file);
    let html = fs.readFileSync(p, 'utf8');
    for (const [from, to] of fixes) html = html.replaceAll(from, to);
    html = html.replaceAll('alt="RNMH"', 'alt="R N Multispeciality Hospital logo"');
    html = html.replace(/<a href="tel:\+911412390320" class="js-phone-link" class="btn btn-ghost"/g, '<a href="tel:+911412390320" class="js-phone-link btn btn-ghost"');
    html = replaceFooterAny(html, footer('../'));
    fs.writeFileSync(p, html);
  }
}

function sitemap() {
  const urls = [
    ['https://rnmh.in/', '1.0', 'weekly', 'https://rnmh.in/hi/'],
    ['https://rnmh.in/doctors.html', '0.9', 'monthly', 'https://rnmh.in/hi/doctors.html'],
    ['https://rnmh.in/contact.html', '0.8', 'monthly', 'https://rnmh.in/hi/contact.html'],
    ['https://rnmh.in/accreditations.html', '0.7', 'monthly', 'https://rnmh.in/hi/accreditations.html'],
    ...servicePages.map((p) => [`https://rnmh.in/services/${p.slug}.html`, '0.8', 'monthly', `https://rnmh.in/hi/services/${p.slug}.html`]),
    ...treatmentPages.map((p) => [`https://rnmh.in/treatments/${p[0]}.html`, '0.75', 'monthly', hiPages[p[0]] ? `https://rnmh.in/hi/treatments/${p[0]}.html` : null]),
    ...Object.keys(hiPages).map((slug) => [`https://rnmh.in/hi/treatments/${slug}.html`, '0.65', 'monthly', `https://rnmh.in/treatments/${slug}.html`])
  ];
  const body = urls.map(([loc, priority, changefreq, alt]) => `  <url>
    <loc>${loc}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>${changefreq}</changefreq>
    <priority>${priority}</priority>${alt ? `
    <xhtml:link rel="alternate" hreflang="${loc.includes('/hi/') ? 'hi' : 'en'}" href="${loc}"/>
    <xhtml:link rel="alternate" hreflang="${loc.includes('/hi/') ? 'en' : 'hi'}" href="${alt}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="${loc.includes('/hi/') ? alt : loc}"/>` : ''}
  </url>`).join('\n\n');
  fs.writeFileSync(path.join(outRoot, 'sitemap.xml'), `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n\n${body}\n\n</urlset>\n`);
}

function generate() {
  fs.mkdirSync(path.join(outRoot, 'treatments'), { recursive: true });
  fs.mkdirSync(path.join(outRoot, 'hi/treatments'), { recursive: true });
  updateCss();
  updateSharedJs();
  updateHomepage();
  updateDoctors();
  updateOtherRootPages();
  for (const page of servicePages) fs.writeFileSync(path.join(outRoot, `services/${page.slug}.html`), serviceHtml(page));
  for (const page of treatmentPages) fs.writeFileSync(path.join(outRoot, `treatments/${page[0]}.html`), treatmentHtml(page));
  for (const [slug, data] of Object.entries(hiPages)) fs.writeFileSync(path.join(outRoot, `hi/treatments/${slug}.html`), hiTreatmentHtml(slug, data));
  updateHindiExisting();
  updateCampaigns();
  sitemap();
}

generate();
