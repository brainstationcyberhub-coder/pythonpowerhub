import qrcode
import os
def run_qr_generator():
    print(r"""                                      
▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄    
                                               
▄█████▄ █████▄     ▄████  ██████ ███  ██       
██ ▄ ██ ██▄▄██▄   ██  ▄▄▄ ██▄▄   ██ ▀▄██       
▀█████▀ ██   ██    ▀███▀  ██▄▄▄▄ ██   ██       
     ▀▀                                        
▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄    
                                Welcome to our Qr Gen tool v1.0                                                                                                           
    """)
    while True:
        print("\n1. Start QR Generator")
        print("2. Return to Main Menu")
        menu = input("Choose (1/2): ").strip()
        if menu == "1":
            break
        elif menu == "2":
            return
        else:
            print("Invalid choice")
            continue
    while True:
        x = input("Do you want to create a qr code? (yes/no) : ").strip().lower()
        if x == "yes":
            name = input("Write the folder name where you want to save your qrcode : ").strip()
            folder_path = name
            if not os.path.isdir(folder_path):
                os.mkdir(folder_path)
                print("Folder Created")
            info = input("Enter the text or url for the qr : ").strip()
            if info == "":
                print("You must type something to create a qr code")
                continue
            qr_name = input("Input the qr file name (without png or any extension): ").strip()
            if qr_name == "":
                print("You must input qr name.")
                continue
            if "." in qr_name:
                print("Type name without any dot or extension.")
                continue
            directory = os.path.join(folder_path, qr_name + ".png")
            img = qrcode.make(info)
            img.save(directory)
            print("QR code made Successfully")
            print("Can be found at :", directory)
            z = input("Do you want to create another one? (yes/no) : ").strip().lower()
            if z == "yes":
                continue
            elif z == "no":
                break
            else:
                print("Invalid choice")
                continue
        elif x == "no":
            break
        else:
            print("Invalid Choice")
            continue
