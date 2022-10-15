"""
    Neste arquivo estão todas as funções necessárias para
    as operações matemáticas suportadas pelo CLI_CALCULATOR.
"""


def operator_verification(data_str):
    """
        Essa função recebe como parâmetro uma string que contêm a
        operação desejada pelo usuário. Uma string recebida no formato
        ex: 10 + 12 + 13. A função separa os operadores dos operando e retorna
        um dictionary contendo os dados separados.
    """
    if " " in data_str:
        operation_data = data_str.split()
        operand = []
        for iterate in operation_data:
            if iterate.isnumeric():
                operand.append(iterate)
            elif (iterate == "+") or (iterate == "-") or (iterate == "*") or (iterate == "/") or (iterate == "^"):
                operator = iterate
        operation_dict = {
            "operand": operand,
            "operator": operator
        }
        return operation_dict


def addition(operand):
    sum = 0
    for x in operand:
        sum += int(x)
    return sum

def subtraction(operand):
    difference = int(operand[0])
    operand = list(operand[1:])
    for x in operand:
        difference = difference - int(x)
    return difference

def multiplication(operand):
    product = int(operand[0])
    operand = list(operand[1:])
    for x in operand:
        product = product * int(x)
    return product

def division(operand):
    quotient = int(operand[0])
    operand = list(operand[1:])
    for x in operand:
        quotient = quotient / int(x)
    return quotient
