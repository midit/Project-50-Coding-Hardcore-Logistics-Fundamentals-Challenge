import json
import datetime

def update_profile(file_path, **changes):
    try:
        with open(file_path, "r") as profile:
            profile_json = json.load(profile)
            for key, value in changes.items():
                if key in profile_json:
                    old_value = profile_json[key]
                    if isinstance(old_value, list):
                        snapshot_old = old_value.copy()

                        profile_json[key].append(value)

                        log_entry = f"[{datetime.datetime.now()}] {key}: {snapshot_old} -> {profile_json[key]}"
                        profile_json["history"].append(log_entry)
                        print(f"Updated list {key}: Added '{value}'")
                    else:
                        log_entry = f"[{datetime.datetime.now()}] {key}: {old_value} -> {value}"
                        profile_json["history"].append(log_entry)
                        print(f"Changed {key} from {old_value} to {value}")

                        profile_json[key] = value
                    
                    now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    profile_json["last_updated"] = now_str
                else:
                    print("[!] Жодної з вказаних колонок не знайдено.")
                    return
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(profile_json, f, indent=4, ensure_ascii=False)
            
    except Exception as e: print(e)

if __name__ == "__main__":
    file_path = "Phase_2_Files_Data/other/Day_16/profile.json"
    update_profile(file_path, skills = "what time is it?")