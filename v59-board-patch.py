from pathlib import Path
import re,random
p=Path('index.html')
s=p.read_text(encoding='utf-8')
assert len(s)>1_000_000, 'Refusing to edit incomplete game'
m=re.search(r'const seq=\[([^\]]+)\];const catcolors=',s)
assert m, 'Board category sequence missing'
old=[int(v) for v in m.group(1).split(',')]
assert len(old)==54 and all(old.count(i)==6 for i in range(9))
rng=random.Random(5903)
for attempt in range(10000):
    seq=[v for v in range(9) for _ in range(6)]
    rng.shuffle(seq)
    if all(seq[i]!=seq[(i+1)%54] for i in range(54)):
        break
else: raise ValueError('No valid category ordering')
s=s[:m.start(1)]+','.join(map(str,seq))+s[m.end(1):]
assert 'const size=1.095;' in s
s=s.replace('const size=1.095;', 'const size=.555;',1)
# Increase glyph contrast with dark backing on all category tiles.
anchor='for(let i=1;i<cells.length;i++)glyph(seq[i],cells[i][0],cells[i][1]);'
assert anchor in s
s=s.replace(anchor, "for(let i=1;i<cells.length;i++){box(cells[i][0],.166,cells[i][1],.38,.008,.38,color('#12354a'));glyph(seq[i],cells[i][0],cells[i][1]);}",1)
# Replace the original settings dock with a collapsible settings menu only during gameplay.
inject=r"""
<script id="v59BoardSettings">
(function(){
'use strict';
const css=document.createElement('style');
css.textContent='body:not(.playing) #v59Settings{display:none!important}#v59Settings{position:fixed;right:12px;top:12px;z-index:1100;background:#0b3046;color:white;border:1px solid #e2bd77;border-radius:12px;padding:10px;max-width:240px;box-shadow:0 6px 24px #0008}#v59Settings summary{cursor:pointer;font-weight:bold}#v59Settings #v51LandscapeControls{position:static!important;top:auto!important;right:auto!important;bottom:auto!important;left:auto!important;display:flex!important;width:200px!important;max-width:100%!important;margin-top:10px!important;box-shadow:none!important}#v59Settings:not([open]) #v51LandscapeControls{display:none!important}';
document.head.append(css);
const dock=document.getElementById('v51LandscapeControls');
if(!dock)return;
const details=document.createElement('details');details.id='v59Settings';
const summary=document.createElement('summary');summary.textContent='⚙ Einstellungen';
details.append(summary);details.append(dock);document.body.append(details);
})();
</script>
"""
assert '</body>' in s
s=s.replace('</body>',inject+'</body>',1)
assert all(seq[i]!=seq[(i+1)%54] for i in range(54))
assert len(s)>1_000_000
p.write_text(s,encoding='utf-8')
print('Version 59: 54 distinct categories checked, corners resized, symbols contrasted, settings moved')
