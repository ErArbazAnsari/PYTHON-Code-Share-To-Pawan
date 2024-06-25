# Fibonnaci Series
term=int(input("Enter Nth Term : "))
n1,n2=0,1
counter=0
if(term<=0):
    print("Please Enter Positive Values")
else:
    print("Fibonnci Series")
    while(counter<term):
        print(n1)
        nth=n1+n2
        #Updation
        n1=n2
        n2=nth
        counter+=1

