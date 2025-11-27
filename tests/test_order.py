import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder:
    def setup_method(self):
        # Clear class lists
        Order.all_orders = []
        Customer.all_customers = []
        Coffee.all_coffees = []

    def test_order_init_valid(self):
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 5.0)
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 5.0
        assert order in Order.all_orders
        assert order in customer.orders()
        assert order in coffee.orders()

    def test_customer_validation(self):
        coffee = Coffee("Latte")
        with pytest.raises(TypeError):
            Order("not_customer", coffee, 5.0)

    def test_coffee_validation(self):
        customer = Customer("Bob")
        with pytest.raises(TypeError):
            Order(customer, "not_coffee", 5.0)

    def test_price_validation(self):
        customer = Customer("Charlie")
        coffee = Coffee("Cappuccino")
        
        # Too low
        with pytest.raises(ValueError):
            Order(customer, coffee, 0.5)
        
        # Too high
        with pytest.raises(ValueError):
            Order(customer, coffee, 15.0)
        
        # Not number
        with pytest.raises(TypeError):
            Order(customer, coffee, "five")

    def test_price_converted_to_float(self):
        customer = Customer("Denis")
        coffee = Coffee("Mocha")
        order = Order(customer, coffee, 7)  # int
        assert order.price == 7.0
        assert isinstance(order.price, float)

    def test_order_adds_to_lists(self):
        customer = Customer("Eve")
        coffee = Coffee("Americano")
        order = Order(customer, coffee, 4.5)
        assert order in customer._orders
        assert order in coffee._orders
        assert order in Order.all_orders
