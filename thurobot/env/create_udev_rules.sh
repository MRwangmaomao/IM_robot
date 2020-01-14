
#!/bin/bash

echo "remap the device serial port(ttyUSBX) to  rikibase"
echo "rikibase usb connection as /dev/rikibase , check it using the command : ls -l /dev|grep ttyUSB"
echo "start copy rikibase.rules to  /etc/udev/rules.d/"
echo "`rospack find thurobot`/env/rikibase.rules"
sudo cp `rospack find thurobot`/env/rikibase.rules  /etc/udev/rules.d
echo " "
echo "Restarting udev"
echo ""
sudo service udev reload
sudo service udev restart
echo "finish "
