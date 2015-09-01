'''
Created by: Brian Richard, Jonathan Zhang, Aneel Yelamanchili
on July 28 2014
bcr53@cornell.edu, jyz22@cornell.edu, ajy35@cornell.edu
'''

from MidiFile import MIDIFile
import song_maker, GUI

#builds a midi, melody, and three harmonies
midi1 = MIDIFile(1)
mel1 = song_maker.Melody(4)
harm = song_maker.Harmony(mel1)
mel1.buildNotes()
harm.buildNotes()
harm.buildNotes()
harm.buildNotes()

mel1.buildMelody(midi1)
harm.buildHarmony(midi1)

#writes to MIDI file
with open('output.mid', 'wb') as my_file:
    midi1.writeFile(my_file)
    
melDuration = []
melNotes = []

harmDuration = []
harm1Notes = []
harm2Notes = []
harm3Notes = []

lenHarms = len(harm.notes)

x=lenHarms/3 #used to split harmony into three separate parts

#0 -> x used for first harmony
#x - > 2x used for second harmony
#2x -> 3x used for third harmony
for i in range(x):
    harm1Notes.append(harm.notes[i][2])
for i in range(x,2*x):
    harm2Notes.append(harm.notes[i][2])
for i in range(2*x,3*x):
    harm3Notes.append(harm.notes[i][2])

#creates lists of individual notes and durations from the melody
for i in range(len(mel1.notes)):
    melDuration.append(mel1.notes[i][4])
    melNotes.append(mel1.notes[i][2])
    
for i in range(x):
    harmDuration.append(harm.notes[i][4])

#creates and executes GUI
app = GUI.MainView(melDuration, melNotes, harmDuration, harm1Notes, harm2Notes, harm3Notes)
app.mainloop()