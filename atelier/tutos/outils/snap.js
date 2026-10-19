// Capture autonome de l'écran courant (à exécuter dans la page, compte de démonstration uniquement).
// Définit window.__s() : renvoie le HTML (CSS intégré, images réduites en data URI, valeurs des champs,
// défilement de la page et du volet [role=dialog]). Le résultat est ensuite extrait par grab.py.
window.__s = async () => {
  const css = [];
  for (const sh of document.styleSheets) { try { css.push([...sh.cssRules].map(r => r.cssText).join('\n')) } catch (e) {} }
  const clone = document.documentElement.cloneNode(true);
  clone.querySelectorAll('script,link[rel=stylesheet],link[rel=preload],link[rel=modulepreload],style,noscript,iframe').forEach(n => n.remove());
  const live = document.querySelectorAll('input,textarea,select'), cl = clone.querySelectorAll('input,textarea,select');
  live.forEach((el, i) => { const c = cl[i]; if (!c) return;
    if (el.tagName === 'TEXTAREA') c.textContent = el.value;
    else if (el.tagName === 'SELECT') [...c.options].forEach((o, j) => { if (j === el.selectedIndex) o.setAttribute('selected', '') });
    else if (el.type === 'checkbox' || el.type === 'radio') { if (el.checked) c.setAttribute('checked', '') }
    else c.setAttribute('value', el.value) });
  const imgs = clone.querySelectorAll('img'), limg = document.querySelectorAll('img');
  for (let i = 0; i < imgs.length; i++) {
    const L = limg[i]; if (!L || !L.currentSrc) continue;
    try {
      const r = L.getBoundingClientRect(), k = Math.min(1, Math.min(1400, 2 * Math.max(r.width, 40)) / (L.naturalWidth || 1));
      const cv = document.createElement('canvas');
      cv.width = Math.max(1, Math.round((L.naturalWidth || r.width) * k)); cv.height = Math.max(1, Math.round((L.naturalHeight || r.height) * k));
      const bm = await createImageBitmap(await (await fetch(L.currentSrc)).blob());
      cv.getContext('2d').drawImage(bm, 0, 0, cv.width, cv.height);
      imgs[i].src = cv.toDataURL((r.width < 220 && /\.png|svg/i.test(L.currentSrc)) ? 'image/png' : 'image/jpeg', 0.85); imgs[i].removeAttribute('srcset');
    } catch (e) {}
  }
  const st = document.createElement('style'); st.textContent = css.join('\n'); clone.querySelector('head').appendChild(st);
  const dlg = document.querySelector('[role=dialog]');
  const meta = { url: location.href, w: innerWidth, h: innerHeight, scrollY: Math.round(scrollY), dlgTop: dlg ? Math.round(dlg.scrollTop) : 0 };
  return '<!doctype html>\n<!--GPSNAP ' + JSON.stringify(meta) + '-->\n' + clone.outerHTML;
};
'prêt';
