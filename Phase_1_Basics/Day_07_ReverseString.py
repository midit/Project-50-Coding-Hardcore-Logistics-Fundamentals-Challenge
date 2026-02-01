def reverse_string(s):
    s_reversed = []

    for i in range(len(s)-1, -1, -1):
        s_reversed.append(s[i])

    return ''.join(s_reversed)
    

if __name__ == "__main__":
    print(reverse_string("GitHub"))
    print(reverse_string("12345"))
    print(reverse_string("Hello World"))

