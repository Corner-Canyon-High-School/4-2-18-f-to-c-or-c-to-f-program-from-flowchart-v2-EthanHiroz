temp = int(input("Enter the Current Temperature: "))

choice = input("Type 1 for a Fahrenheit to Centigrade. Type 2 for Centigrade to Fahrenheit: ")

if choice == "1":
    centigrade = (5/9) * (temp - 32)
    print(centigrade)

elif choice == "2":
    fahrenheit = (9*temp + (32 * 5))/5
    print(fahrenheit)

else:
    print("Invaild Input")