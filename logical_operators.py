loyalt_discount = 10
total_bill = input('Insert bill total: ')
in_loyalt_program = input('Is the client in the loyalt program? Please insert Yes or No: ') 

if in_loyalt_program == 'Yes' and float(total_bill) >= 100:
     print('Thank you for being part of our program, your total without the discount is: ' + str(total_bill))
     bill_discount = float(total_bill) - float(loyalt_discount)
     print('Total bill is now: ' + str(bill_discount))
else: 
    print('Sadly the bill is less than $100.00, keep shopping!')

if in_loyalt_program == 'No':
    print('As of right now, you are not part of our program. So your total is:' + str(total_bill))