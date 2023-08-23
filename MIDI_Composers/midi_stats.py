import os
import glob
import pretty_midi

directory_path = os.getcwd()

# open a new file to write the output to
with open(os.path.join(directory_path, "midi_stats.txt"), "w") as file:
    for folder in os.listdir(directory_path):
        if os.path.isdir(os.path.join(directory_path, folder)):
            
            # get a list of all MIDI files in the folder
            midi_files = glob.glob(os.path.join(directory_path, folder, "*.mid"))
            file_count = len(midi_files)
            file.write(f"\n{folder}: {file_count} files\n")
            
            # iterate over all MIDI files in the folder
            for midi_file in midi_files:
                midi_data = pretty_midi.PrettyMIDI(midi_file)
                
                # calculate the playtime of the MIDI file in minutes and seconds
                playtime_sec = midi_data.get_end_time()
                playtime_min, playtime_sec = divmod(playtime_sec, 60)
                playtime = f"{int(playtime_min):02}:{int(playtime_sec):02}"
                
                # get the name of the MIDI file
                midi_filename = os.path.basename(midi_file)
                
                # write the song name and playtime to the file
                file.write(f"  {midi_filename}: {playtime}\n")
