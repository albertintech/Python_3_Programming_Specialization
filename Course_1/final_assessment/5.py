inventory = [("shoes", 12, 29.99), ("shirts", 20, 9.99),
             ("sweatpants", 25, 15.00), ("scarves", 13, 7.75)]

for items in inventory:
    quantity = items[1]
    item = items[0]
    price = items[2]
    print('The store has {} {}, each for {:.2f} USD.'.format(quantity, item, price))
