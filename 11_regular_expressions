# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers. 

import re

hand = open('actual_data_test.txt')

sum = 0
for line in hand:
    numbers = re.findall('[0-9]+', line)
    #print(numbers)
    for n in numbers:
        sum += int(n)
print(sum)

######################
# with comprehension #
######################
fname = open('reg_test.txt')
hand = fname.read()
line = re.findall("[0-9]+", hand)
nums = [int(i) for i in line]
sum = 0
for k in nums:
	sum += k
print(sum)

