#If one inch of rain falls on an acre of land, how many
#gallons of water have accumulated on that acre?

if __name__ == '__main__':
    inches_str = input('enter the inches of rain fall: ')
    inches_float = float(inches_str)

    volume = (inches_float / 12) * 43560
    gallons = volume * 7.5

    print('the calculated volume is of rain fall is: ',volume, '\n' 'and gallons accumulated rain is: ',gallons)
