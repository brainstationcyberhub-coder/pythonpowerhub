import requests
import os
def run_webhosting():
    print(r"""  
▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ 
   
██     ██ ██████ █████▄   ██  ██ ▄████▄ ▄█████ ██████ ██ ███  ██  ▄████     
██ ▄█▄ ██ ██▄▄   ██▄▄██   ██████ ██  ██ ▀▀▀▄▄▄   ██   ██ ██ ▀▄██ ██  ▄▄▄    
 ▀██▀██▀  ██▄▄▄▄ ██▄▄█▀   ██  ██ ▀████▀ █████▀   ██   ██ ██   ██  ▀███▀     
                                                                              
▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄                                                                                   
                                                      WELCOME TO USE OUR FREE WEB HOSTING TOOL (β0.1)                                                                                
    """)
    while True:
        print("\n1. Start Web Hosting Tool")
        print("2. Return to Main Menu")
        menu = input("Choose (1/2): ").strip()
        if menu == "1":
            break
        elif menu == "2":
            return
        else:
            print("Invalid choice")
            continue
    x = input("Do you want to host a file? (yes/no): ").strip().lower()
    api = "https://evanxplore.site/api/upload.php"
    while True:
        if x == 'yes':
            file_link = input("Enter the file path to upload: ").strip()
            if not os.path.isfile(file_link):
                print("File does not found. Please try again.")
                continue
            else:
                with open(file_link, 'rb') as f:
                    files = {'file': f}
                    print("Uploading your files...")
                    upload = requests.post(api, files=files)
                    filename = os.path.basename(file_link)
                    print("Your file link:")
                    print("https://evanxplore.site/uploads/" + filename)
            z = input("Do you want to upload more files? (yes/no): ").strip().lower()
            if z == "yes":
                x = "yes"
                continue
            elif z == "no":
                break
            else:
                print("Invalid choice")
                continue
        elif x == 'no':
            break
        else:
            print("Invalid choice")
            x = input("Do you want to host a file? (yes/no): ").strip().lower()
            continue
