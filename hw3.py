
#Task 1
firstString = "mr.Antonio"


if len(firstString)>2:
   result = ''
   result = firstString[0:2]
   result = result + firstString[len(firstString)-2:len(firstString)]
   
   print(result)
else:
   print("")

#Task 2
phoneNumber = "019698689a"

if phoneNumber.isdigit():
   if len(phoneNumber)==10:
      print("What a wonderful number!")
   else:
      print("Sorry, print your phone number in a right format, please...")
else:
   print("Ooops... Something went wrong!")


#Task 3
your_name = input("Enter your name, please: ")

test_name = "dmytro"

your_name = your_name.lower()

if your_name==test_name:
   print("Cool! You're a right person.")
else:
   print("Oh, you might be a thief... I'm calling the police!")


