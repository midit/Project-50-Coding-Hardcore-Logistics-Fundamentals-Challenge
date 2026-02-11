from pathlib import Path

def scan_directory(user_path):
    p = Path(user_path)
    print("PATH: ", p)
    for sub_file in p.iterdir():
        if not sub_file.is_file():
            continue
        file_size = sub_file.stat().st_size/1024
        print(f"{sub_file.name} | Size: {file_size:.2f}KB")

if __name__ == "__main__":
    scan_directory('Phase_2_Files_Data/')


    