import string
def equity_tracker(transactions):
	From, Ans, To, Acc, Accounts = [], [], [], [], {}
	#Split the list into three lists(parts of transaction)
	for l in transactions:
		record = l.split(":")
		From.append(record[0])
		To.append(record[1])
		Acc.append(record[2])
		#Add users to the dictionary
		for account in record:
			if record.index(account) != 2:
				if Accounts.has_key(account) == False:
					Accounts[account] = 0
	#Carry out the transfers
	for num,pers in zip(Acc,From):
		Accounts[pers] -= float(num)
	for num,pers in zip(Acc,To):
		Accounts[pers] += float(num)
	# Present the data in the format required
	for key,value in Accounts.items():
		m = key,":",str(value)
		m = list(m)
		m = ''.join(m)
		Ans.append(m)
		Ans.sort()
	return Ans

print equity_tracker(["owen:susan:10", "owen:robert:10", "mark:drew:10"])