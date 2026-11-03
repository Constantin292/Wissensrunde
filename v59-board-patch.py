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
# Integrate controls in the actual Alter & Schwierigkeitsgrad modal.
anchor="audio.onclick=v55AudioSettings;makeSelect(root,'Fragen auswählen nach'"
assert anchor in s, 'Original settings modal structure changed'
replacement="""audio.onclick=v55AudioSettings;
let envBtn=el('button','🌦 Jahreszeiten & Wetter',root);envBtn.className='action';
envBtn.onclick=()=>openConfig('Jahreszeiten & Wetter',pane=>{
 const season=document.getElementById('v51Season'),weather=document.getElementById('v51Weather');
 if(!season||!weather){el('p','Wettersteuerung nicht verfügbar.',pane);return}
 makeSelect(pane,'Jahreszeit',['Sommer','Frühling','Herbst','Winter'],season.value,v=>{season.value=v;season.dispatchEvent(new Event('change'))});
 makeSelect(pane,'Wetter',['Klar','Regen','Schnee'],weather.value,v=>{weather.value=v;weather.dispatchEvent(new Event('change'))});
 let back=el('button','Zurück',pane);back.className='action';back.onclick=settings;
});
makeSelect(root,'Fragen auswählen nach'"""
s=s.replace(anchor,replacement,1)
# Hide original floating environment toolbar. Its controls remain active and are synchronized.
s=s.replace('</body>', '<style id="v59EnvHidden">#v51LandscapeControls{display:none!important}</style></body>',1)
assert '</body>' in s
s=s.replace('</body>',inject+'</body>',1)
assert all(seq[i]!=seq[(i+1)%54] for i in range(54))
assert len(s)>1_000_000
p.write_text(s,encoding='utf-8')
print('Version 59: 54 distinct categories checked, corner fields selectively adjusted, symbols contrasted, settings moved')

# Trigger preview build
