import re
import os

# 1. Fix FAQs in index.html
with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to extract the new FAQs and put them inside the original FAQ block
# New FAQs string:
new_faqs_en = """    <div class="card"><div class="card-core"><h3>Is R N Multispeciality Hospital near Mansarovar Metro Station?</h3><p class="desc" style="margin-top:10px;">Yes. R N Multispeciality Hospital is located on Main Kings Road, Nirman Nagar, Jaipur, near Mansarovar Metro Station.</p></div></div>
    <div class="card"><div class="card-core"><h3>Which hospital is available on Kings Road, Nirman Nagar, Jaipur?</h3><p class="desc" style="margin-top:10px;">R N Multispeciality Hospital is a 50-bed multispeciality hospital on Main Kings Road, Nirman Nagar, Jaipur, offering 24x7 emergency care, specialist consultations, surgery, diagnostics, ICU/NICU and cashless insurance support.</p></div></div>
    <div class="card"><div class="card-core"><h3>Is there a gynaecologist near Nirman Nagar or Mansarovar Metro Station at RNMH?</h3><p class="desc" style="margin-top:10px;">Yes. Obstetrics, gynaecology and fertility consultations are available at R N Multispeciality Hospital on Main Kings Road, Nirman Nagar, Jaipur, near Mansarovar Metro Station.</p></div></div>
    <div class="card"><div class="card-core"><h3>Is RNMH accessible from Mansarovar and Shyam Nagar?</h3><p class="desc" style="margin-top:10px;">Yes. RNMH is located in Nirman Nagar near Mansarovar Metro Station and is accessible from Mansarovar, Shyam Nagar, Brijlalpura, Gopalpura Bypass, Kings Road and nearby Jaipur areas.</p></div></div>
    <div class="card"><div class="card-core"><h3>Does RNMH provide emergency care near Kings Road Jaipur?</h3><p class="desc" style="margin-top:10px;">Yes. RNMH provides 24x7 emergency care at its hospital on Main Kings Road, Nirman Nagar, Jaipur.</p></div></div>"""

# Remove the broken block
bad_block = """</div>
  <div class="grid-3" style="margin-top:32px;">
    <div class="card"><div class="card-core"><h3>Is R N Multispeciality Hospital near Mansarovar Metro Station?</h3><p class="desc" style="margin-top:10px;">Yes. R N Multispeciality Hospital is located on Main Kings Road, Nirman Nagar, Jaipur, near Mansarovar Metro Station.</p></div></div>
    <div class="card"><div class="card-core"><h3>Which hospital is available on Kings Road, Nirman Nagar, Jaipur?</h3><p class="desc" style="margin-top:10px;">R N Multispeciality Hospital is a 50-bed multispeciality hospital on Main Kings Road, Nirman Nagar, Jaipur, offering 24x7 emergency care, specialist consultations, surgery, diagnostics, ICU/NICU and cashless insurance support.</p></div></div>
    <div class="card"><div class="card-core"><h3>Is there a gynaecologist near Nirman Nagar or Mansarovar Metro Station at RNMH?</h3><p class="desc" style="margin-top:10px;">Yes. Obstetrics, gynaecology and fertility consultations are available at R N Multispeciality Hospital on Main Kings Road, Nirman Nagar, Jaipur, near Mansarovar Metro Station.</p></div></div>
    <div class="card"><div class="card-core"><h3>Is RNMH accessible from Mansarovar and Shyam Nagar?</h3><p class="desc" style="margin-top:10px;">Yes. RNMH is located in Nirman Nagar near Mansarovar Metro Station and is accessible from Mansarovar, Shyam Nagar, Brijlalpura, Gopalpura Bypass, Kings Road and nearby Jaipur areas.</p></div></div>
    <div class="card"><div class="card-core"><h3>Does RNMH provide emergency care near Kings Road Jaipur?</h3><p class="desc" style="margin-top:10px;">Yes. RNMH provides 24x7 emergency care at its hospital on Main Kings Road, Nirman Nagar, Jaipur.</p></div></div>

  </div></section>"""

if bad_block in html:
    html = html.replace(bad_block, "")
    
    # Inject it before the closing of the grid-3
    faq_grid_end = "    <div class=\"card\"><div class=\"card-core\"><h3>How can I book an appointment?</h3><p class=\"desc\" style=\"margin-top:10px;\">Patients can book an appointment on WhatsApp or call <span class=\"js-phone-display\">0141 239 0320</span>.</p></div></div>\n  </div>"
    
    new_faq_grid_end = "    <div class=\"card\"><div class=\"card-core\"><h3>How can I book an appointment?</h3><p class=\"desc\" style=\"margin-top:10px;\">Patients can book an appointment on WhatsApp or call <span class=\"js-phone-display\">0141 239 0320</span>.</p></div></div>\n" + new_faqs_en + "\n  </div>"
    
    html = html.replace(faq_grid_end, new_faq_grid_end)

with open('site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("FAQ block fixed on index.html")
