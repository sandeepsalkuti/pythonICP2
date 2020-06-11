#second question


def main():
    str = input("enter the string")#taking input from user
    print(string_alternative(str)) #calling sub function from main function and outputting the result
def string_alternative(str):
    b = ""                        #creating empty string
    for i in range(len(str)):     #for loop to take each character from the input string
        if (i % 2) == 0:          #taking characters located at even places from string using modulus operator
            b += str[i]           #adding character obtained to string
    return b                      #function sending return statement to calling function
if __name__ == '__main__':
    main()                        #calling main functioon