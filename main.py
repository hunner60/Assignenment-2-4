
# input statements
salary = float(input())
numDependents = float(input())

# tax calculations
state_tax = salary * 0.065  # State tax rate of 6.5%
federal_tax = salary * 0.28  # Federal tax rate of 28%
dependent_deduction = numDependents * 1500.0  # Deduction per dependent

# calculate total withholding and take home pay
total_withholding = state_tax + federal_tax + dependent_deduction
takeHomePay = salary - total_withholding

# output statements
print("State Tax: $" + str(state_tax))
print("Federal Tax: $" + str(federal_tax))
print("Dependents: $" + str(dependent_deduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
