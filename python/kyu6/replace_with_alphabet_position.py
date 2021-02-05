# https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text: str) -> str:
    abc = "abcdefghijklmnopqrstuvwxyz"
    ret = ""
    for letter in text:
        found = abc.find(letter.lower())
        if found != -1:
            ret += str(found + 1) + " "

    return ret.strip()


t = alphabet_position("The sunset sets at twelve o' clock.")
if t == '20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11':
    print("SUCESS")
else:
    print("ERROR")