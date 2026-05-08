num = input("Enter the number: ")

total = 0
reverse = num[::-1]

for i in range(len(reverse)):
    digit = int(reverse[i])

    if i % 2 == 1:
        digit = digit * 2
        if digit > 9:
            digit = digit - 9

    total = total + digit

if total % 10 == 0:
    print("Valid number")
else:
    print("Invalid number")