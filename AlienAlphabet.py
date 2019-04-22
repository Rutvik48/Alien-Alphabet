def getOutput(sender, text):

    list = []
    senderLen = len(sender)
    textlen = len(text)

    for i in range(senderLen):
        count = text.count(sender[i])
        if(count>0):
            for j in range (count):
                list.append(sender[i])
                text.replace(sender[i], "")

        count = text.count(sender[i].upper())

        if (count > 0):
            for j in range(count):
                list.append(sender[i].upper())
                text.replace(sender[i].upper(), "")

        if(len(text) == 0):
            break

    return ''.join(list)


if __name__ == '__main__':
    sender = input()
    text = input()
    #turnStr = ''.join()
    print(getOutput(sender, text))
