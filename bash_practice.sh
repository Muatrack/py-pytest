ps aux | grep python | grep 'practice' | awk '{ print $2 }' | xargs kill -9
nohup  python practice_elc_modbus.py > /tmp/t.log 2>&1 &
