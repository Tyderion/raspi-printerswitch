#! /bin/sh
# /etc/init.d/checkarchie

### BEGIN INIT INFO
# Provides:          checkarchie
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Simple script to start a program at boot
# Description:       A simple script from www.stuffaboutcode.com which will start / stop a program a boot / shutdown.
### END INIT INFO

# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting checkarchie"
    # run application you want to start
    /home/pi/raspi-printerswitch/check_archie.py &
    ;;
  stop)
    echo "Stopping checkarchie"
    # kill application you want to stop
    killall check_archie.py
    ;;
  *)
    echo "Usage: /etc/init.d/noip {start|stop}"
    exit 1
    ;;
esac

exit 0
