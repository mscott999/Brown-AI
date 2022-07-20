def task1():
    done = False
    while (done == False):
        try:
            hours = float(input("How many hours? "))
            minutes = hours * 60
            print(hours, "hours is equal to", minutes, "minutes.")
            done = True
        except ValueError:
            print("Please enter a valid number of hours.")
            continue

def task2():
    done1 = False
    while (done1 == False):
        timeType = input("Start with minutes or hours? ")
        if (timeType == "minutes"):
            done2 = False
            while (done2 == False):
                try:
                    minutes = float(input("How many minutes? "))
                    hours = minutes / 60
                    print(minutes, "minutes is equal to", hours, "hours.")
                    done1 = True
                    done2 = True
                except ValueError:
                    print("Please enter a valid number of minutes.")
                    continue 
        elif (timeType == "hours"):
            done2 = False
            while (done2 == False):
                try:
                    hours = float(input("How many hours? "))
                    minutes = hours * 60
                    print(hours, "hours is equal to", minutes, "minutes.")
                    done1 = True
                    done2 = True
                except ValueError:
                    print("Please enter a valid number of hours.")
                    continue 
        else:
            print("Please enter either \"minutes\" or \"hours\".")

def task3():
    done = False
    while (done == False):
        word = input("Please type in a word. ")
        numberOfLetters = len(word)
        if (numberOfLetters == 0):
            continue
        print("There are", numberOfLetters, "letters in", word, end=".\n")
        done = True