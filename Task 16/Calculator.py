# Write a simple calculator program

import logging
from datetime import datetime
import os

log_file = 'calculator_operations.txt'

logging.basicConfig(filename=log_file, filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(message)s',datefmt='%d/%m/%Y %I:%M:%S %p')
logging.info("-----------------------------------")
logging.info('Calculator Program Start.')


def add(a, b):
    logging.info(f"The value of num1 and num2 is {a} and {b}.")
    try:
        Result = a + b
        logging.info(f"Addition Operation Successful : {Result}")
    except ZeroDivisionError as err:
        logging.error("Zero Division Error",exc_info="True")
    return Result

def sub(a, b):
    logging.info(f"The value of num1 and num2 is {a} and {b}.")
    try:
        Result =  a - b
        logging.info(f"Substaction Operation Successful: {a} - {b} = {Result}")
    except ZeroDivisionError as err:
        logging.error("Zero Division Error",exc_info="True")
    return Result

def multi(a, b):
    logging.info(f"The value of num1 and num2 is {a} and {b}.")
    try:
        Result =  a * b
        logging.info(f"Multiplication Operation : {a} * {b} = {Result}")
    except ZeroDivisionError as err:
        logging.error("Zero Division Error",exc_info="True")
    return Result

def divi(a, b):
    logging.info(f"The value of num1 and num2 is {a} and {b}.")
    if b == 0:
        logging.error(f"Error Division by Zero {a} / {b}")
        return "Error! Division by Zero"
    try:
        Result =  a / b
        logging.info(f"Division Operation : {a} / {b} = {Result}")
    except ZeroDivisionError as err:
        logging.error("Zero Division Error",exc_info="True")
    return Result

def Modulo(a, b):
    logging.info(f"The value of num1 and num2 is {a} and {b}.")
    try:
        Result = a % b
        logging.info(f"Modulo Operation : {a} % {b} = {Result}")
    except ZeroDivisionError as err:
        logging.error("Zero Division Error",exc_info="True")
    return Result

def get_input(prompt):
    while True:
        value = input(prompt)
        if not value:
            logging.error("Empty Input Error.")
            print("Value can not be Empty Please Enter valid Input.")
            continue
        try:
            return float(value)
        except ValueError as v:
            logging.error(f"Invalid Value Input error {v}")
            print(f"Error {v}, Please enter valid input.")

def Calculator():
    while True:
        print("------------------")
        print("Select Operation to Perform Calculation:")
        print("'+'. Addition")
        print("'-'. Subtraction")
        print("'*'. Multiplication")
        print("'/'. Division")
        print("'%'. Modulo")
        print("'0'. Exit")
        print("------------------")

        choice = input("Enter choice (+/-/*///%/0): ")

        if choice not in ['+', '-', '*', '/', '%','0']:
            print("Invalid choice! Please enter a choice between (+/-/*///%/0).")
            continue

        if choice == '0':
            print("Exiting the application. Thank You.")
            logging.info("Calculator Program End.")
            break

        num1 = float(get_input("Enter First number: "))
        num2 = float(get_input("Enter Second number: "))

        if choice == '+':
            Result = add(num1, num2)
            print(f"{num1} + {num2} = {Result}")
        elif choice == '-':
            Result = sub(num1, num2)
            print(f"{num1} - {num2} = {Result}")
        elif choice == '*':
            Result = multi(num1, num2)
            print(f"{num1} * {num2} = {Result}")
        elif choice == '/':
            Result = divi(num1, num2)
            print(f"{num1} / {num2} = {Result}")
        elif choice == '%':
            Result = Modulo(num1, num2)
            print(f"{num1} % {num2} = {Result}")


# Entry point for the calculator program
if __name__ == "__main__":
    Calculator()
