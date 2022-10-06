"""Generate sales report showing total melons each salesperson sold."""


salespeople = []    #initializes empty lists
melons_sold = []

f = open('sales-report.txt')    #assign 'sales-report.txt' to f

for line in f:  #loop over lines in 'sales-report.txt'
    line = line.rstrip()    #remove whitespace to the right
    entries = line.split('|')   #make a list of each line
    salesperson = entries[0]    #1st item in list is the salesperson
    melons = int(entries[2])    #3rd item in list is # of melons

    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
        
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')