/* R N Multispeciality Hospital — site behaviour
   - Footer year + experience counters
   - Mobile nav
   - WhatsApp booking: number assembled at runtime (kept out of the static HTML
     so it is not openly scrapable), per-department routing, 1-click messages,
     a floating "Book on WhatsApp" button, and structured-form handling. */

// ---- CONFIGURATION (Edit these numbers directly to update the whole site!) ----
var CONFIG_PHONE_DISPLAY = "0141 239 0320";
var CONFIG_PHONE_TEL     = "+911412390320";

document.querySelectorAll('.js-phone-display').forEach(function(el){ el.textContent = CONFIG_PHONE_DISPLAY; });
document.querySelectorAll('.js-phone-link').forEach(function(el){ el.href = "tel:" + CONFIG_PHONE_TEL; });

// ---- footer year ----
document.querySelectorAll('[data-year]').forEach(function(el){ el.textContent = new Date().getFullYear(); });


// ---- mobile nav ----
var burger = document.getElementById('burger');
var mob = document.getElementById('mobileMenu');
if(burger && mob){ burger.addEventListener('click', function(){
  mob.style.display = (mob.style.display === 'flex') ? 'none' : 'flex';
}); }

// ---- speciality card images follow the existing learn-more link ----
document.querySelectorAll('#specialities .card-img').forEach(function(img){
  var card = img.closest('.card');
  var link = card && card.querySelector('a.more[href]');
  if(!link) return;
  img.setAttribute('role', 'link');
  img.setAttribute('tabindex', '0');
  img.setAttribute('aria-label', link.textContent.trim());
  img.addEventListener('click', function(){
    window.location.href = link.href;
  });
  img.addEventListener('keydown', function(e){
    if(e.key === 'Enter' || e.key === ' '){
      e.preventDefault();
      window.location.href = link.href;
    }
  });
});

// ---- WhatsApp numbers (assembled at runtime, not stored as plain text) ----
var HOSPITAL_WA = ['91','952','132','3878'].join('');   // +91 95213 23878 (hospital line / Dr Robin Bothra)
var DR_CHITRA   = ['91','636','751','7838'].join('');   // +91 63675 17838 (Dr Chitra Soni)

// Department -> WhatsApp number. Anything not listed falls back to the hospital line.
var WA_ROUTES = {
  'gynaecology': DR_CHITRA,        // Dr Chitra Soni
  'general-surgery': HOSPITAL_WA,  // Dr Robin Bothra (hospital line)
  'pain-spine': HOSPITAL_WA        // Dr Naveen Soni — TODO: swap in dedicated number when supplied
};
function waNumberFor(dept){ return (dept && WA_ROUTES[dept]) || HOSPITAL_WA; }

var isHindi = (document.documentElement.lang === 'hi');

function openWhatsApp(number, message){
  var url = 'https://wa.me/' + number + '?text=' + encodeURIComponent(message);
  window.open(url, '_blank', 'noopener');
}

// 1-click quick-book message (name left blank for the patient to type)
function quickBookMessage(target){
  if(isHindi){
    return 'नमस्ते, मुझे R N Multispeciality Hospital में अपॉइंटमेंट चाहिए।'
         + '\nनाम: '
         + '\nडॉक्टर / विभाग: ' + (target || 'सामान्य पूछताछ');
  }
  return 'Hello, I would like to book an appointment at R N Multispeciality Hospital.'
       + '\nName: '
       + '\nDr / Department: ' + (target || 'General enquiry');
}

// ---- 1-click WhatsApp links/buttons (class "js-wa") ----
// Optional data attributes: data-dept (routing key), data-doc (doctor name),
// data-deptlabel (readable department). No number sits in the markup.
document.addEventListener('click', function(e){
  var el = e.target.closest ? e.target.closest('.js-wa') : null;
  if(!el) return;
  e.preventDefault();
  var dept = el.getAttribute('data-dept') || '';
  var doc = el.getAttribute('data-doc') || '';
  var deptLabel = el.getAttribute('data-deptlabel') || '';
  
  // If no dept/doc specified, see if we are inside a doctor card
  if(!dept && !doc) {
    var docCard = el.closest('.doc');
    if(docCard) {
      var h3 = docCard.querySelector('h3');
      if(h3) doc = h3.textContent.trim();
      
      // Auto-route based on doctor name
      if(doc.indexOf('Chitra') !== -1) dept = 'gynaecology';
      else if(doc.indexOf('Bothra') !== -1) dept = 'general-surgery';
      else if(doc.indexOf('Naveen') !== -1) dept = 'pain-spine';
    }
  }

  var target = doc ? (doc + (deptLabel ? ' — ' + deptLabel : '')) : deptLabel;
  openWhatsApp(waNumberFor(dept), quickBookMessage(target));
});

// ---- booking form (structured: name, phone, department, date, time slot) ----
var form = document.getElementById('bookForm');
if(form){
  form.addEventListener('submit', function(e){
    e.preventDefault();
    // use elements[] so the input named "name" is not shadowed by HTMLFormElement.name
    var f = form.elements;
    var name  = (f['name'] && f['name'].value || '').trim();
    var phone = (f['phone'] && f['phone'].value || '').trim();
    var deptEl = f['department'];
    var dept  = deptEl ? deptEl.value : 'other';
    var deptLabel = deptEl ? deptEl.options[deptEl.selectedIndex].text : '';
    var date  = (f['prefDate'] && f['prefDate'].value || '').trim();
    var slot  = (f['prefTime'] && f['prefTime'].value || '').trim();
    var when  = [date, slot].filter(Boolean).join(', ');

    var msg = isHindi
      ? ('नमस्ते, मुझे अपॉइंटमेंट चाहिए।\nनाम: ' + name + '\nफ़ोन: ' + phone +
         '\nविभाग: ' + deptLabel + (when ? ('\nपसंदीदा समय: ' + when) : ''))
      : ('Hello, I would like to book an appointment.\nName: ' + name + '\nPhone: ' + phone +
         '\nDepartment: ' + deptLabel + (when ? ('\nPreferred: ' + when) : ''));

    var ok = document.getElementById('formOk');
    if(ok){ ok.style.display = 'block'; }
    openWhatsApp(waNumberFor(dept), msg);
  });
}

// ---- floating "Book on WhatsApp" button (injected; no number in the HTML) ----
(function(){
  if(document.querySelector('.wa-fab')) return;
  var a = document.createElement('a');
  a.className = 'wa-fab js-wa';
  a.href = '#';
  a.setAttribute('aria-label', isHindi ? 'व्हाट्सऐप पर बुक करें' : 'Book on WhatsApp');
  a.innerHTML =
    '<svg viewBox="0 0 32 32" width="26" height="26" aria-hidden="true" focusable="false">' +
    '<path fill="currentColor" d="M16 3C9.4 3 4 8.4 4 15c0 2.1.6 4.1 1.6 5.9L4 29l8.3-1.6c1.7.9 3.6 1.4 5.7 1.4 6.6 0 12-5.4 12-12S22.6 3 16 3zm0 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7.7.7-3.6-.2-.4c-1-1.6-1.5-3.4-1.5-5.3 0-5.4 4.4-9.8 9.8-9.8s9.8 4.4 9.8 9.8-4.4 9.8-9.8 9.8zm5.4-7.3c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-1.8-.9-3-1.6-4.2-3.6-.3-.5.3-.5.9-1.6.1-.2 0-.4 0-.6s-.7-1.7-1-2.3c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.8s1.2 3.3 1.4 3.5c.2.2 2.4 3.7 5.8 5.1 2.1.9 2.9.9 4 .8.6-.1 1.8-.7 2.1-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.2-.6-.4z"/>' +
    '</svg><span>' + (isHindi ? 'व्हाट्सऐप पर बुक करें' : 'Book on WhatsApp') + '</span>';
  document.body.appendChild(a);
})();
