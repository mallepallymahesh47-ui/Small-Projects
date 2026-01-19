import random

# Create an account
def Create_Account():
    Name=input("Enter Your Name : ")
    Acc_No= random.randint(10**11, 10**12 - 1) 
    Pin=int(input("Set 4-digit Pin : "))
    deposite=float(input("Enter Inital desposite : "))

    # Store it in a file
    with open("Bank.txt","a")as f:
        f.write(f"{Name},{Acc_No},{Pin},{deposite}\n")
    print(f"Account Created Successfully....")
   


# Check balance
def Check_balance():
    Acc_No=int(input("Enter Your 12-digit Account Number : "))
    Pin=int(input("Enter 4-digit Pin : "))
    #open bank file
    with open("Bank.txt", 'r') as f:
        found=False
        for line in f:
            data=line.strip().split(',')
            if(data[1]==str(Acc_No)) and (data[2]==str(Pin)):
                print(f"\nAccount Holder : {data[0]}")
                print(f"Current balance : ₹{data[3]}")
                found=True
                break
        if not found:
            print("Account Not Found or Invalid Pin")


# Deposite Amount 
def Deposite():
    Acc_No=int(input("Enter Your Account Number : "))
    Pin=int(input("Enter 4-digit Pin : "))
    Amount=float(input("Enter Deposite Money : ₹"))
    lines=[]
    found=False
    #Open bank File
    with open("Bank.txt", "r") as f:
        lines=f.readlines()

    with open("Bank.txt", "w") as f:
        for line in lines:
            data=line.strip().split(',')
            if (data[1]==str(Acc_No)) and (data[2]==str(Pin)):
                New_amount=float(data[3]) + Amount
                f.write(f"{data[0]},{data[1]},{data[2]},{New_amount}\n")
                print(f"Sucessfully Deposited Amount ₹{Amount}. Current Balance is ₹{New_amount}")
                found=True
            else:
                f.write(line)
    if not found:
        print("Invalid Pin or Account Not Found") 
                

# Withdraw Amount
def Withdraw():
    Acc_No=int(input("Enter Your Account Number : "))
    Pin=int(input("Enter 4-digit Pin : "))
    Amount=float(input("Enter Amount to withdraw : ₹"))
    lines=[]
    found=False
    # Open bank file for validation
    with open("Bank.txt","r") as f:
        lines=f.readlines()
    with open("Bank.txt", "w") as f:
        for line in lines:
            data=line.strip().split(',')
            if (data[1]==str(Acc_No)) and (data[2]==str(Pin)):
                current_balance=float(data[3])
                if(current_balance>=Amount):
                    updated_balance=(current_balance - Amount)
                    f.write(f"{data[0]},{data[1]},{data[2]},{updated_balance}\n")
                    print(f"Withdraw sucessfull of ₹{Amount}. Current Balance is ₹{updated_balance}")
                else:
                    print("Insufficent Balance...!")
                    f.write(line)
                found=True
            else:
                f.write(line) 
    if not found:
        print("Account Not Found or Invalid Pin")
def main():
    while True:
        # Provide Option for user now! 
        print("<===== ACCOUNT MANAGEMENT SYSTEM =====>")
        print("1. Create a new Account")
        print("2. Check Balance")
        print("3. Deposite Amount")
        print("4. Withdraw Amount")    
        print("5. Exit")
        choice=input("Enter Your Choice(1,2,3,4 & 5) : ")

        if (choice=="1"):
            Create_Account()
        elif(choice=="2"):
            Check_balance()
        elif(choice=="3"):
            Deposite()
        elif(choice=="4"):
            Withdraw()
        elif(choice=="5"):
            print("Exit Successful...!")
            break
        else:
            print("Invalid option choose form '1' to '5'")
            break

if __name__=="__main__":
    main()

