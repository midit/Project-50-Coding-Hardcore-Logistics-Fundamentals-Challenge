import re

def word_frequency_counter(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    text = text.split()

    word_dict = {
    }

    for word in text:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict.update({word:1})

    for word in word_dict:
        print(f"{word} : {word_dict[word]}")

if __name__ == "__main__":
    word_frequency_counter("Apple apple Orange orange orange Banana.")
    print("\n")
    word_frequency_counter("Python is great! Is Python great? Yes, Python is great.")
    print("\n")
    word_frequency_counter("Testing, testing... One, two! One, two, three. Does it work? It should work. WORK, work, work!")