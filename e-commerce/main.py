class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.cart.append((product, quantity))
            product.stock -= quantity
            print(f"Added {quantity} of {product.name} to the cart.")
        else:
            print(f"Sorry, only {product.stock} items left in stock.")

    def view_cart(self):
        if len(self.cart) == 0:
            print("Your cart is empty")
        else:
            print("\nYour Cart")
            total = 0
            for product, quantity in self.cart:
                print(f"{product.name} - {quantity} pcs - ${product.price * quantity}")
                total += product.price * quantity
            print(f"Total: ${total}\n")

    def checkout(self):
        if len(self.cart) == 0:
            print("Cart is empty. Cannot proceed to checkout.")
        else:
            print("Proceeding to checkout")
            self.cart.clear()
            print("Order placed successfully")


class ECommerceApp:
    def __init__(self):
        self.products = []
        self.shopping_cart = ShoppingCart()

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        print("\nAvailable Products")
        for product in self.products:
            print(f"ID: {product.id} | {product.name} | ${product.price} | Stock: {product.stock}")
        print()

    def run(self):
        print("Welcome to the E-commerce App!\n")
        while True:
            print("1. View Products")
            print("2. Add Product to Cart")
            print("3. View Cart")
            print("4. Checkout")
            print("5. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                self.show_products()
            elif choice == "2":
                self.show_products()
                product_id = int(input("Enter the product ID: "))
                quantity = int(input("Enter the quantity: "))
                product = next((p for p in self.products if p.id == product_id), None)
                if product:
                    self.shopping_cart.add_to_cart(product, quantity)
                else:
                    print("Invalid Product ID")
            elif choice == "3":
                self.shopping_cart.view_cart()
            elif choice == "4":
                self.shopping_cart.checkout()
            elif choice == "5":
                print("Thank you for shopping with us!")
                break
            else:
                print("Invalid option, please try again")


# Create instance of the app and add products
app = ECommerceApp()
app.add_product(Product(1, "Laptop", 800, 10))
app.add_product(Product(2, "Smartphone", 500, 15))
app.add_product(Product(3, "Headphones", 50, 30))
app.add_product(Product(4, "Camera", 250, 5))

# Run the app
app.run()
