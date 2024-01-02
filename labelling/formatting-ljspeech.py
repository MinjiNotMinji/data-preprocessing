file_path = "/home/minji.tts/Dataset/metadata.csv"
content = ''

with open(file_path, 'r') as f:    
    lines = f.readlines()
    for l in lines:
        content += f"{l.rstrip()}|{l.split('|')[1].strip()}\n"

with open(file_path, 'w') as f:
    f.write(content)
