import pandas as pd
import matplotlib.pyplot as plt

USER_FILE = "user_data.csv"
ORDERS_FILE = "orders.csv"

if not pd.io.common.file_exists(USER_FILE):
    user_df = pd.DataFrame(columns=["Username", "Password"])
else:
    user_df = pd.read_csv(USER_FILE)

if not pd.io.common.file_exists(ORDERS_FILE):
    orders_df = pd.DataFrame(columns=["Username", "Car Model", "Status"])
else:
    orders_df = pd.read_csv(ORDERS_FILE)


inventory = [
    "Toyota Camry", "Honda Accord", "Ford Mustang", "Chevrolet Corvette", "Tesla Model S",
    "BMW 3 Series", "Audi A4", "Mercedes-Benz C-Class", "Nissan Altima", "Hyundai Sonata",
    "Kia Optima", "Volkswagen Golf", "Subaru Outback", "Mazda CX-5", "Jeep Wrangler",
    "Lexus RX", "Porsche 911", "Ferrari 488", "Lamborghini Aventador", "Aston Martin DB11",
    "Volvo XC90", "Land Rover Range Rover", "Jaguar F-Type", "Mitsubishi Outlander",
    "Chrysler 300", "Dodge Charger", "GMC Sierra", "Ram 1500", "Cadillac Escalade",
    "Buick Enclave"
]

print("=== Online Car Dealership ===")
print("1. Sign Up")
print("2. Log In")
print("3. Exit")
choice = input("Enter your choice: ")

# Sign Up
if choice == "1":
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    
    if username in user_df["Username"].values:
        print("Username already exists. Please try again.")
    else:
        new_user = pd.DataFrame({"Username": [username], "Password": [password]})
        user_df.to_csv(USER_FILE, index=False)
        print("Sign-up successful!")

# Log In
elif choice == "2":
    username = input("Enter your username: ")
    password = input("Enter your password: ")


    user = user_df[(user_df["Username"] == username) & (user_df["Password"] == password)]
    if not user.empty:
        print(f"Welcome back, {username}!")
        print("=== My Account ===")
        print("1. Place an Order")
        print("2. Track My Orders")
        print("3. View Sales Statistics")
        print("4. View Inventory")
        account_choice = input("Enter your choice: ")

        
        if account_choice == "1":
            car_choice = int(input("Enter the number of the car you want to order: "))
            if 1 <= car_choice <= len(inventory):
                car_model = inventory[car_choice - 1]
                new_order = pd.DataFrame({"Username": [username], "Car Model": [car_model], "Status": ["Pending"]})
                orders_df.to_csv(ORDERS_FILE, index=False)
                print("Order placed for {car_model}. Status: Pending")
            else:
                print("Invalid choice. Please try again.")

        
        elif account_choice == "2":
            user_orders = orders_df[orders_df["Username"] == username]
            if not user_orders.empty:
                print("Your Orders:")
                print(user_orders[["Car Model", "Status"]])
            else:
                print("You have no orders yet.")

        # View Sales Statistics
        elif account_choice == "3":
            if not orders_df.empty:
                
                sales_data = orders_df["Car Model"].value_counts()
                print("Sales Statistics:")
                print(sales_data)

                
                sales_data.plot(kind="bar", color="green")
                plt.title("Car Sales Statistics")
                plt.xlabel("Car Model")
                plt.ylabel("Number of Orders")
                plt.show()
            else:
                print("No sales data available.")

        # View Inventory
        elif account_choice == "4":
            print("Available Cars:")
            for i, car in enumerate(inventory, 1):
                print(f"{i}. {car}")

        else:
            print("Invalid choice. Please try again.")

    else:
        print("Invalid username or password.")

# Exit
elif choice == "3":
    print("Exiting the program. Goodbye!")

else:
    print("Invalid choice. Please try again.")
