import os
from mido import MidiFile

def get_note_sequence(filename):
    """Extracts the note sequence from a MIDI file."""
    midi = MidiFile(filename)
    notes = []
    for msg in midi:
        if msg.type == 'note_on':
            notes.append(msg.note)
    return tuple(notes)

def compare_midi_files(input_file, folder):
    """Compares an input MIDI file to all other MIDI files in a folder."""
    input_sequence = get_note_sequence(input_file)
    similarities = []
    for file in os.listdir(folder):
        if file.endswith('.mid'):
            file_path = os.path.join(folder, file)
            sequence = get_note_sequence(file_path)
            similarity = len(set(input_sequence) & set(sequence)) / len(set(input_sequence) | set(sequence))
            similarities.append(similarity)
    return sum(similarities) / len(similarities)

input_file = 'MIDI_Generated/Schumann_250.mid'
folder = 'MIDI_Composers/Schumann'

similarity_score = compare_midi_files(input_file, folder)
print(f'The similarity score between {input_file} and the MIDI files in {folder} is {similarity_score}')
