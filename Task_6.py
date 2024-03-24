def greedy_algorithm(items, budget):
  # Сортування страв за співвідношенням калорійності до вартості
  sorted_items = sorted(items.keys(), key=lambda item: items[item]["calories"] / items[item]["cost"], reverse=True)
  
  chosen_items = []
  remaining_budget = budget
  
  for item in sorted_items:
    if items[item]["cost"] <= remaining_budget:
      chosen_items.append(item)
      remaining_budget -= items[item]["cost"]
  
  return chosen_items

def dynamic_programming(items, budget):
  # Створення таблиці DP
  dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]
  
  # Заповнення таблиці DP
  for i in range(1, len(items) + 1):
    for j in range(1, budget + 1):
      item = items[list(items.keys())[i - 1]]
      cost = item["cost"]
      calories = item["calories"]
      
      if cost > j:
        dp[i][j] = dp[i - 1][j]
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
  
  # Відновлення оптимального набору страв
  chosen_items = []
  i = len(items)
  j = budget
  
  while i > 0 and j > 0:
    if dp[i][j] != dp[i - 1][j]:
      chosen_items.append(list(items.keys())[i - 1])
      j -= items[list(items.keys())[i - 1]]["cost"]
    i -= 1
  
  return chosen_items


# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100

chosen_items = greedy_algorithm(items, budget)
chosen_items = dynamic_programming(items, budget)
print("Жадібний алгоритм:", chosen_items)
print("Алгоритм динамічного програмування:", chosen_items)