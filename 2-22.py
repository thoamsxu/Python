def capitals(word):
    return [
        index for index in range(len(word))
        if word[index] == word[index].upper()
    ]


print("====== CodEWaRs ======")
print(capitals("CodEWaRs"))


def digital_root(inputNumber):
    print("====== digital root " + str(inputNumber) + " ======")
    int_result = inputNumber
    while (int_result >= 10):
        str_num = str(int_result)
        list_num = [int(str_num[index]) for index in range(len(str_num))]
        int_result = sum(list_num)

        print("=> " + " + ".join(map(str, list_num)))
        print("=> %d" % int_result)

#递归
def digital_root1(inputNumber):
    if inputNumber < 10:
        print("=> ", inputNumber)
        return inputNumber
    else:
        arr = list(str(inputNumber))
        print(" + ".join(arr))
        num_sum = sum(map(int, arr))
        if (num_sum > 10):
            print("=> ", num_sum, " ...")
        digital_root1(num_sum)


number1 = 16
number2 = 942
number3 = 132189
number4 = 493193
digital_root1(number1)
digital_root1(number2)
digital_root1(number3)
digital_root1(number4)