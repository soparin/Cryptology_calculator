import numpy as np
from random import randint
from algebra_calculations import read_natur_num

class fibonach_gen:

    def __init__(self, level:int, mnum:int):
        self.seed = []
        self.sequence = []
        self.level = level
        self.mode = 2**mnum
        if level == 1:
            print("Level 1 (Easy)")
            self.__j_parameter = 24
            self.__k_parameter = 55
        else:
            print("Level 2 (Hard)")
            self.__j_parameter = 65
            self.__k_parameter = 71

        print(f"Seed will be randomly generated and saved in seed.txt")
        self.seed.clear()
        for i in range(self.__k_parameter):
            rnd = randint(0, self.mode)
            self.seed.append(rnd)
        with open('seed.txt', 'w', encoding='utf-8') as seed:
            seed.write(str(self.seed))
        print("Seed has saved in seed.txt")

    def generating(self, counter):
        self.sequence = self.seed
        for i in range(self.__k_parameter+1, counter+self.__k_parameter+1):
            self.sequence.append((self.sequence[i-self.__j_parameter] * 
                                self.sequence[i-self.__k_parameter])%self.mode)
        with open('generated.txt', 'w', encoding='utf-8') as seed:
            for num in self.seed:
                seed.write(str(num)+' ')
        print(self.seed)
        print("Generated sequence has saved in genetated.txt")
        return self.seed

