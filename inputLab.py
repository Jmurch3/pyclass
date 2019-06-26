import random
name = input("Enter your name: ")
salary= input("Enter your salary: V")
raise_per=(random.randint(0,100))
raise_amount=((int(salary) * raise_per) /int(100)+ int(salary))
print(f"{name}, you make V{salary} vbucks a year :(")
print(f"you got a raise of %{raise_per} :D")
print(f"You now make V{raise_amount} vbucks a year!")
