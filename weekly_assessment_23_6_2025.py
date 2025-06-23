# 1. power of four

def power_of_four(n):
	return n > 0 and (n & (n-1)) == 0 and ((n-1) % 3) == 0 

print(power_of_four(16))
print(power_of_four(5))

# =======================================================

# 2. unique morse code words

#morse_code = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..'}

#input = ['gin', 'zen', 'gig', 'msg']

#def unique_morse_code(lst):
#	result = {}
#	for i in lst:
#		temp = ''
#		for j in i:
#			temp += morse_code[j]
#		result[temp] = result.setdefault(temp, 0) + 1
#	return len(result)

#print(unique_morse_code(input))

# =======================================================

# 3. replace elements with greatest element on right side

#def my_func(lst):
#	last_elem = -1
#	list_len = len(lst)-1
	
#	for i in range(list_len, -1, -1):
#		curr_elem = lst[i]
#		lst[i] = last_elem
#		if curr_elem > last_elem:
#			last_elem = curr_elem
#	return lst

#print(my_func([17,18,5,4,6,1]))
#print(my_func([400]))

# =======================================================

# 4. permutation in string

#from itertools import permutations

#def my_func(s1, s2):
#	perm_lst = [''.join(x) for x in permutations(s1)]
#	output = False

#	for i in perm_lst:
#		if i in s2:
#			output = True
#			break
#	return output 

#print(my_func('ab', 'eidbaooo'))
#print(my_func('ab', 'eidboaoo'))

# =======================================================

# 5. count trailing zeros in factorial

#def factorial(n):
#	if n == 1:
#		return 1
#	return n * factorial(n-1)

#def count_trailing_zero(num):
#	count = 0
#	fac = str(factorial(num))

#	for i in range(len(fac)-1, -1, -1):
#		if fac[i] != '0':
#			break
#		count += 1
#	return count

#print(count_trailing_zero(5))
#print(count_trailing_zero(100))
