
#to find gcd of two numbers 
def gcd(a,b):
  if (b==0):
    return a
  else:
    return (gcd(b,a%b))

print(gcd(12,6))


#to print the table with square root of numbers and sqrt() functions
def fu(a):
  
  x=3
  while True:
    y=(x+(a/x))/2
    if y==x:
      break
    x=y
    
  return y
print(fu(4))
import math
def test():
  for i in range(1,10):
    print(i,fu(i),math.sqrt(i),fu(i)-math.sqrt(i),sep="\t")

test()

#Write a function called eval_loop that iteratively prompts the user, takes the resulting input and evaluates it using eval, and prints the result.

def l():
  while True:
    print("enter exp")
    line=input()
    
    if(line=='done'or line=='Done'or line=='DONE'):
      break
    else:
      y=eval(line)
      print(y)
  print(y)
    
      
l()