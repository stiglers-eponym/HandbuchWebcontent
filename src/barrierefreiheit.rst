.. _sec-barrierefreiheit:

Barrierefreiheit
================

Barrierefreiheit bei längeren Dokumenten wie Webseiten beinhaltet
insbesondere folgende Aspekte:

#. Das Dokument hat eine klare, logische Struktur.

#. Die visuelle Darstellung ist auch für Menschen mit schlechten Augen
   erkennbar. Beispielsweise ist der Text groß genug und hat einen
   ausreichenden Kontrast zum Hintergrund.

#. Für rein visuelle Elemente wie Bilder oder Logos sind kurze Text zur
   Beschreibung hinterlegt, die von Screenreadern vorgelesen werden
   können. Alternativ können Elemente auch als irrelevant für
   Screenreader gekennzeichnet werden.

#. Das Dokument hat eine Navigation, die mit verschiedenen
   Eingabegeräten genutzt werden kann. Üblich sind Maus, Touchscreen und
   Tastatur (mit der Tab-Taste). Menüs sind als solche auch für
   Screenreader erkennbar.

#. Texte sind verständlich geschrieben, klar strukturiert und einfach zu
   lesen. Fachbegriffe werden vermieden oder erklärt. Das ist zwar kein
   technischer Punkt, aber trotzdem wichtig.

Die Punkte 1 bis 4 werden
üblicherweise beim Erstellen einer Webseite oder eines Designs bedacht.
Beim Hinzufügen neuer Inhalte sollten sich diese Punkte ohne Mehraufwand
ergeben.

Auch Punkt 2 zur visuellen
Darstellung muss bereits beim Erstellen eines Designs bedacht werden.
Aber auch bei einzelnen Inhalten, etwa bei der Darstellung von Text vor
einem Bild, muss ein ausreichender Kontrast und ausreichend große
Schrift bedacht werden.

Wesentlich beim Erstellen von Inhalten ist
Punkt 3 zur Beschreibung von visuellen
Elementen. Für jedes Bild sollte eine kurze Beschreibung erstellt
werden. Üblicherweise geschieht das noch von Hand. Der sogenannte
“alt”-Text für Bilder wird angezeigt, wenn ein Bild nicht angezeigt
werden kann, und er beschreibt das Bild beim Vorlesen der Seite durch
einen Screenreader. Bei WordPress kann man für jedes Bild einen alt-Text
anlegen und auch bei Facebook-Posts kann ein alt-Text für Bilder
angegeben werden. Falls Videos eingebettet werden, können Untertitel zur
Barrierefreiheit beitragen. Es gibt Software zum automatischen
Hinzufügen von Untertiteln, die aber in der Regel noch eine manuelle
Korrektur brauchen.

Checkliste
^^^^^^^^^^

-  Haben alle Bilder einen alt-Text mit einer kurzen Beschreibung?

-  Hat der Text immer einen ausreichender Kontrast zum Hintergrund?

-  Falls mehrere Absätze mit Text vorhanden sind: Gibt es eine klare
   Struktur?

-  Ist der Text auf allen Geräten (Computer, Smartphone, evtl. Tablet)
   gut zu lesen?

.. rubric:: Fortgeschritten

-  Sind Links ausreichend weit voneinander entfernt, damit man auf einem
   Touchscreen nicht versehentlich das falsche anklickt?

-  Bei einer Webseite: Kann man mit der Tab-Taste gut durch die auf der
   Webseite vorhandenen Links und Menüs navigieren?

Automatische Tests
^^^^^^^^^^^^^^^^^^

-  :ref:`Lighthouse <sec-lighthouse>`, https://pagespeed.web.dev

-  :ref:`Pa11y <sec-pally>`, https://pa11y.org
