# input statements
salary = float(input("Enter salary: 60,000"))
numDependents = int(input("Enter number of dependents: 3 "))

# tax calculations
state_tax = salary * 0.065 

# Example state tax rate of 6.5%
federal_tax = salary * 0.28  

# Example federal tax rate of 28%
dependent_deduction = numDependents * 1500.0 

# Example deduction per dependent
# calculate total withholding and take home pay
total_withholding = state_tax + federal_tax + dependent_deduction
takeHomePay = salary - total_withholding

#ouptut statements

# print statements
print("State Tax: $" + str(state_tax))
print("Federal Tax: $" + str(federal_tax))
print("Dependents: $" + str(dependent_deduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
