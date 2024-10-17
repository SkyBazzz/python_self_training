# time complexity logN
# Omega notation On

sorted_data = list(range(1, 1004))
SEARCH_VALUE = 6

ATTEMPTS = 1

LOW = 0
high = len(sorted_data) - 1
while LOW < high:
    middle = (LOW + high) // 2

    guess = sorted_data[middle]
    print("Guess it's -", guess)
    if SEARCH_VALUE == guess:
        break
    if SEARCH_VALUE < guess:
        high = middle - 1
    elif SEARCH_VALUE > guess:
        LOW = middle + 1

    ATTEMPTS += 1

print(ATTEMPTS)
