# 2) Most Frequent K Elements in List

from collections import Counter

#def frequent_elements(nums, k):
#	freq = Counter(nums)
#	result = sorted(freq.items(), key=lambda x: x[1], reverse=True)
#	return list(dict(result[:k]).keys())

#print(frequent_elements([4,4,4,6,6,7,8],2))


# 3) Add Minimum Brackets to Balance String

#def my_func(expr):
#	while '()' in expr:
#		expr = expr.replace('()', '')	
#	print(len(expr))
	
#my_func("(()")
#my_func(")))")
#my_func("(()())")


# 4) First Pattern: Pascal's Triangle (First 5 Rows)

def pascal_triangle(n):
	for i in range(1, n+1):
		for j in range(i):
			if j==0 or j==n:
				print(j+1)

pascal_triangle(5)


# 5) Second Pattern: Increasing Number Triangle

#def my_func(n):
#	s = ''
#	for i in range(1, n+1):
#		s = f'{s}{str(i)} '
#		print(s)

#my_func(5)