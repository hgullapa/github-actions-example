import os
import sys

def main(secret):

    num1 = 18
    num2 = 12
  
    # Adding two nos 
    sum = num1 + num2 
  
    # printing values 
    print("Sum of {0} and {1} is {2}" .format(num1, num2, sum)) 
    if secret==25:
       print("I am 25")
if __name__ == "__main__":
    main(sys.argv[1])
  
 
