# ZeitzoneConverter

Dieses Programm ist ein einfacher Zeitzonen-Konverter, der mit der PyQt5-Bibliothek erstellt wurde. Es ermöglicht die Umrechnung der aktuellen Zeit von einer Standard-Zeitzone in eine ausgewählte Zeitzone.

## Installation

Um das Programm auszuführen, müssen zunächst die erforderlichen Bibliotheken installiert werden. Die Installation kann mit dem Paketmanager `pip` erfolgen:

`pip install pytz PyQt5`


## Verwendung

Das Programm kann durch Ausführen des Skripts `zeitzone_converter.py` gestartet werden. Dazu können Sie den folgenden Befehl in der Befehlszeile verwenden:

`python zeitzone_converter.py`


Nach dem Starten des Programms wird ein Fenster geöffnet, das die aktuelle Zeit in der ausgewählten Standard-Zeitzone und die konvertierte Zeit in der ausgewählten Zeitzone anzeigt. Die Standard-Zeitzone ist standardmäßig auf "Europe/Berlin" eingestellt, kann jedoch über das Dropdown-Menü geändert werden. Die ausgewählte Zeitzone ist standardmäßig auf "UTC" eingestellt und kann ebenfalls über das Dropdown-Menü geändert werden.

Um die angezeigten Zeiten zu aktualisieren, können Sie auf die Schaltfläche "Aktualisieren" klicken. Die Zeiten werden automatisch alle 1 Sekunde aktualisiert.

## Beispiel

Hier ist ein Beispiel, wie das Programm verwendet werden kann:

1. Starten Sie das Programm mit dem Befehl `python zeitzone_converter.py`.
2. Das Programm öffnet ein Fenster mit den Dropdown-Menüs für die Standard-Zeitzone und die ausgewählte Zeitzone.
3. Wählen Sie Ihre gewünschten Zeitzonen aus den Dropdown-Menüs aus.
4. Das Fenster zeigt die aktuelle Zeit in der Standard-Zeitzone und die konvertierte Zeit in der ausgewählten Zeitzone an.
5. Die Zeiten werden automatisch alle 1 Sekunde aktualisiert.

## Anmerkungen

- Das Programm verwendet die `pytz`-Bibliothek, um auf eine umfangreiche Datenbank mit Zeitzoneninformationen zuzugreifen.
- Die PyQt5-Bibliothek wird verwendet, um das GUI-Fenster zu erstellen und zu verwalten.
- Die `datetime`- und `QtCore`-Module werden für die Zeitberechnungen und das Aktualisieren des GUI verwendet.

Bitte stellen Sie sicher, dass Sie die erforderlichen Abhängigkeiten installiert haben, bevor Sie das Programm ausführen. Weitere Informationen zur Verwendung des Programms finden Sie in den Kommentaren im Quellcode.
