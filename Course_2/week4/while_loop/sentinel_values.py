"""In this program, zero is a sentinel value, a value used to signal the end of the loop."""


def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input("Enter price of item (0 when done): "))
        if price != 0:
            count += 1
            total += price
            print("Subtotal: $", total)
        else:
            moreItems = False
    average = total / count
    print("Total items: ", count)
    print("Total $", total)
    print("Average price per item: $", average)


checkout()
