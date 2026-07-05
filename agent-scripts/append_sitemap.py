from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')

with open("site/sitemap.xml", "r", encoding="utf-8") as f:
    sitemap = f.read()

sitemap = sitemap.replace("</urlset>", "")

for p in ["location", "hi/location"]:
    url = f"https://rnmh.in/{p}.html"
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
