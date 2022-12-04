'''
Author: Ethanlinyf e.yflin@gmail.com
Date: 2022-12-04 13:11:38
LastEditors: Ethanlinyf e.yflin@gmail.com
LastEditTime: 2022-12-04 13:12:47
FilePath: /Pokemon-Park/Example/fabonacci_recursion.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("Please Input the Terms:"))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))