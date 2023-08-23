import os
import mido
import numpy as np
import tensorflow as tf

# Load the MIDI data
data_dir = 'MIDI_Composers/Mendelssohn'
note_sequences = []

for file in os.listdir(data_dir):
    if file.endswith('.mid'):
        midi = mido.MidiFile(os.path.join(data_dir, file))
        note_sequence = []
        for msg in midi:
            if msg.type == 'note_on':
                note_sequence.append(msg.note)
        note_sequences.append(note_sequence)

# Concatenate the note sequences
notes = [note for note_sequence in note_sequences for note in note_sequence]

# Define the vocabulary of possible notes
vocab = sorted(set(notes))
note_to_int = {note: i for i, note in enumerate(vocab)}
int_to_note = {i: note for note, i in note_to_int.items()}

# Define the length of the input/output sequences
num_timesteps = 64

# Convert the note sequences to input/output pairs
input_sequences = []

for i in range(len(notes) - num_timesteps):
    input_sequence = notes[i:i+num_timesteps]
    input_sequences.append([note_to_int[note] for note in input_sequence])

# Convert the input sequences to numpy arrays
x = np.reshape(input_sequences, (len(input_sequences), num_timesteps, 1))
x = x / float(len(vocab))

# Define the autoencoder model
input_layer = tf.keras.layers.Input(shape=(num_timesteps, 1))
encoded = tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(1000))(input_layer)
encoded = tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(100))(encoded)
encoded = tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(10))(encoded)
encoded = tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(100))(encoded)
encoded = tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(1000))(encoded)
decoded = tf.keras.layers.LSTM(64, return_sequences=True)(encoded)
decoded = tf.keras.layers.LSTM(32, return_sequences=False)(decoded)
decoded = tf.keras.layers.RepeatVector(num_timesteps)(decoded)
decoded = tf.keras.layers.LSTM(32, return_sequences=True)(decoded)
decoded = tf.keras.layers.LSTM(64, return_sequences=True)(decoded)
decoded = tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(1))(decoded)

autoencoder = tf.keras.models.Model(inputs=input_layer, outputs=decoded)

autoencoder.compile(optimizer='adam', loss='mse')
autoencoder.summary()

autoencoder.fit(x, x, epochs=250, batch_size=128)

# Generate a sequence of notes
generated_sequence = autoencoder.predict(x[0:1])

num_iterations = 10  # Number of iterations to generate additional notes
for i in range(num_iterations):
    # Use the most recently generated notes as input for the next iteration
    input_sequence = generated_sequence[:, -num_timesteps:, :]
    
    # Generate new notes based on the input sequence
    new_sequence = autoencoder.predict(input_sequence)
    
    # Append the newly generated notes to the sequence
    generated_sequence = np.concatenate([generated_sequence, new_sequence], axis=1)

# Convert the generated sequence to MIDI format and write it to a file
midi_file = mido.MidiFile()
track = mido.MidiTrack()
midi_file.tracks.append(track)

for note_int in generated_sequence[0]:
    note_idx = int(np.round(note_int[0]*len(vocab))) % len(vocab)
    note = int_to_note[note_idx]
    on = mido.Message('note_on', note=note, velocity=64, time=0)
    off = mido.Message('note_off', note=note, velocity=0, time=100)
    track.append(on)
    track.append(off)

midi_file.save('MIDI_Generated/Mendelssohn_250.mid')