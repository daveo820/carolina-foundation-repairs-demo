// CFR concept: reveals, laser sweep, menu, demo form
(function(){
 var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
 var els = document.querySelectorAll('.rv,.laser');
 function on(e){ e.classList.add(e.classList.contains('laser') ? 'on' : 'in'); }
 if (reduce || !('IntersectionObserver' in window)) { els.forEach(on); }
 else {
  var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ on(e.target); io.unobserve(e.target);} }); },{rootMargin:'0px 0px -6% 0px',threshold:.05});
  els.forEach(function(e){ io.observe(e); });
 }
 var b = document.querySelector('.menu-btn'), m = document.getElementById('menu');
 if (b && m) b.addEventListener('click', function(){ var o = m.classList.toggle('open'); b.setAttribute('aria-expanded', o); });
 var f = document.getElementById('qform');
 if (f) f.addEventListener('submit', function(ev){ ev.preventDefault(); document.getElementById('qmsg').textContent = 'Thanks. This is a demo, so nothing was sent. On the real site this goes to the office in New Bern.'; });
})();
