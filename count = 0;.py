count = 0  
count_symvols=0   
#Opens a file in read mode  
file = open("data.txt", "r")  
      
#Gets each line till end of file is reached  
for line in file:  
    #Splits each line into words  
    temp=line.replace(".","").replace(",","").replace(" - ","")
    words = temp.split() 
    #Counts each word  
    count =  len(words) 
    line_symvols="".join(line.split())
    count_symvols=len(line_symvols)
    print(line)
    print("Amount of words:",count)
    print("Amount of symbols:",count_symvols)
    print()
file.close()
