
"""myaranjan Pattnaik
Write a function that opens a file, reads its contents, and closes the file. Ensure proper exception handling to deal with potential issues,
such as file not found or file reading errors."""

# def my_fun(n):
#     try:
#         with open(n,'r') as text_file:
#             file_reading = text_file.readlines()
#             print(file_reading)
#
#     except FileNotFoundError as e:
#         print(e)
#
# my_fun("file_path")


"""Create a Python class representing a simple bank account.
The class should have methods for deposit, withdrawal, and checking the account balance."""


# class bank_account:
#     def __init__(self,user_name,initial_balance=0):
#         self.user_name = user_name
#         self.initial_balance = initial_balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.initial_balance += amount
#             print(f'deposited amount is {amount} and total balance is {self.initial_balance}')
#         else:
#             print('invalid balance')
#
#     def withdrawl(self, amount):
#         if 0 < amount <= self.initial_balance:
#             self.initial_balance -= amount
#             print(f'withdral amount is {amount} and remaining balance is {self.initial_balance}')
#
#         else:
#             print("insufficient Balamce")
#
#     def check_balance(self):
#         print(f"balance is {self.initial_balance}")
#
# obj = bank_account("avinash",initial_balance=1000)
# obj.deposit(1000)
# obj.withdrawl(500)
# obj.check_balance()


"""if I search "iphone 13" on Amazon.in and in the search results there are multiple variants of "iphone 13", 
so your task is to write Xpath to find their price along with their model name."""
