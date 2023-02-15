# def get_formatted_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# if __name__ == '__main__':
#     musician = get_formatted_name('simi', 'hendrix')
#     print(musician)
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


if __name__ == '__main__':
    musician = get_formatted_name('jimi', 'hendrix')
    print(musician)

    musician = get_formatted_name('john', 'hooker', 'lee')
    print(musician)