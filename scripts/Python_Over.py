import os
import shutil

source_folder = r"C:\MyLibrary\3_English_Translated_Vol2"
destination_folder = r"H:\ไฟล์ใหญ่เกิน95"
size_limit = 95 * 1024 * 1024  # แปลง 95 MB ให้เป็นหน่วย Bytes

# สร้างโฟลเดอร์ปลายทางหากยังไม่มี
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print(f"สร้างโฟลเดอร์ปลายทางแล้ว: {destination_folder}")

# ตรวจสอบและย้ายไฟล์
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    
    # ตรวจสอบว่าเป็นไฟล์ (ไม่ใช่โฟลเดอร์) และขนาดเกิน 95 MB หรือไม่
    if os.path.isfile(file_path) and os.path.getsize(file_path) > size_limit:
        shutil.move(file_path, destination_folder)
        print(f"ย้ายไฟล์แล้ว: {filename}")