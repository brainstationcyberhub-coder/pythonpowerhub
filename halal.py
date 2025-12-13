def run_halal_checker():
    print(r"""
▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄          
                                                                                                
██  ██ ▄████▄ ██     ▄████▄ ██       ▄█████ ██  ██ ██████ ▄█████ ██ ▄█▀ ██████ █████▄            
██████ ██▄▄██ ██     ██▄▄██ ██       ██     ██████ ██▄▄   ██     ████   ██▄▄   ██▄▄██▄           
██  ██ ██  ██ ██████ ██  ██ ██████   ▀█████ ██  ██ ██▄▄▄▄ ▀█████ ██ ▀█▄ ██▄▄▄▄ ██   ██           
                                                                                                                                                                                                
▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄          
                                                          WELCOME TO HALAL BARCODE CHECKER v0.1
    """)

    while True:
        print("\n1. Start Halal Checker")
        print("2. Return to Main Menu")
        menu = input("Choose (1/2): ").strip()

        if menu == "1":
            break
        elif menu == "2":
            return
        else:
            print("Invalid choice")
            continue
    name = input("Type your name: ").strip().title()
    while True:
        halal = input(f"Hello {name}, Type the barcode number: ").strip()
        halal_barcodes = ["4829157304821","5903748291047","7291836450293","8801947356204","6932847591036","8693014759280","9554837201946","8882045736192","6229483756201","7452038691049","5302847561923","7892034756190","9472038561042","8041926735019","6920475319284","8992037465128","7503948201673","9128475630912","6419283756021","7012948560317","8203947561203","6902847510394","8712394057612","5562039475109","9682035746103","7348291057641","9038475620139","7802946157032","6928475012936","8602947156021"]
        if halal in halal_barcodes:
            print(f"The barcode number {halal} is HALAL. Enjoy your meal, {name}!")
        else:
            print(f"The barcode number {halal} is not found in our database, so we cannot confirm its halal status. Please check again, {name}.")
        again = input("Do you want to check another barcode? (yes/no): ").strip().lower()
        if again == "yes":
            continue
        else:
            print("Thank you for using Halal Barcode Checker. Goodbye!")
            return