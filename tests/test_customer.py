import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def setup_method(self):
        # Clear class lists to avoid interference between tests
        Customer.all_customers = []

    def test_customer_init_valid(self):
        customer = Customer("John")
        assert customer.name == "John"
        assert customer in Customer.all_customers

    def test_customer_name_validation(self):
        # Too short
        with pytest.raises(ValueError):
            Customer("")
        
        # Too long
        with pytest.raises(ValueError):
            Customer("A" * 16)
        
        # Not string
        with pytest.raises(TypeError):
            Customer(123)

    def test_orders_empty(self):
        customer = Customer("Alice")
        assert customer.orders() == []

    def test_coffees_empty(self):
        customer = Customer("Alice")
        assert customer.coffees() == []

    def test_create_order(self):
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        order = customer.create_order(coffee, 5.0)
        assert isinstance(order, Order)
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 5.0
        assert order in customer.orders()
        assert order in coffee.orders()

    def test_orders_after_adding(self):
        customer = Customer("Alice")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Latte")
        customer.create_order(coffee1, 3.5)
        customer.create_order(coffee2, 4.0)
        orders = customer.orders()
        assert len(orders) == 2
        assert all(order.customer == customer for order in orders)

    def test_coffees_unique(self):
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        customer.create_order(coffee, 3.5)
        customer.create_order(coffee, 4.0)  # Same coffee again
        coffees = customer.coffees()
        assert len(coffees) == 1
        assert coffees[0] == coffee

    def test_most_aficionado_with_orders(self):
        coffee = Coffee("Espresso")
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        customer1.create_order(coffee, 3.5)  # $3.5
        customer2.create_order(coffee, 4.0)  # $4.0
        customer2.create_order(coffee, 5.0)  # Total $9.0
        assert Customer.most_aficionado(coffee) == customer2

    def test_most_aficionado_no_orders(self):
        coffee = Coffee("Latte")
        assert Customer.most_aficionado(coffee) is None

    def test_most_aficionado_empty(self):
        # If no customers or orders, probably None
        Customer.all_customers = []  # Clear
        coffee = Coffee("Cappuccino")
        assert Customer.most_aficionado(coffee) is None
