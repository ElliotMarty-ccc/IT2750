#importing what i need. random for random nums, string for constants(https://docs.python.org/2/library/string.html#string-constants)
#os and Path for writing files, datetime for getting date and time
import random, string, os, datetime
from pathlib import Path

#generation. saves lines
def generation(length):
    print('----------------------------------------------------')
    print('Generating password...')
    print('----------------------------------------------------')
    print("Your new password is: " + str(passCreation(pwLength)))
    print('====================================================')

#where the actual password generation happens. takes the characters you/it decided and mixes them up in the acceptable length.
def passCreation(length):
    global newPassword
    newPassword = ""
    while len(newPassword) < length:
        newPassword = newPassword + random.choice(chars)
    
    return newPassword

#more info command for the generator
def moreInfoGen():
    print("Choosing 1(the custom password option) will let you choose the length, and whether to use uppercase letters, lower case letters, numbers, and symbols, respectively.\nChoosing 0(the preset option) will generate a password that is anywhere from 10 characters long to 16 long. It will also include upper and lowercase letters, numbers, and symbols. ")

#more info command for the absolute path stuff with the file saving
def moreInfoPath():
    print("To get the absolute path, navigate to the folder you want to save the password list in, and click the file path and copy it.")

#oooooo fancy
print('====================================================')
print('====== OnePass Password Generator and Storage ======')
print('====================================================')

#ask whether they want to make their own or have it generate a secure one
customOrPreset = input("Wold you like to customize the password, or do you want to generate a secure password? Type '1' for custom or '0' for preset.\nIf you need more information, simply type help.\n      >>>")

for char in customOrPreset:#this for loop checks for punctuation in the text area. breaks if it does.
    if char in string.punctuation:
        print("That's not the right command. The correct format is 'help'.")
        break
if str.isalpha(customOrPreset):#checks if it's all letters, which would be the help command.
    if customOrPreset == "help":
        moreInfoGen()
    else:
        print("That wasn't the right command. The correct format is 'help'.")

if str.isnumeric(customOrPreset):#checks if it's numbers, which is what we want.
    if int(customOrPreset):#custom generation. asks whether or not the user wants to use each of those options.
        chars = ""
        newPassword = ""

        pwLength = int(input('How long would you like the new password to be?\n        >>> '))
        useUpper = bool(int(input('Would you like to use uppercase letters? 1 = Yes, 0 = No\n       >>> ')))
        useLower = bool(int(input('Would you like to use lowercase letters? 1 = Yes, 0 = No\n       >>> ')))
        useNumbers = bool(int(input('Would you like to use numbers? 1 = Yes, 0 = No\n       >>> ')))
        useSymbols = bool(int(input('Would you like to use symbols? 1 = Yes, 0 = No\n       >>> ')))
    
        if useUpper:
            chars = chars + string.ascii_uppercase
        if useLower:
            chars = chars + string.ascii_lowercase
        if useNumbers:
            chars = chars + string.digits
        if useSymbols:
            chars = chars + string.punctuation
    
        generation(pwLength)

    elif int(customOrPreset) == 0:#preset password. basically says yes to all the options above and chooses a length between 10 and 16.
        newPassword = ""
        pwLength = random.randrange(10,16)
        chars = string.ascii_letters + string.digits + string.punctuation
        
        generation(pwLength)
    
    else:
        print("That's not the correct format. You need to choose either 1 or 0.")

reasonForPw = str(input("Add a description to the password to remember what it's for.\n     >>>"))#Description for password      
chooseToSave = bool(int(input("Would you like to save your new password to a text file? 1 = Yes, 0 = No\n        >>>")))#would you like to save it in a text file.?
if chooseToSave:
    filename = input("What would you like the new file to be called? Input the name of your current password list if you already have one created.\n      >>>")#asks for file name
    whichDir = bool(int(input("Would you like to save it to your current directory, or would you like to choose a different directory? 1 = Current Directory, 0 = Different Directory\n     >>>")))#asks whether you want it in the cwd or a different one
    if whichDir:
        dirToSave = os.getcwd()#if you chose the current, gets the cwd and uses it
    elif not whichDir:
        dirToSave = str(input("What is the directory you would to save to? Make sure it's the absolute path. Type help if you need help\n       >>>"))#if you chose to use a different one, it asks you for it
        dirToSave = Path(dirToSave)
        if dirToSave == 'help':
            moreInfoPath()#displays help if you dont know where to get the absolute path
        while dirToSave.is_absolute() == False:#tells you if the path isnt absolute
            moreInfoPath()
            dirToSave = str(input("What is the directory you would to save to? Make sure it's the absolute path.\n       >>>"))
            dirToSave = Path(dirToSave)

e = datetime.datetime.now()
dateAndTime = str(e.strftime("%m-%d-%Y %H:%M:%S"))#get the current date and time in military time to save to the text file

passDict = {}#creates a dictionary since it's neater and also using normal strings was annoying
passDict.update({"Password":newPassword})
passDict.update({"Date Added":dateAndTime})
passDict.update({"Purpose":reasonForPw})

if os.path.exists(dirToSave):#checks if a password list with the same name exists in the same directory
    appendOrWrite = 'a' # append if already exists
else:
    appendOrWrite = 'w' # make a new file if not
passFile = open(os.path.join(dirToSave, str(filename) + '.txt'), appendOrWrite)#if the file doesnt exist, it creates a new one. if it does, it appends to the existing one.
passFile.write(str(passDict) + "\n")#writes the dictionary in the text file, and creates a new line after
print(f"The new password: {newPassword} has been written to the newly created text file named: {filename}")#displays results when you are finished
passFile.close()
        






































































































































































































