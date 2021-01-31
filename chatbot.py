from nltk.chat.util import Chat, reflections
import tkinter as tk
import pickle,random

class Response:
    pairs = [
        ['How are you?',['I am fine, How about you?']],
        ['(.*)(Fine|Good|great)',["That is good to hear, How can i help you?"]],
        ['(Bye|Good Bye|See You Late|Exit|Quit)', ["See you", "Bye, have a nice day"]],
        ['(What is|Why) NSIT?',["Netaji Subhas Institute of Technology (NSIT), two kilometers away from Bihta Railway Station, has been established at Amhara in Patna district. It is approved by AICTE, New Delhi and recognized by Department of Science & Technology, Government of Bihar, affiliated to Aryabhatta Knowledge University Patna and State Board of Technical Education, Patna.\nFor more visit: https://nsit.in/"]],
        ['My name is (.*)', ['Hello %1, How may i help you?']],
        ['(Who|What) are you?', ['I am a chatbot designed to provide information about NSIT.']],
        ['(hi|hello|hey|hey there)', ['Hey there, How may i help you?', 'Hello', 'Hey there', 'Hello, How may i help you?']],
        ['(.*)(course|courses)(.*)',['Courses we provide at NSIT are:\n1. Computer Science and Engineering(CSE)\n2. Civil Engineering(CE)\n3. Machenical Engineering(ME)\n4. Eletrical Engineering(EE)\n'
                           '5. Eletronics and Communication Engineering(ECE)\ntype course name (as Eletrical Engineering or EE or Eletrical) for more details.']],
        ['(.*)(Computer Science|Computer Science and Engineering|CSE|CS)',['Computer Science & Engineering (CSE) is an academic program at many universities which comprises scientific and engineering aspects of computing.\n'
                                                           'CSE is also a term often used in Europe to translate the name of engineering informatics academic programs. \nFor more: https://nsit.in/computer-science']],
        ['(.*)(Eletronics and Communication Engineering|ECE|Electronics and Communication)',['Electronic engineering (also called electronics and communications engineering) is an electrical engineering discipline which utilizes nonlinear and active electrical components (such as semiconductor devices, especially transistors and diodes) to design electronic circuits, devices, integrated circuits and their systems.\n'
                                                                                                 'For more: https://nsit.in/ece']],
        ['(.*)(Eletrical Engineering|EE|Electrical)',['Electrical engineering is an engineering discipline concerned with the study, design and application of equipment, devices and systems which use electricity, electronics, and electromagnetism.\n'
                                                                                                 'For more: https://nsit.in/ee']],
        ['(.*)(Mechanical Engineering|ME|Mechanical)',['Mechanical engineering is the study, design, development, construction, and testing of mechanical and thermal sensors and devices, including tools, engines, and machines.\n'
                                                                                                 'For more: https://nsit.in/mechanical']],
        ['(.*)(Civil Engineering|CE|Civil)',['Civil engineering is a professional engineering discipline that deals with the design, construction, and maintenance of the physical and naturally built environment, including public works such as roads, bridges, canals, dams, airports, sewerage systems, pipelines, structural components of buildings, and railways.\n'
                                                                                                 'For more: https://nsit.in/civil']],
        ['(.*)(Admission|Apply)(.*)',['For Admission Details:\nContact:  7781020349/ 7781020359 /7781020341\nVisit: www.nsit.in ']],
        ['(.*)Placement',['Visit here for details regarding placement: https://nsit.in/placement-Statistics']],
        ['(.*)(Location)(.*)',['We are located at Patna, Bihar\nCheck on google maps: https://www.google.com/maps/contrib/117403092237678772767/place/ChIJL2O6XXdWjTkRe2TyxthQJB4/@25.5383367,84.8568576,15.92z/'
                                 'data=!4m6!1m5!8m4!1e1!2s117403092237678772767!3m1!1e1']],
        ['(.*)',["I didn't understand. Please try again by typing courses, admission, location etc."]],
    ]
    chatdata=[]
    filename = str(random.randrange(0, 9999))
    def clearTextInput(self):
        self.chatdata=[]
        self.filename=str(random.randrange(0,9999))
        txtarea.delete("0.0", "end")

    def savefile(self):
        with open('chat'+self.filename+'.txt', 'wb') as fp:
            pickle.dump(self.chatdata, fp)

    def convo(self):
        txtarea.configure(state="normal")
        chat = Chat(self.pairs, reflections)
        reply='Bot:'+chat.respond(inp.get())
        # print(type(reply))
        send= "You:"+inp.get()
        # print(type(inp.get()))
        self.chatdata.extend([send,reply])
        txtarea.insert(tk.END, '\n'+send)
        inp.delete(0,tk.END)
        txtarea.insert(tk.END, '\n'+ reply)
        txtarea.configure(state="disable")
        if reply=='Bot:See you' or reply=='Bot:Bye, have a nice day':
            exit()

if __name__ == '__main__':
    resp = Response()
    root = tk.Tk()
    root.title("ChatBot")
    txtarea=tk.Text(root, width=65)
    txtarea.grid(row=0, column=0)
    txtarea.configure(state="disabled")
    sc = tk.Scrollbar(root, command=txtarea.yview)
    sc.place(x=525,y=2, height=390)
    inp=tk.Entry(root, width=75)
    # inp.grid(row=1, column=0)
    filemenu = tk.Menu()
    filemenu.add_command(label='New', command=resp.clearTextInput)
    filemenu.add_command(label='Save', command=resp.savefile)
    main_menu = tk.Menu(root)
    main_menu.add_cascade(label='File', menu=filemenu)
    main_menu.add_command(label='Exit', command=root.quit)
    root.config(menu=main_menu)
    inp.place(x=2,y=395)
    root.geometry('545x425')
    root.resizable(False,False)
    btn=tk.Button(root, text='Send', bg='blue', activebackground='light green', width=10, height=1, command=resp.convo).place(x=460,y=392)
    root.mainloop()


