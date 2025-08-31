class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_items(self, **kwargs):
        for item, (price, qty) in kwargs.items():
            if item in self.cart:
                self.cart[item]['quantity'] += qty
            else:
                self.cart[item] = {"price": price, "quantity": qty}
        print(f"Added items: {list(kwargs.keys())}")

    def remove_item(self, *args):
    
        for item in args:
            if item in self.cart:
                del self.cart[item]
                print(f"Removed {item}")
            else:
                print(f"{item} not found in cart")

    def update_quantity(self, item, qty):
      
        if item in self.cart:
            self.cart[item]['quantity'] = qty
            print(f"Updated {item} quantity to {qty}")
        else:
            print(f"{item} not found in cart")

    def show_cart(self):
        if not self.cart:
            print("\n🛒 Cart is empty!")
            return

        print("\n🛒 Shopping Cart:")
        total = 0
        for item, details in self.cart.items():
            price = details["price"]
            qty = details["quantity"]
            subtotal = price * qty
            total += subtotal
            print(f"- {item}: ₹{price} x {qty} = ₹{subtotal}")

        print(f"\n✅ Total Bill: ₹{total}")


cart = ShoppingCart()

cart.add_items(Shoes=(2000, 2), Shirt=(1500, 1), Watch=(3500, 1))
cart.show_cart()

cart.update_quantity("Shoes", 3)
cart.remove_item("Watch")
cart.show_cart()
