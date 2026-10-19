(async()=>{const css=[];for(const sh of document.styleSheets){try{css.push([...sh.cssRules].map(r=>r.cssText).join('\n'))}catch(e){}}
const clone=document.documentElement.cloneNode(true);
clone.querySelectorAll('script,link[rel=stylesheet],link[rel=preload],link[rel=modulepreload],style,noscript,iframe').forEach(n=>n.remove());
const live=document.querySelectorAll('input,textarea,select'),cl=clone.querySelectorAll('input,textarea,select');
live.forEach((el,i)=>{const c=cl[i];if(!c)return;if(el.tagName==='TEXTAREA'){c.textContent=el.value}else if(el.tagName==='SELECT'){[...c.options].forEach((o,j)=>{if(j===el.selectedIndex)o.setAttribute('selected','')})}else{if(el.type==='checkbox'||el.type==='radio'){if(el.checked)c.setAttribute('checked','')}else c.setAttribute('value',el.value)}});
const imgs=clone.querySelectorAll('img'),limg=document.querySelectorAll('img');
for(let i=0;i<imgs.length;i++){const src=limg[i]&&limg[i].currentSrc;if(!src)continue;try{const b=await(await fetch(src)).blob();imgs[i].src=await new Promise(r=>{const f=new FileReader();f.onload=()=>r(f.result);f.readAsDataURL(b)});imgs[i].removeAttribute('srcset')}catch(e){}}
const sc=[...document.querySelectorAll('*')].filter(e=>e.scrollTop>0).map(e=>{const p=[];let n=e;while(n&&n!==document.documentElement){const par=n.parentElement;if(!par)break;p.unshift([...par.children].indexOf(n));n=par}return{p,t:e.scrollTop}});
const st=document.createElement('style');st.textContent=css.join('\n');clone.querySelector('head').appendChild(st);
const meta={url:location.href,w:innerWidth,h:innerHeight,scrollY:scrollY,inner:sc};
return '<!doctype html>\n<!--GPSNAP '+JSON.stringify(meta)+'-->\n'+clone.outerHTML})()
