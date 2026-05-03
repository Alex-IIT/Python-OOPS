class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=False
        self.menu()
    def menu(self):
        user_input=input("""Welcome to chatbook !! How would you like to proceed  
         1. Press 1 to signup
         2. Press 2 to login
         3. Press 3 to write a post
         4. Press 4 to message a friend\n""")
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.login()
        elif user_input=="3":
            pass    
        elif user_input=="4":
            pass
        else:
            exit()
    def signup(self):
        email= input("Enter your username->")
        pwd=input("Enter your password->")
        self.username=email
        self.password=pwd
        print("Signed Up successfully")
        self.menu()
    def login(self):
        if self.username=='' and self.password=="":
            print("Please sign up first by pressing 1 in the main menu")
        else:
            uname=input("Enter your username->")
            pwd=input("Enter your password->")
            if self.username==uname and self.password==pwd:
                print("Logged in successfully !!") 
                self.loggedin=True
            else:
                print("Invalid Credentials")
        print("\n")
        self.menu()

chatbook1=chatbook()
