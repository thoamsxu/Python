import operator

#有序字符数
def ordered_count(tmpstr):
    chardict = dict()
    for x in tmpstr:
        if x in chardict:
            n = chardict[x] + 1
            chardict[x] = n
        else:
            chardict.update({x: 1})

    sorted_x = sorted(
        chardict.items(), key=operator.itemgetter(1), reverse=True)

    print(sorted_x)

#缩写双字名称
def abbrevName(strName):
    tempName = ""
    for word in strName.split():
        tempName = tempName + word[:1].upper() + "."
    if tempName != "":
        print(tempName[0:len(tempName) - 1])


ordered_count("abracadabraeeriqzaefhaieha")
abbrevName("Sam France")
