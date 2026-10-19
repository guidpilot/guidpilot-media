// Capture autonome de l'écran courant (à exécuter dans la page, compte de démonstration uniquement).
// window.__s() : HTML autonome (CSS utile seulement, images réduites, valeurs des champs, défilement).
// window.__cap(masques) : capture + masques texte [[avant, après], ...] → window.__P, renvoie la taille.
// window.__chunk(n) : morceau n (240 000 caractères) préfixé '@@CHUNKn@@' — à extraire avec grab_chunks.py.
window.__s = async () => {
  const keep = (sel) => { try { const s = sel.replace(/(?<!\\)::?[a-z-]+(\([^)]*\))?/gi, '').trim() || '*'; return !!document.querySelector(s) } catch (e) { return true } };
  const ser = (rules) => { const out = []; for (const r of rules) {
      if (r instanceof CSSStyleRule) { if (r.selectorText.split(',').some(keep)) out.push(r.cssText) }
      else if (r.cssRules && !(r instanceof CSSKeyframesRule)) { const inner = ser(r.cssRules); if (inner.length) { const head = r.cssText.slice(0, r.cssText.indexOf('{')); out.push(head + '{' + inner.join('\n') + '}') } }
      else out.push(r.cssText) } return out };
  const css = [];
  for (const sh of document.styleSheets) { try { css.push(ser(sh.cssRules).join('\n')) } catch (e) {} }
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
window.__cap = async (masks) => { let h = await window.__s(); for (const [a, b] of (masks || [])) h = h.split(a).join(b); window.__P = h; return [h.length, Math.ceil(h.length / 240000)] };
window.__chunk = (n) => '@@CHUNK' + n + '@@' + window.__P.slice(n * 240000, (n + 1) * 240000);
'prêt';
