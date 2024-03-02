.. meta::
   :description lang=de: automatische Tests für Webseiten
   :keywords lang=de: Webseiten
   :author: Valentin Bruch

.. _sec-tests:

Automatische Tests
==================

Für Webseiten gibt es einige automatische Tests. Diese Tests dienen
zum Erkennen von Fehlern und zum Optimieren etwa von Webseiten. Sie
können jedoch das bewusste Beachten der hier formulierten Emfehlungen
nicht ersetzen. Die folgende Auflistung ist zudem unvollständig.

.. _sec-lighthouse:

Lighthouse
^^^^^^^^^^

`Lighthouse <https://github.com/GoogleChrome/lighthouse>`__ ist ein
Werkzeug zum automatischen Testen von Webseiten. Getestet werden die
Aspekte Leistung, Barrierefreiheit, Best Practice und die Bewertung
durch Suchmaschinen (search engine optimization, SEO).

Man kann den Test sowohl für Computer, als auch für die Ansicht auf
Smartphones durchführen. Die Ergebnisse von Lighthouse geben einen
guten Überblick über wichtige Aspekte einer Webseite und konkrete
Handlungsempfehlungen. Allerdings sind diese Handlungsempfehlungen
etwas technisch.

Zum Nutzen von Lighthouse gibt es zwei Methoden [1]_

-  ganz einfach: über die Webseite https://pagespeed.web.dev

-  fortgeschritten: `über die
   Chrome-Entwicklertools <https://developer.chrome.com/docs/lighthouse/overview?hl=de#devtools>`__

.. caution::

   Beim Nutzen der Chrome-Entwicklertools sollte man vorsichtig sein.
   Insbesondere sollte man die Konsole (Texteingabe) nur verwenden,
   wenn man wirklich weiß was man tut.

.. _sec-wcc:

Website Carbon Calculator
^^^^^^^^^^^^^^^^^^^^^^^^^

Der `Website Carbon Calculator <https://www.websitecarbon.com>`__
schätzt ab, wie viel Energie eine Webseite braucht und welcher
CO\ :sub:`2`-Ausstoß damit einhergeht. Webseiten werden auf einer leicht
verständlichen Skala bewertet, die Ergebnisse sind also stark
vereinfacht und nicht detailliert.

.. _sec-wpscan:

WPScan
^^^^^^

Mit `WPScan <https://wpscan.com>`__ können WordPress-Webseiten
automatisch auf bekannte Sicherheitslücken geprüft werden. Ein solcher
Test ersetzt nicht das Prüfen von Plugins oder das regelmäßige
Einspielen von Sicherheitsupdates.

.. _sec-pally:

Pa11y
^^^^^

`Pa11y <https://pa11y.org>`__ ist ein Werkzeug zum Testen der
Barrierefreiheit von Webseiten. Dieses Werkzeug zu nutzen erfordert
technisches Hintergrundwissen und sollte nicht ohne technisches
Wissen zu JavaScript eingerichtet werden.

.. caution::

   Bitte nicht versuchen, dieses Werkzeug zu installieren, wenn man
   die Hintergründe einer Anleitung zur Installation nicht versteht!


.. rubric:: Fußnoten

.. [1]
   Für Expert*innen gibt es noch mehr Methoden.
