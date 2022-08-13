def greet(lang,name):
    if lang=='welcome':
        print('Hey ',name)
    elif lang=='bid':
        print('byeee',name)

name1='manoj'
name2='mayur'

greet('welcome',name1)
greet('bid',name1)
print('\n')
greet('welcome',name2)
greet('bid',name2)
