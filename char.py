text = open("text.txt","r")
word = text.read().split(' ')
print(f'{word}')
# char = input("enter char ")
l= len(word)
print(f'{l}')

alph_list=list()
for x in range(0,l):
	test=list(word[x])
	for x in range(len(test)):
		rearr= test[x]
		number=ord(rearr)
		if number ==123:
			number =97
			print(chr(number))

		elif number==124:
			number=98
		else:
			number +=2
	
		char=chr(number)
		print(f'{test} -------  {char}')

	
	alph_list =alph_list +test



# print(f'{alph_list}')
# for x in range(len(alph_list)):
# 	alph= alph_list[x]
# 	number = ord(alph)
# 	if number ==123:
# 		number =97
# 		print(chr(number))

# 	elif number==124:
# 		number=98
# 	else:		
# 		number +=2
# 	char = chr(number)

# 	print(f'{char}', end='')




# number = ord(char)
# number +=2


# char = chr(number)
# print(f'{char}')