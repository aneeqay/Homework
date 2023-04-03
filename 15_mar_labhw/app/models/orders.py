from datetime import date 

from models.order import Order

order1 = Order("Red Box", "Mr Box", date(2022, 11, 1), 5, "NA")
order2 = Order("Green Box", "Mrs Box", date(2023, 1, 15), 10, "A really pretty green box")
order3 = Order("Blue Box", "Ms Box", date(2023, 2, 6), 2, "NA")

orders = [order1, order2, order3]
