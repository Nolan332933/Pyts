import datetime

# Initialize an empty list to store payment history
payment_history = []

def display_menu():
    print("\n- - Bill Payment App - -")
    print("1. Pay a Bill")
    print("2. View Payment History")
    print("3. Exit")
    
    choice = input("Please select an option (1-3): ")
    return choice

def display_bills():
    print("\n- - Available Bills - -")
    print("1. Electricity Bill")
    print("2. Water Bill")
    print("3. Internet Bill")
    print("4. Phone Bill")
    
    bill_choice = input("Please select a bill to pay (1-4): ")
    return bill_choice

# Function to handle the bill payment process
def pay_bills():
    bill_choice = display_bills()
    bill_name = ""

    if bill_choice == "1":
        bill_name = "Electricity bill"
    elif bill_choice == "2":
        bill_name = "Water bill"
    elif bill_choice == "3":
        bill_name = "Internet bill"
    elif bill_choice == "4":
        bill_name = "Phone bill"
    else: 
        print("Invalid choice. Returning to main screen")
        return
    
    amount = float(input(f"Enter the amount to pay for {bill_name}: $"))
    confirm = input(f"Confirm payment of ${amount:.2f} for {bill_name}? (yes/no): ").lower()

    if confirm == 'yes':
        payment = {
            'bill_name': bill_name,
            "amount": amount,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        payment_history.append(payment)
        print(f"Payment of ${amount:.2f} for {bill_name} successful.")
    else:
        print("Payment cancelled")

# Function to view payment history
def view_payment_history():
    if not payment_history:
        print("\nNo payment history found")
    else:
        print("\n- - Payment History - -")
        for payment in payment_history:
            print(f"Bill: {payment['bill_name']}, Amount: ${payment['amount']:.2f}, Date: {payment['date']}")

# Main application loop
def main():
    while True:
        choice = display_menu()  # Call the function correctly
        if choice == "1":
            pay_bills()
        elif choice == "2":
            view_payment_history()
        elif choice == "3":
            print("Exiting the app. Thank you!")
            break
        else: 
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
