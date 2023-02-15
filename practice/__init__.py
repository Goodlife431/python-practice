if __name__ == '__main__':
    # alien_0 = {'color': 'green', 'points': 5}
    # alien_1 = {'color': 'yellow', 'points': 10}
    # alien_2 = {'color': 'red', 'points': 15}
    #
    # aliens = [alien_0, alien_1, alien_2]
    #
    # for i in aliens:
    #     print(i)
    # aliens = []
    #
    # for i in range(30):
    #     new_aliens = {'color': 'green', 'point': 5, 'speed': 'slow'}
    #     aliens.append(new_aliens)
    # for alien in aliens[5:10]:
    #     if alien['color'] == 'green':
    #         alien['color'] = 'yellow'
    #         alien['speed'] = 'medium'
    #         alien['point'] = 10
    #     print(alien)
    # for x in aliens[:5]:
    #     print(x)
    # print('.....')
    # print('Total number of aliens: ' + str(len(aliens)))

    # pizza = {
    #     'crust': 'thick',
    #     'toppings': ['mushrooms', 'extra cheese'],
    # }
    # active = True
    # while active:
    #     message = input()
    #     if message == "quit":
    #         active = False
    #     else:
    #         print(message)

    current_number = 0
    while current_number != 10:
        current_number += 1
        if current_number % 2 == 0:
            continue
        print(current_number)


