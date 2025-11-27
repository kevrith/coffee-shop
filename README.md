# Coffee Shop Domain Model

This is a Python application modeling a Coffee Shop domain using object-oriented programming principles. It consists of three main entities: `Customer`, `Coffee`, and `Order`, establishing many-to-many relationships through the `Order` entity.

## Domain Relationships

- A `Customer` can place many `Orders`.
- A `Coffee` can have many `Orders`.
- An `Order` belongs to one `Customer` and one `Coffee`.

## Classes

### Customer
- Attributes: name (string, 1-15 characters)
- Methods:
  - `orders()`: Returns list of all orders for the customer
  - `coffees()`: Returns unique list of coffees the customer has ordered
  - `create_order(coffee, price)`: Creates a new order
  - `most_aficionado(coffee)`: Class method returning customer who spent most on a coffee

### Coffee
- Attributes: name (string, at least 3 characters)
- Methods:
  - `orders()`: Returns list of all orders for the coffee
  - `customers()`: Returns unique list of customers who ordered the coffee
  - `num_orders()`: Returns total orders for the coffee
  - `average_price()`: Returns average price of orders

### Order
- Attributes: customer, coffee, price (float, 1.0-10.0)
- Establishes relationships by adding itself to customer and coffee order lists

## Installation

1. Clone the repository
2. Install pipenv: `pip install pipenv`
3. Set up virtual environment: `pipenv install`
4. Enter virtual environment: `pipenv shell`

For tests (optional):
```bash
pipenv install pytest
pipenv run pytest
```

## Usage

Run the debug script to see example usage:

```bash
python debug.py
```

## Testing

Bonus testing available in `tests/` directory. Run with pytest:

```bash
pytest
```

