#Rezwana Kabita
#empl Id- 23589014

def isprime(n):
    if n<= 1:
     return false
            
    for i in range(2,n):
        if n % i == 0:
         return False
    return True


def PrimeNumberPrint(n):
    for i in range(2,n+1):
        if isprime(i):
            print(i,",")



def collatz(k):
 print(k)
 if k == 1:
  return False
 elif k % 2 == 0:
  return collatz(k/2)

 elif k % 2 == 1:
  return collatz(3*k+1)





def primefactor(p):
 print("the prime factors of",x, "are:")
 for i in range(1,x+1):
    if x % i == 0:
     print(i)
























p=int(input("Enter a number to make collatz sequence:"))
collatz(p)


n= int(input("Enter a number to check prime numbers:"))
PrimeNumberPrint(n)

a= int(input("Enter a number:"))
b= int(input("Enter a number:"))
if int(a)==a and int(b)==b:
    if b!=0:
        print(a/b)

n= int(input("Enter a number to check prime factors:"))
primefactor(n)



















