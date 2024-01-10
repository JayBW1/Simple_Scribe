# a tool where users can make and edit txt documents
import os

Valid_chars = [" ","_","-",",",".","*","()","a","b","c","d","e","f","g","h"\
,"i","j","k","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"\
,"1","2","3","4","5","6","7","8","9","0"]

def starting_option():
    while True:
        start_select = input("[1] Open File\n[2] New File\nSelect Option: ")
        if start_select == "1":
            open_file()
            break
        elif start_select == "2":
            new_file()
            break
        else:
            ("Invalid Input")

def new_file(): # name change
    global file,file_name
    while True:
        valid_entry = True
        file_name = input("Name Your Document: ")
        file_name = file_name.replace(".txt","")
        file_name = f"{file_name}.txt"
        if os.path.exists(file_name): # checks if file name in use
            print("File Name Already In Use\n")
        elif len(file_name) <= 30: # max character limit 30
            for character in file_name:  # checks for invalid characters
                if character.lower() not in Valid_chars:
                    print("Entry Contains Invalid Characters\n")
                    valid_entry = False
                    break # invalid character found, restart loop
            if valid_entry == True:
                file = open(f"{file_name}","a")
                print(f"'{file_name}' Open\n")
                break
        else:
            print("Entry Too Long\n")
            break

def open_file():
    global file,file_name
    while True:
        file_name = input("\nEnter File Name: ")
        if file_name == "0":
            print("\n")
            break
        if os.path.exists(file_name):
            file = open(f"{file_name}","a")
            print(f"'{file_name}' Open\n")
            break
        else:
            print("File Not Found")

session_ended = False
settings_list = [
    "Other Documents",
    "Document Statistics",
    "User Operation",
]
def settings():
    for i,setting in enumerate(settings_list):
        print(f"[{i}] {setting}")

starting_option()
            
while True: # main loop
    user_write = input("")
    if user_write == "-0": # end session
        file.close()
        break
    elif user_write == "-00": # settings
        settings()
    elif user_write == "-01": # delete file
        print(f"{file_name} Deleted")
        file.close()
        os.remove(file_name)
        break
    elif user_write.lower() == "-b": # bold
        pass
    elif user_write.lower() == "-i": # italic
        pass
    elif user_write.lower() == "-u": # underline
        pass
    elif user_write.lower() == "-c": # clear file
        file = open(f"{file}","w")
        file.write("")
        file.close()
        file = open(f"{file}","a")
    else:
        file.write(f"{user_write}\n")