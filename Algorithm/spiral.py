
import math

print("=================================================================================\n")

num = 49
#num = input("What number would you like to spiral?: ")     # for command prompt / Terminal usage
print("What number would you like to spiral?: 49")
print("\n")

num_list = list(range(1,num+1))
print(num_list)

sqrt_ceil = math.ceil(math.sqrt(num))
sqrt_floor = math.floor(math.sqrt(num))

if (sqrt_ceil % 2) == 1:
      if num >= math.ceil((sqrt_ceil**2 - sqrt_floor**2)/2):
            height = sqrt_ceil
      elif num < math.ceil((sqrt_ceil**2 - sqrt_floor**2)/2):
            height = sqrt_floor

elif (sqrt_ceil % 2) == 0:

width = 
height = 