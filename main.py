import os

doExit = False
while not doExit:
    print("What action would you like to do?")
    action = input()
    if action == "help":
        #print all commands
        pass
    elif action == "add":
        #adds today's work
        print("How many kanji?")
        kanji = int(input())
        print("How long did your work in the book take?")
        book = int(input().split(":"))
        print("How long did anki take?")
        anki = int(input().split(":"))
    elif action == "remove":
        #removes a specific day's work. Should ask if you're sure before completing the action.
        print("Which day would you like to remove?")
        removedDay = input() #maybe in date form? could be MM/DD/YYYY?
    elif action == "daily stats":
        #prints today's stats.
        #maybe ask which day specifically the user wants to know about. 
        #"today" should be an input option.
        #needs to read the file and then print the most recent entry.
        pass
    elif action == "all stats":
        #prints all stats averaged out as well as cumulative.
        #needs to read the file, and calculate the average values over all days.
        #average time on anki, book, and total daily time.
        #average time per kanji, divided up into anki, book, and total average spent on card.
        #%of days studied. Starts from the first entry, and then the amount of days that have an entry up until the current day.
        pass
    elif action == "all days":
        #prints all day stats order linearly. Maybe limit it a bit. Like default to 10 days in previously?
        pass
    elif action == "quit":
        doExit = True
    else:
        print("I'm sorry, I didn't get that.")
os.sys("cls")
print("Thanks for using the stats tracker!")