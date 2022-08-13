hrs = input("Enter Hours:")#working hours
h = float(hrs)
r = input("Enter rate:")#rate per hours
r = float(r)
if h <= 40:
    print(h * r)
else:
    print(40 * r + (h - 40) * r * 1.5)
