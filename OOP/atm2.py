class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
        
    def menu(self):
        while True:
            user_input = input("""
Select an option:
1. Create Pin
2. Deposit
3. Withdraw
4. Check Balance
5. Exit
Enter your choice: """)
            
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def create_pin(self):
        self.pin = input("Enter a new 4-digit PIN: ")
        print("PIN created successfully!")
        
    def deposit(self):
        if self.pin == "":
            print("Please create a PIN first.")
            return
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            amount = float(input("Enter the amount to deposit: "))
            if amount > 0:
                self.balance += amount
                print(f"${amount:.2f} deposited successfully.")
            else:
                print("Invalid amount. Please enter a positive value.")
        else:
            print("Incorrect PIN.")
    
    def withdraw(self):
        if self.pin == "":
            print("Please create a PIN first.")
            return
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            amount = float(input("Enter the amount to withdraw: "))
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"${amount:.2f} withdrawn successfully.")
            elif amount > self.balance:
                print("Insufficient balance.")
            else:
                print("Invalid amount. Please enter a positive value.")
        else:
            print("Incorrect PIN.")
    
    def check_balance(self):
        if self.pin == "":
            print("Please create a PIN first.")
            return
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            print(f"Your current balance is: ${self.balance:.2f}")
        else:
            print("Incorrect PIN.")


atm = Atm()
