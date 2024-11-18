import sys
import ast

def quantization(array, bits, alpha, beta):
    #Scaling Factor of Equation (2)
    #Divides a given range of real values r into a number of partitions.

    quantizedVector = []

    S = (beta - alpha) / ((2**bits) - 1) #Equation (4) in paper
    for r in array:
        qValue = (int(r/S) - 0) #Assuming we don't have a Zero Point Integer
        quantizedVector.append(qValue)
    return quantizedVector

if __name__ == "__main__":
    if len(sys.argv) > 1:
        array = ast.literal_eval(sys.argv[1])  #Convert the input string to a list
        bits = int(sys.argv[2])
        beta = float(sys.argv[3])
        alpha = float(sys.argv[4])


        result = quantization(array, bits, alpha, beta)

        #Compare Result with Expected Result
        print(result)
        print("Expected Result: [63, -127, 127, 0, 84, 57, 104]")

    #else:
    #    print("Missing arguments, please use this format: python3 input.py array bits beta alpha")
