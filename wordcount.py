#third question
fileopen = open("count.txt", "rt")    #opening file in read mode and text file it is
wordcount={}                          #giving empty dictionary to append values later
for stri in fileopen.read().split():  #taking each word by reading file and performing split operation inside
    if stri in wordcount:
        wordcount[stri]+=1            #if word exists in dict then increment count
    else:
        wordcount[stri]=1             #if word doesnot exists then give count 1 to word
for key in list(wordcount.keys()):    #taking each key from dict
    x=key + ":" + str(wordcount[key]) #storing key and count in temp variable
    print(x)                          #console output of data
    f = open("count.txt", "a+")       #opening the existing file in append mode to write data
    f.write("\n")
    f.write(x)                        #writing the same dat to file

f.close()                             #at the end closing the file