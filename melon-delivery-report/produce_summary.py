def daily_summary(the_file):
    """Prints a summary of melon deliveries.

    Reads a file containing lines in the form
    '<melon>|<quantity>|<cost>' and prints a report with lines in the form 
    'Delivered <quantity> <melon>(s) for a total of $<cost>'
    """

    for line in open(the_file):
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        if count == '1':
            plural = ''
        else: plural = 's'

        print(f"Delivered {count} {melon}{plural} for total of ${amount}")

print("Day 1\n")
daily_summary("um-deliveries-day-1.txt")

print("\nDay 2\n")
daily_summary("um-deliveries-day-2.txt")

print("\nDay 3\n")
daily_summary("um-deliveries-day-3.txt")
