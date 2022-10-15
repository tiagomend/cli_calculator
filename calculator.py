#!/usr/bin/python3

from sys import argv
from operation import subtraction, operator_verification, addition, multiplication, division

if len(argv) > 1:
    if argv[1] == "-a":
        operation = []
        for x in argv[2:]:
            operation.append(int(x))
        sum = addition(operation)
        print("Soma = {}".format(sum))

    elif argv[1] == "-s":
        try:
            operation = []
            for x in argv[2:]:
                operation.append(int(x))
            difference = subtraction(operation)
            print("Diferença = {}".format(difference))
        except:
            print("Atenção! Passe como parâmetro, números separados por espaço.")
            print("Ex.: -a 10 10 retornará o valor 20")

    elif argv[1] == "-m":
        operation = []
        for x in argv[2:]:
            operation.append(int(x))
        produto = multiplication(operation)
        print("Produto = {}".format(produto))
    
    elif argv[1] == "-d":
        operation = []
        for x in argv[2:]:
            operation.append(int(x))
        quotient = division(operation)
        print("Quociente = {}".format(quotient))

else:
    interaction_data = input("Digite uma operação matemática: ")
    operation_dict = operator_verification(interaction_data)
    if operation_dict["operator"] == "+":
        sum = addition(operation_dict["operand"])
        print("Soma = {}".format(sum))

    elif operation_dict["operator"] == "-":
        difference = subtraction(operation_dict["operand"])
        print("Diferença = {}".format(difference))

    elif operation_dict["operator"] == "*":
        produto = multiplication(operation_dict["operand"])
        print("Produto = {}".format(produto))

    elif operation_dict["operator"] == "/":
        quotient = division(operation_dict["operand"])
        print("Quociente = {}".format(quotient))
