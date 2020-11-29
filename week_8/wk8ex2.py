# wk8ex2.py
# Opgave 2: lussen
#
# Naam: Sander Kroeze
#

# opgaves String-2
def double_char(str):
    result = ''

    for c in str:
        result += c*2

    return result

def count_hi(str):
	count = 0

	for i in range (len(str)):
		if str[i:i + 2] == 'hi':
			count += 1

	return count

def cat_dog(str):
	cat_count = 0
	dog_count = 0

	for i in range(len(str)):
		if str[i:i + 3] == 'cat':
			cat_count += 1
		if str[i:i + 3] == 'dog':
			dog_count += 1

	return cat_count == dog_count

def count_code(str):
	count = 0
	
	for i in range(len(str)):
		'''if str[i:i+2] == 'co':
			if str[i+3:i+4] == 'e':
				count += 1'''
		if str[i:i+2] == 'co' and str[i+3:i+4] == 'e':
			count += 1

	return count

# Ik weet dat dit geen for loop is, maar dit lijkt mij de korste route, en kan het niet zo 1 2 3 bedenken hoe het met een for of while loop makkelijker zou kunnen
def end_other(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    return s1.endswith(s2) or s2.endswith(s1)

def xyz_there(str):
  for i in range(len(str) - 2):
    if str[i:i + 3] == "xyz" and str[i -1 :i] != ".":
      return True
      
  return False


# opgaves list-2
def count_evens(nums):
	count = 0

	for i in range(len(nums)):
		if nums[i] % 2 == 0:
			count += 1

	return count

def big_diff(nums):
  max_num = nums[0]
  min_num = nums[0]
  
  for i in range( 0, len(nums), 1):
    max_num = max(max_num, nums[i])
    min_num = min(min_num, nums[i])

  return max_num - min_num

def centered_average(nums):
  nums.sort()
  count = 0
  total = 0
  
  for i in range(1, len(nums) - 1):
    count += 1
    total += nums[i]
    
  return total / count

def sum13(nums):
	tot = 0
	i = 0

	while i < len(nums):
		if nums[i] == 13:
			i += 1
		else:
			tot += nums[i]
		i += 1
		
	return tot

def sum67(nums):
	tot = 0
	found = False
	
	for i in range(len(nums)):
		if nums[i] == 6:
			found = True
		if not found:
			tot += nums[i]
		if nums[i] == 7 and found:
			found = False
			
	return tot

def has22(nums):
	for i in range(len(nums) - 1):
		if nums[i] == 2 and nums[i + 1] == 2:
			return True
			
	return False
