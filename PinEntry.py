
for i in range(3):
    text = input("Enter your PIN\n")
    if len(text) == 4 :
        print ("You entered:", text)
        break
    else:
        print ("Invalid PIN. Please entere a 4 digit PIN")
