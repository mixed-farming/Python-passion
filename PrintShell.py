while True:
    line = input('>>> ')
    if line=='quit':
        break
    if(line[0]=='#'):
        continue
    if line.find('print') != -1: #printing statement
        if line[0:7]=='print(\'' or line[0:7]=='print("':
            print(line[7:],'\b\b\b')
    else:
        print('NameError: name \'',end="")
        print(line,end="")
        print('\' is not deifned')
print('Done!')