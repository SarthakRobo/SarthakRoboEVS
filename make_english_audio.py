import asyncio
import edge_tts
import os
import re

audio_dir = "static/audios"
if not os.path.exists(audio_dir):
    os.makedirs(audio_dir)

async def main():
    print("English Audio banna shuru ho raha hai (Pro Teacher Style)...")
    
    if not os.path.exists("english_data.txt"):
        print("Error: english_data.txt nahi mili!")
        return

    with open("english_data.txt", "r", encoding="utf-8") as file:
        lines = [l.strip() for l in file.readlines() if l.strip()]

    slide_num = 1
    for line in lines:
        parts = line.split('Answer:')
        if len(parts) == 2:
            q_part = parts[0].strip()
            a_part = parts[1].strip()
        else:
            q_part = line
            a_part = ""

        # Point bolne ka rule (Jaise 1.1 ko 1 point 1 padhega)
        q_clean = re.sub(r'Sawaal (\d+)\.(\d+)\.?', r'Sawaal \1 point \2, ', q_part)
        
        # Blanks ke liye underscore ko "Blank" padhwana
        q_clean = q_clean.replace("_____", "blank")
        a_part = a_part.replace("_____", "blank")

        # Question ke liye Male Voice (MadhurNeural)
        q_comm = edge_tts.Communicate(q_clean, "hi-IN-MadhurNeural")
        await q_comm.save("temp_q.mp3")

        # Answer ke liye Female Voice (SwaraNeural)
        if a_part:
            a_clean = "Answer: " + a_part
            a_comm = edge_tts.Communicate(a_clean, "hi-IN-SwaraNeural")
            await a_comm.save("temp_a.mp3")

        # Dono audio ko jodkar ek final mp3 banana
        final_path = f"{audio_dir}/english_slide_{slide_num}.mp3"
        with open(final_path, "wb") as f:
            with open("temp_q.mp3", "rb") as q: 
                f.write(q.read())
            if a_part and os.path.exists("temp_a.mp3"):
                with open("temp_a.mp3", "rb") as a: 
                    f.write(a.read())

        print(f"✅ english_slide_{slide_num}.mp3 taiyar hai!")
        slide_num += 1

    if os.path.exists("temp_q.mp3"): 
        os.remove("temp_q.mp3")
    if os.path.exists("temp_a.mp3"): 
        os.remove("temp_a.mp3")
        
    print("🎉 Saari English audio files Pro Teacher Style mein ban gayin!")

if __name__ == "__main__":
    asyncio.run(main())
