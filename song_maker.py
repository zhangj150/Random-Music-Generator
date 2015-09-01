'''
Created by: Brian Richard, Jonathan Zhang, Aneel Yelamanchili
on July 28 2014
bcr53@cornell.edu, jyz22@cornell.edu, ajy35@cornell.edu
'''
import random
from MidiFile import MIDIFile
#imports random library for various random selections
#imports midi for music "jazz"

class Melody:
    '''this class and its methods quasi-randomly generate notes in a major scale as a line of melody'''
    
    def __init__(self, sect = 1, notes = []):
        self.notes = notes
        self.melloc = 0
        self.sections = sect
        self.instrs = dict([('piano',0), ('harpsichord',6), ('glock',9), ('vibes',11), #dictionary of instruments that we could use
                            ('marimba',12), ('organ',19), ('guitar',24), ('bass',32),
                            ('violin',40), ('cello',42), ('harp',46), ('timps',47),
                            ('voice',54), ('trumpet',56), ('tuba',58), ('horn',60),
                            ('alto sax', 65), ('oboe',68), ('bassoon',70), ('clarinet',71),
                            ('flute',73), ('recorder',74), ('bottle',75), ('whistle',78),
                            ('fifths',96), ('koto',107),
                            ('bagpipe',109), ('taiko',116), ('toms',117), ('breath',121),
                            ('bird',123), ('applause',126)])
        
    def buildNotes(self):
        for i in range(self.sections):
            randnum = random.randint(55, 67)
            if randnum == 57:
                randnum = 60
            elif randnum == 66:
                randnum = 65
            x = randnum
            for j in range(16):
                randjump = random.choice([-7, -5, 0, 2, 2, 2, 4, 5, 7, 9, 11])
                if randjump == 57:
                    randjump = 60
                if randjump == 66:
                    randjump = 65
                if j == 0:
                    tempnote = (0, 0, randnum, self.melloc, 1, 100)
                    #0 is track, 0 is channel, 1 is length, 100 is volume percentage
                    self.melloc += 1    #1 is length
                    self.notes.append(tempnote)
                else:
                    randnum = randnum + randjump
                    #print('new note' + str(randnum))
                    '''if randnum >= 88 or randnum <= 1:
                        randnum = x               #resets value to starting key
                        randnum = randnum + randjump'''
                    tempnote = (0, 0, randnum, self.melloc, 1, 100)
                    randnum = x
                    #print('did it change' + str(randnum))
                    self.melloc = int(self.melloc) + 1
                    self.notes.append(tempnote)
                splitchoice = random.choice([0, 0, 0, 1])
                if splitchoice == 1:
                    self.melloc = self.melloc - 1
                    self.notes.pop()
                    summation = 0
                    count = 0
                    choices = [.25, .5]
                    while summation < 1:
                        randjump = random.choice([ -5, 0, 2, 2, 2, 4, 5])
                        randnum = randnum + randjump
                        intervalchoice = random.choice(choices)
                        count += 1
                        summation = summation + intervalchoice
                        if summation > .5 and .5 in choices:
                            choices.remove(.5)
                        tempnote = (0, 0, randnum, self.melloc, intervalchoice, 100)
                        randnum = x
                        self.melloc = self.melloc + intervalchoice
                        self.notes.append(tempnote)

#original version:
    '''def buildNotes(self):
            for i in range(self.sections):
                randnum = random.randint(55, 67)
                x = randnum
                print ('first note' + str(x))
                for j in range(15):
                    randjump = random.choice([-7, -8, -5, -2, 0, 1, 2, 2, 2, 4, 5])
                    if j == 0:
                        tempnote = (0, 0, randnum, self.melloc, 1, 100) #if inputting first note, randomly select a note between 55 and 67
                        #0 is track, 0 is channel, 1 is length, 100 is volume percentage
                        self.melloc += 1
                        self.notes.append(tempnote)  #add this first note to the list of notes
                    else:
                        randnum = randnum + randjump
                #for subsequent notes, generate note by adding one of the random intervals to the starting note to attain a pitch
                        #print('new note' + str(randnum))
                        tempnote = (0, 0, randnum, self.melloc, random.choice([0.25, 0.5, 1, 2, 3, 4]), 100)
                        randnum = x
                        self.melloc += 1
                        self.notes.append(tempnote)  #finally append that new generated note to list of notes'''
                    
    def change_instr(self, instr, midfile):  #defining setting the instrument
        midfile.addProgramChange(0, 0, self.melloc, instr)

    def buildMelody(self, midfile):
        self.change_instr(self.instrs['piano'], midfile)  #set instrument here
        for i in range(len(self.notes)): #self.notes is a list of tuples, each tuple contains the attributes of a note
            midfile.addNote(self.notes[i][0], self.notes[i][1], self.notes[i][2], self.notes[i][3], self.notes[i][4], self.notes[i][5])
        midfile.addNote(0, 0, self.notes[-16][2], self.melloc, 4, 100)
        #building a melody into a midifile by inputting each note that was stored in the list [self.notes]

class Harmony:
    '''This class builds harmonic lines based off of the notes in the melody built above'''
    
    def __init__(self, mel, notes = []):
        self.refmel = mel  #import melody to write harmony off of
        self.notes = notes #notes in harmony
        self.harloc = 0

    def buildNotes(self):
        self.harloc = 0      #resetting to beginning of music staff for every extra harmony
        for i in range(len(self.refmel.notes)): #building harmony length based off of length of melody
            randjump = random.choice([-5, -8, 4, -2])
            templist = []
            lastint = 0
            for j in range(len(self.refmel.notes)):
                if int(self.refmel.notes[i][3])%2 == 0 and int(self.refmel.notes[i][2]) != lastint:
                    randnum = [self.refmel.notes[i][2] + randjump, self.refmel.notes[i][3]]
                    templist.append(randnum)
                    lastint = int(self.refmel.notes[i][2])
            for j in range(len(templist)):
                if self.harloc%2 == 0:  #this limits us to half-notes in the harmonies, its cleaner that way
                    tempnote = (0, 1, templist[j][0], templist[j][1], 2, 65)
                    self.notes.append(tempnote)
                else:
                    tempnote = (0, 1, randnum[0], templist[j][1], 2, 65)
                    self.notes.append(tempnote)
                self.harloc += 1
        
    def buildHarmony(self, midfile):
        for i in range(len(self.notes)):
            midfile.addNote(self.notes[i][0], self.notes[i][1], self.notes[i][2], self.notes[i][3], self.notes[i][4], self.notes[i][5])
        #midfile.addNote(0, 1, self.notes[-16][2], self.harloc, 4, 100)
