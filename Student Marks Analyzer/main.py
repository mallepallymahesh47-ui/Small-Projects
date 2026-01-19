

# Grade Systaem
'''90 - 100 (A+)
   80 - 90 (A)
   70 - 80 (B)
   60 - 70 (C)
   below 50 (F)
'''
def Grade_system(Avg):
    if (100>=Avg>=90):
        return "A+"
    elif (90>=Avg>=80):
        return "A"
    elif (80>=Avg>=70):
        return "B"
    elif (70>=Avg>=60):
        return "C"
    else:
        return "F"

# Takes marks of a student in 5 subjects
def add_student_record():
    name=input("Enter Your Name : ")
    marks=[]
    for i in range(1,6):
        try:
            stu=int(input(f"Enter Your Subject {i} Marks : " ))
            marks.append(stu)
        except ValueError as V:
            print(V)

    # Calculates total marks, average, and grade(A/B/C/F)
    Total=sum(marks)
    Avg=(Total/5)
    Grade=Grade_system(Avg)
    
    # Display Result
    Data=f"\n ------Student Report------\n Name : {name}\n Marks Scored : {Total}\n Average Markes : {Avg}\n {name} Secured a Grade of {Grade}"
    print(Data)
    
    # Stores results in a file (like text or CSV)
    with open("Student_Marks.txt","a") as f:
        f.write(Data)

# View all stored results
def View_all_records():
    try:
        with open("Student_Marks.txt", "r") as f:
            print(f.read())
    except FileNotFoundError as F:
        print(F)

# Add options
def main():
    while True:
        print("\n ------Student Report Analyzer------")
        print("1. View All Records")
        print("2. Add New Student Record")
        print("3. Exit")

        choice=input("Enter Your Choice (1,2,3) : ")
        if (choice=="1"):
            View_all_records()
        elif(choice=="2"):
            add_student_record()
        elif(choice=="3"):
            print("Exiting...!")
            break
        else:
            print("Invalid choice.. Try Again")

if __name__=="__main__":
    main()










