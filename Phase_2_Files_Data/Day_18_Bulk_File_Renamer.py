from pathlib import Path

def file_rename(user_path, old_file_suffix, new_file_suffix):
    p = Path(user_path)
    print("PATH: ", p)
    for sub_file in p.iterdir():
        if not sub_file.is_file():
            continue
        if sub_file.suffix == old_file_suffix:
            new_path = sub_file.with_suffix(new_file_suffix)
            if new_path.exists():
                continue
            print(f"Renamed: {sub_file.name} -> {new_path.name}")
            sub_file.rename(new_path)
            


if __name__ == "__main__":
    file_rename('Phase_2_Files_Data/other/Day_18', ".txt", ".log")