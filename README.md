# Grocery-store-project
# Simple Grocery Store System

## Project Description

The Simple Grocery Store System is a basic Python command-line program that allows a user to manage a shopping cart and calculate the final grocery bill.

The program provides a list of available grocery items with their prices. The user can add items to the cart, remove items from the cart, and display the final bill. The program also automatically applies a discount based on the total purchase amount.

## Features

The project includes the following features:

1. Display available grocery items
2. Add an item to the cart
3. Remove an item from the cart
4. Calculate the total bill
5. Apply discount based on the total amount
6. Display the final bill
7. Exit the program

## Grocery Items

The program currently contains the following items:

| Item | Price |
|------|------:|
| Milk | Rs 60 |
| Bread | Rs 40 |
| Rice | Rs 90 |
| Eggs | Rs 70 |
| Sugar | Rs 45 |
| Apple | Rs 120 |

## Discount Rules

The program applies discounts according to the total purchase amount.

| Total Amount | Discount |
|-------------|----------|
| Less than Rs 500 | 0% |
| Rs 500 or more | 5% |
| Rs 1000 or more | 10% |

## Requirements

- Python 3
- No external Python libraries are required.

## How to Run

### Step 1: Open the project folder

Open the project folder in Visual Studio Code.

### Step 2: Open the terminal

In VS Code, select:

`Terminal → New Terminal`

### Step 3: Run the program

Use the following command:

```bash
python3 gocery.py
