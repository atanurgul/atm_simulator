import time
print("Welcome to AtaBank","\nAtaBank created by Atanur in 2034",
      "\nWe are here for your safety and security. We will do our best to make you feel safe.")


while True:
    name = input("Your name please : ").lower().capitalize()
    if name.isalpha():
        print(f"\nWelcome {name}.\n")
        
        break
    
    else:
        print("\nPlease enter a valid name.\n")
    

password = []


print(f"\nNow we can create your account {name}\n")

while True:
    password = input("Can you enter new password ? : ")
    
    if len(password) ==4 and password.isdigit():
        print("\nPassword created\n")
        break
    else:
        print("\nPassword must be at four characters and must be from numbers! ! ! \n")
        continue
print(("------------------------"),("\t\nLOGİN\n"),
      ("------------------------"))



def login():
    name_try = 3
    while True:
        username = input("Name : ").lower().capitalize()
        if username.isalpha() and username==name:
            print(f"{username} welcome back!\n")
            return True
        else:
            print("Try again be careful !!!")
            name_try -= 1
            print(name_try)
            if name_try==0:
                print("You have tried too many times, so now the system is closed until tomorrow morning.")
                exit()

login()

def login2():
    password_try = 3
    while True:
        userpassword = input("Password :")
        if userpassword.isdigit() and userpassword==password:
            return True
        else:
            print("Try again be careful !!!")
            password_try -= 1
            print(password_try)
            if password_try==0:
                print("Your acoount blocked.")
                exit()
login2()
balance = 0
while True:
    print("**********************************************")
    print("\n1.Balance inquiry\n",
        "\n2.Withdraw money\n",
        "\n3.Deposit money\n",
        "\n4.Remittance\n",
        "\n0.Exit\n")
    print("**********************************************")

    select = input("Type of a number : ")
    

    if select.isnumeric() and select == "1":
        print("Balance Inquiry...")
        print(f"Balance = ${balance}")
        
        rselect = input("\n'r' to return to the menu or press 'q' to exit : ").lower()
        
        if rselect== "q":
                print("Exiting......")
                time.sleep(3)
                print("Exited.")
                exit()
            
        elif rselect=="r":
                print("Exiting ......")
                time.sleep(3)
                continue
            
        else:
                time.sleep(3)
                print("Error !!!")
                exit()
    
    elif select.isnumeric() and select == "2" :
        print("Withdraw money...")
        print(f"Balance = ${balance}")
        
        withdrawamount = int(input("Enter amount you want to withdraw : "))
        
        if withdrawamount > 0 :
            balance+= withdrawamount
            print(f"Your new balance is {balance}")

        
        else:
            print("Error !!!")
            time.sleep(3)
            gselect = input("\n'r' to return to the menu or press 'q' to exit : ").lower()
            if gselect== "q":
                print("Exiting......")
                time.sleep(3)
                print("Exited.")
                exit()
            
            elif gselect=="r":
                print("Exiting ......")
                time.sleep(3)
                continue
            
            else:
                time.sleep(3)
                print("Error !!!")
                exit()

    elif select.isnumeric() and select == "3" :
        print("Deposit money...")
        print(f"Balance = ${balance}")
        
        depositamount = int(input("Enter amount you want to deposit : "))
        
        if balance >= depositamount :
            balance-= depositamount
            print(f"Your new balance is {balance}")
            aselect =input("\n'r' to return to the menu or press 'q' to exit : ").lower()
            
            if aselect== "q":
                print("Exiting......")
                time.sleep(3)
                print("Exited.")
                exit()
            
            elif aselect=="r":
                print("Exiting ......")
                time.sleep(3)
                continue
            
            else:
                time.sleep(3)
                print("Error !!!")
                exit()
        
        else:
            print("You cant !!!")
            time.sleep(3)
            continue
            

    elif select.isnumeric() and select == "4" :
        print("Remittance...")
        print(f"Balance = ${balance}")
        
        remittance_n = input("Name : ").lower().capitalize()
        time.sleep(2)
        
        remittance_s = input("Surname : ").upper().capitalize()
        time.sleep(2)
        
        remittance_a = input("Account No : ")
        time.sleep(2)
        
        remittance_b = int(input("Balance : "))
        
        if remittance_b<=balance:
            balance -= remittance_b
           
            print("Being send ...")
            time.sleep(5)
           
            print("transaction successful.\n")
            print("***************************************************************************************************")
           
            print(f"\n${remittance_b} were transferred from your account to the account of {remittance_s} {remittance_n} number {remittance_a}\n")
            time.sleep(3)
           
            print(f"Your new balance is {balance}.")
           
            eselect = input("\n'r' to return to the menu or press 'q' to exit : ").lower()
           
            if eselect == "r":
                time.sleep(3)
                continue
            
            elif eselect=="q":
                print("Exiting.....")
                time.sleep(3)
                print("Exited.")
                exit()
            else:
                print("Error !!!")
                quit()
    else:
        print("Type of a number !!!")
   


