# User will deposit some amount of money
# And then will allow them to bet on two or three lines in slot machine 
# if they got any line which are the same we are just going to multiply
# their bet by the value of the line and add the value to theri balance
# and allow them to keep play untill they cash out 

import random 


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3 
COLS = 3

symbol_count={
    "A" : 2 ,
    "B" : 4 ,
    "C" : 6,
    "D" : 8
}

symbol_value={
    "A" : 5 ,
    "B" : 4 ,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns , lines , bet , values):
    winnings =0
    winning_lines = []
    for line in range(lines):
        symbol= columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line +1)
    return winnings  , winning_lines


def get_slot_machine_spin(rows , cols, symbols):
    all_symbols = []
    for symbol , symbol_count in symbols .items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    
    columns = []
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            column.append(value)
        
        columns.append(column)

    return columns 



def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i , column in enumerate(columns):
            if i != len(columns)- 1:
                print(column[row], end=" | ")
            else:
                print(column[row] , end="")


        print()
    

     
    



def deposit():
    while True:
        amount=input("What would you like to deposit ?? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print("Amont must be greater than 0 ")
        else:
            print("Please enter a number.")

    return amount 


def get_number_of_lines():
    while True:
        lines=input("Enter the number of lines to bet on (1-" +str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines<=MAX_LINES :
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount=input("What would you like to bet on each line ?? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}. ")
        else:
            print("Please enter a number.")

    return amount 

def spin(balance):
    liness = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet= bet * liness

        if total_bet > balance:
           print(f"You do not have enough balance to bet that amount , your current balance is {balance}")
        else:
            break   

    print(f"you are betting ${bet} on {liness} lines . Total bet is equal to {total_bet}")

    # print(balance , liness)


    slots=get_slot_machine_spin(ROWS , COLS, symbol_count)  
    print_slot_machine(slots)
    winnings , winning_lines = check_winnings(slots , liness , bet , symbol_value)
    print( f"You won ${winnings}.")
    print(f" You won on lines :" , *winning_lines)
    return winnings - total_bet


                

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play( press 'q' to quit)")
        if spin == "q":
            break
        balance += spin(balance)


   



main()
                





