#Print the Sum of a Current Number and a Previous number

previous_num = 0

for i in range(1,11):
    sum_value = previous_num + i
    print("Current Number",i,"Previous number",previous_num,"Sum:",sum_value)
    previous_num = i
    