
print("KM to Mile converter")

unit = input("km or mile: ")

amount = float(input("Amount: "))


if unit == "km":
  print(amount / 1.609)

elif unit == "mile":
  print(amount * 1.609)

else:
  print("Error")



