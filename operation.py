
def operator_verification(data_str):
    if " " in data_str:
        operation_data = data_str.split()
        operand = []
        for iterate in operation_data:
            if iterate.isnumeric():
                operand.append(iterate)
            elif iterate == "+" or iterate == "-" or iterate == "*" or iterate == "/" or iterate == "^":
                operator = iterate
        operation_dict = {
            "operand": operand,
            "operator": operator
        }
        return operation_dict

def interactive_addition(operand):
    sum = 0
    for x in operand:
        sum += int(x)
    return sum
