# A = 'Avinash'
# B = '123'
# C = ''
#
# for i, j in zip(A,B):
#     C += i+j
# print(C+ A[4:])
from collections import Counter

"""
Raghu is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of 
their desired size.

Your task is to compute how much money  earned..
6 55
6 45
6 55
4 40
18 60
10 50
"""
# from collections import Counter
#
# stock = map(int, input().split())
#
# dict = Counter(stock)
# cust = int(input())
# earning = 0
#
# for i in range(cust):
#     size,price = map(int, input().split())
#     if dict[size] > 0:
#         earning += price
#         dict[size] -= 1
#
# print(earning)
