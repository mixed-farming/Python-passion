while True:
    line = input('>>> ')
    if line=='quit':
        break
    if(line[0]=='#'):
        continue
    if line.find('print') != -1: #printing statement
        if (line[0:7]=='print(\''and line[len(line)-2]=='\'' and line[len(line)-1]==')') or (line[0:7]=='print("' and line[len(line)-2]=='"' and line[len(line)-1]==')'):
            print(line[7:len(line)-2])
        else:
            print('SyntaxError')
    else:
        print('NameError: name \'',end="")
        print(line,end="")
        print('\' is not deifned')
print('Done!')
