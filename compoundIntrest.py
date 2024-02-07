principal_amount=int(input("Enter the principal amount: "))
time=int(input("Enter the time period (in years): "))
rate=int(input("Enter the rate of interest (in percentage): "))

# calculate Compound intrest
amount=principal_amount*(pow((1+rate/100),time))
ci=amount-principal_amount

print("Compound intrest is:" ,ci)