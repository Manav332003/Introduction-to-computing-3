print("Question3")
list1=[]
list2=[]
s=int(input("enter the number:"))
for i in range(1,s+1):
	list1.append(i)
	list2.append(i**2)
print(list(zip(list1,list2)))
print("End of Question 3")

print("Question 5")
Alphabets=['A','B','C','D','E','F','G','H','I','J','K']
for row in range(0,6):
	column=0
	counter_variable=0
	while column<11:
		if column<row or column>11-row-1:
			print(" ",end="")
			
		else:
			print(Alphabets[counter_variable],end="")
			counter_variable =counter_variable+1
		column =column+1
	print("")
print("End of Question 5")


print("Question 1")
a=input("Enter any String:")
list=a.split()
my_dict={} #Creating an empty dictionary
length=len(list)
if length==1:
        for i in list[0]:
                if i in my_dict:
                        my_dict[i]=my_dict[i]+1
                else:
                        my_dict[i]=1
        print(my_dict)
else:
        for i in list:
                if i in my_dict:
                        my_dict[i]=my_dict[i]+1
                else:
                        my_dict[i]=1
        print(my_dict)
print("End of Question1")	



print("Question 2")
#Taking the inputs from the user
year=int(input("Enter the Year-"))
month=int(input("Enter the Month-"))
date=int(input("Enter the Date-"))

if (year%4==0):
	leap_year=True
else :
	leap_year=False

if month in (1,3,5,7,8,10,12):
	month_length=31
elif month==2:
	if leap_year:
		month_length=29
	else :
		month_length=28
else :
	month_length=30

if (month==12 and date==31):
	n_year=year+1
else :
	n_year=year
if (month==12 and date==31):
	n_date=1
elif (date==month_length):
	n_date=1
else :
	n_date=date
if (date<month_length):
	n_month=month
else :
	n_month=month+1

if (date<month_length):
	n_date=date+1
else :
	n_date=1
if (date!=month_length):
	n_month=month
else:
	n_month=month+1
print(f"Next Day is {n_date}/{n_month}/{n_year}")
print("End of Question 2")
	

print("Question4")
Grade_point=int(input("Enter your Grade_Point:"))
if Grade_point==10:
        print("Your Grade is 'A+' and Outstanding Performance")
elif Grade_point==9:
        print("Your Grade is 'A' and Excellent Performance")
elif Grade_point==8:
        print("Your Grade is 'B+' and Very Good Performance")
elif Grade_point==7:
        print("Your Grade is 'B' and Good Performance")
elif Grade_point==6:
        print("Your Grade is 'C+' and Average Performance")
elif Grade_point==5:
        print("Your Grade is 'C' and Below Average Performance")
elif Grade_point==4:
        print("Your Grade is 'D' and Poor Performance")
else:
	print("Error!")
print("End of Question 4")



print("Question 6")
situation=True
mydict={}
condition="y"
while situation :
	if condition.lower()=="y":
		SID=int(input("Enter the SID of the student:"))
		name=input("Enter the name of the student:")
		mydict[SID]=name
		condition=input("Enter either Y or N:")
		situation=True
	else:
		situation=False
	
print("A)")
for key,value in mydict.items():
	print(f"The SID of {value} is {key}")
print("")

print("B)")
Sort_Values= sorted(mydict.values())
print(f"value sorted dictionary is {Sort_Values}")
print("")

print("C)")
Sort_Keys= sorted(mydict.keys())
print(f"keys sorted dictionary is {Sort_Keys}" )
print("")

print("D)")
SID_tbk=int(input("Enter the SID of the student:"))
if SID_tbk in mydict.keys() :
	print(f"The name of student with {SID_tbk} is {mydict[SID_tbk]}")
else :
	print("The student SID is not present in the mydict")
print("End of Question 6")


print("Question 7")
num=int(input("Enter any number:"))
n1,n2=0,1
sum=0
if num<=0:
	print('please enter a number greater than 0')
else:
	for i in range (0,num):
		print(sum, end=" ")
		n1=n2
		n2=sum
		sum=n1+n2
print()
#Averge of Fibonnaci Series=sum/num
Average=sum/num
print(f"Average of total{num} terms of sequence is {Average}")
print("End of question 7")


print("Question 8")
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}
#Symmetric Difference of Set1 and Set2
print("A)",end=" ")
Set_notboth=Set1^Set2
print(f"Set with no elements common in both sets is {Set_notboth}")


#Symmetric Difference of Set1,Set2,Set3
print("B)",end=" ")
Set_onlyinone=Set1^Set2^Set3
print(f"Set with the elements in only one is {Set_onlyinone}")


#Set with elements common in only two sets
print("C)",end=" ")
Set_onlyintwo=(Set1|Set2|Set2)-(Set1^Set2^Set2)-(Set1&Set2&Set3)
print(f"Set with elements in only two sets is {Set_onlyintwo}")


#Finding elements not common in Set1 and range from 1 to 10
print("D)",end=" ")  
set_1=set()
for i in range(1,11):
	set_1.add(i)
set_notcommon=set_1-Set1
print(f"Set not common in Set1 and range 1 to 10 is {set_notcommon}")


#Set of integers from 1 to 10 and not in Set1,Set2,Set3
print("E)",end=" ")
set_2=set()
for i in range(1,11):
	set_2.add(i)
set_notcommon_2=set_2-(Set1|Set2|Set3)
print(f"Set not common in set_2 and other three sets is {set_notcommon_2}")
print("End of Question 8")


 
                             
