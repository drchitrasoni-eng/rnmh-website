import re
from datetime import datetime

pages = [
    "gynaecologist-near-nirman-nagar-jaipur",
    "gynaecologist-near-mansarovar-metro-station",
    "pregnancy-care-hospital-near-mansarovar-metro",
    "fertility-doctor-nirman-nagar-jaipur",
    "obgyn-kings-road-jaipur",
    "hospital-near-mansarovar-metro-station",
    "multispeciality-hospital-kings-road-jaipur",
    "24x7-emergency-hospital-nirman-nagar-jaipur",
    "cashless-hospital-near-mansarovar-jaipur",
    "laparoscopic-surgeon-near-mansarovar-metro",
    "general-surgeon-nirman-nagar-jaipur",
    "laser-piles-treatment-kings-road-jaipur",
    "hernia-surgery-nirman-nagar-jaipur",
    "back-pain-treatment-nirman-nagar-jaipur",
    "spine-specialist-near-mansarovar-metro",
    "pain-management-doctor-kings-road-jaipur",
]

today = datetime.today().strftime('%Y-%m-%d')

with open("site/sitemap.xml", "r", encoding="utf-8") as f:
    sitemap = f.read()

# Remove the closing </urlset> temporarily
sitemap = sitemap.replace("</urlset>", "")

for p in pages:
    en_url = f"https://rnmh.in/treatments/{p}.html"
    hi_url = f"https://rnmh.in/hi/treatments/{p}.html"
    
    if en_url not in sitemap:
        sitemap += f"""  <url>
    <loc>{en_url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>\n"""
    
    if hi_url not in sitemap:
        sitemap += f"""  <url>
    <loc>{hi_url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>\n"""

sitemap += "</urlset>"

with open("site/sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)

print("Sitemap updated.")
