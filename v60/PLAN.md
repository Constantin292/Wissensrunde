# Wissensrunde 60 – Neun Wissenswelten

Status: Konzept und isolierter Entwicklungszweig. Keine Änderungen an der produktiven index.html.

## Unveränderliche Spielregeln
- 54 Felder, neun Kategorien mit jeweils sechs Feldern.
- Kein direkt aufeinanderfolgendes Feld derselben Kategorie, einschließlich Übergang Feld 54 → Feld 1.
- Vorhandene Würfel-, Fragen-, Pokal-, Spielstand- und Siegmechanik bleiben erhalten.
- Bestehende gespeicherte Spielstände dürfen nicht ohne Migration verändert werden.

## Gestaltung
- Neun unterschiedliche, aber zusammenhängende Landschaftsregionen.
- Kategorien aus der aktuellen Fragenbank übernehmen, nicht blind umbenennen.
- Große, gut erkennbare Spielfelder mit sauberer Eckgeometrie und kontrastreichen Symbolen.
- Natur statt Stadtverkehr; flüssige Darstellung auch auf durchschnittlichen Computern.
- Bestehende Einstellungen verwenden; Jahreszeit, Wetter, Licht und Nachtmodus dort integrieren.
- Vier deutlich unterscheidbare sanfte Instrumentalstücke; nur mit geklärten Nutzungsrechten.

## Technische Phasen
1. Bestehenden HTML-/JavaScript-Code erfassen: Kategorien, Feldgeometrie, Renderer, Steuerung, Speicherung.
2. Szenenarchitektur für neun Regionen als Datenmodell erstellen, ohne die Hauptdatei zu verändern.
3. Erste Region prototypisch rendern; Performance und Darstellung prüfen.
4. Weitere acht Regionen und Wegübergänge ergänzen.
5. Spielfiguren, Animationen und Ereignisse integrieren.
6. Automatisierte Checks und manueller Browser-Test auf separater Testadresse.
7. Nur nach Freigabe in die reguläre Spielversion übernehmen.

## Abnahmekriterien
- Vollständiger Spielstart und spielbare Runde mit zwei bis vier Figuren.
- Alle 54 Felder erkennbar, ohne Kollisionen oder direkte Kategorieduplikate.
- Alle neun Pokale erreichbar; Speichern und Laden funktionieren.
- Menü, Musikregler und Wettereinstellungen korrekt bedienbar.
- Keine Verschlechterung der Ladezeit oder schwerwiegende Konsolenfehler.
- Hauptzweig main bleibt während der Entwicklung unverändert.
