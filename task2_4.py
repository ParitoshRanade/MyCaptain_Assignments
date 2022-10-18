"""
Input is a list and output is only the positive numbers is the list
"""
terms = int(input("Enter the number of terms : "))
nos = []
nos_output = []

for i in range(0, terms):
    temp = int(input("Enter the "+str(i+1) + " value : "))
    nos.append(temp)

for value in nos:
    if value > 0:
        nos_output.append(value)

print("The positive numbers in this range are : ", nos_output)
