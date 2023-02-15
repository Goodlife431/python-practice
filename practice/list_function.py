if __name__ == '__main__':
    # unprinted = ['iphone case', 'robot pendant', 'dodecahedron']
    # completed_models = []
    #
    # while unprinted:
    #     current_design = unprinted.pop()
    #     print('printing model: ' + current_design)
    #     completed_models.append(current_design)
    # print('\nThe following models have been printed: ')
    # for completed_model in completed_models:
    #     print(completed_model)
    def build_profile(first, last, **user_info):
        profile = {}
        profile['first_name'] = first
        profile['first_name'] = last
        for key, value in user_info.items():
            profile[key] = value
        return profile
    user_profile = build_profile('albert', 'einstein',
                                 location= 'princeton',
                                 field= 'pysics')
    print(user_profile)