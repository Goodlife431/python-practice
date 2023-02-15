if __name__ == '__main__':
    # unconfirmed_user = ['alice', 'brian', 'candace']
    # confirmed_user = []
    #
    # while unconfirmed_user:
    #     current_user = unconfirmed_user.pop()
    #
    #     print('Verifying user: ' + current_user.title())
    #     confirmed_user.append(current_user)
    #     print('\n The following users have confirmed: ')
    #
    # for confirmed_user in confirmed_user:
    #     print(confirmed_user.title())

    responses = {}
    polling_active = True

    while polling_active:
        name = input('What is your name? ')
        response = input('Which mountain would you like to climb sometime? ')

        responses[name] = response

        repeat = input('Would you like to let another person respond (Yes/no) ')
        if repeat == 'no':
            polling_active = False

    print('\n ----Polling Result----')
    for name, response in responses.items():
        print(name + 'would like to climb' + response + '.')
