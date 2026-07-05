import json
import os

physicians = [
    {
        "name": "Dr Robin Bothra",
        "speciality": "General & Laparoscopic Surgery",
        "url": "https://rnmh.in/doctors.html#robin-bothra",
        "image": "https://rnmh.in/assets/img/docs/robin-bothra.jpg"
    },
    {
        "name": "Dr Chitra Soni",
        "speciality": "Obstetrics & Gynaecology",
        "url": "https://rnmh.in/doctors.html#chitra-soni",
        "image": "https://rnmh.in/assets/img/docs/chitra-soni.jpg"
    },
    {
        "name": "Dr Naveen Soni",
        "speciality": "Pain Management & Spine",
        "url": "https://rnmh.in/doctors.html#naveen-soni",
        "image": "https://rnmh.in/assets/img/docs/naveen-soni.jpg"
    },
    {
        "name": "Dr Chirag Jain",
        "speciality": "Orthopaedics & Joint Replacement",
        "url": "https://rnmh.in/doctors.html#chirag-jain",
        "image": "https://rnmh.in/assets/img/docs/chirag-jain.jpg"
    },
    {
        "name": "Dr R N Daga",
        "speciality": "Urologist & Andrologist",
        "url": "https://rnmh.in/doctors.html#rn-daga",
        "image": "https://rnmh.in/assets/img/docs/rn-daga.jpg"
    },
    {
        "name": "Dr Pavan Jain",
        "speciality": "Neurosurgery",
        "url": "https://rnmh.in/doctors.html#pavan-jain",
        "image": "https://rnmh.in/assets/img/docs/pavan-jain.jpg"
    },
    {
        "name": "Dr N S Rathore",
        "speciality": "ENT",
        "url": "https://rnmh.in/doctors.html#ns-rathore",
        "image": "https://rnmh.in/assets/img/docs/ns-rathore.jpg"
    },
    {
        "name": "Dr Vishnu Gupta",
        "speciality": "General Medicine",
        "url": "https://rnmh.in/doctors.html#vishnu-gupta",
        "image": "https://rnmh.in/assets/img/docs/vishnu-gupta.jpg"
    },
    {
        "name": "Dr Vinita Jain",
        "speciality": "Pathology",
        "url": "https://rnmh.in/doctors.html#vinita-jain",
        "image": "https://rnmh.in/assets/img/docs/vinita-jain.jpg"
    }
]

schema = []
for p in physicians:
    schema.append({
        "@context": "https://schema.org",
        "@type": "Physician",
        "name": p["name"],
        "medicalSpecialty": p["speciality"],
        "url": p["url"],
        "image": p["image"],
        "worksFor": {
            "@type": "Hospital",
            "name": "R N Multispeciality Hospital"
        }
    })

schema_str = f'\n<script type="application/ld+json">\n{json.dumps(schema, ensure_ascii=False)}\n</script>\n'

for filepath in ['site/doctors.html', 'site/hi/doctors.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if '"@type":"Physician"' not in content:
        content = content.replace("</head>", schema_str + "</head>")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
