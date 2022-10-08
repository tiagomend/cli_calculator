from numpy import product
from operation import interactive_subtraction, operator_verification, interactive_addition, interactive_multiplication, interactive_division

interaction_data = input("Digite uma operação matemática: ")
operantion_dict = operator_verification(interaction_data)
if operantion_dict["operator"] == "+":
    sum = interactive_addition(operantion_dict["operand"])
    print("Soma = {}".format(sum))

elif operantion_dict["operator"] == "-":
    difference = interactive_subtraction(operantion_dict["operand"])
    print("Diferença = {}".format(difference))

elif operantion_dict["operator"] == "*":
    produto = interactive_multiplication(operantion_dict["operand"])
    print("Produto = {}".format(produto))

elif operantion_dict["operator"] == "/":
    quotient = interactive_division(operantion_dict["operand"])
    print("Quociente = {}".format(quotient))
