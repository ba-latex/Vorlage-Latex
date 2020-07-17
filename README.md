# Vorlage-Latex
Die ist eine Latex Vorlage für Projektarbeiten und Belege

Unterhaltung und Besprechung:

[https://talk.4de19.de/channel/latex](https://talk.4de19.de/channel/latex)

## Anleitung

1. Die Dateien herunterladen und sich nicht blöd anstellen...

2. Im Verzeichnis `Latex` befindet sich der Ordner `inhalt_example`, dieser muss kopiert werden und in `inhalt` umbenannt werden. Die `literatur.bib` muss ins Hauptverzeichnis verschoben werden. Der `inhalt` Ordner beinhaltet den persönlichen Inhalt der Arbeit. Außerdem wird er in GitHub nicht mit eingebunden und die Vorlage kann unabhängig davon akutalisiert bzw. bearbeitet werden.

## Hinweise

- Jeder neue Absatz muss mit `\absatz` und einer Leerzeile davor anfangen.

- Das ganze ist etwas Zusammengebastelt

- `\zitat{}` erstellt eine Fußnote wie in der Vorlage gewünscht

- für Onlinequellen `\onlinezitat{}` benutzen; damit diese richtig angezeigt wird muss der Eintrag in die `literatur.bib` folgendermaßen aussehen:
```latex
@Online{LogikSim,
  author   = {Christian BRUGGER},
  title    = {LogikSim - Logische Schaltungen},
  url      = {https://logiksim.dbclan.de/index.html},
  urldate  = {2020-07-22},
  keywords = {logik, sim, schaltungen, logisch},
  year     = {2007},
}
```

- Bilder kann man bequem mittels `\bild[1.0]{schaltung1.png}{Test-Caption}` einfügen. Dabei entspricht *1.0* der horizontalen Größe von *0.0* bis *1.0*, *schaltung1* entspricht dem Bildnamen im Bilder-Verzeichnis und *Test-Caption* entspricht dem Label unter dem Bild und dem Namen im Abbildungsverzeichnis.

- Abkürzungen werden in `Inhalt/Abkürzungen.tex` eingetragen und im Text bspw. mit `\ac{Kürzel}` verwendet, siehe [Acronym](https://www.namsu.de/Extra/pakete/Acronym.html)

- Die Abkürzungen müssen in der richtigen Reihenfolge eingetragen werden

## ToDo

- [ ] Formatierung fürs Literaturverzeichnis erarbeiten.

- [ ] Anhangsverzeichnis

- usw.
