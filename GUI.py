'''
Created by: Brian Richard, Jonathan Zhang, Aneel Yelamanchili
on July 28 2014
bcr53@cornell.edu, jyz22@cornell.edu, ajy35@cornell.edu
'''
import Tkinter as tk, pygame, song_maker, time
from Tkinter import *
from MidiFile import MIDIFile
from thread import start_new_thread

class MainView(tk.Tk):
    def __init__(self, melDuration, melNotes, harmDuration, harm1Notes, harm2Notes, harm3Notes, *args, **kwargs):
        #inherits everything from Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("800x700")
        self.frame = tk.Frame(self)
        self.title("Treble Maker")
        self.frame.pack(side="top", fill="both", expand=True) #adds frame to GUI
        self.label = tk.Label(self, font = ("Courier", 80, "italic"), text = "Treble Maker")
        self.label.pack(in_=self.frame)
        self.subtitle = tk.Label(self, font = ("Courier", 20), text = "A music generator")
        self.subtitle.place(x=285,y=100)
        self.about = tk.Label(self, font = ("Courier", 10, "italic"), text = "Created by Aneel Yelamanchili, Brian Richard, \
                                            and Jonathan Zhang for CS 1110. Version 1.4")
        self.about.pack(side = BOTTOM, in_=self.frame)
        self.button1 = tk.Button(self, text="Start", command=self.appview) #button to go to appview
        self.button1.place(height = 40, width = 200, x=300, y=350)
        
        #initializes attributes of class MainView
        self.melDuration = melDuration
        self.melNums = melNotes
        self.harmDuration = harmDuration
        self.harm1Nums = harm1Notes
        self.harm2Nums = harm2Notes
        self.harm3Nums = harm3Notes
        
        self.melNotes = []
        self.harm1Notes = []
        self.harm2Notes = []
        self.harm3Notes = []
        
        #assigns values to particular notes
        c, csharp, d, dsharp, e, f, fsharp, g, gsharp, a, asharp, b = \
        60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71
        
        #this loop checks to see if the remainder of the current value
        #with a given index is equal to the remainder of a key given a particular octave
        #this loop is for the melody
        for i in range(len(self.melNums)):
            if self.melNums[i] % 12 == c % 12:
                self.melNotes.append('C')
            elif self.melNums[i] % 12 == csharp % 12:
                self.melNotes.append('C#')
            elif self.melNums[i] % 12 == d % 12:
                self.melNotes.append('D')
            elif self.melNums[i] % 12 == dsharp % 12:
                self.melNotes.append('D#')
            elif self.melNums[i] % 12 == e % 12:
                self.melNotes.append('E')
            elif self.melNums[i] % 12 == f % 12:
                self.melNotes.append('F')
            elif self.melNums[i] % 12 == fsharp % 12:
                self.melNotes.append('F#')
            elif self.melNums[i] % 12 == g % 12:
                self.melNotes.append('G')
            elif self.melNums[i] % 12 == gsharp % 12:
                self.melNotes.append('G#')
            elif self.melNums[i] % 12 == a % 12:
                self.melNotes.append('A')
            elif self.melNums[i] % 12 == asharp % 12:
                self.melNotes.append('A#')
            elif self.melNums[i] % 12 == b % 12:
                self.melNotes.append('B')
                
        #this loop checks to see if the remainder of the current value
        #with a given index is equal to the remainder of a key given a particular octave
        #this loop is for harmony one        
        for i in range(len(self.harm1Nums)):
            if self.harm1Nums[i] % 12 == c % 12:
                self.harm1Notes.append('C')
            elif self.harm1Nums[i] % 12 == csharp % 12:
                self.harm1Notes.append('C#')
            elif self.harm1Nums[i] % 12 == d % 12:
                self.harm1Notes.append('D')
            elif self.harm1Nums[i] % 12 == dsharp % 12:
                self.harm1Notes.append('D#')
            elif self.harm1Nums[i] % 12 == e % 12:
                self.harm1Notes.append('E')
            elif self.harm1Nums[i] % 12 == f % 12:
                self.harm1Notes.append('F')
            elif self.harm1Nums[i] % 12 == fsharp % 12:
                self.harm1Notes.append('F#')
            elif self.harm1Nums[i] % 12 == g % 12:
                self.harm1Notes.append('G')
            elif self.harm1Nums[i] % 12 == gsharp % 12:
                self.harm1Notes.append('G#')
            elif self.harm1Nums[i] % 12 == a % 12:
                self.harm1Notes.append('A')
            elif self.harm1Nums[i] % 12 == asharp % 12:
                self.harm1Notes.append('A#')
            elif self.harm1Nums[i] % 12 == b % 12:
                self.harm1Notes.append('B')
                
        #this loop checks to see if the remainder of the current value
        #with a given index is equal to the remainder of a key given a particular octave
        #this loop is for the harmony two
        for i in range(len(self.harm2Nums)):
            if self.harm2Nums[i] % 12 == c % 12:
                self.harm2Notes.append('C')
            elif self.harm2Nums[i] % 12 == csharp % 12:
                self.harm2Notes.append('C#')
            elif self.harm2Nums[i] % 12 == d % 12:
                self.harm2Notes.append('D')
            elif self.harm2Nums[i] % 12 == dsharp % 12:
                self.harm2Notes.append('D#')
            elif self.harm2Nums[i] % 12 == e % 12:
                self.harm2Notes.append('E')
            elif self.harm2Nums[i] % 12 == f % 12:
                self.harm2Notes.append('F')
            elif self.harm2Nums[i] % 12 == fsharp % 12:
                self.harm2Notes.append('F#')
            elif self.harm2Nums[i] % 12 == g % 12:
                self.harm2Notes.append('G')
            elif self.harm2Nums[i] % 12 == gsharp % 12:
                self.harm2Notes.append('G#')
            elif self.harm2Nums[i] % 12 == a % 12:
                self.harm2Notes.append('A')
            elif self.harm2Nums[i] % 12 == asharp % 12:
                self.harm2Notes.append('A#')
            elif self.harm2Nums[i] % 12 == b % 12:
                self.harm2Notes.append('B')

        #this loop checks to see if the remainder of the current value
        #with a given index is equal to the remainder of a key given a particular octave
        #this loop is for the harmony three
        for i in range(len(self.harm3Nums)):
            if self.harm3Nums[i] % 12 == c % 12:
                self.harm3Notes.append('C')
            elif self.harm3Nums[i] % 12 == csharp % 12:
                self.harm3Notes.append('C#')
            elif self.harm3Nums[i] % 12 == d % 12:
                self.harm3Notes.append('D')
            elif self.harm3Nums[i] % 12 == dsharp % 12:
                self.harm3Notes.append('D#')
            elif self.harm3Nums[i] % 12 == e % 12:
                self.harm3Notes.append('E')
            elif self.harm3Nums[i] % 12 == f % 12:
                self.harm3Notes.append('F')
            elif self.harm3Nums[i] % 12 == fsharp % 12:
                self.harm3Notes.append('F#')
            elif self.harm3Nums[i] % 12 == g % 12:
                self.harm3Notes.append('G')
            elif self.harm3Nums[i] % 12 == gsharp % 12:
                self.harm3Notes.append('G#')
            elif self.harm3Nums[i] % 12 == a % 12:
                self.harm3Notes.append('A')
            elif self.harm3Nums[i] % 12 == asharp % 12:
                self.harm3Notes.append('A#')
            elif self.harm3Nums[i] % 12 == b % 12:
                self.harm3Notes.append('B')

    def mainmenu(self, event=None):
        #hides all widgets from appview if mainmenu is called
        self.button2.place_forget()
        self.play.place_forget()
        self.leave.place_forget()
        self.melody.place_forget()
        self.harmony_one.place_forget()
        self.melN.place_forget()
        self.harmonyOneN.place_forget()
        self.harmonyTwoN.place_forget()
        self.harmonyThreeN.place_forget()
        #places/packs widgets into frame
        self.label.pack(in_=self.frame)
        self.button1.place(height = 40, width = 200, x=300, y=275)
        self.subtitle.place(x=285,y=100)
        self.about.pack(side = BOTTOM, in_=self.frame)

    def appview(self, event=None):
        #hides all widgets from mainmenu if appview is called
        self.label.pack_forget()
        self.button1.place_forget()
        self.subtitle.place_forget()
        self.about.pack_forget()
        #creates set of three buttons at bottom of frame
        self.play = tk.Button(self, text="Play", command = self.music)
        self.play.place(width=62,x=301,y=675)
        self.button2 = tk.Button(self, text="Go to main menu", command=self.mainmenu)
        self.button2.place(x=363,y=675)
        self.leave = tk.Button(self, text = "Quit", command = self.quit)
        self.leave.place(x=467,y=675)
        #creates labels that pertain to either the melody or harmony of the song
        self.melody = tk.Label(self, font = ("Courier", 10), text = "melody")
        self.melody.place(x=30,y=30)
        self.harmony_one = tk.Label(self, font = ("Courier", 10), text = "triad")
        self.harmony_one.place(x=30,y=180)
        self.melN = tk.Label(self, font = ("Courier", 90), text = '')
        self.melN.place(x=362,y=30)
        self.harmonyOneN = tk.Label(self, anchor = CENTER, font = ("Courier", 90), text = '')
        self.harmonyOneN.place(x=362,y=180)
        self.harmonyTwoN = tk.Label(self, anchor = CENTER, font = ("Courier", 90), text = '')
        self.harmonyTwoN.place(x=362,y=330)
        self.harmonyThreeN = tk.Label(self, anchor = CENTER, font = ("Courier", 90), text = '')
        self.harmonyThreeN.place(x=362,y=480)
    
    def mel_note(self):
        self.update() #updates frame
        #changes text based on current note
        #note is on screen for it's given duration
        for i in range(len(self.melNotes)):
            self.melN.config(text = self.melNotes[i])
            time.sleep(60/120.0*self.melDuration[i])
            
    def harm_note(self):
        self.update() #updates frame
        for i in range(len(self.harm1Notes)):
            #changes text of all three harmonies
            #note is on screen for it's given duration
            self.harmonyOneN.config(text = self.harm1Notes[i])
            self.harmonyTwoN.config(text = self.harm2Notes[i])
            self.harmonyThreeN.config(text = self.harm3Notes[i])
            time.sleep(60/185.0*self.harmDuration[i])
    
    def music(self):
        #sub function of functioon music
        def play_music(music_file):
            """
            stream music with mixer.music module in blocking manner
            this will stream the sound from disk while playing
            """
            clock = pygame.time.Clock()
            #try-catch for playing audio from MIDI file
            try:
                pygame.mixer.music.load(music_file)
                print "Music file %s loaded!" % music_file
                self.update()
            except pygame.error:
                print "File %s not found! (%s)" % (music_file, pygame.get_error())
                return
            pygame.mixer.music.play() #plays MIDI file
            self.update() #updates frame
        # pick a midi music file you have ...
        # (if not in working folder use full path)
        
        #creates two threads so that both functions
        #can occur at the same time without interfering 
        self.update()
        start_new_thread(self.mel_note, ())
        self.update()
        start_new_thread(self.harm_note, ())
        
        music_file = "output.mid"
        
        freq = 44100    # audio CD quality
        bitsize = -16   # unsigned 16 bit
        channels = 2    # 1 is mono, 2 is stereo
        buffer = 1024    # number of samples
        pygame.mixer.init(freq, bitsize, channels, buffer)
        #self.update()
        # optional volume 0 to 1.0
        pygame.mixer.music.set_volume(0.8)
        
        play_music(music_file) #calls sub function to play music