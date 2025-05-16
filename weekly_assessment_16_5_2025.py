# 1. the time in words

time_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve'}

nums = [n for n in range(1, 13)]

h = 5; m = 39

def check_current_h(num):
	idx = nums.index(num)+1
	return idx+1 if idx < len(nums) else 1

if m == 0:
	print(f"{time_dict[h]} o'clock")
elif m == 15:
	print(f"quarter past {time_dict[h]}")
elif m == 30:
	print(f"half past {time_dict[h]}")
elif m == 45:
	print(f"quarter to {time_dict[check_current_h(h)]}")
elif m % 5 == 0 and m < 30:
	print(f'{m} past {time_dict[h]}')
elif m % 5 != 0 and m < 30:
	print(f"{m} minute{'s' if m > 1 else ''} past {time_dict[h]}")
elif m % 5 == 0 and m > 30:
	print(f'{60-m} to {time_dict[check_current_h(h)]}')
elif m % 5 != 0 and m > 30:
	print(f"{60-m} minute{'s' if m > 1 else ''} to {time_dict[check_current_h(h)]}")


# ========================================================

# 2. count the number of pairs in an array whose sum is divisible by K

#arr = [1,2,3,4,5,6]; k = 5
#arr = [2,2,1,7,5,3]; k = 4
#count = 0

#for i in range(len(arr)):
#	for j in range(i+1,len(arr)):
#		if (arr[i] + arr[j]) % k == 0:
#			count += 1

#print("output ->", count) 

# ========================================================

# 3. sort by frequency

#arr = [4,4,1,2,2,2,3]
#freq_dict = {}

#for i in arr:
#	freq_dict.setdefault(i, []).append(i)

#sorted_freq = sorted(freq_dict.values(), key=len, reverse=True)
#result = sum(sorted_freq, [])
#print(result)

# ========================================================

# 4. staircase

#n = 6

#for i in range(1, n+1):
#	print(f"{' '*(n-i)}{'#'*i}")

# ========================================================

# 5. climbing stairs

#n = 3
