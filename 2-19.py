def even_or_odd(number):
    tmp_list = ["EVEN", "ODD"]
    return tmp_list[abs(number % 2)]


def get_issuer(cardnumber):
    len_card = len(cardnumber)
    if (len_card == 13 or len_card == 16) and cardnumber[0] == "4":
        return "VISA"
    elif (len_card == 16) and (cardnumber[0:2] in [
            "51", "52", "53", "54", "55"
    ]):
        return "MasterCard"
    elif (len_card == 16) and (cardnumber[0:4] == "6011"):
        return "Discover"
    elif (len_card == 15) and (cardnumber[0:2] in ["34", "37"]):
        return "AMEX"
    else:
        return "Unknow"


print("5 is " + even_or_odd(5))
print("4 is " + even_or_odd(4))
print("4111111111111111 is " + get_issuer("4111111111111111"))
print("4111111111111 is " + get_issuer("4111111111111"))
print("4012888811111881 is " + get_issuer("4012888811111881"))
print("378282246310005 is " + get_issuer("378282246310005"))
print("6011111111111117 is " + get_issuer("6011111111111117"))
print("5105105110510510 is " + get_issuer("5105105110510510"))
print("5205105116510511 is " + get_issuer("5205105116510511"))
print("911111111111111 is " + get_issuer("911111111111111"))
