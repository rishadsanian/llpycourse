# Bill Splitter with Receipt
# Needs tabulate for receipt print
#pip install tabulate
# imported tabulate from package
from tabulate import tabulate
# tip % is calculated on amount before tax
# did not format amounts to 2 decimal places or a currency format
# exception handing and data validation parameters not set

# General Receipt
subtotal = float(input("What is your subtotal?"))  # input
taxRate = 0.13
tax = taxRate * subtotal
total = subtotal + tax

# Tip calculation
tippercent = float(
    (float(input("What % tip would you like to give?")))/100)  # input
tipamount = float(subtotal*tippercent)
grandtotal = total + tipamount

# Bill splitter
numppl = int((input("How many people are paying the bill")))  # input
billsplit = grandtotal/numppl

# storing and outputs
receipt = [["Subtotal: ", "$"+str(subtotal)], ["Tax (" + str(taxRate*100)+"%): ", "$" + str(tax)], ["Total: ", "$"+str(
    total)], ["Tip (" + str(tippercent*100)+"%): ", "$"+str(tipamount)], ["Grand total: ", "$"+str(grandtotal)]]
billsplitter = print("Receipt\n", tabulate(receipt)), print(
    "Your bill split", str(numppl), "ways is $", str(billsplit), "per person.")
