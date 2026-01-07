need = 20
bank = 10.5

to_add=float(input("Money to add:"))

if bank+to_add >= need:
    print("Need reached")
else:
    print(f"not reached {bank+to_add}")
