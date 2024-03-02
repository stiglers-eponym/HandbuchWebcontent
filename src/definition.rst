.. meta::
   :description lang=de: Definition von Webcontent für dieses Dokument
   :keywords lang=de: Webseiten, Newsletter
   :author: Valentin Bruch

.. _sec-definition:

Was ist Webcontent?
===================

Das World Wide Web hat seit den 90er Jahren unsere Welt verändert.
Webseiten und Emails zeigen interaktiv und flexibel Inhalte basierend
auf einem gemeinsamen Darstellungsformat an. Diese Inhalte [1]_
bezeichnen wir als *Webcontent*.

Intern besteht Webcontent im Wesentlichen aus einer Textdatei, die Anweisungen
zur Struktur des Dokuments und Hinweise zur Darstellung dieser Struktur
enthält. Ergänzt wird diese Datei durch Bilder, weitere Anweisungen zur
Darstellung und Programmcode für interaktive Elemente. Wichtig ist, dass
die Darstellung stets einer Struktur folgt — oder zumindest folgend
sollte. Die definierte Struktur kann nicht nur zur Darstellung auf einem
Bildschirm genutzt werden, sondern auch zum automatisierten Vorlesen
durch einen Screenreader. Wenn man Webcontent erstellt, ist also nicht
nur die Darstellung auf dem Bildschirm wichtig, sondern auch dem
zugrundeliegende Dokumentenstruktur.

Den Unterschied zwischen Struktur und Darstellung kann man an einer
Überschrift sehen. Wird eine Zeile als Überschrift formatiert, so ist
sie über den Screenreader auch für Menschen mit eingeschränktem
Sehvermögen direkt als Überschrift erkennbar. Wird dagegen die gleiche
Darstellung erreicht, indem händisch eine andere, größere Schrift
ausgewählt wird, so geht die Information über die Struktur verloren und
es ist nicht mehr für jede*n erkennbar, dass es sich um eine Überschrift
handeln soll.


.. rubric:: Fußnoten

.. [1]
   Technisch handelt es sich um HTML-Dokumente mit CSS-Stil.
