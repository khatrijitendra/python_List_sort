integer_list = [] #define empty integer_list
string_list = []  #define empty string_list
for index in range(3): #use for loop and initialize a variable as "index" and define its range 
	index = input("enter integer element of list = ") #get "integer" value from user as input 
        integer_list.append(index) #append list with user input
        index = index + 1 #incerase index
for index1 in range(3): #use for loop and initialize a variable as "index1" and define its range
	index1 = raw_input("enter string element of list = ")#get "string" value from user as input
	string_list.append(index1) #append list with user input
	index = index + 1 #incerase index1
integer_list.extend(string_list) #extend integer_list with string_list
integer_list.sort() #use inbuilt sort function and sort extended integer_list
print integer_list # print sorted integer_list

