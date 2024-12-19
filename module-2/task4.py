principal=input("Enter the Principal amount: ")
rate=input("Enter the rate of interest: ")
time=input("Enter the time(in years): ")

principal=float(principal)
rate=float(rate)
time=float(time)

interest=(principal*rate*time)/100

print("The interest is ",interest)


