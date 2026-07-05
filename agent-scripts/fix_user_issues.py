import os
import re

# =========================================================
# 1. FIX FOOTER LOGO & LINKS
# =========================================================
def fix_footer(base_dir):
    for root, _, files in os.walk(base_dir):
        if "node_modules" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                depth = filepath.replace(base_dir, "").count(os.sep) - 1
                
                prefix = ""
                if depth == 1:
                    prefix = "../"
                elif depth == 2:
                    prefix = "../../"
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Fix the logo in the footer (first column)
                # It looks like: <img src="assets/img/logo.png" or <img src="../assets/img/logo.png" etc
                # We replace <img src=".*?assets/img/logo.png" alt="R N Multispeciality Hospital logo" style="height:40px;background:#fff;border-radius:8px;padding:3px">
                # with the correct prefix
                
                logo_pattern = re.compile(r'<img src=".*?assets/img/logo.png" alt="(.*?)" style="height:40px;background:#fff;border-radius:8px;padding:3px">')
                def logo_repl(match):
                    alt_text = match.group(1)
                    return f'<img src="{prefix}assets/img/logo.png" alt="{alt_text}" style="height:40px;background:#fff;border-radius:8px;padding:3px">'
                
                content = logo_pattern.sub(logo_repl, content)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

# =========================================================
# 2. FIX FAQS IN INDEX.HTML & HI/INDEX.HTML
# =========================================================
def fix_faqs(filepath, is_hindi):
    if not os.path.exists(filepath):
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # The broken injection left something like:
    # </div>
    #   <div class="grid-3" style="margin-top:32px;">
    #     <div class="card"><div class="card-core"><h3>Is R N Multispeciality Hospital near Mansarovar Metro Station...
    # ...
    #   </div></section>
    
    # Let's extract the new FAQs
    if is_hindi:
        start_marker = "क्या R N Multispeciality Hospital मानसरोवर मेट्रो स्टेशन के पास है?"
    else:
        start_marker = "Is R N Multispeciality Hospital near Mansarovar Metro Station?"
        
    if start_marker in html:
        # Find the block we injected
        # Wait, let's just find all new FAQ cards and remove them + the broken wrappers
        if "</div>\n  <div class=\"grid-3\" style=\"margin-top:32px;\">" in html:
            # this is exactly the bad string injected
            # wait, my regex injection for FAQs was:
            # html = re.sub(faq_grid_pattern, r'\1\n' + faq_html.replace('\\', '\\\\'), html, count=1)
            # Actually I used `re.sub(faq_grid_pattern, ...)` which means it was injected INSIDE the original grid-3!
            # Wait, no. My first attempt was `html.replace('<!-- REVIEWS -->', ...)` which was commented out!
            # But the grep output showed:
            # 408-  </div>
            # 409-</div></section>
            # 410-
            # 411-</div>
            # 412-  <div class="grid-3" style="margin-top:32px;">
            # 413:    <div class="card">...
            pass
            
    # I will just write a very specific regex to clean up the bad injection and re-inject it correctly
    # Let's manually do it for both files to be safe
    pass

# =========================================================
# 3. MOVE LOCALITY BLOCK TO NEW PAGE
# =========================================================
def extract_locality_and_create_page():
    pass

fix_footer("site")
print("Footer logos fixed.")
