import speech_recognition as sr
from tkinter import*
from tkinter.messagebox import*
import pyttsx3
import math
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audi):
    engine.say(audi)
    engine.runAndWait()
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak anything:')
        r.dynamic_energy_threshold = 100
        r.pause_threshold = 2
        audio = r.listen(source)

        try:
            print('recognising....')
            text = r.recognize_google(audio)
            print('you said : {}'.format(text))
        except:
            print('sorry i cant listen')
            return ""
    return text



def clck(event):
    print('button clicked......',event)
    if event == '<==':
        fetc = textfield.get()
        fet = fetc[:-1]
        print(fet)
        textfield.insert(0, fet)
        return
    if event == 'AC':
        textfield.delete(0, END)
        return
    if event == 'x':
        textfield.insert(END, '*')
        return
    if event == '=':
        try:
            fetch = textfield.get()
            textfield.insert(END,'=')
            if '^' in fetch:
                k = fetch.replace('^', '**')
                ans=eval(k)
                textfield.insert(END, ans)
                return

            ans = eval(fetch)
            print(ans)
            textfield.insert(END, ans)
        except Exception as e:
            print('Error is', e)
            showerror('Error is:', e)
        return
    textfield.insert(END, event)
def rut():
    k=textfield.get()
    k=eval(k)
    k=math.sqrt(k)
    textfield.insert(END,'=')
    textfield.insert(END, k)
def crut():
    k=textfield.get()
    k=eval(k)
    k=k**(1/3)
    textfield.insert(END, '=')
    textfield.insert(END,k)
def lo():
    k = textfield.get()
    k = eval(k)
    k = math.log(k,2)
    textfield.insert(END, '=')
    textfield.insert(END, k)
def exp():
    k = textfield.get()
    k = eval(k)
    k = math.exp(k)
    textfield.insert(END, '=')
    textfield.insert(END, k)

def extract_from_text(text):
    l = []
    for t in text.split(' '):
        l = []
        for t in text.split(' '):
            try:
                l.append(float(t))
            except ValueError:
                pass
        return l



operations = {'ADD': '+', 'PLUS': '+', 'SUM': '+', 'ADDITION': '+', 'JOD': '+','+':'+',
              'ROOT':'√','SUB': '-', 'SUBTRACT': '-', 'MINUS': '-','-':'-','MOD':'%','MODULAS':'%',
              'DIFFERENCE': '-', 'GHATAO': '-','POWER':'^','^':'^','CUBEROOT':'3√','LOG':'log',
               'E':'e',
              'PRODUCT': '*', 'GUNA': '*', 'MULTIPLY': '*', 'MULTIPLICATION': '*','into':'*',
              'DIVISION': '/', 'BHAG': '/','DIVIDE':'/'}


if __name__ == "__main__":
    print('I am your personal calculator')
    speak('I am your personal calculator')
    print('would you like my graphical interface or you use audio version')
    speak('would you like my graphical interface or you use audio version')
    t  = 'audio'
    if 'audio' in t:
        while(True):
            k = 'e ^  0'
            print(k)
            symbol = []
            if 'shutdown' in k:
                print('have a nice day boss')
                break
            text = k
            for word in text.split(' '):
                if word.upper() in operations.keys():
                    try:
                        print(word)
                        l = extract_from_text(text)
                        symbol.append(operations[word.upper()])
                        print(symbol)
                        print(l)

                    except:
                        print('something went wrong going plz enter again !!')
            window = Tk()
            window.title('my calculator')
            window.maxsize(width=690, height=550)
            window.minsize(width=690, height=550)
            
            fon = ('Algerian', 10, 'bold underline')
            pic = PhotoImage(file='img/cal2.png')
            headlabel = Label(window, image=pic)  
            headlabel.pack(side=TOP, pady=6)
            headlabel = Label(window, text='MY CALCULATOR', font=fon)
            headlabel.pack(side=TOP)
            fan = ('Algerian', 28, 'bold ')
            
            textfield = Entry(window, font=fan, justify=RIGHT)
            textfield.pack(side=TOP, pady=6, fill=X, padx=10)
        
            buttonFrame = Frame(window)
            buttonFrame.pack(side=TOP)
            k = 1
            for i in range(3):
                for j in range(3):
                    btn = Button(buttonFrame, text=k, font=fan, width=4, relief='raised', activebackground='black',
                                 activeforeground='red')
                    btn.grid(row=i, column=j, pady=3, padx=3)
                    btn.bind('<Button-1>', clck)
                    k += 1
            btn1 = Button(buttonFrame, text='.', font=fan, width=4, relief='raised', activebackground='black',
                          activeforeground='red')
            btn1.grid(row=3, column=0, pady=3, padx=3)
            btn2 = Button(buttonFrame, text=0, font=fan, width=4, relief='raised', activebackground='black',
                          activeforeground='red')
            btn2.grid(row=3, column=1, pady=3, padx=3)
            btn3 = Button(buttonFrame, text='=', font=fan, width=4, relief='raised', activebackground='black',
                          activeforeground='red')
            btn3.grid(row=3, column=2, pady=3, padx=3)
            btnplus = Button(buttonFrame, text='+', font=fan, width=4, relief='raised', activebackground='black',
                             activeforeground='red')
            btnplus.grid(row=0, column=3, pady=3, padx=3)
            btnminus = Button(buttonFrame, text='-', font=fan, width=4, relief='raised', activebackground='black',
                              activeforeground='red')
            btnminus.grid(row=1, column=3, pady=3, padx=3)
            btnmul = Button(buttonFrame, text='x', font=fan, width=4, relief='raised', activebackground='black',
                            activeforeground='red')
            btnmul.grid(row=2, column=3, pady=3, padx=3)
            btndiv = Button(buttonFrame, text='/', font=fan, width=4, relief='raised', activebackground='black',
                            activeforeground='red')
            btndiv.grid(row=3, column=3, pady=3, padx=3)
            dele = Button(buttonFrame, text='<==', font=fan, width=9, relief='raised', activebackground='black',
                          activeforeground='red')
            dele.grid(row=4, column=0, pady=3, padx=3, columnspan=2)
            allclear = Button(buttonFrame, text='AC', font=fan, width=9, relief='raised', activebackground='black',
                              activeforeground='red')
            allclear.grid(row=4, column=2, pady=3, padx=3, columnspan=2)
            mod = Button(buttonFrame, text='%', font=fan, width=4, relief='raised', activebackground='black',
                         activeforeground='red')
            mod.grid(row=0, column=4, pady=3, padx=3)
            root = Button(buttonFrame, text=' √', font=fan, width=4, relief='raised', activebackground='black',
                          activeforeground='red')
            root.grid(row=1, column=4, pady=3, padx=3)
            croot = Button(buttonFrame, text='3√', font=fan, width=4, relief='raised', activebackground='black',
                           activeforeground='red')
            croot.grid(row=2, column=4, pady=3, padx=3)
            power = Button(buttonFrame, text='^', font=fan, width=4, relief='raised', activebackground='black',
                           activeforeground='red')
            power.grid(row=3, column=4, pady=3, padx=3)
            power.bind('<Button-1>', clck)
            log = Button(buttonFrame, text='log', font=fan, width=4, relief='raised', activebackground='black',
                         activeforeground='red')
            log.grid(row=4, column=4, pady=3, padx=3)
            expo = Button(buttonFrame, text='e', font=('Baveuse', 21, 'bold'), width=4, relief='raised',
                          activebackground='black', activeforeground='red')
            expo.grid(row=0, column=5, pady=3, padx=3)
            rob = Button(buttonFrame, text='(', font=fan, width=4, relief='raised', activebackground='black',
                         activeforeground='red')
            rob.grid(row=1, column=5, pady=3, padx=3)
            lob = Button(buttonFrame, text=')', font=fan, width=4, relief='raised', activebackground='black',
                         activeforeground='red')
            lob.grid(row=2, column=5, pady=3, padx=3)
            ze = Button(buttonFrame, text='00', font=fan, width=4, relief='raised', activebackground='black',
                        activeforeground='red')
            ze.grid(row=3, column=5, pady=3, padx=3)
            zee = Button(buttonFrame, text='000', font=fan, width=4, relief='raised', activebackground='black',
                         activeforeground='red')
            zee.grid(row=4, column=5, pady=3, padx=3)
            mod.bind('<Button-1>', clck)
            power.bind('<Button-1>', clck)
            rob.bind('<Button-1>', clck)
            lob.bind('<Button-1>', clck)
            ze.bind('<Button-1>', clck)
            zee.bind('<Button-1>', clck)
            btn1.bind('<Button-1>', clck)
            btn2.bind('<Button-1>', clck)
            btn3.bind('<Button-1>', clck)
            btnplus.bind('<Button-1>', clck)
            btnminus.bind('<Button-1>', clck)
            btnmul.bind('<Button-1>', clck)
            btndiv.bind('<Button-1>', clck)
            dele.bind('<Button-1>', clck)
            allclear.bind('<Button-1>', clck)
            try:
                x=len(l)
                y=len(symbol)
                if y>1:
                    t=0
                    j=0
                    for i in range(x+y):
                        if i==0 or i%2==0:
                            clck(l[t])
                            t+=1
                        else:
                            clck(symbol[j])
                            j+=1
                    clck('=')

                else:
                    for i in range(x):
                        clck(l[i])
                        if symbol[i] == '√':
                            rut()
                            break
                        if symbol[i] == '3√':
                            crut()
                            break
                        if symbol[i] == 'log':
                            lo()
                            break
                        if symbol[i] == 'e':
                            exp()
                            break
                        if i>=x-1:break

            except Exception:
                print()
            window.mainloop()
    else:
        speak('okk  sir')
        import cal1
