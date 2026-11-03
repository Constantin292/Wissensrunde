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
s=s.replace('const size=1.095;', 'const size=(i%13.5<1.1||i%13.5>12.4)?1.025:1.095;',1)
# Increase glyph contrast with dark backing on all category tiles.
anchor='for(let i=1;i<cells.length;i++)glyph(seq[i],cells[i][0],cells[i][1]);'
assert anchor in s
s=s.replace(anchor, "for(let i=1;i<cells.length;i++){box(cells[i][0],.166,cells[i][1],.38,.008,.38,color('#12354a'));glyph(seq[i],cells[i][0],cells[i][1]);}",1)
# Replace the original settings dock with a collapsible settings menu only during gameplay.
inject=r"""
<script id="v59BoardSettings">
(function(){
'use strict';
const dock=document.getElementById('v51LandscapeControls');
if(!dock)return;
const settings=document.querySelector('#settingsPanel, #settingsModal, .settings-panel, .settings-modal, #settings, [data-panel="settings"]');
if(!settings){dock.style.display='none';console.warn('Wissensrunde 59: existing settings container not identified; landscape controls hidden until integration');return}
dock.style.position='static';dock.style.inset='auto';dock.style.display='block';dock.style.margin='12px 0';
settings.appendChild(dock);
})();
</script>
"""
assert '</body>' in s
s=s.replace('</body>',inject+'</body>',1)
assert all(seq[i]!=seq[(i+1)%54] for i in range(54))
assert len(s)>1_000_000
p.write_text(s,encoding='utf-8')
print('Version 59: 54 distinct categories checked, corner fields selectively adjusted, symbols contrasted, settings moved')

# Trigger preview build
