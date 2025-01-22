import pandas as pd

data = {
    "PRODUCT": ["Margarita", "Caesar Salad", "Beef Steak", "Spring Rolls", "Iced Tea", "Grilled Chicken", "Fruit Salad", "Shrimp Cocktail", "Espresso", "Veggie Burger", "Greek Salad", "Chicken Wings", "Lemonade", "Fish and Chips", "Caprese Salad", "Bruschetta", "Green Tea", "Pork Chop", "Cobb Salad", "Nachos"],
    "CATEGORY": ["Drink", "Salad", "Main", "Appetizer", "Drink", "Main", "Salad", "Appetizer", "Drink", "Main", "Salad", "Appetizer", "Drink", "Main", "Salad", "Appetizer", "Drink", "Main", "Salad", "Appetizer"],
    "PRICE": [12, 18, 60, 10, 8, 45, 12, 22, 6, 35, 16, 20, 7, 40, 14, 12, 5, 50, 17, 15],
    "AVG RATING": [8, 7, 9, 6, 5, 8, 7, 7, 6, 7, 8, 6, 7, 8, 7, 6, 5, 8, 7, 6],
    "PROFIT": [28000.00, 15000.00, 75000.00, 12000.00, 9000.00, 50000.00, 11000.00, 18000.00, 8000.00, 22000.00, 13000.00, 14000.00, 10000.00, 30000.00, 12000.00, 11000.00, 7000.00, 40000.00, 14000.00, 13000.00]
}

df = pd.DataFrame(data)
df.to_excel("sales_report.xlsx", index=False)