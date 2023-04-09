# TimeZone-Converter

Dieser Code implementiert einen einfachen Zeitzonen-Konverter mit einer GUI, die auf Tkinter basiert. Der Benutzer kann eine Standard-Zeitzone (z.B. die Zeitzone seines Wohnortes) auswählen und eine zweite Zeitzone, in die er die Uhrzeit konvertieren möchte. Die aktuelle Zeit wird in beiden Zeitzonen angezeigt und kann durch einen Aktualisierungs-Button manuell aktualisiert werden.

Benutzung:
Um den Zeitzonen-Konverter zu verwenden, führen Sie die Datei "zeitzone_converter.py" in Python aus. Es öffnet sich ein Fenster mit einem Dropdown-Menü für die Standard-Zeitzone und ein weiteres Dropdown-Menü für die zweite Zeitzone. Wählen Sie die gewünschten Zeitzonen aus und klicken Sie auf "Aktualisieren", um die aktuelle Uhrzeit in beiden Zeitzonen anzuzeigen. Die Uhrzeit wird automatisch alle 10 Sekunden aktualisiert.

Abhängigkeiten:
Dieses Programm verwendet die folgenden Python-Module:

datetime
pytz
tkinter
tkinter.ttk

Bitte stellen Sie sicher, dass diese Module auf Ihrem System installiert sind, bevor Sie das Programm ausführen.

Hinweise zur Zeitzone:
Die verfügbaren Zeitzone-Optionen werden aus der pytz.common_timezones-Liste abgerufen. Wenn Sie eine benutzerdefinierte Zeitzone hinzufügen möchten, können Sie diese der Liste hinzufügen oder eine der folgenden Optionen verwenden:

Einzelne Zeitzonen-Strings können direkt an die timezone-Funktion von pytz übergeben werden (z.B. timezone('US/Eastern')).
Eine Liste von Strings mit Zeitzonen-Namen kann als values-Argument an das ttk.Combobox-Objekt übergeben werden (z.B. values=['US/Eastern', 'US/Central', 'US/Mountain', 'US/Pacific']).

!!Bitte beachten Sie, dass die Angabe von ungültigen oder nicht unterstützten Zeitzonen dazu führen kann, dass das Programm nicht ordnungsgemäß funktioniert.!!
