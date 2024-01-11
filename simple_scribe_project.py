# a tool where users can make and edit txt documents
import os

Valid_chars = [" ","_","-",",",".","*","()","a","b","c","d","e","f","g","h"\
,"i","j","k","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"\
,"1","2","3","4","5","6","7","8","9","0"]

break2 = False

def starting_option():
    global break2
    while True:
        start_select = input("[0] End Session\n[1] Open File\n[2] New File\n\
Select Option: ")
        if start_select == "0":
            print("Session Ended");break2 = True;break
        if start_select == "1":
            open_file();break
        elif start_select == "2":
            new_file();break
        else:
            ("Invalid Input")

def new_file(): # name change
    global file,file_name,break2
    while True:
        valid_entry = True
        file_name = input("\nName Your Document: ")
        if file_name == "0":
            break2 = True;break
        file_name = file_name.replace(".txt","")
        file_name = f"{file_name}.txt"
        if os.path.exists(file_name): # checks if file name in use
            print("File Name Already In Use")
        elif len(file_name) <= 30: # max character limit 30
            for character in file_name:  # checks for invalid characters
                if character.lower() not in Valid_chars:
                    print("Entry Contains Invalid Characters\n")
                    valid_entry = False
                    break # invalid character found, restart loop
            if valid_entry == True:
                file = open(f"{file_name}","a+")
                print(f"'{file_name}' Open\n");ribbon_tab();break
        else:
            print("Entry Too Long\n");break

def open_file():
    global file,file_name,break2
    while True:
        file_name = input("\nEnter File Name: ")
        if file_name == "0":
            print("Session Ended");break2 = True;break
        file_name = file_name.replace(".txt","")
        file_name = f"{file_name}.txt"
        if os.path.exists(file_name):
            file = open(f"{file_name}","a+")
            print(f"'{file_name}' Open")
            file.seek(0)
            print(file.read());ribbon_tab();break
        else:
            print("File Not Found")

session_ended = False
settings_list = [
    "Back",
    "Other Documents",
    "Document Statistics",
    "User Operation",
]
def settings():
    global reset
    while True:
        for i,setting in enumerate(settings_list):
            print(f"[{i}] {setting}")
        setting_input = input("Select Option: ")
        if setting_input == "0":
            reset = True
            break
        elif setting_input == "1":
            pass
        elif setting_input == "2":
            pass
        elif setting_input == "3":
            pass
        else:
            ("Invalid Input")
            
def ribbon_tab():
    line = "-" * 80
    print(f"{line}\n[=-] File\t[=0] Settings\t[+0] Shortcuts\n{line}")

starting_option()
reset = False
while True: # main loop
    if break2 == True:
        break
    if reset == True:
        file.seek(0)
        print(f"\n{file.read()}")
        reset = False
    
    user_write = input("") # backspace
    if user_write == "":
        if file == "":
            continue
        else:
            file.write("\b\b")
            file.seek(0);ribbon_tab()
            print(f"\n{file.read()}")
    elif user_write == "-0": # end session
        file.close()
        print(f"\n{file_name} Closed")
        break
    elif user_write == "=0": # settings
        settings()
    elif user_write == "/0": # delete file
        print(f"\n{file_name} Deleted")
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
        print(f"{file_name} Cleared\n")
        file = open(f"{file_name}","w")
        file.write("")
        file.close()
        file = open(f"{file_name}","a+")
        ribbon_tab()
    else:
        file.write(f"{user_write}\n")