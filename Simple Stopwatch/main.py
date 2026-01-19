import time

# Starts counting time when you say “start”
print("-----Simple Stopwatch-----")
print("Commands : 'start' to being, 'stop' to end and 'exit' to quit")
while True:
    command=input("\n Enter Command : ").lower()
    if (command=="start"):
        start_time=time.time()
        print(f"Stopwatch Started...... Enter 'stop' to stop")

        while True:
            stop_time=input("Command : ")
            end_time=time.time()
            Duration=(end_time - start_time)
            print(f"\nTotal Time is {Duration}sec ({Duration/60}min)")
            break
        
    elif(command=="exit"):
        print("GoodBye......!")
        break
    else:
        print("Invalid Input....Try Again")
