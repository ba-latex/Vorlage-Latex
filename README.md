# Vorlage-Latex
Die ist eine Latex Vorlage für Projektarbeiten und Belege

Unterhaltung und Besprechung:

[https://chat.4de19.de/channel/latex](https://chat.4de19.de/channel/latex)


## Changes 05. Januar 2021

- Titelseiten und Erklärungen an neue Changes und lange Titel angepasst

- Multirow Paket eingefügt

- Kommentare zu SVGs angepasst

- Bild Command benötigt jetzt noch einen weiteren Parameter, den labelnamen

- Absatz Befehl muss überall entfernt werden

- Ausführliche Changes kommen wenn die Tastatur wieder geht


## Changes 22. November 2020

- neue Felder für Adresse von Autor und Praxispartner in 'Titelseite_Praxisbeleg.tex' - müssen direkt dort eingetragen werden, nicht in 'metadaten.sty'

- neues Paket lineno wird geladen, um Warnungen zu vermeiden

- veraltete Befehle durch neue ersetzt, um Warnungen zu vermeiden und Zukunftssicherheit zu verbessern

- neue Erklärung zur Plagiatsprüfung erstellt, Ehrenwörtliche Erklärung überarbeitet, beides aufgeteilt in Versionen für Praxisbeleg und mehrere Autoren

- Sonderzeichen in PDF-Metadaten gefixt, erneut...

## Changes 19. November 2020 - 2

- Es gibt nun ein Formelverzeichnis

- Bitte die neue `Kapitel.tex` aus dem `inhalt_example`-Ordner ins `inhalt`-Verzeichnis kopieren und die alte überschreiben.

- Wer das Formelverzeichnis nicht benötigt muss in `Kapitel.tex` die Zeile `\listofformeln` löschen oder auskommentieren.

- In diesem Zuge wurde eine Formelumgebung eingeführt die benutzt werden muss. Siehe Hinweise.

## Changes 19. November 2020

- Bitte die neue `Kapitel.tex` aus dem `inhalt_example`-Ordner ins `inhalt`-Verzeichnis kopieren und die alte überschreiben.

- Es ist nun möglich ein Codeverzeichnis zu erzeugen, und eine Codeumgebung einzufügen. Siehe dazu Hinweise und die nächste Zeile

- Soll das Codeverzeichnis eingebunden werden, muss im System `Python3` und die Bibliothek `Pygments` (`pip install Pygments`) installiert sein. Außerdem muss im Latex-Compiler die Option `-shell-escape` hinzugefügt werden. Siehe dazu auch die [http://tug.ctan.org/macros/latex/contrib/minted/minted.pdf](http://tug.ctan.org/macros/latex/contrib/minted/minted.pdf) Minted Dokumentation. Wer das Code Verzeichnis nicht benötigt, muss in der Vorlage den Block `%! Hier wird das Codeverzeichnis formatiert` auskommentieren/ entfernen und in `Kapitel.tex` die Zeile `\listofcodes`  

- Ein paar Funktionen wurden in die `vorlage.tex` eingefügt. Siehe dazu auch Hinweise

- Die `literatur.bib` im `inhalt_example`-Ordner enthält nun sinnvolle Beispiele

- Es ist nun möglich ein Logo oben links im Rand einzufügen. Dieses muss sich unter `bilder/logo.png` befinden. ACHTUNG diese DATEI muss EXISTIEREN. Sollte dies nicht gewollt sein, kann in `vorlage.tex` die Zeile 201 `\lohead{\includegraphics[height=8mm]{bilder/logo.png}}` zu `\lohead{}` geändert werden.

- Vielleicht habe ich was vergessen...

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

- Die meisten Metadaten (Titel, Autor(en), Matrikelnummer(n) usw.) werden in die Datei `metadaten.sty` eingetragen und dann im Dokument und in den PDF-Metadaten verwendet. Die Kommandos dazu können natürlich überall verwendet werden. 

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

- `\vglink{url}{datum}` erzeugt eine Fußnote mit vgl. link (xx.xx.2020) nach der gültigen Formatierung

- Soll Programmcode in der Arbeit angezeigt bzw. eingebunden werden so steht dafür nun die Umgebung `\begin{code}` zur Verfügung. Der genaue Syntax ist folgender:
```latex
\begin{code}[H]
    \inputminted[linenos, breaklines, gobble=0, frame=none,
        firstline=27,
        lastline=37,
        firstnumber=17,
        numbers=left,
        numbersep=5pt]{python}{sourcecodes/excel2.py}
    \caption{Auslesen der Daten aus dem Array}
    \label{code:4}
\end{code}
```

- Für mehr Informationen dazu bitte die Minted-Dokumentation konsultieren. Es ist möglich mittels ` \mintinline{python}{print("Toller Code")}` Code in einer Zeile ähnlich dem Mathemathikmodus zu verwenden.

- Die Formelumgebung wird wie folgt aufgerufen:
```latex
\begin{formel}[H]
\captionabove{Die erste aller Formeln}
$[\lnot P\land\lnot Q] \lor R$ \vspace{3mm}\\
$P=\text{was ganz tolles}$ \\
$Q=\text{was noch viel tolleres}$
\label{formel:test}
\end{formel}
```

- Soll die Caption darunter stehen muss `\captionabove{}` durch `\caption{}` ersetzt werden und über `\label{}` geschrieben werden.

- Die einzelnen Zeilen der Formel werden im Mathemathikmodus geschrieben. Die Erklärung der Formelzeichen auch. Siehe dazu auch das HAWA-Dokument.


## ToDo

- Befindet sich ab sofort unter issues
