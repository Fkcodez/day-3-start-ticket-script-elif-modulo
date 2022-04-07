print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("The price for children is 5$")
  elif age <= 18:
    bill = 7
    print("The price for youths is 7$")
  elif age >= 18 and age <= 45 or age >= 55:
   bill = 12
   print("The price for adults is 12$")
  elif age >= 45 or age <= 55:
   bill = 0
   print("The ride is for free for midlife crisis")
  wants_photo = input("Do you want a photo taken? type Y or N")
  if wants_photo == "Y":
    bill = bill + 3
    # bill += 3
  print (f"Your final bill is {bill}$")
else:
  print("Sorry you have to grow taller before you can ride.")

#> greater than
#< less than
#>= greater or equal to
#<= less or equal to
#== equal to
#!= not equal to
#% modulo, devides a number and gives us the remainer eg 7%2=2+2+2+1 result would be 1
