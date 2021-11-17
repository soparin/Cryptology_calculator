"""
Файл, хранящий в себе дубликаты функций, не отчитывающиеся об успешном завершении

"""
from os import cpu_count
import sys 
import logging as log

log.basicConfig(format="[ %(levelname)s ] %(message)s",
                    level=log.INFO, stream=sys.stdout)

# Нахождение НОД
def GCD_min(anum:int, bnum:int):
    while anum != 0 and bnum != 0:
        if anum > bnum:
            anum %= bnum
        else:
            bnum %= anum
    if bnum == 0:
        return anum
    else:
        return bnum

# Каноничное разложение числа nnum на произведение
def decomposition_min(nnum:int):
    bases = set()
    baseIndexes = []
    i = 2
    while nnum > 0:
        index = 0
        while (nnum % i == 0):
            bases.add(i)
            nnum //= i
            index += 1
        i += 1
        if index:
            baseIndexes.append(index)
        if i > nnum:
            break
    bases = sorted(list(bases))
    return bases, baseIndexes

# Определение множества взаимно-простых чисел для числа nnum
def cop_num_set_min(nnum:int):
    sp_set = set()
    sp_set.add(1)
    for i in range(2, nnum):
        if GCD_min(i, nnum)==1:
            sp_set.add(i)
    return sp_set    

# Функция Эйлера от числа nnum
def euler_func_min(nnum:int):
    return len(cop_num_set_min(nnum))


def prim_root_min(mnum:int):
    bases, indexes = decomposition_min(mnum)
    result = ( (len(bases) == 1 and (bases[0] != 2 or 
                (bases[0] == 2 and indexes[0] <= 2))) or    # mnum is 2 or 4
            (len(bases) == 2 and (bases[0] == 2 and 
                indexes[0] == 1)) )                         # mnum is p^k or 2p^k
    if result:
        delta = euler_func_min(mnum)
        Pik = []                                # Pi| delta <-> (delta % Pik[i] = 0)

        for i in range(2, delta):
            if delta % i == 0:
                Pik.append(i)

        flag = False
        anum = 2
        while not flag:
            if GCD_min(anum, mnum) == 1:
                flag = True
                for ind in Pik:
                    if (anum ** ind) % mnum == 1:
                        flag = False
                        anum += 1
                        break
            else:
                anum += 1
        return anum
    else:
        return
    