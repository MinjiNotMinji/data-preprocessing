from os import walk, rename
import whisper
from pydub import AudioSegment

file_list = []
for (_, _, filenames) in walk("/home/minji.tts/Friendshiping/wavs"):
    for file in filenames:
        if file.endswith("wav"):
            file_list.append(file)
    
    break

model = whisper.load_model("large")

index = 1
with open("Friendshiping/metadata.csv", "w") as csv:
    for file in sorted(file_list):
        result = model.transcribe(f"/home/minji.tts/Friendshiping/wavs/{file}")

        csv.write(f"audio{index}|{result['text'].strip()}|{result['text'].strip()}\n")
        
        rename(f"/home/minji.tts/Friendshiping/wavs/{file}", f"/home/minji.tts/Friendshiping/wavs/audio{index}.wav")

        index += 1