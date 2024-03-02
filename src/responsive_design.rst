.. meta::
   :description lang=de: Darstellung von Webcontent auf verschiedenen Geräten
   :keywords lang=de: responsive design, Webseiten, Newsletter
   :author: Valentin Bruch

.. _sec-responsive-design:

Anzeige auf verschiedenen Geräten
=================================

Webcontent soll meist auf verschiedenen, teils sehr unterschiedlichen
Geräten angezeigt werden können: vom Computer (“Desktop”) mit großem,
breiten Display bis zum Smartphone mit kleinem, schmalen Display
(“mobil”). Üblicherweise hat eine Webseite ein Design, das dafür sorgt,
dass die Inhalte auf allen Geräten gut dargestellt werden. Damit das
funktioniert, sollte beim Erstellen der Inhalte nicht zu einseitig auf
die Darstellung auf einem bestimmten Gerät geachtet werden. Wenn man
manuell Einstellungen zur Darstellung wie die Schriftgröße anpasst, oder
wenn man komplexere Elemente wie Spalten oder Tabellen einfügt, sollte
man die Ansicht auf verschiedenen Geräten prüfen. Verwendet man nur die
vorgegebenen Designelemente ohne manuellen Anpassungen, so sollte die
Ansicht automatisch auf allen Geräten funktionieren.

.. hint::

  Auch ein Webseite-Design ist meistens nicht perfekt. Es fällt aber in der
  Regel in den Aufgabenbereich der Admins, an die man sich bei Problemen
  wenden sollte.

Zum Testen der Darstellung kann man Webseiten mit verschiedenen Geräten
öffnen. Es hilft aber auch, am Computer die Größe des Browserfensters zu
verändern und zu prüfen, ob die Webseite weiterhin gut aussieht.
Darüberhinaus bieten viele Desktop-Browser die Möglichkeit, auf eine
mobile Darstellung (also Smartphone-Ansicht) umzustellen. Bei Firefox
gibt es dafür die Tastenkombination Strg+Shift+M. In Google Chrome und
ähnlichen Browsern kommt man über die Entwicklertools an eine ähnliche
Ansicht (erste Strg+Shift+I, dann Strg+Shift+M). So kann man die Ansicht
auf Smartphones verschiedener Größe simulieren.

.. _checkliste-rd:

Checkliste
^^^^^^^^^^

-  Sieht die Darstellung am Computer bei verschieden großem
   Browserfenster gut aus?

-  Sieht die Darstellung auf dem Smartphone gut aus?

-  Genau getestet werden sollte insbesondere wenn...

   -  manuelle Anpassungen z. B. der Schriftgröße vorgenommen wurden

   -  Tabellen, Spalten oder andere kompexere Designelemente verwendet
      werden

.. _tests-rd:

Automatische Tests
^^^^^^^^^^^^^^^^^^

-  :ref:`Lighthouse <sec-lighthouse>`, https://pagespeed.web.dev
