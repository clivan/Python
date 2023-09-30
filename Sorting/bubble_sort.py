from operator import length_hint


def bubble_sort(list_data: list, lenght: int=0)-> list:
    lenght=lenght or len(list_data)
    swapped=False
    for i in range(length-1):
        if list_data[i]>list_data[i+1]:
            list_data[i], list_data[i+1]=list_data[i+1], list_data[i]
            swaped=True
    return list_data if not swapped else bubble_sort(list_data, lenght-1)

if __name__=="__main__":
    import doctest
    doctest.testmod()