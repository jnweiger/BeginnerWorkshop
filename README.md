# Workshop for Beginners - Einsteigerworkshop

## Windows: Installation und erste Schritte

Du kannst dir ```Python``` entweder direkt von der Projektseite *[python.org](https://www.python.org/downloads/)* holen
oder dir eine fertige Python-Distribution, wie beispielsweise *[Anaconda](https://www.continuum.io/downloads)*.
Der Vorteil von Anaconda unter Windows ist, dass bereits so gut wie alle wichtigen Pakete die man irgendwann einmal
gebrauchen könnte mitgeliefert werden. Vor allem in Bezug auf Bibliotheken wie *numpy*, *scipy* etc. ist die
Installation via Anaconda unter Windows sehr angenehm. Der Nachteil ist die enorme Größe.

Wenn du keine speziellen Bedürfnisse hast, sprich Kompatibilität mit Bibliotheken die nur **Python 2.7** unterstützen,
solltest du die neuste Version (mindestens **Python 3.5**) installieren.

# The first contact

Da ```Python``` eine interpretierte Sprache ist, kannst du nach der Installation direkt interaktiv in der Konsole loslegen.
Unter Windows kannst du deine Konsole ganz einfach öffnen indem du mit der <kbd>windows</kbd>-Taste das Start-Menü
öffnest und dann ```cmd``` gefolgt von <kbd>enter</kbd> eintippst.

```bash
$ python3.5
Python 3.5.2 (default, Nov 17 2016, 17:05:23)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Wenn du dann wie oben gezeigt, ```python3.5``` eintippst, öffnet sich der sogenannte **Python-REPL**. ```REPL``` steht
für read-eval-print-loop. Sprich ```Python``` liest jede deiner Eingaben ein, verarbeitet (interpretiert) diese und zeigt
dir dann ein Ergebnis an. Probieren wirs aus!

```bash
>>> 40 + 2
42
```

Wie du siehst, kannst du ```Python``` bereits als Taschenrechner verwenden, selbst wenn du noch über keinerlei
Programmierkenntnisse verfügst.


Lass uns noch weitere Funktionen von Python in der Konsole kennenlernen. Wir möchten unsere Summe nun in einer
Variablen zwischenspeichern:

```bash
>>> summe = 42
>>>
```

Die Variable ```summe``` besitzt nun den Wert 42. Da die Zuweisung aber keine Rückgabe erzeugt, sehen wir nur einen
neunen ```prompt```(>>>).

```bash
>>> summe
42
```

Um den Inhalt der Variable zu sehen reicht es wenn wir den ihren Namen eingeben. Neben diesen sehr
einfachen Beispielen können wir alle Funktionen die uns die Programmiersprache ```Python``` bietet im ```REPL```
verwenden. Gerade wenn man einfach Beispiele hat oder einmal schnell etwas ausprobieren möchte ist dies eine
wunderbare Sache. Darüber hinaus bietet der ```REPL``` mit der Funktion ```help``` einen direkten Zugriff auf die
*man-pages* aller Sprachkonstrukte.

```bash
>>> help(summe)

Help on int object:

class int(object)
 |  int(x=0) -> integer
 |  int(x, base=10) -> integer
 |
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
 |      abs(self)
 |
:
```

So liefert ```help``` für unsere Variable die Dokumentation für die Klasse ```int```, da unsere Variable diesen
Datentyp besitzt. Der Datentyp ```int```bedeutet, dass die jeweilige Variable eine Ganzzahl einhält. Du kannst die
Hilfe durch Eingabe von <kbd>d</kbd> beenden.


### Entwicklungsumgebungen

Nahezu jede gängige Entwicklungsumgebung bietet heute Unterstützung für Python an. Da der ```REPL``` keine wirklich
angenehme Umgebung ist um größere Programme zu schreiben solltest du mindestens einen vernünftigen Editor mit
Syntax-Highlighting verwenden. Unter Windows bietet sich hierfür beispielsweise
[Notepad++](https://notepad-plus-plus.org/) an. Eine andere wunderbare Möglichkeit bietet
[Jupyter](https://jupyter.org/). Ähnlich dem ```REPL``` kannst du hier deinen Code direkt interaktiv ausführen.

Wenn du ehr auf IDEs stehst, sind besonders folgende für die Python Entwicklung zu empfehlen:

- [PyCharm](https://www.jetbrains.com/pycharm/) (kostenlos in der Community-Version)
- [Wing IDE](https://wingware.com/)
- [Komodo](https://www.activestate.com/komodo-ide/python-editor)
- [PyDev](http://www.pydev.org/index.html) (Plug-In für Eclipse)

Wir sehen uns beim Workshop
