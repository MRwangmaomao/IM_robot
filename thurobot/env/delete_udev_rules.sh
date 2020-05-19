#!/bin/bash

echo "delete remap the device serial port(ttyUSBX) to  rikibase"
echo "sudo rm   /etc/udev/rules.d/rikibase.rules"
sudo rm   /etc/udev/rules.d/rikibase.rules
echo " "
echo "Restarting udev"
echo ""
sudo service udev reload
sudo service udev restart
echo "finish  delete"
