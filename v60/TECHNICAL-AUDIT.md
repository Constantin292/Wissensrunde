# Technische Bestandsaufnahme – Wissensrunde 60

## Verifizierte Ausgangsbasis
Die lokal vorliegende Spielversion 57 wurde auf ihren Quellcode untersucht.
- Rendering: eigene WebGL-2-Engine mit `canvas.getContext('webgl2', ...)`.
- 3D-Objekte: eigene `box(...)`-Funktion und Geometrie-/Farbverwaltung; kein nachgewiesenes Three.js.
- Spielbrett: 54 Felder auf quadratischem Rundkurs, Kategorienfolge `seq`, Farbliste `catcolors`, eigene Symbolzeichnung `glyph(...)`.
- Jahreszeiten: vorhandene Funktion `v51SetSeason(...)`.
- Einstellungen: bestehendes `settings()`-Menü.

## Konsequenzen
Ein externes glTF-/GLB-Assetpaket kann nicht ohne eigenen Modell- und Materialimporter in die bestehende Engine geladen werden. Vor Auswahl großer Assetpakete muss der Importweg geprüft und getestet werden. Eine alternative externe 3D-Engine darf nicht unbemerkt das Spiel ersetzen.

## Nächster konkreter Arbeitsschritt
1. Renderer und bestehende Modellrepräsentation isoliert untersuchen.
2. Einen kompatiblen Importpfad für glTF 2.0 / GLB festlegen oder einen schlanken Modellkonverter als Build-Schritt entwerfen.
3. Lizenzierte, stilistisch einheitliche Fantasy-Assets auswählen (Baum, Pilz, Felsen, Haus, Wasserfall).
4. **Ein** Asset in einer Kopie der bestehenden 3D-Spielszene darstellen und Kameraführung, Beleuchtung, Größe und Performance prüfen.
5. Erst danach eine vollständige Naturregion gestalten.

## Qualitätssicherung
- main/index.html bleibt unverändert.
- Neue Arbeiten nur auf entwicklung-v60; veröffentlichte Testdateien klar als Tests markieren.
- Kein zweidimensionales Ersatzbrett; die 2D-Vorschau ist keine Designbasis.
- Keine Zusage auf 1:1-Bildgleichheit ohne echte Asset- und Renderprüfung.
