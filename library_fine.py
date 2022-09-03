# cost to be paid for the book bought from library
no_of_days = input("Enter the number of days : ")
no_of_days = (int(no_of_days))

if no_of_days <= 0:
    print("Enter valid no.of days")

if 0 < no_of_days <= 5:
    print("Cost to be paid for the book is Rs.10")
elif 6 <= no_of_days <= 10:
    print("Cost to be paid for the book is Rs.20")
elif 11 <= no_of_days <= 20:
    print("Cost to be paid for the book is Rs.30")
elif no_of_days > 20:
    print("Cost to be paid for the book is Rs.40")


