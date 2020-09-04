string = input()

lowercaseChars = []
uppercaseChars = []
oddDigits = []
evenDigits = []

for i in string:
    if i.islower():
        lowercaseChars.append(i)
    elif i.isupper():
        uppercaseChars.append(i)
    elif i.isalnum:
        if int(i)%2==1:
            oddDigits.append(i)
        else:
            evenDigits.append(i)

lowercaseChars.sort()
uppercaseChars.sort()
oddDigits.sort()
evenDigits.sort()
print("".join(lowercaseChars)+"".join(uppercaseChars)+"".join(oddDigits)+"".join(evenDigits))
