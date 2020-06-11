
#first question

a = int(input("enter number of students"))     #taking input from user about number of  and converting to integer value
output1=[int(input("enter numbers for conversion")) for ls in range(0,a)]   #applying list comprehension technique here
                                                                       #like looping through each value from user
output= [out*0.453592 for out in output1]       # converting each value by multiplying with 0.453592 where 1lb=0.453592kgs
print("converted numebrs are",output)            #showing converted numbers to user





