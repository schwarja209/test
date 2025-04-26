def divide_inputs(input1, input2):
    num1 = float(input1)
    num2 = float(input2)
    return num1 / num2
def get_inputs():
    input1 = input("Enter the first number: ")
    input2 = input("Enter the second number: ")
    result = divide_inputs(input1, input2)
    print(result)