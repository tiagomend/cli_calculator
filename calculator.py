from operation import operator_verification, interactive_addition

interaction_data = input("Digite uma operação matemática: ")
operantion_dict = operator_verification(interaction_data)
if operantion_dict["operator"] == "+":
    sum = interactive_addition(operantion_dict["operand"])
    print("Soma = {}".format(sum))