import os
from PIL import Image, ImageDraw, ImageFont

def process_images(input_folder, output_folder, width=800, quality=80):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    valid_extensions = ('.jpg', '.jpeg', '.png')
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_extensions):
            try:
                img_path = os.path.join(input_folder, filename)
                with Image.open(img_path) as img:
                    
                    w_percent = (width / float(img.size[0]))
                    h_size = int((float(img.size[1]) * float(w_percent)))
                    img = img.resize((width, h_size), Image.Resampling.LANCZOS)
                    
                    draw = ImageDraw.Draw(img)
                    text = "Project50 - Day 43"
                    
                    font = ImageFont.load_default()

                    draw.text((img.size[0] - 150, img.size[1] - 30), text, fill=(255, 255, 255), font=font)
                    
                    clean_name = os.path.splitext(filename)[0]
                    new_filename = f"{clean_name}_optimized.webp"
                    save_path = os.path.join(output_folder, new_filename)
                    
                    img.save(save_path, "WEBP", quality=quality, optimize=True)
                    print(f"[+] Оброблено: {new_filename}")
                    
            except Exception as e:
                print(f"[!] Помилка у файлі {filename}: {e}")

if __name__ == "__main__":
    INPUT = "Phase_5_Capstone/other/Day_43" 
    OUTPUT = "Phase_5_Capstone/other/Day_43/optimized"
    
    process_images(INPUT, OUTPUT, width=512, quality=75)

    