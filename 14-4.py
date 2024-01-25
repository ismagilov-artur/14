def whoAreYouAndHello():
    x = input()
    while not all([x.isalpha(), x.istitle(), len(x.split()) == 1, x[1:].islower()]):
        x = input()
    print('Привет, {}!'.format(x))


whoAreYouAndHello()