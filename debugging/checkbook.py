class Checkbook:
    """
    A simple checkbook application that allows the user to manage their finances
    by depositing and withdrawing money, and checking the balance.
    """
    def __init__(self):
        """
        Initializes a new Checkbook instance with a balance of zero.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Adds a specified amount to the checkbook balance.

        Parameters:
        amount (float): The amount of money to deposit.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Subtracts a specified amount from the checkbook balance if sufficient funds exist.

        Parameters:
        amount (float): The amount of money to withdraw.

        Returns:
        None: Prints an error message if there are insufficient funds.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to run the Checkbook application. This function handles user
    input and executes appropriate checkbook actions based on that input.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

