#Paweł Majewski EiT Programowanie w języku Python
#zad_19
# Zaimplementuj wielowątkowe liczenie histogramu

from random import randint
import threading
import time


def rand_tab():
    data = []
    for index in range(100):
        data.append(randint(-11, 10))
    print(data)
    print("\n")
    return data


def histogram_thread(input_tab, min_value, output_tab):
    for d in input_tab:
        output_tab[d + min_value] += 1


def print_result(val_1, val_2):
    print_value = []
    for i in range(len(val_1)):
        print_value.append(val_1[i] + val_2[i])
    print(print_value)


def return_tab_with_args():
    temp_tab_data = []
    rand_data = rand_tab()
    min_val = min(rand_data)
    max_val = max(rand_data)
    data_size = len(rand_data)
    temp_tab_data.append(rand_data[0:int(data_size / 2)])
    temp_tab_data.append(rand_data[int(-data_size / 2):])
    temp_tab_data.append([0] * (max_val - min_val + 1))
    temp_tab_data.append([0] * (max_val - min_val + 1))
    temp_tab_data.append(min_val)
    return temp_tab_data


def main():

    tab_data = return_tab_with_args()

    time.sleep(5)
    t1 = threading.Thread(target=histogram_thread, args=(tab_data[0], tab_data[4], tab_data[2],))
    t2 = threading.Thread(target=histogram_thread, args=(tab_data[1], tab_data[4], tab_data[3],))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print_result(tab_data[2], tab_data[3])


if __name__ == '__main__':
    main()
