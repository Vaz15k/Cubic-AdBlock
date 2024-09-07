#!/system/bin/sh

# Checks if the old version of the module (systemless-adblock) is installed
TARGET_DIR="/data/adb/modules/systemless-adblock"

if [ -d "$TARGET_DIR" ]; then
	ui_print "####################################################"
	ui_print "Old version of the module found (Systemless-Adblock)"
	ui_print "                   Removing                         "
	ui_print "####################################################"
	rm -rf "$TARGET_DIR"
fi
