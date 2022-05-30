# Conditional Execution

hrs = input("Enter hours: ")
rate = input("enter rate: ")
fhrs=float(hrs)
frate=float(rate)
if fhrs>40:
  regularpay=40*frate
  overtimepay=(fhrs-40)*(frate*1.5)
  Pay=regularpay+overtimepay
else:
  Pay=fhrs*frate
  print("Pay",Pay)typr