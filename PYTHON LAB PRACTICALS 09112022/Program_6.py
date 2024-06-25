print("***** PYTHON PROGRAM TO CHECK WHETHER THE GIVEN STRING IS PALINDROME OR NOT *****")

#String Input
string1=input("Enter String --> ")

#String CaseFold For Better Result.
string1=string1.casefold()

#String Reversed For Checking/Comparision String is Palindrome Or Not.
string2=reversed(string1)

#Checking Palindrome Or Not
if(list(string1)==list(string2)):
    print("The string is a palindrome.")
else:
    print("The string not is a palindrome.")
