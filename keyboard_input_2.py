from pynput import keyboard
import tkinter as tk
def key_to_str(key):
    numpadDict={f"{i+96}": str(i) for i in range(10)}
    numpadDict["110"]="."
    ctrlDict={f"'\\x0{i}'": chr(i+96) for i in range(1,9)}
    tmpDict={"'\\t'":"i",
             "'\\n'":"j",
             "'\\x0b'":"k",
             "'\\x0c'":"l",
             "'\\r'":"m",
             "'\\x0e'":"n",
             "'\\x0f'":"o",
             "'\\x1a'":"z",
             "'\\x1b'":"[",
             "'\\x1c'":"\\",
             "'\\x1d'":"]",
             "'\\x1e'":"^",
             "'\\x1f'":"_",
             "'\\x00'":"2",
             "'\\\\'":"\\"}
    tmpDict.update({f"'\\x{i}'": chr(i+102) for i in range(10,20)})
    ctrlDict.update(tmpDict)
    if str(key)==None:
        strkey=str(key.vk)
    elif str(key)[0]=="<" and str(key)[-1]==">":
        strkey=numpadDict[str(key.vk)]
    elif "Key." in str(key):
        strkey=str(key)[4:]
    elif "'" in str(key):
        if "\\" in str(key):
            print(2)
            strkey=ctrlDict[str(key)]
        else:
            strkey=str(key)[1]
    else:
        print(1)
        strkey=str(key)
    return strkey

def updateCanvas(l):
    canvas.delete("all")
    canvas.create_text(150,200,font=("Arial",30),text="".join([i+"\n" for i in l]))

def on_press(key):
    global pressedList
    print(key)
    key=key_to_str(key)
    if not key in pressedList:
        pressedList.append(key)
        updateCanvas(pressedList)

def on_release(key):
    global pressedList
    pressedList.remove(key_to_str(key))
    updateCanvas(pressedList)
    
root=tk.Tk()
root.title("Keyboard Inputs")
root.resizable(False,False)
root.wm_attributes("-topmost",-1)
canvas=tk.Canvas(root, height=400,width=300)
listener=keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
pressedList=[]
canvas.pack()
tk.mainloop()
