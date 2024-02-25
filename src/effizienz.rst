.. _`sec:effizienz`:

Effizienz
=========

Die Effizienz von Webcontent ist aus mehreren Gründen wichtig. Effizienz
verringert die Ladedauer von Webseiten und erhöht damit die
Nutzerfreundlichkeit. Außerdem müssen weniger Daten übertragen werden
und der Energieverbrauch ist geringer. Das ist durchaus relevant, denn
der Energiebedarf des Internets ist beachtlich [1]_. Zu bedenken ist die
Effizienz immer, wenn größere Datenmengen übertragen werden, etwa bei
Bildern oder Videos. In anderen Fällen ist die Effizienz eher eine
Aufgabe der Admins.

Codierung von Medien
^^^^^^^^^^^^^^^^^^^^

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
komprimieren. Allerdings ist es insbesondere bei starker Komprimierung
(also kleinen Dateien) besser. WebP wird von allen modernen Webbrowsern
und ca. 97% der global verwendeten Webbrowser unterstützt. [3]_

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

Noch wichtiger als bei Bildern ist die Komprimierung bei Videos. Wenn
man Streamingdienste wie Youtube oder Peertube zum Einbetten von Videos
verwendet, muss man sich um diese Komprimierung in der Regel keine
Sorgen machen. Sonst braucht man in der Regel einen Kompromiss aus
Qualität und Dateigröße.

.. _checkliste-effizienz:

Checkliste
^^^^^^^^^^

-  Sind Bilder im richtigen Format?

-  Haben Bilder die richtige Auflösung?

.. _automatische-tests-effizienz:

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
