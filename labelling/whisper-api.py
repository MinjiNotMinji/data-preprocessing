from os import walk, rename
import whisper

root = "/home/minji.tts/Dataset"

file_list = []
for (_, _, filenames) in walk(f"{root}/wavs"):
    for file in filenames:
        if file.endswith("wav"):
            file_list.append(file)
    
    break

model = whisper.load_model("large")

index = 101
with open(f"{root}/metadata.csv", "w") as csv:
    for file in sorted(file_list):
        result = model.transcribe(f"{root}/wavs/{file}")

        csv.write(f"audio{index}|{result['text'].strip()}\n")
        
        rename(f"{root}/wavs/{file}", f"{root}/wavs/audio{index}.wav")

        index += 1