def infoWrite(newfile, count):
    continuewriting = True
    parenthesis = ".) "
    starspace = "  *  "
    ending = ";"
    print 'we will now start recording'
    while continuewriting == True:
        username = raw_input('username: ')
        password = raw_input('password: ')
        info = raw_input('account type: ')
        writeString = str(count) + parenthesis + 'Username: ' + username + starspace + 'Password: ' + password + starspace + 'Info: ' + info + ending
        newfile.write(writeString)
        newfile.write("\n")
        count+=1
        while True :
            print 'done storing? yes / no: '
            decision = raw_input()
            if decision == "yes":
                continuewriting=False
                print 'alright! we will now be returning to the main menu!'
                break
            elif decision == "no":
                continuewriting=True
                break
            else:
                print 'you have entered an invalid option! please try again' 


def createEntry():
    print 'welcome to the entry creation function'
    print 'please enter the name of the item for which you would like to archive'
    filename=raw_input('enter here: ')
    filenameEX=filename+".txt"
    newfile = open(filenameEX, 'w')
    listfile = open("list archive.txt", 'a')
    filelisting = "*- + -* " + filename + ";"
    listfile.write(filelisting)
    listfile.write("\n")
    count=1
    print 'this file has now been archived.'
    listfile.close()
    infoWrite(newfile,count)
    newfile.close()

def viewList():
    listfile=open("list archive.txt")
    print 'now displaying archive!'
    print listfile.read()
    while True:
        decision=raw_input('enter "quit" to quit: ')
        if decision == "quit":
            break
        else:
            print 'you have enter an invalid option! try again!'


def entryUpdateAdd(filenameEX):
    print 'you can now add to the entry!'
    updatefileAppend = open(filenameEX, 'a')
    updatefileRead = open(filenameEX, 'r')
    strfile = updatefileRead.read()
    accountlistings = strfile.splitlines()
    currentcount= len(accountlistings) + 1
    infoWrite(updatefileAppend, currentcount)
    updatefileAppend.close()
    updatefileRead.close()





def entryUpdateChange(filenameEX):
    print 'you are now in the change phase!'
    updatefile = open(filenameEX, 'r')
    strfile = updatefile.read()
    accountlist = strfile.splitlines()
    Terminator = False
    while Terminator == False:
        accountListIndex = input('please enter the number you would like to update: ')
        lineChange = accountlist[accountListIndex].split('*')
        firstPart = lineChange[0]
        newPassword = raw_input('enter the new password: ')
        endingPart = lineChange[2]
        updatefileWrite = open(filenameEX, 'w')
        accountlist[accountListIndex] = firstPart + 'password: '+ newPassword + 'info: ' + endingPart 
        for item in accountlist:
            updatefileWrite.write("%s\n" % item)
        print 'this is the updated version!'
        print updatefile.read()
        decision = raw_input('update another user? (yes / no): ')
        while True:
            if decision == "yes":
                print 'alright! lets continue!'
            elif decision == "no":
                print 'alright, we are now returning to the main menu!'
                Terminator = True
                break
            else:
                print 'the option that you have entered is not valid! TRY AGAIN!'
    updatefile.close()

    
    




def entryUpdate(filenameEX):
    print 'welcome to the entry update function!'
    print 'would you like to add to the entry or change something about the entry'
    while True:   
        decision=raw_input('add/change: ')
        if decision=="add":
            entryUpdateAdd(filenameEX)
            break
        elif decision=="change":
            entryUpdateChange(filenameEX)
            break
        else:
            print 'the value you have enter is invalid! try again!'


    

def viewEntry():
    print 'welcome to the entry viewing function'
    filename = raw_input('please enter the name of the entry: ')
    filenameEX = filename + ".txt"
    viewingfile= open(filenameEX)
    print 'now displaying information'
    print viewingfile.read()
    print 'would you like to update this entry or go back to the main menu'
    while True:
        decision = raw_input('update/main: ')
        if decision == "update":
            viewingfile.close()
            entryUpdate(filenameEX)
            break
        elif decision == "main":
            viewingfile.close()
            print 'now returning to the main menu'
            break
        else:
            print 'the option you have entered is not valid! try again!'
            
    



#this is the prototype for the password storage program
print 'welcome to the password storage program ver. 1.0'
print 'At the moment, you can quit the program by either clicking the X or typing quit at main menu only'
terminator = False

while terminator == False:
    print 'you have the following options from which you can chooose from:'
    print '1) create a new entry       (type create)'
    print '2) view/update an entry     (type view)'
    print '3) view archive list        (type list)'
    print 'type "quit" to quit'
    decision = raw_input('enter option: ')

    if decision == "create":
        createEntry()
    elif decision == "view":
        viewEntry()
    elif decision == "list":
        viewList()
    elif decision=="quit":
        terminator = True
    else:
        print 'the option you have entered is not valid'
print 'thanks for using the program, BAI!'