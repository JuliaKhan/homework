#Homework: comment on what line 4-12 does and make a change so it prints 
#Tuesday orders instead of Monday (Everything after line 12 is mine.)

log_file = open("um-server-01.txt") #initialize log_file as the saved .txt


def generate_sales_reports(log_file): #defines a function which accepts a .txt
    for line in log_file: #for loop that iterates over every line in the .txt
        line = line.rstrip() #removes whitespace at end of line str
        day = line[0:3]     #initialize day as the 1st 3 chars of line
        if day == "Mon":    #begin if loop checking for only the chosen day
            print(line)     #prints only lines for chosen day

def LeadingZero(x): #to simplify count_orders function below
    """Adds leading zeros to make a User # 3 digits long."""

    NeedZero = 8 - len(x)
    return(x[:5] + NeedZero * '0' + x[5:])

def count_orders(log_file): #for fun / harder practice. 
    """Outputs list of users and how many orders they made."""

    orders = []
    tally = []
    final_list = []
    for line in log_file:
        line = line.rstrip()
        user_loc = line.index("User ")
        user = LeadingZero(line[user_loc:])
        if user not in orders:
            orders.append(user)
            tally.append(1)
        else:
            order_loc = orders.index(user)
            tally[order_loc] += 1
    x = 0
    while x < len(orders):
        final_list.append([orders[x],tally[x]])
        x += 1
    final_list.sort()
    for row in final_list:
        a = f"{row[0]} made {row[1]} order"
        if row[1] > 1:
            a = a + 's'
        a = a + '.'
        print(a)
    


#generate_sales_reports(log_file) #run function on log_file
count_orders(log_file)