import csv

def csv_extractor(file_path, *columns):
    try:
        with open(file_path, newline='') as csvfile:
            extract_column = csv.reader(csvfile, delimiter=",")
            headers = next(extract_column)
            headers_lower = [h.lower() for h in headers]

            indices = []

            for column in columns:
                if column.lower() in headers_lower:
                    idx = headers_lower.index(column.lower())
                    indices.append(idx)

            if not indices:
                print("[!] Жодної з вказаних колонок не знайдено.")
                return

            for row in extract_column:
                selected_data = [row[i] for i in indices]
                print(" | ".join(selected_data))
                
            
    except Exception as e: print(e)

if __name__ == "__main__":
    file_path = "Phase_2_Files_Data/other/Day_15/users.csv"
    csv_extractor(file_path, "name", "City")
    