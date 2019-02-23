#统计元音字母数
def getCount(inputStr):

    list_vowels = ["a", "e", "i", "o", "u"]
    num_vowels = len([ch for ch in inputStr if ch in list_vowels])
    return num_vowels

#反转字符串
#多余5个字母的单词必须反转
def spinWords(inputStr):

    list_str = [ch if len(ch) < 5 else ch[::-1] for ch in inputStr.split()]
    return " ".join(list_str)

print("------getCount------")
print('%s -> %d' % ("abraca dabra", getCount("abraca dabra")))
print("------spinWords------")
print('%s -> %s' % ("Hey fellow warriors", spinWords("Hey fellow warriors")))
print('%s -> %s' % ("This is a test", spinWords("This is a test")))
print('%s -> %s' % ("This is another test", spinWords("This is another test")))