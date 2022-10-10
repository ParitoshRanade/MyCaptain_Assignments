"""
The task is to print the fibonacci sequence. Input is the number of terms and output is the fibonacci sequence
"""

repeat = int(input("Enter the total numbers : "))

fibonacci_no = [0, 1]
prev_no_2 = 0
prev_no_1 = 1

for i in range(0, repeat - 2):
    current_no = prev_no_1 + prev_no_2
    fibonacci_no.append(current_no)
    prev_no_2 = prev_no_1
    prev_no_1 = current_no

print(fibonacci_no)
