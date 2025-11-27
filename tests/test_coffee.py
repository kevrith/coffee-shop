import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee:
    def setup_method(self):
        # Clear class lists
        Coffee.all_coffees = []
        Customer.all_customers = []
        Order.all_orders = []

    def test_coffee_init_valid(self):
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"
        assert coffee in Coffee.all_coffees

    def test_coffee_name_validation(self):
        # Too short
        with pytest.raises(ValueError):
            Coffee("Hi")
        
        # Not string
        with pytest.raises(TypeError):
            Coffee(123)

    def test_orders_empty(self):
        coffee = Coffee("Espresso")
        assert coffee.orders() == []

    def test_customers_empty(self):
        coffee = Coffee("Espresso")
        assert coffee.customers() == []

    def test_num_orders_empty(self):
        coffee = Coffee("Espresso")
        assert coffee.num_orders() == 0

    def test_average_price_no_orders(self):
        coffee = Coffee("Espresso")
        assert coffee.average_price() == 0

    def test_orders_after_adding(self):
        coffee = Coffee("Espresso")
        customer = Customer("Alice")
        customer.create_order(coffee, 3.5)
        assert len(coffee.orders()) == 1

    def test_customers_unique(self):
        coffee = Coffee("Espresso")
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        customer1.create_order(coffee, 3.5)
        customer2.create_order(coffee, 4.0)
        customers = coffee.customers()
        assert len(customers) == 2
        assert set(customers) == {customer1, customer2}

    def test_num_orders(self):
        coffee = Coffee("Espresso")
        customer = Customer("Alice")
        customer.create_order(coffee, 3.5)
        customer.create_order(coffee, 4.0)
        assert coffee.num_orders() == 2

    def test_average_price(self):
        coffee = Coffee("Espresso")
        customer = Customer("Alice")
        customer.create_order(coffee, 3.0)
        customer.create_order(coffee, 4.0)
        assert coffee.average_price() == 3.5

    def test_average_price_single_order(self):
        coffee = Coffee("Espresso")
        customer = Customer("Alice")
        customer.create_order(coffee, 5.0)
        assert coffee.average_price() == 5.0
