.. _sec-email:

Emails und Newsletter
=====================

Email ist ein Standardprotokoll sind zum Verschicken von Nachrichten,
das für Text entwickelt wurde. Es erlaubt aber auch das Verschicken von
HTML-Code, also von Webcontent im gleichen Format wie auf Webseiten.
Beim Verwenden von Emails über reinen Text hinaus sollte man folgendes
beachten.

Sicherheitsrisiken in Emails
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Per Email kann man jemandem direkt Webcontent schicken, oft ohne dass
eine echte Überprüfung des Absenders stattfindet. Deshalb sind Emails
beliebte Einfallstore für Cyberangriffe. Um dem entgegenzuwirken, ist es
vernünftig, nur unbedenkliche Inhalte in Emails direkt anzuzeigen. Ein
so eingestelltes Emailprogramm wird also Emails möglicherweise
abgewandelt darstellen. Deshalb sollte man in Emails auf Elemente
verzichten, die potentiell für Hackerangriffe genutzt werden könnten
(z. B. JavaScript). Sonst wirkt eine Email schnell potentiell gefährlich.

Zwei Alternativen in einer Email
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Die sicherste Darstellung von Emails beschränkt sich nur auf den Text.
Oft besteht eine Email technisch aus zwei alternativen Teilen: einem
nur-Text-Teil und einem HTML-Teil (Webcontent). Das Emailprogramm der
Empfänger*in entscheidet, welcher Teil davon angezeigt wird. Programme
zum Versenden von Newslettern sind meistens so eingestellt, dass der
damit erstellte Webcontent automatisch in einen nur-Text-Teil konvertiert
und in der Email mitgeschickt wird. Das funktioniert dann gut, wenn man
sich an die Empfehlungen zur :doc:`barrierefreiheit` hält.

Anhänge
^^^^^^^
Eine praktische Funktion von Emails sind Anhänge. Jedoch ist zu beachten,
dass der Datentransfer per Emailanhang grundsätzlich ineffizienter ist
als andere Formen des Datentransfers. Große Anhänge verbrauchen
Speicherplatz bei Sender*in und Empfänger*in, und machen das Laden von
Emails langsam. Deshalb ist typischerweise eine Maximalgröße für
eingehende Emails eingestellt, sodass zu große Emails einfach nicht
zugestellt werden — teils ohne dass der oder die Absender*in das merkt.

Wenn große Dateien verschickt werden sollen, gibt es meist effizientere
Lösungen als Emails. Die zu verschickende Datei wird bei einem
Cloudservices (z. B. Nextcloud) oder auf einer Webseite hochgeladen und
per Email wird nur der Link zu der Datei verschickt. Das ist effizienter
und lässt die Email schneller laden, insbesondere wenn es sich um eine
große Datei handelt.

Verteiler und Datenschutz
^^^^^^^^^^^^^^^^^^^^^^^^^
Eine weitere Gefahr bei Emails sind versehentliche Datenlecks. Wenn man
eine Email an viele Empfänger*innen (also einen großen Verteiler)
schickt, sollte man diese Empfänger*innen immer in BCC packen, sodass
die Emailadressen gegenseitig nicht einsehbar sind. Das verschicken von
Emails an einen offenen Verteiler kann einen Verstoß gegen den
Datenschutz bedeuten. Außerdem erhöht es das Risiko von Spam- und
Phishingemails und damit auch von erfolgreichen Cyberangriffen.

.. _checkliste-email:

Checkliste
^^^^^^^^^^

-  große Verteilung immer in BCC, nicht in Adressat oder CC

-  keine großen Anhänge per Email verschicken

-  niemals große Anhänge per Email an einen großen Verteiler schicken

-  Emails sollten im nur-Text-Format und in HTML lesbar sein

.. topic:: Fortgeschritten

   -  Wenn Newsletter verschickt werden, sollten DKIM und SPF-records
      angepasst sein. (Aufgabe für Domain-Admins)
