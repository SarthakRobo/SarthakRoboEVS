import os

# 1. Purani app.py ko padhna
with open("app.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 2. Galat jagah add hue purane English route ko clean karna
clean_lines = []
skip = False
for line in lines:
    if "# === ENGLISH TEACHER ROUTE" in line:
        skip = True
    if not skip:
        clean_lines.append(line)

# 3. Main server command dhoondhna taaki usse theek pehle code daal sakein
insert_index = len(clean_lines)
for i, line in enumerate(clean_lines):
    if "if __name__ == '__main__':" in line or 'if __name__ == "__main__":' in line:
        insert_index = i
        break

# 4. Sahi code
english_route_code = """
# === ENGLISH TEACHER ROUTE ===
@app.route('/get_english_slide/<int:slide_id>')
def get_english_slide(slide_id):
    english_slides = []
    if os.path.exists('english_data.txt'):
        with open('english_data.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                line = line.strip()
                if line:
                    if 'Answer:' in line:
                        parts = line.split('Answer:')
                        q_text = parts[0].strip()
                        a_text = 'Answer: ' + parts[1].strip()
                    else:
                        q_text = line
                        a_text = ''
                    english_slides.append({
                        'id': i+1,
                        'is_heading': False,
                        'question': q_text,
                        'answer': a_text,
                        'audio': f'/static/audios/english_slide_{i+1}.mp3'
                    })
    
    for slide in english_slides:
        if slide['id'] == slide_id:
            return jsonify(slide)
    return jsonify({'error': 'Slide not found'})

"""

# 5. Sahi jagah par code insert karna
clean_lines.insert(insert_index, english_route_code)

# 6. File ko wapas save karna
with open("app.py", "w", encoding="utf-8") as f:
    f.writelines(clean_lines)

print("✅ PERFECT FIX APPLIED! Ab English section bilkul chalega!")
