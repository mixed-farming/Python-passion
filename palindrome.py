str = input('Enter a word : ')
j = -1
flag = 0
for i in str:
	if i != str[j]:
		flag = 1
		break
	j = j - 1

if flag == 1:
	print("NO...",str,"is not a palindrome.")
else:
	print("Yes...",str,"is a palindrome.")
