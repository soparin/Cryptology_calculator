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
        if mnum >= 1000:
            countind_mode = read_natur_num("Chose a kind of counting: " +
                                   "brutforce - 1, algorithm - 2: ", "flag")
        else:
            countind_mode = 1
        with alive_bar(prim_root_order) as bar:
            start = time.time()
            ord_a = {i:1 for i in range(1, mnum) if GCD_min(i, mnum) == 1}
            for key  in ord_a.keys():
                bar()
                if countind_mode == 1:
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
        log.info(f"time = {finish - start} sec.")

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

    if to_str:
        pass
    else:
        if mode == '+':
            for sb_key in subgroups_dict.keys():
                counter = list(subgroups_dict.keys()).index(sb_key) + 1
                output_str = f"ord {uniq_ords[sb_key]} = {sb_key}: H{counter} = " + \
                    f"{subgroups_dict[sb_key][0]} |H{counter}| = {i}, [Z{mnum}({mode}):" + \
                    f"H{counter}] = {int(mnum / len(subgroups_dict[sb_key][0]))}"
                related_classes_strs = []
                for rl_class in range(len(subgroups_dict[sb_key][1:])):
                    related_classes_str = f"a = {int(subgroups_dict[sb_key][1:][rl_class][0] - subgroups_dict[sb_key][0][0])}" + \
                    f" is not included in H{counter}: {subgroups_dict[sb_key][1:][rl_class]}"
                    related_classes_strs.append(related_classes_str)
                log.info(output_str)
                for one_str in related_classes_strs:
                    log.info(one_str)
        else:
            for sb_key in subgroups_dict.keys():
                counter = list(subgroups_dict.keys()).index(sb_key) + 1
                output_str = f"ord {uniq_ords[sb_key]} = {sb_key}: H{counter} = " + \
                    f"{subgroups_dict[sb_key][0]} |H{counter}| = {i}, [Z{mnum}({mode}):" + \
                    f"H{counter}] = {int(euler_func_min(mnum) / len(subgroups_dict[sb_key][0]))}"
                related_classes_strs = []
                for rl_class in range(len(subgroups_dict[sb_key][1:])):
                    related_classes_str = f"a = {int(subgroups_dict[sb_key][1:][rl_class][0]/subgroups_dict[sb_key][0][0])}" + \
                    f" is not included in H{counter}: {subgroups_dict[sb_key][1:][rl_class]}"
                    related_classes_strs.append(related_classes_str)
                log.info(output_str)
                for one_str in related_classes_strs:
                    log.info(one_str)    

    return subgroups_dict

def elipt_polinom(mnum:int):
    nums = []
    for x in range(23):
        for y in range(23):
            if (y**2)%mnum == (x**3+x+1)%mnum:
                nums.append((x, y))

    out_str = ""
    for i in range(0,(len(nums)//8)*8,8):
        for j in range(8):
            out_str += (str(nums[i+j]) + "  ")
        out_str += '\n'
    

    for j in range(len(nums) - (len(nums)//8)*8+1):
        out_str += str(nums[(len(nums)//8)*8+j-1]) + "  "

    print(out_str)
    return