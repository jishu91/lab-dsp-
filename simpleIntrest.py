principal_amount=int(input("Enter the principal amount: "))
time=int(input("Enter the time period (in years): "))
rate=int(input("Enter the rate of interest (in percentage): "))


# calculate simple intrest
si=principal_amount*rate*time/100

print("Simple intrest is:" ,si)