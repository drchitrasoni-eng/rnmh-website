import os
import glob

def append_link(filepath, is_hi=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # We want to append to the <p class="footer-aeo-links"> block
    # English: <p class="footer-aeo-links" ...>
    # Hindi: same
    
    if is_hi:
        link = '<a href="{prefix}hi/treatments/pcos-treatment-jaipur.html">PCOS एवं पीरियड्स का इलाज</a>'
    else:
        link = '<a href="{prefix}treatments/pcos-treatment-jaipur.html">PCOS & Period Problems Treatment</a>'
        
    # We need to find the right prefix. The easiest way is just to find the last </a></p> in that block and append to it.
    # Actually, we can just replace '</p></div>\n    <p class="center" style="margin-top:20px; color:var(--muted); font-size:0.85rem">' or similar.
    # Let's just find `</a></p></div>` which closes the footer-aeo-links div.
    
    # Let's find <p class="footer-aeo-links" ...>...</p>
    import re
    # Wait, the string is `<a href="...">...</a></p></div>`
    # We can just append right before `</p></div>\n    <p class="center"` inside the footer.
    # Let's look for `>24x7 इमरजेंसी केयर</a>` or `>24x7 Emergency Care</a>` which are the last links.
    
    if ">24x7 Emergency Hospital</a>" in html:
        # It's an English page
        # Get depth
        depth = filepath.count('/') - 1
        prefix = "../" * depth
        link_str = f' &middot; <a href="{prefix}treatments/pcos-treatment-jaipur.html">PCOS &amp; Period Problems Treatment</a>'
        html = html.replace(">24x7 Emergency Hospital</a>", ">24x7 Emergency Hospital</a>" + link_str)
    elif ">24x7 इमरजेंसी केयर</a>" in html:
        depth = filepath.count('/') - 1
        prefix = "../" * depth
        link_str = f' &middot; <a href="{prefix}hi/treatments/pcos-treatment-jaipur.html">PCOS एवं पीरियड्स का इलाज</a>'
        html = html.replace(">24x7 इमरजेंसी केयर</a>", ">24x7 इमरजेंसी केयर</a>" + link_str)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)


# Update all files
for root, dirs, files in os.walk("site"):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            append_link(filepath, is_hi="/hi/" in filepath or filepath.startswith("site/hi/"))

print("Appended PCOS link to footer everywhere.")
