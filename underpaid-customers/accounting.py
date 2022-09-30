melon_cost = 1.00                       #sets the global cost of a melon


def paid_vs_expected(name, qty, paid, cost = melon_cost):
    """Checks if an order was paid correctly.
    
    Function accepts a customer's name, a qty of melons purchased, how much 
    they paid, and (optional) what each melon cost.
    
    Function flags customers who paid the wrong amount and prints a summary.
    
    >>> paid_vs_expected("David", 4, 4.00)

    >>> paid_vs_expected("Ashley", 3, 2.00)
    Ashley paid $2.00, expected $3.00
    """

    expected = int(qty) * float(cost)   #calculates expected payment
    paid = float(paid)
    if expected != paid:                #flags sales with incorrect payment
        print(f"{name} paid ${paid:.2f},",
            f"expected ${expected:.2f}" #prints discrepency statement
            )


def parse_customer_orders(file_name):
    """Runs paid_vs_expected on a text file.
    
    Accepts the name of a text file with lines in the form of
    "<integer order number>|<customer name>|<integer qty>|<float payment>"
    and runs paid_vs_expected function using each line as an input.
    """

    for line in open(file_name):
        line = line.rstrip()
        words = line.split('|')
        paid_vs_expected(words[1],words[2],words[3])

parse_customer_orders('customer-orders.txt')    #runs parse_customer_orders on
                                                #'customer-orders.txt'