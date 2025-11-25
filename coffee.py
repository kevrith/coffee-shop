class Coffee:
    all_coffees = []

    def __init__(self, name):
        self.name = name
        Coffee.all_coffees.append(self)
        self._orders = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string!!")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        self._name = value

    def orders(self):
        # Returns a list of all orders for this coffee
        return self._orders
    
    def customers(self):
        # Returns a unique list of all customers who have orderd this coffee
        return list(set(order.customer for order in self._orders))
    
    def num_orders(self):
        # Returns the total number of times this coffee has been ordered
        return len(self._orders)
    
    def average_price(self):
        # Returns the average proce for this coffee based on its orders
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)