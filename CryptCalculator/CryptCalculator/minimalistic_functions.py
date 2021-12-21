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

def reverse_elem_Zm_min(anum:int, mnum:int):
    if mnum < 1:
        log.info(f"Wrong value of nature number argument mnum = {mnum}")
        log.info ("BREAKING...")
        return
    if GCD_min(anum, mnum) != 1:
        log.info(f"({anum},{mnum}) != 1, numbers is not coprime")
        log.info(f"Sorry, {anum} have not a reverse element with module {mnum}")
        log.info ("BREAKING...")
        return
    unum = 0

    while((unum * (anum % mnum)) % mnum != 1):
        unum += 1

    return unum

def legendre_symbol_min(anum:int, pnum:int, to_str=False):
    if GCD_min(abs(anum), abs(pnum)) != 1:
        log.info(f"Sorry, the solution CAN'T BE FOUND, " +
                f"because GCD({abs(anum)},{pnum}) != 1")
        log.info ("BREAKING...")
        return

    leg_symb = 1
    if (anum * pnum < 0):
        leg_symb *= (-1) ** ((pnum - 1) / 2)
    processed_anum = abs(anum) % pnum
    bases, indexes = decomposition_min(processed_anum)
    for i in indexes:
        i %= 2
    for i in range(len(bases)):
        if indexes[i]:
            flag = ((bases[i] % pnum) ** int((pnum - 1) / 2)) % pnum
            if flag == (pnum - 1):
                flag = -1
            elif flag != 1:
                log.info(f"Ups, we have some problem: " +
                        f"Legendre symbol can't be {flag}")
                log.info(f"BREAKING...")
                return
            leg_symb *= flag
    if to_str:
        print(f"Legendre symbol of {anum}/{pnum} is {int(leg_symb)}")
    else:
        log.info(f"Legendre symbol of {anum}/{pnum} is {int(leg_symb)}")
    return int(leg_symb)
    