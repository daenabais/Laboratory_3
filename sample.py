monthly_salary = float(input("Please input your montly salary here:₱"))
loan = float(input("How much would you like to borrow?:"))
if monthly_salary >= 30000.00:
        max_amount=monthly_salary * 0.10
        if loan >= monthly_salary:
          print ("You are eligible for a loan")
          months_to_pay = int(input("Please input how many months you are gonna pay:"))
          interest = loan * 0.10
          total_amount = interest + loan
          print(f"loan amount: ₱{loan: .2f}")
          print(f"Total costs to pay back:₱{total_amount:.2f}")
          print(f"You have {months_to_pay} months to pay your loan:₱{total_amount/months_to_pay:.2f} ")        
        else:
            print (f"Your monthly salary is too low for the loan. Please enter another amount ₱{max_amount:.2f}")
else:
    print("You are not eligble for a loan because your salary is way too low.")
