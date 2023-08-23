import mido
import os
import csv

def extract_sequences(midi_file):
    sequences = []
    for track in midi_file.tracks:
        for msg in track:
            if msg.type == 'note_on':
                sequences.append(msg.note)
    return sequences

# set the directory where the MIDI files are stored
midi_folder = 'MIDI_Generated'

# create an empty list to store all the note sequences
all_note_sequences = []

# loop through all the MIDI files in the folder
for file_name in os.listdir(midi_folder):
    if file_name.endswith('.mid'):
        # load the MIDI file
        midi_file = mido.MidiFile(os.path.join(midi_folder, file_name))
        
        # extract the note sequence from the MIDI file
        note_sequence = extract_sequences(midi_file)
        
        # add the note sequence to the list of all note sequences
        all_note_sequences.append([file_name] + note_sequence)

# write the note sequences to a CSV file
with open('Codes/CSV/note_sequences.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(all_note_sequences)
