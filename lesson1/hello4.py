def helloworld():
    f = open('data.txt')
    name = f.read()
    message = 'Hello ' + name + ' !'
    print(message)

helloworld()
