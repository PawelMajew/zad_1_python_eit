#Paweł Majewski EiT Programowanie w języku Python
#zad_10 unittesty

import unittest
import zad_10
import random


class MyTestCase(unittest.TestCase):
    def test_something(self):
        for index in range(100):
            tab = []
            temp_tab_1 = []
            for i in range(50):
                tab.append(random.randint(1, 200))
            for i in range(50):
                temp_tab_1.append(tab[i])

            zad_10.My_Sort(tab)  # my sort
            temp_tab_1.sort()  # correct sort
            self.assertEqual(tab, temp_tab_1)  # add assertion here


if __name__ == '__main__':
    unittest.main()
