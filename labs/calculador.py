#calculador
#-array sum 
def convertToInt(lst):
    for i in range(0, len(lst)):
        lst[i] = int(lst[i])

    return lst 
    

expr = input("Entre com os numeros para soma: ")

if expr.find("+") :
    nums = expr.split("+")
    nums = convertToInt(nums)
    print(sum(nums))






