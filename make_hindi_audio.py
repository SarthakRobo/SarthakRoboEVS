import os


print("Hindi Audio banna shuru ho raha hai...")

# hindi_data.txt ko padhna
with open("hindi_data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

slide_num = 1
for line in lines:
    text = line.strip()
    if text: # Agar line khali nahi hai
        # hi-IN-SwaraNeural ek premium female teacher ki aawaz hai
        # Gents aawaz ke liye ise hi-IN-MadhurNeural kar sakte hain
        command = f'edge-tts --voice "hi-IN-SwaraNeural" --text "{text}" --write-media "static/audios/hindi_slide_{slide_num}.mp3"'
        os.system(command)
        print(f"✅ hindi_slide_{slide_num}.mp3 taiyar hai!")
        slide_num += 1

print("🎉 Saari audio files ban gayin!")
