#列表排序
def shell_sort(source):
    step = int(len(source) / 2)
    while step > 0:
        print("---step ---", step)

        for index in range(len(source)):
            compare_index = index + step
            if compare_index < len(source):
                current_val = source[index]
                if current_val > source[compare_index]:
                    source[index] = source[compare_index]
                    source[compare_index] = current_val
        step = int(step / 2)
    else:
        print(source)
        for index in range(1, len(source)):
            current_pos = index
            current_val = source[index]
            while current_pos > 0:
                if current_val < source[current_pos - 1]:
                    source[current_pos] = source[current_pos - 1]
                    source[current_pos - 1] = current_val
                current_pos -= 1
    return source


source = [8, 6, 4, 9, 7, 3, 2, -4, 0, -100, 99]
print(shell_sort(source))


#字符串逆序输出
def reverse_string(tmpstr):
    newstr = ""
    for index in range(len(tmpstr)):
        newstr = newstr + tmpstr[-1 - index]
    return newstr


tmpstr = "abcdefg"
print(tmpstr + " -->> " + reverse_string(tmpstr))


#seq[start:end:step] 开始:结束:步长
def get_primenum(maxnum):
    primelist = [True] * maxnum
    primelist[:2] = [False, False]  #0,1不是素数
    for i in range(2, int(maxnum / 2) + 1):
        if primelist[i]:
            primelist[i * i::i] = [False] * len(primelist[i * i::i])
    return ",".join([str(ch[0]) for ch in enumerate(primelist) if ch[1]])
print("----------- Prime Number in 100 -----------")
print(get_primenum(100))