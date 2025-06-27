# 1. 

#nested_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3, 'f': 4}}}

#for key,val in nested_dict.items():
#	if type(val).__name__ == 'dict':
#		print(key, val)


# =======================================================

# 2. given a alphanumeric string s, extract maximum numeric value from s

import re

s = "100klh564abc365bg"

print('maximum numeric value ->', max(re.split(r'\D', s)))

# =======================================================

# 3. check if there exists a pair in array whose sum is x

#def my_func(arr, x):
#	for i in range(len(arr)):
#		for j in range(i+1, len(arr)):
#			if arr[i] + arr[j] == x:
#				return True
#	return False

#print(my_func([1,4,45,6,10,8], 16))

# =======================================================

# 4. 

#def my_func(arr):
#	total_goods = sum(arr)
#	distributed_goods = 0

#	for i in range(1, len(arr)+1):
#		distributed_goods += i

#	return total_goods == distributed_goods

#print(my_func([7,4,1,1,2]))

# =======================================================

# 5. count substring with exactly k distinct characters

#from collections import Counter

#def count_substring(s, k):
#	distinct_s = set()
#	output = []

#	for i in range(len(s)):
#		temp = s[i]
#		for j in range(i+1, len(s)):	
#			temp += s[j]
#			distinct_s.add(temp)

#	for x in distinct_s:
#		freq = Counter(x)
#		if len(freq) == k:
#			output.append(x)

#	return len(output)

#print(count_substring('abcba', 2))
#print(count_substring('aabab', 3))
#print(count_substring('pqpqs', 2))





