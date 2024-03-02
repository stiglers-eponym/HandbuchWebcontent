.. meta::
   :description lang=de: Hinweise zur Effizienz und Geschwindigkeit von Webseiten
   :keywords lang=de: Effizienz, Komprimierung, Geschwindigkeit
   :author: Valentin Bruch

.. _`sec:effizienz`:

Effizienz
=========

Die Effizienz von Webcontent ist aus mehreren Gründen wichtig. Effizienz
verringert die Ladedauer von Webseiten und erhöht damit die
Nutzerfreundlichkeit. Außerdem müssen weniger Daten übertragen werden
und der Energieverbrauch ist geringer. Das ist durchaus relevant, denn
der Energiebedarf des Internets ist beachtlich [1]_.

Zu bedenken ist die Effizienz immer, wenn größere Datenmengen übertragen
werden, etwa bei Bildern oder Videos. In anderen Fällen ist die Effizienz
eher eine Aufgabe der Admins.

Codierung von Medien
^^^^^^^^^^^^^^^^^^^^

Bei Bildern, Videos und Audiodaten sucht man typischerweise einen
Kompromiss zwischen Dateigröße und Qualität. Entscheidend sind die
Auflösung von Bildern und Videos, aber auch das Dateiformat und andere
Einstellungen. Durch ein grundlegendes Verständnis davon kann man
vermeiden, dass Ladedauer und Energieverbrauch der Webseite ein
Vielfaches des Nötigen betragen.

Bilder
------

Das häufigste Problem bei der Effizienz von Webcontent ist das Format
von Bildern. Verschiedene Dateiformate von Bildern sind für verschiedene
Anwendungen geeignet. Für Logos und Zeichnungen, bei denen viele Pixel
die exakt gleiche Farbe haben, eignet sich das PNG-Format, mit dem
Bilder verlustfrei komprimiert werden. [2]_ Für Fotos eignet sich das
JPEG-Format, bei dem ein Kompromiss aus Dateigröße und Bildqualität
meist so gewählt werden kann, dass ohne sichtbare Qualitätsverluste eine
deutlich kleinere Datei erzeugt wird.

Speichert man ein Logo als JPEG statt als PNG, so wirkt es bei genauer
Betrachtung leicht verpixelt. Wenn man ein Foto als PNG statt als JPEG
speichert, dann kann die Datei schnell zehn mal so groß wie nötig
werden. Das kann eine Webseite erheblich verlangsamen und sehr
ineffizient machen.

Neben PNG und JPEG gibt es das modernere Format WebP. WebP kann Bilder
entweder verlustfrei (wie PNG) oder verlustbehaftet (wie JPEG)
komprimieren und ist insbesondere bei starker Komprimierung besser.
WebP wird von ca. 97% der Endgeräte unterstützt. [3]_

Neben dem Format ist die Auflösung von Bildern entscheidend für die
Dateigröße. Zu geringe Auflösung von Bildern lässt diese verpixelt
wirken. Eine zu hohe Auflösung verzögert das Laden einer Webseite oder
Email. Es gibt Webseiten, die Bilder automatisch in der passenden
Auflösung bereitstellen. Wenn das aber nicht der Fall ist, müssen
diejenigen, die Bilder hinzufügen, auf die passende Auflösung der Bilder
achten.

Übrigens: Technisch ist es möglich, Bilder in verschiedenen Auflösungen
und Dateiformaten bereitzustellen, sodass je nach Endgerät und
Webbrowser die passende Version geladen wird. Das Einrichten dieser
Funktion ist aber Aufgabe der Admins.

Videos
------

Noch wichtiger als bei Bildern ist die Komprimierung (oder Codierung)
bei Videos, da für Videos deutlich mehr Daten übertragen werden müssen.
Die Komprimierung ist hier grundsätzlich ein Kompromiss zwischen
Qualität, Datenrate bzw. Dateigröße und der zum Komprimieren benötigten
Rechenleistung.

Wenn man Streamingdienste wie YouTube oder PeerTube zum Einbetten von
Videos verwendet, muss man sich um die Komprimierung in der Regel keine
Sorgen machen. Man lädt das Video in hoher Qualität hoch und der
Streamingdienst codiert es passend. [4]_
Außerdem haben diese Dienste in der Regel viele Server,
um die Videos bereitzustellen. So wird der eigene Server entlastet.
Jedoch muss ggf. in der Datenschutzerklärung einer Webseite darauf
hingewiesen werden, dass externe Anbieter zum Streamen von Videos
verwendet werden, da dadurch Daten an diese externen Dienstleister
übertragen werden.

Wenn man keinen Streamingdienst verwendet und sich selbst um die
Komprimierung kümmert, gibt es einige Einstellungen zu beachten.
Die Auswahl des Videocodecs ist entscheidend für die Effizienz der
Codierung und dafür, welche Endgeräte das Video abspielen können.
Zu beachten ist, dass das Videocodec nicht gleichbedeutend mit dem
Dateiformat und der Dateiendung ist: MP4-Videos können beispielsweise
unterschiedliche Videocodecs nutzen, von denen nicht alle auf allen
Geräten funktionieren. Verbreitete Videocodecs für Webcontent sind:

-  VP9 (in WebM-Videos): von den meisten Endgeräten unterstützt
-  H.264 (in mp4-Videos): alt und weniger effizient, von quasi allen
   Endgeräten unterstützt

Modernere Codecs wie AV1 und H.265 erreichen bei gleicher Qualität
geringere Dateigrößen, werden jedoch von weniger Endgeräten unterstützt. [5]_

Bei der Codierung gibt es zudem Einstellungen zu Datenrate oder
Qualität von Video und Audio sowie teils zum Rechenaufwand der
Codierung. Dazu kommen Einstellungen zur Auflösung und Framerate,
die in der Regel bereits beim Aufzeichnen des Videos gesetzt werden.
Allgemeine Empfehlungen dazu findet man bei Software zu Videocodierung
wie etwa `ffmpeg <https://trac.ffmpeg.org/wiki/Encode/VP9>`__.

.. _checkliste-effizienz:

Checkliste
^^^^^^^^^^

-  Sind Bilder im richtigen Format?

-  Haben Bilder die richtige Auflösung?

-  Sind eingebettete Videos effizient komprimiert und nicht zu groß?

.. _tests-effizienz:

Automatische Tests
^^^^^^^^^^^^^^^^^^

-  :ref:`Website Carbon Calculator <sec-wcc>`,
   https://www.websitecarbon.com

-  :ref:`Lighthouse <sec-lighthouse>`, https://pagespeed.web.dev


.. rubric:: Fußnoten

.. [1]
   Laut Website Carbon Calculator ist der Energiebedarf des Internets
   höher als der Stromverbrauch von Großbritannien
   (https://www.websitecarbon.com).

.. [2]
   Bei falscher Verwendung kann die Komprimierung im PNG-Format
   ausgeschaltet werden, wodurch das Übertragen von Bildern sehr
   ineffizient wird.

.. [3]
   Quelle: https://caniuse.com/webp, Stand Februar 2024

.. [4]
   Empfohlene Einstellungen zum Hochladen bei Youtube:
   https://support.google.com/youtube/answer/1722171

.. [5]
   Es ist technisch möglich, verschiedene Formate bereitzustellen,
   sodass das Endgerät sich das passende Format aussucht. Dann können
   moderne Formate wie AV1 verwendet werden. Die begrenzte
   Unterstützung von H.265 durch Browser hat (auch) lizenzrechtliche
   Gründe.
