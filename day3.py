# returns if given word is a Polindrome

word = input("Enter a polindrome word :")

def is_polindrome(txt):
    result = "".join(char for char in txt if char.isalnum()).lower()
    return result==result[::-1]

print(is_polindrome(word))

