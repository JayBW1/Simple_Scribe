# a tool where users can make and edit txt documents

def name_file(): # name change
    global file,file_name
    while True:
        file_name = input("Name Your Document: ")
        if len(file_name) <= 20:
            if file_name.isalnum():
                file = open(f"{file_name}.txt","a")
                print(f"Document {file_name} Created\n")
                break
            else:
                print("Entry Contains Invalid Characters\n")
        else:
            print("Entry Too Long\n")
            
session_ended = False
            
def entry():
    global session_ended,file
    while True:
        if session_ended == True:
            file.close()
            break
        user_write = input("")
        if user_write == "-0":
            session_ended = True
        elif user_write == "-00":
            # settings
            pass
        elif user_write == "-01":
            # delete file
            print(f"{file_name} Deleted")
            del(file)
            break
        elif user_write.lower() == "-b":
            # bold
            pass
        elif user_write.lower() == "-i":
            # italic
            pass
        elif user_write.lower() == "-u":
            # underline
            pass
        elif user_write.lower() == "-c":
            # clear file
            file_clear = open(f"{file_name}.txt","w")
            file_clear.write("")
            file_clear.close()
        else:
            file.write(f"{user_write}\n")
    
name_file()
entry()