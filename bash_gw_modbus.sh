ps aux | grep python | grep 'gw_modbus' | awk '{ print $2 }' | xargs kill -9 
nohup  python main_elc_gw_modbus_04.py > /tmp/t.log 2>&1 &
