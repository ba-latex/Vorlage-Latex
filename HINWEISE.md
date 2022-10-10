# Hinweise

Hier befinden sich einige Hinweise dazu, wie verschiedene Anforderungen der HAWA umgesetzt werden können.

## Allgemeines

- Metadaten (Titel, Autor(en), Matrikelnummer(n) usw.) werden in die Datei `metadaten.sty` eingetragen und dann im Dokument und in den PDF-Metadaten verwendet. Die Kommandos dazu können natürlich überall verwendet werden. Sollte ein sehr langer Titel gewählt werden, ist es möglich, dass dieser auf den Titelseiten oder den Erklärungen zu Problemen führt. Diese müssen in den jeweiligen Titelseiten- (verringerte Abstände und/oder Schriftgröße) bzw. Erklärungsdateien (zusätzliche Zeilen) behoben werden.

- Anhand der Metadaten wird automatisch entschieden, welche Versionen der Titelseite und Erklärungen verwendet werden.

- in den Dateien `main_abstract.tex` und `main_zustimmung.tex` befinden sich das Abstract und die Zustimmung zur Plagiatsprüfung, da beide jeweils extra abzugeben sind.

## Fußnoten und Referenzen

- Fußnoten sollten durch `\fn{Fußnotentext}`, Online-Zitate durch `\onlinezitat{key}`, andere Zitate durch `\zitat[Seite]{key}` eingetragen werden. Beispiele dazu, wie Quellen zu speichern sind, sind in `literatur.bib` zu finden. Außerdem existieren äquivalente Befehle für sinngemäße Zitate: `\vgonlinezitat{key}` bzw. `\vgzitat[Seite]{key}`. In `Doku-Test.tex` sind Beispiele zur Nutzung zu finden.

- Mit `\label{bezeichner:name}` können Bezeichner für Elemente erstellt werden. Auf diese kann über LaTeX-eigene oder in `vorlage/vorlage-commands.tex` definierte Kommandos `\literef` und `\fullref` zugegriffen werden.
Für weitere Details zu Referenzen siehe `Doku-Test.tex` bzw. die standardmäßig daraus generierte PDF.

- `\vglink{url}{datum}` erzeugt eine Fußnote mit vgl. link (xx.xx.2020) nach der gültigen Formatierung

- Soll in der Caption einer Abbildung / Tabelle / Code / Formel / usw. eine Fußnote verwendet werden, oder ein `\vglink`, so sind zwei zusätzliche Befehle notwendig.
    - Statt `\caption{Beispielcaption}` muss in der Float-Umgebung `\linkcaption{Beispielcaption}` verwendet werden.
    Diese Fußnote wird am Ende der Caption angefügt.
    - Nach der Float-Umgebung, muss entweder mit `\footnotetext{Die gewünschte Fußnote}` oder mit `\vgcaption{Link}{Datum}` der entsprechende Fußnotentext gesetzt werden. 
    - Beispiel mit `\vgcaption`:
        ```tex
        \begin{code}
        \linkcaption{Beispielcode}
        \label{code:example2}
        \end{code}
        \vgcaption{https://example.com}{06.07.2022}
        ```
    - **Besonderheit:** Soll die Fußnote im Text der Caption stehen, ist eine andere Vorgehensweise nötig (ausführlich: https://tex.stackexchange.com/questions/10181/using-footnote-in-a-figures-caption):
        ```tex
        \begin{code}
        \caption[Caption ohne Fußnote]{Caption mit\footnotemark Fußnote}
        \end{code}
        \footnotetext{Text der Fußnote}
        ```

## Grafiken
- Pixelgrafiken kann man mittels `\bild[skalierung]{dateiname}{Beschriftung}{label}` einfügen
- Vektorgrafiken im SVG-Format analog dazu per `\svg[...]` (besser).

## Abkürzungen
- Abkürzungen werden in `Inhalt/Abkürzungen.tex` eingetragen und im Text bspw. mit `\ac{Kürzel}` verwendet, siehe [Acronym](https://www.namsu.de/Extra/pakete/Acronym.html). Wichtig ist, dass zu Beginn der Umgebung `\begin{acronym}[SSHHH]` in die eckigen Klammern das längste Akronym eingetragen wird. Ansonsten wird die Seite nicht korrekt formatiert.
    - Abkürzungen in der Mehrzahl: `\acp{Kürzel}`
    - erzwungene Kurzform: `\acs{Kürzel}`
    - erzwungene Langform: `\acf{Kürzel}`
    - Abkürzungen in Überschriften ausschließlich ohne `\ac{}`-Kommandos verwenden

- Abkürzungen müssen in der richtigen Reihenfolge eingetragen oder das `sortieren.py`-Script verwendet werden.


## Float-Umgebungen (Code, Verzeichnisse, usw.)
- Soll Programmcode in der Arbeit angezeigt bzw. eingebunden werden so steht dafür nun die Umgebung `\begin{code}` zur Verfügung. Der genaue Syntax ist folgender:
    ```tex
    \begin{code}
        \inputminted[
            firstline=27,
            lastline=37,
            firstnumber=17,
            numbersep=5pt]{python}{sourcecodes/excel2.py}
        \caption{Auslesen der Daten aus dem Array}
        \label{code:4}
    \end{code}
    ```

- Um Verzeichnisstrukturen darzustellen, wird `\verzeichnis` mit den eigenen Befehlen `\dtfolder` und `\dtfile` genutzt:
  - Dieses Kommando basiert auf Dirtree, in dessen [Doku](http://tug.ctan.org/macros/generic/dirtree/dirtree.pdf) weitere nützilche Kommandos erläutert werden.
    ```tex
    \verzeichnis{%
        .1 \dtfolder Ordner 1. %Ebene 1
        .2 \dtfolder Unterordner 1. %Ebene 2
        .3 \dtfile Datei 1. %Ebene 3
        .2 \dtfolder Unterordner 2. %Ebene 2
        .3 \dtfolder Unter-Unterordner 1. %Ebene 3
        .4 \dtfile Datei 2. %Ebene 4
        .3 \dtfolder Unter-Unterordner 2. %Ebene 3
    }{Beschriftung}{label}
    ```

- Für mehr Informationen dazu bitte die Minted-Dokumentation konsultieren. Es ist möglich mittels ` \mintinline{python}{print("Toller Code")}` Code in einer Zeile ähnlich dem Mathemathikmodus zu verwenden.

- Die Formelumgebung wird wie folgt aufgerufen:
    ```tex
    \formula{$Formel$}{Legende}{Beschreibung}{Label}
    ```
    - Beispiel:
    ```tex
    \formula{$\Delta p_{WZ}=\Delta p\cdot\dfrac{\dot{V}^2_S}{\dot{V}^2_G}$}{%
        $\dot{V}^2_S = $ Spitzendurchfluss $\left[ m^3/h\right]$\\
        $\dot{V}^2_G = $ maximaler Durchfluss im Wasserzähler $\left[ m^3/h\right]$\\
        $\Delta p = $ Druckverlust bei $V_{max} \left[bar\right]$}{Druckverlust}{formel:ohm}
    ```

- Die einzelnen Zeilen der Formel werden im Mathemathikmodus geschrieben. Die Legende ebenfalls. Siehe dazu auch das HAWA-Dokument.

- Die Positionierung von Float-Umgebungen wird in der `vorlage.tex` definiert. Standard ist `htbp`, was bedeutet, dass alle "Floats" (Abbildungen, Tabellen, Codes, Formeln, Verzeichnisbäume...) standardmäßig, wenn möglich, "hier" (also an der selben Stelle wie im LaTeX-Code) positioniert werden (h), ansonsten am oberen Ende der Seite (t), ansonsten am Ende Seite (b) oder, notfalls, auf einer Seite voller Floats (p).

- Soll ein Float unbedingt exakt an der selben Stelle wie im Quellcode platziert werden, kann dies mit `[H]` erzwungen werden (bspw. `\begin{table}[H]`).

- In Floats wird standardmäßig ebenfalls der durch die BA geforderte Zeilenabstand von 1,3 genutzt. Falls hier ein kleinerer Zeilenabstand gewünscht ist, kann dieser manuell per `\linespread{1}` innerhalb des Floats oder global durch Entfernen der zu diesem Zweck in `vorlage.tex` auf `\usepackage{setspace}` folgend eingesetzten Zeilen auf 1 gesetzt werden.

## Sonstiges
- Normale Anführungszeichen ("") entsprechen nicht der Deutschen Rechtschreibung. Hierzu das Kommando `\striche{Text}` verwenden.

- Reverse SyncTeX: Um aus der PDF-Ansicht an die entsprechende Stelle im Code zu gelangen, diese mit gehaltener STRG-Taste anklicken.

- Forward SyncTeX: Um aus dem Code an die entsprechende Stelle der PDF zu gelangen, STRG+ALT+J drücken. Hierzu muss allerdings die Tastenkombination bearbeitet werden.
  -  hintereinander STRG+K, STRG+S drücken
  -  im erscheinenden Fenster "Tastenkombinationen" nach "Synctex from cursor" suchen
  -  Rechtsklick auf die Zeile mit Tastenzuordnung "STRG+ALT+J" --> "when-Ausdruck ändern"
  -  `editorTextFocus && !config.latex-workshop.bind.altKeymap.enabled && editorLangId == 'latex'` durch `editorTextFocus && editorLangId == 'latex'` ersetzen (bzw. `!config.latex-workshop.bind.altKeymap.enabled &&` entfernen)
  -  mit Enter bestätigen
  -  alternativ kann folgender Codeblock in die "keybindings.json" des Benutzers einfügen: (STRG+UMSCH+P --> Einstellungen: Tastenkombinationen öffnen (JSON))
    ```json
    [
        {
            "key": "ctrl+alt+j",
            "command": "latex-workshop.synctex",
            "when": "editorTextFocus && editorLangId == 'latex'"
        },
        {
            "key": "ctrl+alt+j",
            "command": "-latex-workshop.synctex",
            "when": "editorTextFocus && !config.latex-workshop.bind.altKeymap.enabled && editorLangId == 'latex'"
        }
    ]
    ```
