# WAP to create a class Product having
# product_no, product_name, cost, quantity
# total_amount member functions: input(), calculate(), display()
# calculate() is used to find total amount and display the product details.

class Product:

    def input(self):
        self.product_no = int(input("Enter product number: "))
        self.product_name = input("Enter product name: ")
        self.cost = float(input("Enter cost: "))
        self.quantity = int(input("Enter quantity: "))

    def calculate(self):
        self.total_cost = self.cost * self.quantity

    def display(self):
        print("Product no:", self.product_no)
        print("Product name:", self.product_name)
        print("Product cost:", self.cost)
        print("Product quantity:", self.quantity)
        print("Total cost:", self.total_cost)


Products = []

for i in range(5):
    print("\nEnter Product", i + 1)
    P = Product()
    P.input()
    P.calculate()
    Products.append(P)

highest = Products[0]

for p in Products:
    if p.total_cost > highest.total_cost:   # Fixed here
        highest = p

print("\nProduct with highest total cost:")
highest.display()