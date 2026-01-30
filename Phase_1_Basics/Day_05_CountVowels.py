def count_vowels(s):
    vowels = {"a", "e", "i", "o", "u", "а", 
            "е", "є", "и", "і", "ї", "о", 
            "у", "ю", "я"}
    
    return sum(1 for char in s.lower() if char in vowels)

if __name__ == "__main__":
    print(count_vowels("Hello World"))
    print(count_vowels("Оселедець"))
    print(count_vowels("12345!@#$%"))
    print(count_vowels(""))