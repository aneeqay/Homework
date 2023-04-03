from datetime import date

class Order:
    def __init__(self, title, customer_name, order_date, quantity, description = ""):
        self.title = title
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.description = description

