class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        Customer.all_customers.append(self)
        self._orders = []

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Nmae must be a string!!")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        """Returns a list of all orders for this customer"""
        return self._orders
    
    def coffees(self):
        """Returns a unique list of all coffees the customer has ordered"""
        return list(set(order.coffee for order in self._orders))
    
    def create_order(self, coffee, price):
        """Creates a new order for the customer"""
        from order import Order 
        order = Order(self,coffee, price)
        return order
    
    @classmethod
    def most_aficionado(cls, coffee):
        """Returns the customer who has spent the most on the given coffee"""
        if not coffee.orders():
            return None
        
        customer_spending ={}
        for order in coffee.orders():
            customer = order.customer
            if customer not in customer_spending:
                customer_spending[customer] = 0
            customer_spending[customer] += order.price

        if not customer_spending:
            return None
        
        return max(customer_spending, key=customer_spending.get)