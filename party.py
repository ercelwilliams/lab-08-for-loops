userinput = int (input("How long until the party?"))
# usernum = int(userinput)

if userinput < 1:
	print ("PARTY ON!!")
else:
	for i in range(usernum, 0, -1):
		print(i)
		if i == 1:
			print("PARTY TIME!!")
