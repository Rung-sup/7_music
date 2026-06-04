import os
import json

def generate_music_db():
    # 1. หาตำแหน่งของโฟลเดอร์ 7_music (ถอยออกจากโฟลเดอร์ scripts 1 ชั้น)
    current_script_path = os.path.abspath(__file__)
    scripts_dir = os.path.dirname(current_script_path)
    base_dir = os.path.dirname(scripts_dir) # นี่คือโฟลเดอร์ 7_music
    
    # 2. กำหนด Path ของเป้าหมาย
    music_dir = os.path.join(base_dir, 'audio_files')
    output_file = os.path.join(base_dir, 'metadata', 'music_db.json')
    
    music_list = []
    
    # 3. ตรวจสอบว่ามีโฟลเดอร์เก็บเพลงหรือยัง ถ้าไม่มีให้สร้างรอไว้
    if not os.path.exists(music_dir):
        os.makedirs(music_dir)
        print(f"สร้างโฟลเดอร์ใหม่: {music_dir} (กรุณานำไฟล์ MP3 มาใส่ที่นี่)")
        return

    # 4. เริ่มสแกนไฟล์ MP3
    for root, dirs, files in os.walk(music_dir):
        for file in files:
            if file.lower().endswith(".mp3"):
                # สร้าง Path แบบ Relative (เริ่มจาก 7_music/...) 
                # เพื่อให้แอปหลักเรียกใช้งานได้สะดวก
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_dir)
                
                music_list.append({
                    "title": os.path.splitext(file)[0],
                    "file_name": file,
                    "path": rel_path,
                    "folder": os.path.basename(root)
                })
    
    # 5. บันทึกลงไฟล์ JSON ในโฟลเดอร์ metadata
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(music_list, f, ensure_ascii=False, indent=4)
        
    print(f"--- สแกนสำเร็จ! ---")
    print(f"พบเพลงทั้งหมด: {len(music_list)} รายการ")
    print(f"บันทึกฐานข้อมูลไว้ที่: {output_file}")

if __name__ == "__main__":
    generate_music_db()