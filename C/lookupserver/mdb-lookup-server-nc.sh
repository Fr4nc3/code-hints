#!/bin/sh
on_ctrl_c() {
echo "Ignoring Ctrl-C"
}
# Call on_ctrl_c() when the interrupt signal is received.
# The interrupt signal is sent when you press Ctrl-C.
trap on_ctrl_c INT

# add +x executable permission to the file if it doesn't have it 
#chmod a+x mdb-lookup-server-nc.sh

pid=$$

mkfifo mypipe-$pid
cat mypipe-$pid | nc -l $1 | mdb-lookup > mypipe-$pid


rm -f mypipe-$pid