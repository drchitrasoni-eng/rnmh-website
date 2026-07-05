from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')

extra_pages = [
    "orthopedic-doctor-nirman-nagar-jaipur",
    "knee-replacement-surgeon-kings-road-jaipur",
    "urologist-nirman-nagar-jaipur",
    "neurosurgeon-nirman-nagar-jaipur",
    "ent-specialist-kings-road-jaipur",
    "general-physician-nirman-nagar-jaipur",
    "pathology-lab-nirman-nagar-jaipur"
]

with open("site/sitemap.xml", "r", encoding="utf-8") as f:
    sitemap = f.read()

sitemap = sitemap.replace("</urlset>", "")

for p in extra_pages:
    for lang_prefix in ["", "hi/"]:
        url = f"https://rnmh.in/{lang_prefix}treatments/{p}.html"
        if url not in sitemap:
            sitemap += f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>\n"""

sitemap += "</urlset>"

with open("site/sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)
print("Sitemap updated with extra pages.")
