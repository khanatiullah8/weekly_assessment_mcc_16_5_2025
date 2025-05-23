# 1: letter combination of a phone number

#digits = "23"
#dialpad = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqr', '8':'stu', '9':'wxyz'}

# ==========================================

# 2: automorphic numbers

#num = 76
#sq_num = num**2

#if str(sq_num).endswith(str(num)):
#	print(True)
#else:
#	print(False)


# ==========================================

# 3: keyboard row words

#kbd = ["qwertyuiop","asdfghjkl","zxcvbnm"]
#words = ["hello","alaska","dad","peace"]
#result = []

#for word in words:
#	for k in kbd:
#		temp = [l for l in word if l in k]
#		if "".join(temp) == word:
#			if word not in result: result.append(word)
#print(result)


# ==========================================

# 4: decode string

#s = "3[a]2[bc]"
#s = "3[a2[c]]"



# ==========================================

# 5: 

nums = [3,2,6,4,1,8]
#nums = [5,3,1]
#nums = [-2,-4,0,2,4]
#nums = [2,4,6,8,10,12]

missing = None

for n in range(len(nums)):
	if nums[n] % 2 == 0:
		if (nums[n] + 2) not in nums:
			missing = nums[n] + 2
			break
		else: 
			missing = nums[n]
		
print(f"missing even numer is {2 if not missing else missing}")






