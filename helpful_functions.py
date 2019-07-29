def return_complex_tuple_into_list(list_of_complex_tuples):
    normal_list = []

    for single_tuple in list_of_complex_tuples:
        complex_item = []
        for item in single_tuple:
            complex_item.append(item)
        normal_list.append(complex_item)

    return normal_list