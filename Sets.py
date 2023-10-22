import random

if __name__ == '__main__':
    con_a = {1, 2, 3, 4, 5}
    try:
        print(con_a[0])
    except TypeError:
        print('Sets são indexáveis.')

    list_num = []
    
    for num in range(100):
        list_num.append(random.randint(1, 50))
    print(list_num)
