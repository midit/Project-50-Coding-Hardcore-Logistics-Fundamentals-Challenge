def polindrome(s):
    s_clean = s.lower()
    s_clean = s_clean.replace(" ", "")
    
    i = 0
    j = len(s_clean)-1

    while i < j:
        if s_clean[i] != s_clean[j]:
            return (f"Sequence '{s}' is not a polindrome.") 

        i += 1
        j -= 1
            
    return (f"Sequence '{s}' is a polindrome.")
    

if __name__ == "__main__":
    print(polindrome("Anna"))
    print(polindrome("A man a plan a canal Panama"))
    print(polindrome("orange"))