def getInput():
    str_ = input("Введте что-нибудь: ")
    return str_

def testInput(k):
    try:
        k = int(k)
        return True
    except:
        return False

def strTolnt(k):
    return int(k)

def printInt(k):
    print(k)

str_ = getInput()
if testInput(str_): printInt(strTolnt(str_))