def bank(x, y):
    rate = 0.10
    for _ in range(y):
        x += x * rate
    return x

initial_deposit = 1000
years = 5
final_amount = bank(initial_deposit, years)
print(f'Суммана счету через {years} лет будет: {final_amount} рублей')