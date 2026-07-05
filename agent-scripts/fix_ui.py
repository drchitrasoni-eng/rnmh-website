import os
import re

new_map_iframe = '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3558.5888643270596!2d75.7522776!3d26.8848005!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x396db5509560e757%3A0xf39ab10b9bb91cff!2sR%20N%20Multispeciality%20hospital!5e0!3m2!1sen!2ssg!4v1781663911966!5m2!1sen!2ssg" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'

# Fix Contact Page HTML template to match user request (Index page scroll look)
def fix_contact_page(filepath, is_hi):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The layout in contact.html is currently a single .band with a .grid-2
    # We want it to be 2 sections: 
    # 1. The booking form (like index)
    # 2. The Contact & location block
    
    if is_hi:
        book_title = "व्हाट्सएप पर अनुरोध भेजें"
        book_lead = "फ़ॉर्म भरें और यह सही विभाग को एक व्हाट्सएप संदेश तैयार कर देगा। या हमें किसी भी समय <a href='tel:+911412390320'><b>0141 239 0320</b></a> पर कॉल करें।"
        book_ticks = "<li>24x7, 365 दिन खुला</li><li>कैशलेस बीमा, TPA, RGHS और MAA योजना स्वीकार्य</li><li>NABH मान्यता प्राप्त · मानसरोवर मेट्रो के पास</li>"
        
        loc_title = "संपर्क और स्थान"
        loc_address = "109-110, शिव शक्ति नगर, किंग्स रोड, निर्माण नगर, जयपुर 302019 (मानसरोवर मेट्रो के पास)"
        loc_hours = "24x7, 365 दिन खुला"
        loc_btn = "व्हाट्सएप पर संदेश भेजें →"
    else:
        book_title = "Send a request on WhatsApp"
        book_lead = "Fill the form and it opens a ready-to-send WhatsApp message to the right department. Or call us any time of day at <a href='tel:+911412390320'><b>0141 239 0320</b></a>."
        book_ticks = "<li>Open 24x7, 365 days</li><li>Cashless insurance, TPA, RGHS & MAA Yojana accepted</li><li>NABH accredited · near Mansarovar Metro Station</li>"
        
        loc_title = "Contact & location"
        loc_address = "109-110, Shiv Shakti Nagar, Kings Road, Nirman Nagar, Jaipur 302019 (near Mansarovar Metro)"
        loc_hours = "Open 24x7, 365 days"
        loc_btn = "Message us on WhatsApp →"

    new_body = f'''
<section class="band" style="padding-bottom: 64px;"><div class="wrap grid-2" style="align-items:center">
  <div>
    <span class="eyebrow">{'अपॉइंटमेंट बुक करें' if is_hi else 'Book an appointment'}</span>
    <h2 style="font-size:clamp(1.6rem,3vw,2.2rem);margin:6px 0 12px">{book_title}</h2>
    <p class="lead">{book_lead}</p>
    <ul class="ticks">{book_ticks}</ul>
  </div>
  <form class="form-card" id="bookForm">
    <div class="field"><label for="name">{'आपका नाम' if is_hi else 'Your name'}</label><input id="name" name="name" required></div>
    <div class="field"><label for="phone">{'फ़ोन नंबर' if is_hi else 'Phone number'}</label><input id="phone" name="phone" type="tel" required></div>
    <div class="field"><label for="department">{'विभाग' if is_hi else 'Department'}</label>
      <select id="department" name="department">
        <option value="pain-spine">Pain Management & Spine</option>
        <option value="gynaecology">Gynaecology & Fertility</option>
        <option value="general-surgery">General & Laparoscopic Surgery</option>
        <option value="orthopaedics">Orthopaedics</option>
        <option value="urology">Urology</option>
        <option value="neurosurgery">Neurosurgery</option>
        <option value="ent">ENT</option>
        <option value="general-medicine">General Medicine</option>
        <option value="pathology">Pathology & Diagnostics</option>
        <option value="other">Other / not sure</option>
      </select>
    </div>
    <button class="btn btn-primary" type="submit" style="margin-top:14px;width:100%">{'व्हाट्सएप पर अनुरोध भेजें' if is_hi else 'Send request on WhatsApp'}</button>
  </form>
</div></section>

<section style="padding: 64px 0; background: var(--surface);"><div class="wrap">
  <div class="sec-head">
    <span class="eyebrow">{'हमसे जुड़ें' if is_hi else 'Find us'}</span>
    <h2>{loc_title}</h2>
  </div>
  <div class="grid-2" style="align-items: start; margin-top: 32px;">
    <div>
      <div class="info-row"><span class="k">{'पता' if is_hi else 'Address'}</span><span>{loc_address}</span></div>
      <div class="info-row"><span class="k">{'कॉल' if is_hi else 'Call'}</span><span><a href="tel:+911412390320">0141 239 0320</a></span></div>
      <div class="info-row"><span class="k">{'व्हाट्सएप' if is_hi else 'WhatsApp'}</span><span><a href="#" class="js-wa">{loc_btn}</a></span></div>
      <div class="info-row"><span class="k">{'समय' if is_hi else 'Hours'}</span><span>{loc_hours}</span></div>
    </div>
    <div>
      {new_map_iframe}
    </div>
  </div>
</div></section>
'''
    
    # Replace the existing `<section class="band">...` with new_body
    start_tag = '<section class="band">'
    end_tag = '</section>'
    
    start_idx = content.find(start_tag)
    if start_idx != -1:
        # Find the matching closing section tag
        # Because there might be multiple sections, we look for footer to be safe or just find the next <footer
        footer_idx = content.find('<footer', start_idx)
        if footer_idx != -1:
            content = content[:start_idx] + new_body + content[footer_idx:]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

def fix_all_html():
    for root, dirs, files in os.walk('site'):
        if "node_modules" in root:
            continue
        for file in files:
            if not file.endswith('.html'):
                continue
            filepath = os.path.join(root, file)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            modified = False

            # Replace old maps URL with new
            if 'https://maps.google.com/maps?q=26.8848' in content:
                content = re.sub(r'<iframe[^>]*https://maps\.google\.com/maps[^>]*></iframe>', new_map_iframe, content)
                modified = True
            
            if 'https://maps.app.goo.gl/XUaDA6R4gQ7tML9RA' in content:
                content = content.replace('https://maps.app.goo.gl/XUaDA6R4gQ7tML9RA', 'https://maps.app.goo.gl/JJ4gArXVvhqm3ZyMA')
                modified = True

            # Fix Topbar Navigation consistency
            # Determine path depth
            is_hi = '/hi/' in filepath or '\\hi\\' in filepath
            depth = filepath.count('/') - 1
            if '\\' in filepath: depth = filepath.count('\\') - 1
            base_dir = '../' * max(0, depth)

            # English and Hindi standard Nav elements
            if is_hi:
                en_equivalent = filepath.replace('/hi/', '/').replace('\\hi\\', '\\')
                en_link = base_dir + en_equivalent.split('site/')[1] if 'site/' in en_equivalent else '../index.html'
                if file == 'index.html' and depth == 0:
                    en_link = '../index.html'
                nav_menu = f'<nav class="menu"><a href="{base_dir}index.html">होम</a><a href="{base_dir}index.html#specialities">विभाग</a><a href="{base_dir}doctors.html">डॉक्टर</a><a href="{base_dir}index.html#facilities">सुविधाएँ</a><a href="{base_dir}index.html#reviews">समीक्षाएँ</a><a href="{base_dir}contact.html">संपर्क</a><a class="lang" href="{en_link}">English</a><a class="btn btn-primary js-wa" href="#">अपॉइंटमेंट बुक करें</a></nav>'
            else:
                hi_equivalent = filepath.replace('site/', 'site/hi/').replace('site\\', 'site\\hi\\')
                hi_link = base_dir + 'hi/' + filepath.split('site/')[1]
                nav_menu = f'<nav class="menu"><a href="{base_dir}index.html">Home</a><a href="{base_dir}index.html#specialities">Specialities</a><a href="{base_dir}doctors.html">Doctors</a><a href="{base_dir}index.html#facilities">Facilities</a><a href="{base_dir}index.html#reviews">Reviews</a><a href="{base_dir}contact.html">Contact</a><a class="lang" href="{hi_link}">हिन्दी</a><a class="btn btn-primary js-wa" href="#">Book appointment</a></nav>'

            nav_match = re.search(r'<nav class="menu">.*?</nav>', content, flags=re.DOTALL)
            if nav_match:
                if nav_match.group(0) != nav_menu:
                    content = content[:nav_match.start()] + nav_menu + content[nav_match.end():]
                    modified = True

            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

if __name__ == '__main__':
    fix_contact_page('site/contact.html', False)
    fix_contact_page('site/hi/contact.html', True)
    fix_all_html()
    print("Done")
