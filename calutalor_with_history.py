HISTORY_FILE = "history.tx"

def show_history():
    file = open (HISTORY_FILE, "r")
    lines =file.readlines()
    file.close()
    if len == 0:
        print("No history found!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close

def clear_history():
    file = open (HISTORY_FILE, "w")
    file.close()
    print("History cleared.")

def save_to_history(equation,result):
    file = open (HISTORY_FILE, "a")
    file.write(equation + "=" + str(result) +"\n")
    file.close()

def calculator(user_input):
    parts = user_input.split()
    if len(parts) !=3:
        print('Invalid input. Use format: number operator number e.g. 8+8')
        return

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("you cannot divide")
        return
    else:
        print("INVALID OPERATOR. USE ONLY +-*/")
        return
    if int(result) == result:
        result = int(result)
    print("RESULT", result)
    save_to_history(user_input, result)

def main():
    print("Welcome to the calculator with history!")
    while True:
        user_input = input("enter calculation (+,-,*,/) or command (history,clear,exit):")
        if user_input == "exit":
            print('GOODBYE')
            break
        elif user_input == "clear":
            clear_history()
        elif user_input == "history":
            show_history()
        else:
            calculator(user_input)
main()
