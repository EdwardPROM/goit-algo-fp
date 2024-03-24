import random

def monte_carlo_simulation(num_trials):
    # Створюємо словник для зберігання кількості випадінь кожної суми
    sums_count = {i: 0 for i in range(2, 13)}
    
    # Проводимо симуляцію num_trials разів
    for _ in range(num_trials):
        # Кидаємо два кубика та обчислюємо суму
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        # Збільшуємо лічильник для відповідної суми
        sums_count[total] += 1
    
    # Обчислюємо ймовірності кожної суми
    probabilities = {i: count / num_trials * 100 for i, count in sums_count.items()}
    
    return probabilities

# Виконуємо симуляцію з великою кількістю кидків
num_trials = 1000000
probabilities = monte_carlo_simulation(num_trials)
 
print("| Сума  | Монте-Карло |")
print("|-------|-------------|")
for total, probability in probabilities.items():
    print(f"| {total:<5} | {probability:>10.2f}% |")