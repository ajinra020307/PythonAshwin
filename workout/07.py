

def findTotalChars(para):
    output = {}
    for letter in para:
        if letter not in output:
            output[letter] = 1
        else:
            output[letter] = output[letter] + 1

    return output


para = 'fdsj lksdj lsd klsjfls dklf jsld lsdj lf sdl'
output = findTotalChars(para)
print(output)