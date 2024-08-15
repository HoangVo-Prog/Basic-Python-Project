import re
import random
import sys


MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1
moneySpare_previousGame = 0

ROWS = 3
COLS = 3

symbol_count = {
    "A": 4,
    "B": 8,
    "C": 12,
    "D": 16,
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}


def check_winnings(columns, lines, total_bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * total_bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    print("@")
    print(columns)
    print("@")

    return columns


def get_bet():
    while True:
        bet = input(f"What would you like to bet on each line? $")
        if matches := re.search(r"^[0-9]*$", bet):
            bet = int(bet)
            if bet in range(MIN_BET, MAX_BET + 1):
                return bet
            else:
                print(f"Amount must be between (${MIN_BET}-${MAX_BET}).")
        else:
            print("Enter a valid amount of bet.")


def compare_totalBet_balance(balance, lines):
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(
                f"You do not enough to bet that amount, your current balance is: ${balance}."
            )
        else:
            return total_bet, bet


def get_number_of_line():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINE})? ")
        if matches := re.search(r"^[0-9]*$", lines):
            lines = int(lines)
            if lines in range(1, MAX_LINE + 1):
                return lines
            else:
                print(f"Line must be between (1-{MAX_LINE}).")
        else:
            print("Enter a valid number of lines.")


def spin(balance):
    lines = get_number_of_line()
    total_bet, bet = compare_totalBet_balance(balance, lines)

    print(
        f"You are betting ${bet} in {lines} lines. Total bet is equal to: ${total_bet}"
    )

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, total_bet, symbol_value)
    print(f"You won ${winnings}.")
    if winning_lines:
        print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if matches := re.search(r"^[0-9]*$", amount):
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")
        else:
            print("Deposit must be cash, please enter a number.")


def main():
    while True:
        print("Starting ...")
        global moneySpare_previousGame
        balance = deposit()
        balance += moneySpare_previousGame
        while True:
            print(f"Current balance is ${balance}")
            answer = input("Press enter to play (q to quit). ")
            if answer == "q":
                break
            balance += spin(balance)
            if balance < 3:
                print(f"Not enough money to make a spin. You left with ${balance}.")
                break
        print(f"You left with ${balance}. ")
        decision = input("Wanna play more (Y/N)? ")
        if decision == "N":
            print("See you")
            sys.exit("Ending ...")
        else:
            moneySpare_previousGame = balance


if __name__ == "__main__":
    main()
