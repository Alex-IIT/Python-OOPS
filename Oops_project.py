class chatbook:

    __user_id=0
    def __init__(self):
        self.id=chatbook.__user_id
        chatbook.__user_id+=1
        self.__name="Default User"
        self.username=""
        self.password=""
        self.loggedin=False
        # self.menu()
    @staticmethod
    def get_id():
        return chatbook.__user_id
    @staticmethod
    def set_id(value):
        chatbook.__user_id=value



    def getname(self):
        return self.__name
    def setname(self,value):
        self.__name=value




    def menu(self):
        user_input=input("""Welcome to chatbook !! How would you like to proceed  
         1. Press 1 to signup
         2. Press 2 to login
         3. Press 3 to write a post
         4. Press 4 to message a friend\n ->""")
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.login()
        elif user_input=="3":
            self.my_post()    
        elif user_input=="4":
            self.sendmsg()
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
    def my_post(self):
        if self.loggedin==True:
            txt=input("Enter your message here->")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to sign in to post something.")    
        print("\n")
        self.menu()
    def sendmsg(self):
        if self.loggedin==True:
            txt=input("Enter your message here->")
            friend=input("Whom you want to send the message? -> ")
            print(f"Your message has been sent to {friend}")
        else:
            print(" You need to sign in first to message a friend" )
        print("\n")
        self.menu()    



# user=chatbook()
