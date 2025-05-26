#Remove first n characters from a string
def remove_chars(word, n):
    if n>len(word):
        return "out of range"
    else:
        return word[n:]

string = input("Enter a word: ")
num = int(input("Enter a number: "))
print(remove_chars(string,num))