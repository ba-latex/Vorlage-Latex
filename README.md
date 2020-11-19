# Vorlage-Latex
Die ist eine Latex Vorlage für Projektarbeiten und Belege

Unterhaltung und Besprechung:

[https://chat.4de19.de/channel/latex](https://chat.4de19.de/channel/latex)

## Changes 19. November 2020

- Es ist nun möglich ein Codeverzeichnis zu erzeugen, und eine Codeumgebung einzufügen. Siehe dazu Hinweise und die nächste Zeile

- Soll das Codeverzeichnis eingebunden werden, muss im System `Python3` und die Bibliothek `Pygments` (`pip install Pygments`) installiert sein. Außerdem muss im Latex-Compiler die Option `-shell-escape` hinzugefügt werden. Siehe dazu auch die [http://tug.ctan.org/macros/latex/contrib/minted/minted.pdf](http://tug.ctan.org/macros/latex/contrib/minted/minted.pdf) Minted Dokumentation. Wer das Code Verzeichnis nicht benötigt, muss in der Vorlage den Block `%! Hier wird das Codeverzeichnis formatiert` auskommentieren/ entfernen und in `Kapitel.tex` die Zeile `\listofcodes`  

- Ein paar Funktionen wurden in die `Vorlage.tex` eingefügt.


## Changes Juli 2020

- Die Ehrenwörtliche Erklärung wird jetzt direkt in der `Anhang.tex` eingebunden, da diese ja auch zum Anhang gehört

- Es gibt Änderung in `Kapitel.tex` und `Anhang.tex` bitte daher die aktuellen Vorlagen aus den `inhalt_example`-Ordner verwenden.

- Fertiges Anhangsverzeichnis

- neues System für Metadaten - unbedingt `metadaten.sty` in `Latex` verschieben und anpassen, da sonst das Kompilieren fehlschlägt

- nun auch Kapitelnummern in den PDF Lesezeichen

## Anleitung

1. RTFM!

2. Im Verzeichnis `Latex` befindet sich der Ordner `inhalt_example`, dieser muss kopiert werden und in `inhalt` umbenannt werden. Die `literatur.bib` und `metadaten.sty` müssen ins Hauptverzeichnis verschoben werden. Der `inhalt` Ordner beinhaltet den persönlichen Inhalt der Arbeit. Außerdem wird er in GitHub nicht mit eingebunden und die Vorlage kann unabhängig davon akutalisiert bzw. bearbeitet werden.

## Hinweise

- Die Metadaten (Titel, Autor(en), Matrikelnummer(n) usw.) werden in die Datei `metadaten.sty` eingetragen und dann im Dokument und in den PDF-Metadaten verwendet. Die Kommandos dazu können natürlich überall verwendet werden.

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

- mit `\label{bezeichner:name}` kann man in einer section oder sonst wo ein Label erstellen, was später oder eher mit `\fullref{bezeichner:name}` aufgerufen werden kann, fügt an der Stelle im Text ein `(siehe Kapitel x.x.x Schule ist schön)` ein.

- Bilder kann man bequem mittels `\bild[1.0]{schaltung1.png}{Test-Caption}` einfügen. Dabei entspricht *1.0* der horizontalen Größe von *0.0* bis *1.0*, *schaltung1* entspricht dem Bildnamen im Bilder-Verzeichnis und *Test-Caption* entspricht dem Label unter dem Bild und dem Namen im Abbildungsverzeichnis.

- Abkürzungen werden in `Inhalt/Abkürzungen.tex` eingetragen und im Text bspw. mit `\ac{Kürzel}` verwendet, siehe [Acronym](https://www.namsu.de/Extra/pakete/Acronym.html). Wichtig ist, dass zu Beginn der Umgebung `\begin{acronym}[SSHHH]` in die eckigen Klammern ein langer Name eingefügt ist, damit die Formatierung stimmt.

- Die Abkürzungen müssen in der richtigen Reihenfolge eingetragen werden

## ToDo

- Befindet sich ab sofort unter issues
