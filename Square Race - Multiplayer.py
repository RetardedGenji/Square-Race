import tkinter as tk
from tkinter import PhotoImage, CENTER, NW, GROOVE
import time
import winsound
def noQuit():
    pass


class Square:
    
    def __init__(self, parent=None):
        
        self._running = 0
        self.activ = 0
        self.Checkpoint = 0
        self.Checkpoint2 = 3
        self.win = 0
        self.latence = 0
        self.time = tk.StringVar()
        self.csec = self.dsec = self.seconde = self.minute = 0
        self.csec_score = 0
        self.coords1 = (0,600)
        self.coords2 = (725,600)

        self.canvas = tk.Canvas(main, width=750, height=625, highlightthickness=0)
        self.canvas.focus_set()
        self.canvas.bind("<Key>", self.Clavier)
        self.mapFull = PhotoImage(file='mapFull.gif')
        self.canvas.create_image(0,0, anchor=NW, image=self.mapFull)
        self.canvas.pack(pady=45)
        

    def RegleDuJeu(self):
        
        if not self._running:
            
            tl1 = tk.Toplevel()
            tl1.title('Règles du jeu')
            tl1.overrideredirect(0)
            tl1.geometry("%dx%d+0+0" % (w, h))
            tl1.resizable(0, 0)
            tl1.protocol('WM_DELETE_WINDOW', noQuit)
            tl1.overrideredirect(1)
            
            self.canvas2 = tk.Canvas(tl1, width=1345, height=180, bg='white')
            self.canvas2.place(x=5, y=100)
            self.canvas3 = tk.Canvas(tl1, width=1290, height=180, bg='white')
            self.canvas3.place(x=60, y=305)
            self.canvas4 = tk.Canvas(tl1, width=1235, height=180, bg='white')
            self.canvas4.place(x=115, y=510)
            
            
            self.label_Bienvenue = tk.Label(tl1,
                                         text='Bienvenue à \nSquare Race Multiplayer',
                                         font=font1)
            self.label_Carrés = tk.Label(tl1,
                                      text='- Le joueur n°1 est représenté par le Carré Rouge\n\n- Le joueur n°2 est représenté par le Carré Bleu',
                                      bg='white', font=font2)
            self.label_Piege = tk.Label(tl1,
                                     text='Sur votre route, vous rencontrerez des Pièges qui clignotes: Vert=Respawn - Blanc=Passe',
                                     bg='white', font=font2)
            self.label_Check = tk.Label(tl1,
                                     text='Pour vous aider à atteindre la ligne d\'arrivée, il y aura deux Checkpoints',
                                     bg='white', font=font2)
            self.label_Goal = tk.Label(tl1,
                                    text='Un Décompte va être lancé une fois le Boutton Appuyé\n\nLe but est d\'arrivé avant l\'autre Joueur',
                                    bg='white', font=font2)
            self.stopwatch = tk.PhotoImage(file='stopwatch.gif')
            self.button_stopwatch = tk.Button(self.canvas4, width=60, height=60, compound=CENTER, image=self.stopwatch, relief=GROOVE)
            
            self.canvas2.create_rectangle(1155, 20, 1215, 80, fill='red')
            self.canvas2.create_rectangle(1155, 100, 1215, 160, fill='blue')
            self.canvas3.create_rectangle(1100, 20, 1160, 80, fill='lightgreen')
            self.canvas3.create_rectangle(1100, 100, 1160, 160, fill='orange')         
            self.label_Bienvenue.pack(pady=4)
            self.label_Carrés.place(x=15, y=140)
            self.label_Piege.place(x=70, y=340)
            self.label_Check.place(x=70, y=410)
            self.label_Goal.place(x=125, y=550)
            self.button_stopwatch.place(x=1044, y=60)
            

            def goto_Mode():
                
                tl1.destroy()
                self.Mode()           
            self.button_gotomode = tk.Button(tl1, text='C\'EST PARTI', width=14, height=3, relief=GROOVE, command=goto_Mode)
            self.button_gotomode.place(x=630, y=680)
            
        elif self._running:
            self.Mode()
            
            
    def Mode(self):
        
        if self._running:
            self._running = 0
            self.coords1 = (0,600)
            self.coords2 = (725,600)
            self.Checkpoint = 0
            self.Checkpoint2 = 3
            self.canvas.delete(self.rectangle1)
            self.canvas.delete(self.rectangle2)
            self.IsVisible = False
            self.latence = 99999
            self.csec = self.dsec = self.seconde = self.minute = 0
            self.name = tk.StringVar()
                      
        if not self._running:
            
            tl2 = tk.Toplevel()
            tl2.title('Mode de Jeu')
            tl2.geometry('230x250')
            tl2.resizable(0, 0)
            tl2.protocol('WM_DELETE_WINDOW', noQuit)
            
            self.label_title = tk.Label(tl2, text='Choisissez votre Mode de Jeu', font=font3)
            self.label_title.pack(pady=5)
            
        
            def lazy():
                self.latence = 900
            self.check1 = tk.Checkbutton(tl2, text='Lazy', command=lazy)
            self.check1.pack(pady=10)
            
            def normal():
                self.latence = 700
            self.check2 = tk.Checkbutton(tl2, text='Normal', command=normal)
            self.check2.pack(pady=10)
            
            def hard():
                self.latence = 500
            self.check3 = tk.Checkbutton(tl2, text='HardCore', command=hard)
            self.check3.pack(pady=10)
        
            def goto_createAll():
                tl2.destroy()
                self.createAll()
            self.button_gotocreateSquare = tk.Button(tl2, text='    OK    ', command=goto_createAll)
            self.button_gotocreateSquare.pack(pady=15)
          
            
    def createAll(self):
        for i in range(3):
            winsound.Beep(450,450)
            time.sleep(0.5)
        winsound.Beep(650, 550)
        if self._running:
            pass
        if not self._running:
            self.rectangle1 = self.canvas.create_rectangle(0,600,25,625, fill='red')
            self.rectangle2 = self.canvas.create_rectangle(725,600,750,625, fill='blue')
            
            self.caseNoires = ((75, 0), (275, 0), (300, 0), (325, 0), (350, 0), (375, 0), (400, 0),
                               (425, 0), (450, 0), (650, 0), (50, 25), (75, 25), (100, 25), (125, 25),
                               (150, 25), (175, 25), (200, 25), (225, 25), (500, 25), (525, 25), (550, 25),
                               (575, 25), (600, 25), (625, 25), (650, 25), (675, 25), (25, 50), (200, 50), 
                               (225, 50), (250, 50), (275, 50), (300, 50), (325, 50), (400, 50), (425, 50),
                               (450, 50), (475, 50), (500, 50), (525, 50), (700, 50), (0, 75), (75, 75),
                               (100, 75), (125, 75), (150, 75), (250, 75), (325, 75), (400, 75), (475, 75),
                               (575, 75), (600, 75), (625, 75), (650, 75), (725, 75), (50, 100), (75, 100),
                               (175, 100), (225, 100), (250, 100), (275, 100), (300, 100), (425, 100), (450, 100),
                               (475, 100), (500, 100), (550, 100), (650, 100), (675, 100), (25, 125), (50, 125),
                               (75, 125), (125, 125), (175, 125), (350, 125), (375, 125), (550, 125), (600, 125),
                               (650, 125), (675, 125), (700, 125), (25, 150), (125, 150), (175, 150), (200, 150),
                               (225, 150), (250, 150), (275, 150), (300, 150), (325, 150), (350, 150), (375, 150),
                               (400, 150), (425, 150), (450, 150), (475, 150), (500, 150), (525, 150), (550, 150),
                               (600, 150), (700, 150), (25, 175), (75, 175), (100, 175), (125, 175), (350, 175),
                               (375, 175), (600, 175), (625, 175), (650, 175), (700, 175), (25, 200), (100, 200),
                               (150, 200), (175, 200), (200, 200), (225, 200), (250, 200), (275, 200), (300, 200),
                               (425, 200), (450, 200), (475, 200), (500, 200), (525, 200), (550, 200), (575, 200),
                               (625, 200), (700, 200), (25, 225), (50, 225), (100, 225), (250, 225), (275, 225),
                               (300, 225), (325, 225), (400, 225), (425, 225), (450, 225), (475, 225), (625, 225),
                               (675, 225), (700, 225), (25, 250), (100, 250), (150, 250), (175, 250), (200, 250),
                               (250, 250), (475, 250), (525, 250), (550, 250), (575, 250), (625, 250), (700, 250),
                               (25, 275), (75, 275), (100, 275), (150, 275), (250, 275), (300, 275), (325, 275),
                               (350, 275), (375, 275), (400, 275), (425, 275), (475, 275), (575, 275), (625, 275),
                               (650, 275), (700, 275), (25, 300), (75, 300), (150, 300), (200, 300), (225, 300),
                               (250, 300), (350, 300), (375, 300), (475, 300), (500, 300), (525, 300), (575, 300),
                               (650, 300), (700, 300), (25, 325), (75, 325), (150, 325), (225, 325), (250, 325),
                               (275, 325), (300, 325), (350, 325), (375, 325), (425, 325), (450, 325), (475, 325),
                               (500, 325), (575, 325), (650, 325), (700, 325), (75, 350), (125, 350), (150, 350),
                               (175, 350), (225, 350), (350, 350), (375, 350), (500, 350), (550, 350), (575, 350),
                               (600, 350), (650, 350), (0, 375), (25, 375), (50, 375), (75, 375), (150, 375),
                               (175, 375), (275, 375), (300, 375), (325, 375), (350, 375), (375, 375), (400, 375),
                               (425, 375), (450, 375), (550, 375), (575, 375), (650, 375), (675, 375), (700, 375),
                               (725, 375), (0, 400), (175, 400), (225, 400), (250, 400), (275, 400), (450, 400),
                               (475, 400), (500, 400), (550, 400), (725, 400), (0, 425), (50, 425), (75, 425),
                               (100, 425), (125, 425), (150, 425), (175, 425), (200, 425), (225, 425), (325, 425),
                               (400, 425), (500, 425), (525, 425), (550, 425), (575, 425), (600, 425), (625, 425),
                               (650, 425), (675, 425), (725, 425), (275, 450), (300, 450), (325, 450), (400, 450),
                               (425, 450), (450, 450), (0, 475), (25, 475), (50, 475), (75, 475), (100, 475),
                               (125, 475), (150, 475), (175, 475), (200, 475), (225, 475), (250, 475), (325, 475),
                               (400, 475), (475, 475), (500, 475), (525, 475), (550, 475), (575, 475), (600, 475),
                               (625, 475), (650, 475), (675, 475), (700, 475), (725, 475), (225, 500), (325, 500),
                               (400,  500), (500, 500), (25, 525), (50, 525), (75, 525), (100, 525), (125, 525),
                               (150, 525), (175, 525), (225, 525), (275, 525), (325, 525), (400, 525), (450, 525),
                               (500, 525), (550, 525), (575, 525), (600, 525), (625, 525), (650, 525), (675, 525),
                               (700, 525), (100, 550), (225, 550), (275, 550), (325, 550), (400, 550), (450, 550),
                               (500, 550), (625, 550), (0, 575), (25, 575), (50, 575), (100, 575), (175, 575),
                               (200, 575), (225, 575), (275, 575), (325, 575), (400, 575), (450, 575), (500, 575),
                               (525, 575), (550, 575), (625, 575), (675, 575), (700, 575), (725, 575), (100, 600),
                               (275, 600), (450, 600), (625, 600))
            
            self._running = 1
            self.createPieges()
            self.Check_Pieges()



    def createPieges(self):
        self.Pieges = ((200, 550), (200, 450), (75, 400), (125, 225), (225, 375),
                       (225, 175), (75, 225), (0, 125), (250, 125), (150, 0))
        self.Pieges2 = ((525, 550), (525, 450), (650, 400), (600, 225), (500, 375),
                        (500, 175), (650, 225), (725, 125), (475, 125), (575, 0))
        
        self.IsVisible = True
        self.clignoter()
        
    def clignoter(self):
        if self.IsVisible:
            self.activ = 1                
                
            self.piege1 = self.canvas.create_rectangle(200,550,225,575, fill='lightgreen', outline='')
            self.piege2 = self.canvas.create_rectangle(200,450,225,475, fill='lightgreen', outline='')
            self.piege3 = self.canvas.create_rectangle(75,400,100,425, fill='lightgreen', outline='')
            self.piege4 = self.canvas.create_rectangle(125,225,150,250, fill='lightgreen', outline='')
            self.piege5 = self.canvas.create_rectangle(225,375,250,400, fill='lightgreen', outline='')
            self.piege6 = self.canvas.create_rectangle(225,175,250,200, fill='lightgreen', outline='')
            self.piege7 = self.canvas.create_rectangle(75,225,100,250, fill='lightgreen', outline='')
            self.piege8 = self.canvas.create_rectangle(0,125,25,150, fill='lightgreen', outline='')
            self.piege9 = self.canvas.create_rectangle(250,125,275,150, fill='lightgreen', outline='')
            self.piege10 = self.canvas.create_rectangle(150,0,175,25, fill='lightgreen', outline='')
            self.piege11 = self.canvas.create_rectangle(525,550,550,575, fill='lightgreen', outline='')
            self.piege12 = self.canvas.create_rectangle(525,450,550,475, fill='lightgreen', outline='')
            self.piege13 = self.canvas.create_rectangle(650,400,675,425, fill='lightgreen', outline='')
            self.piege14 = self.canvas.create_rectangle(600,225,625,250, fill='lightgreen', outline='')
            self.piege15 = self.canvas.create_rectangle(500,375,525,400, fill='lightgreen', outline='')
            self.piege16 = self.canvas.create_rectangle(500,175,525,200, fill='lightgreen', outline='')
            self.piege17 = self.canvas.create_rectangle(650,225,675,250, fill='lightgreen', outline='')
            self.piege18 = self.canvas.create_rectangle(725,125,750,150, fill='lightgreen', outline='')
            self.piege19 = self.canvas.create_rectangle(475,125,500,150, fill='lightgreen', outline='')
            self.piege20 = self.canvas.create_rectangle(575,0,600,25, fill='lightgreen', outline='')           
            self.IsVisible = False

        elif not self.IsVisible:
            self.activ = 0
            self.canvas.delete(self.piege1, self.piege2, self.piege3, self.piege4, self.piege5,
                               self.piege6, self.piege7, self.piege8, self.piege9, self.piege10,
                               self.piege11, self.piege12, self.piege13, self.piege14, self.piege15,
                               self.piege16, self.piege17, self.piege18, self.piege19, self.piege20)           
            self.IsVisible = True
        self.canvas.after(self.latence, self.clignoter)
        

    def Clavier(self, event=None):
        if self._running:
            if event.keysym == 'z' and self.coords1[1] >= 25:
                if (self.coords1[0], self.coords1[1] - 25) not in self.caseNoires:
                    self.coords1 = (self.coords1[0], self.coords1[1] - 25)
                    self.Deplacement1()
                
            if event.keysym == 's' and self.coords1[1] <= 575:
                if (self.coords1[0], self.coords1[1] + 25) not in self.caseNoires:
                    self.coords1 = (self.coords1[0], self.coords1[1] + 25)
                    self.Deplacement1()
                
            if event.keysym == 'd' and self.coords1[0] <= 325:
                if (self.coords1[0] + 25, self.coords1[1]) not in self.caseNoires:
                    self.coords1 = (self.coords1[0] + 25, self.coords1[1])
                    self.Deplacement1()
                
            if event.keysym == 'q' and self.coords1[0] >= 25:
                if (self.coords1[0] - 25, self.coords1[1]) not in self.caseNoires:
                    self.coords1 = (self.coords1[0] - 25, self.coords1[1])
                    self.Deplacement1()               

            if self.coords1 == (100, 350):
                self.Checkpoint = 1
            if self.coords1 == (50, 250):
                self.Checkpoint = 2
            if self.coords1 == (100,0):
                self.win = 1
                self.Win_Option()
            
         
            if event.keysym == 'Up' and self.coords2[1] >= 25:
                if (self.coords2[0], self.coords2[1] - 25) not in self.caseNoires:
                    self.coords2 = (self.coords2[0], self.coords2[1] - 25)
                    self.Deplacement2()
                
            if event.keysym == 'Down' and self.coords2[1] <= 575:
                if (self.coords2[0], self.coords2[1] + 25) not in self.caseNoires:
                    self.coords2 = (self.coords2[0], self.coords2[1] + 25)
                    self.Deplacement2()
                
            if event.keysym == 'Right' and self.coords2[0] <= 700:
                if (self.coords2[0] + 25, self.coords2[1]) not in self.caseNoires:
                    self.coords2 = (self.coords2[0] + 25, self.coords2[1])
                    self.Deplacement2()
                
            if event.keysym == 'Left' and self.coords2[0] >= 400:
                if (self.coords2[0] - 25, self.coords2[1]) not in self.caseNoires:
                    self.coords2 = (self.coords2[0] - 25, self.coords2[1])
                    self.Deplacement2()

            if self.coords2 == (625, 350):
                self.Checkpoint2 = 4
            if self.coords2 == (675, 250):
                self.Checkpoint2 = 5
            if self.coords2 == (625, 0):
                self.win = 2
                self.Win_Option()    
            
            
           
    def Deplacement1(self):
        self.canvas.coords(self.rectangle1,
                           self.coords1[0],
                           self.coords1[1],
                           self.coords1[0]+25,
                           self.coords1[1]+25)
    def Deplacement2(self): 
        self.canvas.coords(self.rectangle2,
                           self.coords2[0],
                           self.coords2[1],
                           self.coords2[0]+25,
                           self.coords2[1]+25)
        
        
    def Check_Pieges(self):
        if self._running:
            if self.coords1 in self.Pieges and self.activ == 1:
                self.lastCheckpoint1()
            if self.coords2 in self.Pieges2 and self.activ == 1:
                self.lastCheckpoint2()

            self.csec += 1
            self.csec_score += 1
            if self.csec > 99:
                self.seconde += 1
                self.csec = 0
            if self.seconde > 60:
                self.minute += 1
                self.seconde = 0              
            self.time.set('%02d:%02d:%02d' % (self.minute, self.seconde, self.csec))

            self.canvas.after(10, self.Check_Pieges)
            

    def lastCheckpoint1(self):
        self.checkpoint0 = (0, 600)
        self.checkpoint1 = (100, 350)
        self.checkpoint2 = (50, 250)        

        if self.Checkpoint == 0:
            self.coords1 = self.checkpoint0
        elif self.Checkpoint == 1:
            self.coords1 = self.checkpoint1            
        elif self.Checkpoint == 2:
            self.coords1 = self.checkpoint2
            
        self.Deplacement1()
        
        
    def lastCheckpoint2(self):
        self.checkpoint3 = (725, 600)
        self.checkpoint4 = (625, 350)
        self.checkpoint5 = (675, 250)
        
        if self.Checkpoint2 == 3:
            self.coords2 = self.checkpoint3
        elif self.Checkpoint2 == 4:
            self.coords2 = self.checkpoint4
        elif self.Checkpoint2 == 5:
            self.coords2 = self.checkpoint5
      
        self.Deplacement2()
        
        

    def Win_Option(self):
        self._running = 0
        self.tl = tk.Toplevel(main)
        self.tl.title('Terminé')
        self.tl.geometry('500x100')
        self.tl.resizable(0,0)

        if self.win == 1:
            L = tk.Label(self.tl, text='Carré Rouge gagne en:', font=font3)
            L.place(x=15, y=15)
            
        elif self.win == 2:
            L = tk.Label(self.tl, text='Carré Bleu gagne en:', font=font3)    
            L.place(x=15, y=15)
            
        L_sw = tk.Label(self.tl, textvariable=self.time, font=font3)    
        L_sw.place(x=170, y=16)

        self.name = tk.StringVar()
        self.new_score = self.csec_score

        self.label_Name = tk.Label(self.tl, text="Entrez votre Nom puis appuyez sur 'OK'")
        self.entry_Name = tk.Entry(self.tl, textvariable=self.name)
        self.button_Name = tk.Button(self.tl, text=' OK ', relief=GROOVE, command=self.saveScore)
        self.label_Name.place(x=260, y=20)
        self.entry_Name.place(x=280, y=55)
        self.button_Name.place(x=430, y=52)
        

    def saveScore(self):
        self.name = self.entry_Name.get()
        self.label_Name.destroy()
        self.entry_Name.destroy()
        self.button_Name.destroy()
    
        if type(self.name) == type(tk.StringVar()):
            print('pas reconnu')
            self.name = 'Inconnu'

        with open("scores.txt","r") as fichier:
            self.scores = eval(fichier.read()) #On récupère la variable et la retransforme en dictionnaire
        try:
            self.best_score = self.scores[self.name]
            if self.new_score > self.best_score:
                self.scores[self.name] = self.new_score

        except KeyError:
            self.scores[self.name] = self.new_score
        with open("scores.txt","w") as fichier:
            fichier.write(str(self.scores))

        B_Restart = tk.Button(self.tl, text='Restart', relief=GROOVE, command=self.Restart)
        B_Quit = tk.Button(self.tl, text='Quit', relief=GROOVE, command=main.destroy)        
        B_Restart.place(x=70, y=55)
        B_Quit.place(x=170, y=55)
        

    def Restart(self):
        self.tl.destroy()
        self._running = 1
        self.Mode()


        
main = tk.Tk()
main.title('Square Race - Multiplayer')
w = main.winfo_screenwidth()
h = main.winfo_screenheight()
main.geometry("%dx%d+0+0" % (w, h))
main.protocol('WM_DELETE_WINDOW', noQuit)
main.overrideredirect(1)

sq = Square()
font1 = '-family {capsuula} -size 28 -weight normal'
font2 = '-family {capsuula} -size 20 -weight normal'
font3 = '-family {capsuula} -size 14 -weight normal'

start = tk.PhotoImage(file='start2.gif')
button_regle = tk.Button(main, width=40, height=40, compound=CENTER, image=start, relief=GROOVE, command=sq.RegleDuJeu)
quitt = tk.PhotoImage(file='quit.gif')
button_quitt = tk.Button(main, width=40, height=40, compound=CENTER, image=quitt, relief=GROOVE, command=main.destroy)
button_regle.place(x=546, y=690)
button_quitt.place(x=776, y=690)

main.mainloop()
