# class Dog():
#     def __int__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(self.name.title() + " is now sitting.")
#
#     def roll_over(self):
#         print(self.name.title() + "rolled over! ")
def describe_pet(animal_type, pet_name):
    print('\n I have' + animal_type + '.')
    print('My ' + animal_type + 'name is ' + pet_name.title() + '.')


describe_pet(animal_type='hamster', pet_name='harry')


