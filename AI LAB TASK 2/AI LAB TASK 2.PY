num = 1

while num <= 100:

    if num % 15 == 0:
        print("Fizz Buzz")

    elif num % 3 == 0:
        print("Fizz")

    elif num % 5 == 0:
        print("Buzz")

    else:
        print(num)

    num += 1

movies = [
 ("Eternal Sunshine of the Spotless Mind", 20000000),
 ("Memento", 9000000),
 ("Requiem for a Dream", 4500000),
 ("Pirates of the Caribbean: On Stranger Tides", 379000000),
 ("Avengers: Age of Ultron", 365000000),
 ("Avengers: Endgame", 356000000),
 ("Incredibles 2", 200000000)
]

budgets = []

for m in movies:
    budgets.append(m[1])

average = sum(budgets) / len(budgets)

print("Average Budget:", average)

higher = 0

for name, budget in movies:
    if budget > average:
        print(name, "budget is higher than average by", budget - average)
        higher += 1

print("Movies with higher budget than average:", higher)    