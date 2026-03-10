simple_interest = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in %): "))
time_period = float(input("Enter the time period (in years): "))
simple_interest = (simple_interest * rate_of_interest * time_period) / 100
print("The simple interest is: ", simple_interest)