def next_id(num_list):

    if len(num_list) == 0:
        return 0
    else:
        for i in range(len(num_list) + 1):
            if i not in num_list:
                return i


def get_middle(tmpstr):
    if tmpstr == "":
        return "NULL"
    else:
        pos = int(len(tmpstr) / 2)
        if len(tmpstr) % 2 == 0:
            return tmpstr[pos - 1:pos + 1]
        else:
            return tmpstr[pos]


print("[         ] next id is " + str(next_id([])))
print("[0,1,2,3,4] next id is " + str(next_id([0, 1, 2, 3, 4])))
print("[5,4,3,2,1] next id is " + str(next_id([5, 4, 3, 2, 1])))
print("[0,0,0,0,0] next id is " + str(next_id([0, 0, 0, 0, 0])))
print("[0,1,2,3,5] next id is " + str(next_id([0, 1, 2, 3, 5])))
print("test is " + get_middle("test"))
print("testing is " + get_middle("testing"))
print("middle is " + get_middle("middle"))
print("A is " + get_middle("A"))
print("of is " + get_middle("of"))
print(" is " + get_middle(""))
