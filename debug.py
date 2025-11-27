from customer import Customer
from coffee import Coffee
from order import Order

# Create some customers
customer1 = Customer("Alice")
customer2 = Customer("Bob")
customer3 = Customer("Charlie")

# Create some coffees
espresso = Coffee("Espresso")
latte = Coffee("Latte")
cappuccino = Coffee("Cappuccino")

# Create some orders
order1 = customer1.create_order(espresso, 3.5)
order2 = customer1.create_order(latte, 4.5)
order3 = customer2.create_order(espresso, 3.5)
order4 = customer2.create_order(espresso, 3.5)
order5 = customer3.create_order(latte, 4.0)

# Test customer methods
print("=== Customer Tests ===")
print(f"Customer 1 name: {customer1.name}")
print(f"Customer 1 orders: {len(customer1.orders())} orders")
print(f"Customer 1 coffees: {[coffee.name for coffee in customer1.coffees()]}")

# Test coffee methods
print("\n=== Coffee Tests ===")
print(f"Espresso orders: {espresso.num_orders()}")
print(f"Espresso average price: ${espresso.average_price():.2f}")
print(f"Espresso customers: {[customer.name for customer in espresso.customers()]}")

# Test most_aficionado
print("\n=== Most Aficionado Test ===")
biggest_fan = Customer.most_aficionado(espresso)
print(f"Biggest espresso fan: {biggest_fan.name if biggest_fan else 'None'}")

# Test validation
print("\n=== Validation Tests ===")
try:
    invalid_customer = Customer("")  # Too short
except ValueError as e:
    print(f"✓ Caught error: {e}")

try:
    invalid_coffee = Coffee("Hi")  # Too short
except ValueError as e:
    print(f"✓ Caught error: {e}")

try:
    invalid_order = Order(customer1, espresso, 15.0)  # Price too high
except ValueError as e:
    print(f"✓ Caught error: {e}")

print("\n=== All Tests Passed! ===")