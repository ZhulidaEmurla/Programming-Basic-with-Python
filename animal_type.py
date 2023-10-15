animal = input()
user_output = "unknown"

if animal == "dog":
    user_output = "mammal"

elif animal == "crocodile" or "tortoise" or "snake":
    user_output = "reptile"

else:
    print("unknown")

print(user_output)
