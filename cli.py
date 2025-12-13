import requests
API_URL = "https://evanxplore.site/api/mistral.php"
def call_mistral(prompt):
    params = {"prompt": prompt}
    response = requests.get(API_URL, params=params)
    data = response.json()
    text = data.get("response", "").replace("\\n", "\n").strip()
    return text
def run_cli_chatbot():
    print(r""" 
▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄
                                                                                                                                                
▄█████ ██     ██   ▄█████ ██  ██ ▄████▄ ██████ █████▄ ▄████▄ ██████ 
██     ██     ██   ██     ██████ ██▄▄██   ██   ██▄▄██ ██  ██   ██   
▀█████ ██████ ██   ▀█████ ██  ██ ██  ██   ██   ██▄▄█▀ ▀████▀   ██   

▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄
                                                        WELCOME TO THE CLI CHATBOT TOOL (β0.1)
    """)
    while True:
        print("\n1. Start Chatbot")
        print("2. Return to Main Menu")
        menu = input("Choose (1/2): ").strip()
        if menu == "1":
            break
        elif menu == "2":
            return
        else:
            print("Invalid choice")
    print("\nType 'exit' anytime to go back.\n")
    while True:
        prompt = input("You: ").strip()
        if prompt.lower().strip() == "exit":
            print("Returning to menu...")
            return
        response = call_mistral(prompt)
        print("\n" + response)
        print("\n" + "-" * 40 + "\n")
