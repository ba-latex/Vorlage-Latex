# Hinweise

Hier befinden sich einige Hinweise, wie verschiedene Anforderungen der HAWA umgesetzt werden können:

- Metadaten (Titel, Autor(en), Matrikelnummer(n) usw.) werden in die Datei `metadaten.sty` eingetragen und dann im Dokument und in den PDF-Metadaten verwendet. Die Kommandos dazu können natürlich überall verwendet werden. 

- Fußnoten sollten durch `\fn{Fußnotentext}`, Online-Zitate durch `\onlinezitat{key}`, andere Zitate durch `\zitat{key}` eingetragen werden. Beispiele dazu, wie Quellen zu speichern sind, sind in `literatur.bib` zu finden.

- Mit `\label{bezeichner:name}` können Bezeichner für Elemente erstellt und später bspw. mit `\literef{label}` (generiert "Kapitel X"), `\fullref{label}` (generiert "siehe Kapitel X"), `\aref{label}` (für Anhänge), `\bref{label}` (für Abbildungen) usw. aufgerufen werden.

- Pixelgrafiken kann man mittels `\bild[skalierung]{dateiname}{Beschriftung}{label}` einfügen. Vektorgrafiken im SVG-Format analog dazu per `\svg[...]` (besser).

- Abkürzungen werden in `Inhalt/Abkürzungen.tex` eingetragen und im Text bspw. mit `\ac{Kürzel}` verwendet, siehe [Acronym](https://www.namsu.de/Extra/pakete/Acronym.html). Wichtig ist, dass zu Beginn der Umgebung `\begin{acronym}[SSHHH]` in die eckigen Klammern das längste Akronym eingetragen wird. Ansonsten wird die Seite nicht korrekt formatiert.

- Abkürzungen müssen in der richtigen Reihenfolge eingetragen oder das `sortieren.py`-Script verwendet werden.

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

- Normale Anführungszeichen ("") entsprechen nicht der Deutschen Rechtschreibung. Hierzu das Kommando `\striche{Text}` verwenden.

- Reverse SyncTeX: Um aus der PDF-Ansicht an die entsprechende Stelle im Code zu gelangen, diese mit gehaltener STRG-Taste anklicken.

- Forward SyncTeX: Um aus dem Code an die entsprechende Stelle der PDF zu gelangen, STRG+ALT+J drücken.
