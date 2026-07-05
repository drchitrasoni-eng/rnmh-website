import os
import re
import json

def update_seo():
    base_dir = "site"
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        if "node_modules" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))

    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract title and description
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']\s*>', content, re.IGNORECASE | re.DOTALL)
        
        title = title_match.group(1).strip() if title_match else "R N Multispeciality Hospital"
        desc = desc_match.group(1).strip() if desc_match else "R N Multispeciality Hospital, Nirman Nagar, Jaipur"

        # Check if OG tags already exist
        if 'property="og:title"' not in content:
            og_tags = f"""<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://rnmh.in/assets/img/exterior.jpg">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
"""
            # Insert before </head>
            content = content.replace("</head>", og_tags + "</head>")
        
        # Add alt attributes to all <img> tags missing it (simple regex)
        # Assuming most img tags might already have alt, but some might not.
        # Actually it's safer to not do blanket regex for alt because of formatting.
        
        # Check if it's a services page
        if "/services/" in filepath or "\\services\\" in filepath:
            if '"@type":"BreadcrumbList"' not in content:
                # Add BreadcrumbList Schema
                page_name = title.split("|")[0].split("—")[0].strip()
                is_hi = "/hi/" in filepath or "\\hi\\" in filepath
                home_url = "https://rnmh.in/hi/" if is_hi else "https://rnmh.in/"
                page_url = "https://rnmh.in/" + filepath.split("site/")[1].replace("\\", "/")
                
                breadcrumb = {
                    "@context": "https://schema.org",
                    "@type": "BreadcrumbList",
                    "itemListElement": [
                        {
                            "@type": "ListItem",
                            "position": 1,
                            "name": "Home" if not is_hi else "होम",
                            "item": home_url
                        },
                        {
                            "@type": "ListItem",
                            "position": 2,
                            "name": "Specialities" if not is_hi else "विभाग",
                            "item": f"{home_url}index.html#specialities"
                        },
                        {
                            "@type": "ListItem",
                            "position": 3,
                            "name": page_name,
                            "item": page_url
                        }
                    ]
                }
                schema_str = f'\n<script type="application/ld+json">\n{json.dumps(breadcrumb, ensure_ascii=False)}\n</script>\n'
                content = content.replace("</head>", schema_str + "</head>")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == "__main__":
    update_seo()
    print("Done")
