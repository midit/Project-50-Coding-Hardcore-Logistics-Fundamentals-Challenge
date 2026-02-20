def lambda_sort(data, desc):
    return sorted(data, key=lambda x: x[1], reverse=desc)

if __name__ == "__main__":
    students = [("Олексій", 85), ("Марія", 92), ("Іван", 78)]
    print(f"За зростанням: {lambda_sort(students, False)}")
    print(f"За спаданням: {lambda_sort(students, True)}")