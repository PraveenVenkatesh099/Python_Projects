#Print characters present at an even index number

String_input = input("Enter a String: ")
print("Original String is",String_input)
print("Printing only even index chars")
for i in range(0,len(String_input),2):   
    print(String_input[i])
    
    
    