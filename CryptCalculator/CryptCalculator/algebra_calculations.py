from os import cpu_count
from alive_progress import alive_bar
import sys 
import time
import logging as log


from minimalistic_functions import *
from arithm_calculations import *

log.basicConfig(format="[ %(levelname)s ] %(message)s",
                    level=log.INFO, stream=sys.stdout)

def num_group_ord(mnum:int, mode:str, to_str=False):

    log.info(f"Order of numbers in group Z{mnum} is FINDING")
    
    if mode == '+':
    # a * ord a (mod m) = e(+) = 0
        with alive_bar(mnum - 1) as bar:
            start = time.time()
            prim_root_order = mnum
            ord_a = {i:1 for i in range(mnum) }
            for i in range(1, mnum):
                bar()
                ord_a[i] = int(mnum / GCD_min(mnum, i))
            finish = time.time()
    else:
    # a ^ ord a (mod m) = e(*) = 1
        prim_root_order = euler_func_min(mnum)
        countind_mode = read_natur_num("Chose a kind of counting: " +
                                   "brutforce - 1, algorithm - 2: ", "flag")
        with alive_bar(prim_root_order) as bar:
            start = time.time()
            ord_a = {i:1 for i in range(1, mnum) if GCD_min(i, mnum) == 1}
            for key  in ord_a.keys():
                bar()
                if countind_mode == 1:     # approximate point of equality
                    for i in range(1, mnum):
                        if (key ** i) % mnum == 1:
                            ord_a[key] = i
                            break
                elif countind_mode == 2:
                    ord_a[key] = mult_ord_finding(key, mnum)
                else:
                    log.info(f"Can't recognise an argument, algorithm will be in use")
                    ord_a[key] = mult_ord_finding(key, mnum)
            finish = time.time()
        
        
    log.info(f"Order of numbers in group Z{mnum} HAS FOUND")

    nums = list(ord_a.keys())
    ord_a_list = []
    for key in nums:
        ord_a_list.append(ord_a[key])
    if to_str:
        print(f"|Z{mnum}({mode})| = {prim_root_order}")
        print(f"a:\t", nums)
        print(f"ord a:", ord_a)
    else:
        log.info(f"|Z{mnum}({mode})| = {prim_root_order}")
        log.info(f"a:\t {nums}")
        log.info(f"ord a:  {ord_a_list}")
        log.info(f"time = {finish - start} seconds")

    return nums, ord_a_list

def mult_ord_finding(key:int, mnum:int):
    bases, powers = decomposition_min(euler_func_min(mnum))
    euler_coef = euler_func_min(mnum)
    ord_pows = powers                               # elements copying
    for i in range(len(powers)):
        substract = powers[i]
        while substract:
            if (key ** int(euler_coef/(bases[i]**substract))) % mnum == 1:
                ord_pows[i] -= substract
                break
            else:
                substract -= 1
    ord_a = 1
    for i in range(len(bases)):
        ord_a *= bases[i] ** ord_pows[i]
    return ord_a


def decompos_into_subgroups(mnum:int, mode:str, to_str=False):
    a_nums, ords_a = num_group_ord(mnum, mode)

    uniq_ords = dict()        # dict of unique ords and minimal nums with these
    for i in range(len(a_nums)):
        if ords_a[i] not in uniq_ords.keys():
            uniq_ords[ords_a[i]] = a_nums[i]
    
    subgroups_dict = dict()
    for uniq_ord in sorted(uniq_ords.keys()):
        subgrp_list = []
        if uniq_ord != 1:
            subgrp_list.clear()
            if mode == '+':
                for j in range(int(len(a_nums)/uniq_ord)):  # \/
                    j_list = []
                    for i in range(1,  uniq_ord + 1):
                        j_list.append((j + uniq_ords[uniq_ord] * i) % mnum)  
                    subgrp_list.append(sorted(j_list))
            else:
                for j in range(1, int(len(a_nums)/uniq_ord) + 1):  # \/
                    j_list = []
                    for i in range(1,  uniq_ord + 1):
                        j_list.append(j * (uniq_ords[uniq_ord] ** i) % mnum)  
                    subgrp_list.append(sorted(j_list))
        else:
            subgrp_list.clear()
            for i in a_nums:
                subgrp_list.append([i])

        subgroups_dict[uniq_ord] = subgrp_list      # {key = i:[[],[],...,[]]} 



    '''if to_str:
        print(f"|Z{mnum}({mode})| = {prim_root_order}")
        print(f"a:\t", nums)
        print(f"ord a:", ord_a)
    else:
        log.info(f"|Z{mnum}({mode})| = {prim_root_order}")
        log.info(f"a:\t {nums}")
        log.info(f"ord a:  {ord_a_list}")
        log.info(f"time = {finish - start} seconds")'''

    print(subgroups_dict)

    return subgroups_dict