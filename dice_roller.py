# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj = Service()
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://www.amazon.in/")
#
# text_box = driver.find_element(By.XPATH,"(//input[@type='text'])[1]")
#
# text_size = text_box.location
# print(text_size)
# time.sleep(3)


class bank_account:
    def __init__(self,user_name,initial_balance=0):
        self.user_name = user_name
        self.initial_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.initial_balance += amount
            print(f'deposited amount is {amount} and total balance is {self.initial_balance}')
        else:
            print('invalid balance')

    def withdrawl(self, amount):
        if 0 < amount <= self.initial_balance:
            self.initial_balance -= amount
            print(f'withdral amount is {amount} and remaining balance is {self.initial_balance}')

        else:
            print("insufficient Balamce")

    def check_balance(self):
        print(f"balance is {self.initial_balance}")

obj = bank_account("avinash",initial_balance=1000)
obj.deposit(1000)
obj.withdrawl(500)
obj.check_balance()


