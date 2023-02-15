if __name__ == '__main__':
    def make_pizza(size, *toppings):
        print('\nMaking a ' + str(size) + '-inch pizza with the following toppings:')
        for topping in toppings:
            print('-' + topping)
            