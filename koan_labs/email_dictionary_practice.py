def email_largest(ci):
	coursename,person,email,temp,mails,mail1,comail = [],[],[],[],"",[],{}
	#Separating the strings into 3 
	for i in ci:
		record = i.split(":")
		coursename.append(record[0])
		person.append(record[1])
		email.append(record[2])
		#Initializing a course - email dictionary
		if comail.has_key(record[0]) == False:
			comail[record[0]] = ""
	for course,email in zip(coursename,email):
		emh = email + " "
		comail[course] += emh
		n = len(comail[course])
		temp.append(n)
		if len(comail[course]) == max(temp):
			mails = comail[course]
	mail1 = mails.rstrip(" ")
	t = mail1.split(" ")
	t.sort()
	ans = " ".join(t)
	return ans

email_largest(["CompSci 100:Fred Jack Smith:fjs@duke.edu","History 117:Fred Jack Smith:fjs@duke.edu","CompSci 102:Arielle Marie Johnson:amj@duke.edu","CompSci 100:Arielle Marie Johnson:amj@duke.edu","CompSci 006:Bertha White:bw@duke.edu","Econ 051:Bertha White:bw@duke.edu","English 112:Harry Potter:hp@duke.edu","CompSci 100:Harry Potter:hp@duke.edu"])