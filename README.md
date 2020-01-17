# Projektvorhaben für Projekt "MyWines"

## Abstract
Eine App um Weine zu verwalten und Empfehlungen zu erhalten.

## Projekt-Idee
Es können Weine hinzugefügt und gelöscht (wenn getrunken) werden. Beim Hinzufügen wird nach dem Namen, dem Jahrgang, der Rebsorte, der Region, dem bezahlten Preis, sowie Speisen gefragt, die gut zum Wein passen würden. Eine Übersicht zeigt alle Weine, geordnet nach Jahrgang an. Es soll zudem möglich sein, ein Gericht einzugeben und dann einen Weinvorschlag zu erhalten.
-> Kommentar nach Implementierung: Die Ordnung nach Jahrgang ist technisch zwar möglich, wurde beim Umsetzen jedoch absichtlich nicht so gemacht. Es wird nach dem Zeitpunkt des Hinzufügens sortiert. Im realen Leben kauft man Weine um sie zu lagern. Es macht daher Sinn, die am längsten gelagerten Weine zuerst aufzulisten, da diese am ehesten bereits trinkbar sind.

## Anforderungen
Liste (Dictionary), Loops & eine Art Datenbank im Hintergrund.
-> Kommentar nach Implementierung: Eine Liste hat gereicht, ein Dictionary war aufgrund der Indexierung nicht hierfür geeignet. Zudem fungiert ein einfaches JSON File als Datenbank.

# Installationsanleitung
Für MyWines müssen Python, Flask und Jinja2 installiert sein.
Um MyWines zu starten, führen Sie in der Kommandozentrale das File main.py mittels "python main.py" aus.
MyWines ist lokal über den Port 5000 aufrufbar, i.d.R. über: http://localhost:5000
Die Bedienung von MyWines ist grösstenteils selbsterklärend und wo nicht der Fall, ausführlich in der App beschrieben.
Einige Beispielsweine befinden sich bereits im Weinkeller. Diese können Sie selbstverständlich löschen und Ihre eignen Weine hinzufügen.
Zum Wohl!