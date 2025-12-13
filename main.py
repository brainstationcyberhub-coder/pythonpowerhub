import qrgen
import webhosting
import cli
import halal
print(r"""                                                            
█████▄ ██  ██ ██████ ██  ██ ▄████▄ ███  ██                  
██▄▄█▀  ▀██▀    ██   ██████ ██  ██ ██ ▀▄██                  
██       ██     ██   ██  ██ ▀████▀ ██   ██                  
                                                                                                                                                                                          
█████▄ ▄████▄ ██     ██ ██████ █████▄  ██  ██ ██  ██ █████▄ 
██▄▄█▀ ██  ██ ██ ▄█▄ ██ ██▄▄   ██▄▄██▄ ██████ ██  ██ ██▄▄██ 
██     ▀████▀  ▀██▀██▀  ██▄▄▄▄ ██   ██ ██  ██ ▀████▀ ██▄▄█▀ 
                                                   WELCOME TO PYTHON POWERHUB (β0.1)""")
while True:
    print("\n=== PYTHON POWERHUB MENU ===")
    print("\t1. CLI CHATBOT")
    print("\t2. HALAL FOOD CHECKER")
    print("\t3. File Hosting Tool ")
    print("\t4. QR Code Generator ")
    print("\t5. Exit")
    choice = input("Choose (1/2/3/4/5): ").strip()
    if choice == "1":
        cli.run_cli_chatbot()
    elif choice == "2":
        halal.run_halal_checker()
    elif choice == "3":
        webhosting.run_webhosting()
    elif choice == "4":
        qrgen.run_qr_generator()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
