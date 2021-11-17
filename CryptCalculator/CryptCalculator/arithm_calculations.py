from os import cpu_count
import sys 
import logging as log

from minimalistic_functions import *

log.basicConfig(format="[ %(levelname)s ] %(message)s",
                    level=log.INFO, stream=sys.stdout)

def read_natur_num(output_str, arg):
    while(1):
        flag = 0
        input_str = input(output_str).replace(' ','')
        for c in input_str:
            if not c.isdigit():
                print("There are no-digital symbols in the input")
                flag = 1
                break
        if not flag:
            if input_str.isdigit():
                if int(input_str) > 0:
                    n = int(input_str)
                    break
                else:
                    print("Wrong number.")
                    input("Press ENTER to exit to the menu")
                    continue
            else:
                print("Use only natural numbers, please")
                input(f"Press ENTER to correct the argument {arg} ")
                continue
    return n

def read_num(output_str, arg):
    while(1):
        flag = 0
        negative = 1
        input_str = input(output_str).replace(' ','')
        if '-' in input_str:
            negative = -1
            input_str = input_str.replace('-','')
        for c in input_str:
            if not c.isdigit():
                print("There are no-digital symbols in the input")
                flag = 1
                break
        if not flag:
            if input_str.isdigit():
                n = int(input_str)
                break
            else:
                print("Can't read the input like a digit")
                input(f"Press ENTER to correct the argument {arg} ")
                continue
    return negative*n

# Нахождение наибольшего общего делителя (anum, bnum) = НОД
def euclid_GCD(anum:int, bnum:int, to_str=False):
    atemp, btemp = anum, bnum
    log.info("Euclidean algorithm is RUNNING")
    while anum != 0 and bnum != 0:
        if anum > bnum:
            anum %= bnum
        else:
            bnum %= anum
    if to_str:
        print(f"({atemp},{btemp}) = {max(anum, bnum)}")
    else:
        log.info(f"({atemp},{btemp}) = {max(anum, bnum)}")
    log.info("Euclidean algorithm HAS COMPLITED\n")            
    if bnum == 0:
        return anum
    else:
        return bnum

# Расширенный алгоритм Евклида
# (anum,bnum) = anum*unum + bnum*vnum = NOD
def extended_euclid(anum:int, bnum:int, to_str=False):
    unum, x, vnum, y = 1, 0, 0, 1
    atemp, btemp = anum, bnum
    log.info("Extended Euclidean algorithm is RUNNING")
    while bnum:
        q = anum // bnum
        (anum, bnum) = (bnum, anum % bnum)
        (unum, x) = (x, unum - x*q)
        (vnum, y) = (y, vnum - y*q)
    if to_str:
        print(f"({atemp},{btemp}) = {anum}")
        print(f"{atemp} * {unum} + {btemp} * {vnum} = {anum}")
    else:
        log.info(f"({atemp},{btemp}) = {anum}")
        log.info(f"{atemp} * {unum} + {btemp} * {vnum} = {anum}")
    log.info("Extended Euclidean algorithm HAS COMPLITED\n")
    return (unum, vnum, anum)

# Решето Эратосфена для нахождения списка простых чисел до границы nnum
def eratosthenes(nnum:int, to_str=False):

    log.info(f"Eratosthen screen to N = {nnum} is RUNNING")
    if nnum > 10**8:
        log.info("Counting is not recomended")
        return eratosthenes (10**8) 
    screen = list(i + 1 for i in range(nnum))
    for i in screen:
        if i > 1:
            for j in range(i + i, len(screen), i):
                screen[j] = 0
    simples = [x for x in screen if x != 0]
    log.info("A list with simple numbers HAS CREATED")
    if to_str:
        ans = input("Do you want to print all numbers? y/n: ")
        if ans == 'y':
            print(simples)
        elif ans == 'n':
            print(f"{simples[0]}, {simples[1]}, {simples[2]}, {simples[3]}, . . . , " +
                f"{simples[len(simples)-2]}, {simples[len(simples)-1]}")
    else:
        log.info(f"{simples[0]}, {simples[1]}, {simples[2]}, {simples[3]}, . . . , " +
                f"{simples[len(simples)-2]}, {simples[len(simples)-1]}")
    log.info(f"Eratosthen screen to N = {nnum} HAS COMPLITED\n")
    return simples

# Каноничное разложение числа nnum на произведение 
# степенных функций от простых чисел ... * (bases[i]^base_indexes[i]) * ...

def decomposition(nnum:int, to_str=False):
    log.info(f"Canonical decomposition of {nnum} is RUNNING")
    if nnum == 1:
        if to_str:
            print("1 is simple number")
        else:
            log.info("1 is simple number")
        return [1],[1]
    temp = nnum
    bases = set()
    base_indexes = []
    i = 2
    while nnum > 0:
        index = 0
        while (nnum % i == 0):
            bases.add(i)
            nnum //= i
            index += 1
        i += 1
        if index:
            base_indexes.append(index)
        if i > nnum:
            break
    bases = sorted(list(bases))
    log.info(f"Canonical decomposition of {temp} HAS COMPLITED")
    if to_str:
        show = f"{temp} ="
        for i in range(len(bases)):
            show += f" {bases[i]}^{base_indexes[i]} *"
        print(show[:-1])
    else:
        log.info("Bases: " + str(bases))
        log.info("Indexes: " + str(base_indexes) + '\n')
    return bases, base_indexes

# Определение множества взаимно-простых чисел для числа nnum
def cop_num_set(nnum:int, to_str=False):

    sp_set = set()
    sp_set.add(1)
    for i in range(2,nnum):
        if GCD_min(i,nnum) == 1:
            sp_set.add(i)
    log.info(f"Coprime numbers set for module {nnum} HAS CREATED:")
    if to_str:
        print(sp_set)
        print()
    else:
        log.info(sp_set)
        print()
    return sp_set        

# Функция Эйлера от числа nnum
def euler_func(nnum:int, to_str=False):
    fi = len(cop_num_set(nnum))
    if to_str:
        print(f"ф({nnum}) = {fi}\n")
    else:
        log.info(f"ф({nnum}) = {fi}\n")
    return fi    

# Нахождение обратного элемента числа а по модулю mnum
# a*u mod m = 1
def reverse_elem_Zm(anum:int, mnum:int, to_str=False):
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
    if to_str:
        print(f"u = {unum} for a = {anum} in Zm={mnum}")
    else:
        log.info(f"a = {anum}, Zm={mnum} -> u = {unum}")
    return unum

# Нахождение множества обратных элементов по модулю mnum
def reverse_U_set(mnum:int, to_str=False):
    
    Um_list = []
    cop_list = cop_num_set(mnum)
    log.info("COUNTING the reverse elements for each number in the set:\n")
    for i in cop_list:
        rev_elem = reverse_elem_Zm(i, mnum)
        if rev_elem != -1:
            Um_list.append(rev_elem)
    if to_str:
        print()
        print(Um_list)
    else:
        print()
        log.info(f"Reverse numbers set (mod {mnum}) HAS CREATED")
        log.info(Um_list)
    return Um_list

# Рушение сравнений ax=b(mod m)
def comparison_sol(anum:int, bnum:int, mnum:int, var:str = 'x', to_str=False):
    log.info(f"Decision of {anum}*{var} = {bnum}(mod {mnum}) IS FINDING")
    anum = anum % mnum
    bnum = bnum % mnum
    dnum = GCD_min(anum, mnum)
    if bnum % dnum == 0:
        if to_str:
            print("Comparison has a solution/\n")
        else:
            log.info("Comparison has a solution\n")
    else:
        log.info("Comparison has not a solution")
        return
    anum //= dnum
    bnum //= dnum
    mnum //= dnum
    unum = reverse_elem_Zm(anum, mnum)
    bnum = (unum * bnum) % mnum
    if to_str:
        print(f"Solution: {var} = {bnum} + {mnum}*k, k " + u'\u2208' + " Z\n")
    else:
        log.info(f"{var} = {bnum} + {mnum}*k, k " + u'\u2208' + " Z\n")
    return bnum, mnum

def china_solution_of_comparison_system(anums:list, bnums:list,
                                    mnums:list, to_str=False):
    if (len(anums) == len(bnums) == len(mnums)):
        comp_count = len(bnums)
    else:
        log.info("Check length of your a, b and m arguments, please. " +
                "Length must be same")
        log.info ("BREAKING...")
        return

    log.info(f"Decision of ")
    for j in range(comp_count):
        log.info(f"|\t{anums[j]}*x = {bnums[j]}(mod {mnums[j]})")
    log.info("IS FINDING")

    log.info("Reduction to the form x = b(mod m)")
    print()
    for i in range(comp_count):
        anums[i] = anums[i] % mnums[i]
        bnums[i] = bnums[i] % mnums[i]
        NOD = GCD_min(anums[i], mnums[i])
        if NOD != 1 and bnums[i] % NOD != 0:
            log.info(f"Comparison #{i + 1} has not a solution")
            return
        else:
            anums[i] //= NOD
            bnums[i] //= NOD
            mnums[i] //= NOD
        
        unum = reverse_elem_Zm(anums[i], mnums[i])
        anums[i] *= unum 
        anums[i] %= mnums[i]
        bnums[i] *= unum
        bnums[i] %= mnums[i]

    print()

    for i in range(comp_count):
        for j in range(i + 1, comp_count):
            if GCD_min(mnums[i], mnums[j]) != 1:
                log.info(f"{GCD_min(mnums[i], mnums[j])}")
                log.info("Not all modules is coprime to each other")
                log.info("System does not match Chinese convergence theorem")
                log.info ("BREAKING...")
                return
    
    # M - grand module
    M = 1
    for m in mnums:
        M *= m
    log.info(f"The Grand module M = {M}")
    
    log.info("CREATING a solution table\n")
    Mi_nums = []                                 # list of Mi that is M/mi
    Yi_nums = []                                 # list of reverse_Mi (mod mi)
    for m in mnums:
        Mi_nums.append(M // m)                 
    
    for i in range(comp_count):
        Yi_nums.append(reverse_elem_Zm(Mi_nums[i], mnums[i]))
    
    x = 0
    for i in range(comp_count):
        x += bnums[i] * Mi_nums[i] * Yi_nums[i]
    if to_str:
        print(f"bi\tmi\tMi\tyi")
        for i in range(comp_count):
            print(f"{bnums[i]}\t{mnums[i]}\t{Mi_nums[i]}\t{Yi_nums[i]}")
        print(f"Solution: {x % M} + {M}*k, k " + u'\u2208' + " Z")
        log.info("A solution HAS FOUND\n")
    else:
        log.info(f"bi\tmi\tMi\tyi")
        for i in range(comp_count):
            log.info(f"{bnums[i]}\t{mnums[i]}\t{Mi_nums[i]}\t{Yi_nums[i]}")
        log.info("The solution HAS FOUND")
        log.info(f"Solution: {x % M} + {M}*k, k " + u'\u2208' + " Z\n")
        
    return x%M

def deduction_solution(anum:int, index:int, mnum:int, to_str=False):
    if mnum == 1:
        log.info(f"Sorry, the solution CAN'T BE FOUND, because m must have not to be 1")
        log.info ("BREAKING...")
        return
    log.info("Solution of deduction IS FINDING")
    if GCD_min(anum, mnum) != 1:
        log.info(f"Sorry, the solution CAN'T BE FOUND, because ({anum},{mnum}) != 1")
        log.info ("BREAKING...")
        return
    m_bases, m_indexes = decomposition(mnum)
    length = len(m_bases)
    if length * m_indexes[0] == 1:                   # число не простое, если хоть одна степень больше 1
        log.info(f"Module is a SIMPLE number")
        solution = (anum ** (index % (mnum - 1))) % mnum
    else:
        log.info(f"Module is a COMPOSITE number")
        log.info(f"MAKING a comparison system with {length} comparisons")
        anums = [1 for x in range(length)]
        # a^index(mod mnum)
        # mnum = m_bases[0]^m_indexes[0] * m_bases[1]^m_indexes[1] * ...
        # a^ri(mod m_bases[i]^mIndex[i])
        # ri = index(mod m_bases[i]^mIndex[i] - 1)
        mnums = [m_bases[i] ** m_indexes[i] for i in range(length)]
        bnums = [anum ** (index % (mnums[i] - 1)) for i in range(length)]
        solution = china_solution_of_comparison_system(anums, bnums, mnums)
    log.info("Solution of deduction HAS FOUND")
    if to_str:
        print(f"{anum}^({index})(mod {mnum}) =  {solution}\n")
    else:
        log.info(f"{anum}^({index})(mod {mnum}) =  {solution}\n")
    return solution

def mod_has_prim_root(mnum:int, to_str=False):
    print()
    bases, indexes = decomposition_min(mnum)
    result =( (len(bases) == 1 and (bases[0] != 2 or 
                (bases[0] == 2 and indexes[0] <= 2))) or    # mnum is 2 or 4
            (len(bases) == 2 and (bases[0] == 2 and 
                indexes[0] == 1)) )                         # mnum is p^k or 2p^k
    if to_str:
        if not result:
            print(f"Primary root of {mnum} IS NOT EXIST")
            print(f"Reason: {mnum} not included in the set: 2, 4, p^k, 2*(p^k),",
            "p is odd natural number,  k " + u'\u2208' + " Z")
            print()
    else:
        if not result:
            log.info(f"Primary root of {mnum} IS NOT EXIST")
            log.info(f"Reason: {mnum} not included in the set: 2, 4, p^k, 2*(p^k),")
            log.info(f"p is odd natural number,  k " + u'\u2208' + " Z")
            print()
    return result

def prim_root(mnum:int, to_str=False):
    if not mod_has_prim_root(mnum):
        log.info ("BREAKING...\n")
        return
    delta = euler_func_min(mnum)
    Pik = []                                # Pi| delta <-> (delta % Pik[i] = 0)
    log.info(f"PRIMARY ROOT of {mnum} IS FINDING")
    for i in range (2, delta):
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

    log.info(f"PRIMARY ROOT of {mnum} has FOUND")
    if to_str:
        print(f"Primary root of {mnum} is {anum}\n")
    else:
        log.info(f"Primary root of {mnum} is {anum}\n")

    return anum

def reduced_deduction_sys(mnum:int, to_str=False):
    log.info(f"Reduced deduction system of {mnum} IS CREATING")
    RDSys = []
    pr_root = prim_root(mnum)
    if pr_root is None:
        log.info(f"Reduced deduction system of {mnum} CAN'T BE CREATED")
        return
        
    for pow in range(euler_func_min(mnum)):
        RDSys.append((pr_root ** pow) % mnum)
    log.info(f"Reduced deduction system of {mnum} HAS CREATED")
    if to_str:
        print(RDSys)
    else:
        log.info(RDSys)

# Индекс - в какую степень нужно возвести первообразный корень
# aroot, чтобы по модулю mnum оно было равно bnum
# discLog = ind b
#              a

def gamma_indexes_table(mnum:int):
    delta = euler_func_min(mnum)
    root = prim_root_min(mnum)
    if not root:
        log.info(f"Gamma indexes for m={mnum} CAN NOT BE FOUND")
        print()
        return

    log.info(f"Table with gamma indexes for module {delta} IS CREATING")

    gamma_ind_table = {((root ** i) % mnum): i for i in range(delta)}

    log.info("PRINTING: B to GAMMA INDEXES")
    
    bnumbers = list(gamma_ind_table.keys())
    bnumbers.sort()
    log.info("B numbers:")
    log.info(bnumbers)

    ind_bnum = []
    for key in bnumbers:
        ind_bnum.append(gamma_ind_table[key])

    log.info("Gamma indexes:")
    log.info(ind_bnum)
    log.info(f"Table with gamma indexes for module {delta} HAS CREATED")
    print()
    return gamma_ind_table

# Показательное сравнение x^nnum = bnum(mod mnum)
def revealing_comparison(anum:int, nnum:int, bnum:int, mnum:int, to_str=False):

    if GCD_min(bnum, mnum) != 1:
        log.info(f"({bnum},{mnum}) != 1, numbers is not coprime")
        log.info(f"A solution CAN'T BE FOUND")
        log.info ("BREAKING...")
        return

    root = prim_root(mnum)
    if not root:
        if to_str:
            print(f"x^({nnum}) = {bnum}(mod {mnum}) HAS NOT a solution")
            print()
        else:
            log.info(f"x^({nnum}) = {bnum}(mod {mnum}) HAS NOT a solution")
            print()
        return
    
    delta = euler_func(mnum)
    gamma = gamma_indexes_table(mnum)
    dnum = GCD_min(nnum, delta)
    
    if (gamma[bnum] % dnum != 0):
        if to_str:
            print(f"The solution can't be found")
            print(f"Choose another b={bnum} coefficient, ind b must be" +
                    f"devidable by GCD of n={nnum} and ф(m)={delta}")
            print("BREAKING...")
            return
        else:
            log.info(f"The solution can't be found")
            log.info(f"Choose another b={bnum} coefficient, ind b must be" +
                    f" devidable by GCD of n={nnum} and ф(m)={delta}")
            log.info("BREAKING...")
            return

    log.info(f"Solution of {anum}*x^({nnum}) = {bnum}(mod {mnum}) IS FINDING")
    
    log.info(f"Transformating to x^n = b2(mod m):")
    bnum2, m2 = comparison_sol(anum, bnum, mnum, "x^n")
       
    log.info(f"Transformating to n*ind x = ind b(mod ф(m):")
    log.info(f"{nnum} ind x = {gamma[bnum2 % mnum]}(mod {delta})")
    indb, indm = comparison_sol(nnum, gamma[bnum2 % mnum], delta, "ind x")

    log.info(f"Solution of {anum}*x^({nnum}) = {bnum}(mod {mnum}) HAS FOUND")
    if to_str:
        print(f"x = {root}^({indb}+{indm}*k), k " + u'\u2208' + " Z ")
    else:
        log.info(f"x = {root}^({indb}+{indm}*k), k " + u'\u2208' + " Z ")
        return root, indb, indm                         # root^(indb + indm*k)


# Степенное сравнение nnum^x = bnum(mod mnum)
def power_comparison(nnum:int, bnum:int, mnum:int, to_str=False):
    
    if GCD_min(bnum, mnum) != 1:
        log.info(f"({bnum},{mnum}) != 1, numbers is not coprime")
        log.info(f"A solution CAN'T BE FOUND")
        log.info ("BREAKING...")
        return

    log.info(f"Solution of ({nnum})^x = {bnum}(mod {mnum}) IS FINDING")

    delta = euler_func(mnum)
    log.info(f"Transformating to x*ind nnum = ind bnum(mod ф(mnum):")
    log.info(f"x * ind {nnum} = ind {bnum}(mod {delta})")

    gamma = gamma_indexes_table(mnum)
    ngamma = gamma[nnum]
    bgamma = gamma[bnum]
    log.info(f"Processing to solve: {ngamma}*x = {bgamma}(mod {delta})")
    log.info("SOLVING...")
    bsolve, msolve = comparison_sol(ngamma, bgamma, delta)

    log.info(f"Solution of ({nnum})^x = {bnum}(mod {mnum}) HAS FOUND")
    if to_str:
        print(f"x = {bsolve}+{msolve}*k, k " + u'\u2208' + " Z ")
    else:
        log.info(f"x = {bsolve}+{msolve}*k, k " + u'\u2208' + " Z ")

    return bsolve, msolve

def legendre_symbol(anum:int, pnum:int, to_str=False):
    if GCD_min(abs(anum), abs(pnum)) != 1:
        log.info(f"Sorry, the solution CAN'T BE FOUND, " +
                f"because ({abs(anum)},{pnum}) != 1")
        log.info ("BREAKING...")
        return

    p_bases, p_indexes = decomposition_min(abs(pnum))
    if len(p_bases) * p_indexes[0] != 1:
        log.info(f"There is not a SIMPLE number p={pnum}")
        log.info(f"Start to find a Jacobi symbol\n")
        return jacobi_symbol(anum, pnum)

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
        print(f"Legendre symbol of {anum} / {pnum} is {int(leg_symb)}")
    else:
        log.info(f"Legendre symbol of {anum} / {pnum} is {int(leg_symb)}")
    return int(leg_symb)

def jacobi_symbol(anum:int, mnum:int, to_str=False):
    if GCD_min(anum, mnum) != 1:
        log.info(f"Sorry, the solution CAN'T BE FOUND, " +
                f"because ({anum},{mnum}) != 1")
        log.info ("BREAKING...")
        return
    
    jcb_symb = 1

    if (anum * mnum < 0):
        jcb_symb *= (-1) ** int((abs(mnum) - 1) / 2)
    bases, indexes = decomposition(abs(mnum))
    for i in indexes:
        i %= 2
    
    for i in range(len(bases)):
        if indexes[i]:
            try:
                jcb_symb *= legendre_symbol(anum % bases[i], bases[i])
            except:
                log.info(f"Some steps of symbol Jacobi counting CAN'T be done")
                log.info(f"Jacobi symbol of {anum % bases[i]} / {bases[i]} " +
                        f"CAN'T BE FOUNDED")
                log.info ("BREAKING...")
                return 
    if to_str:
        print(f"Jacobi symbol of {anum} / {mnum} is {int(jcb_symb)}")
    else:
        log.info(f"Jacobi symbol of {anum} / {mnum} is {int(jcb_symb)}")
    return int(jcb_symb)


#wideEuclid(1234, 54)
#eratosthenes(-1, 1)      # ~ O(n)
#print(decomposition(360, 1))
#a = simplPairSet(36)
#comparisonSol(24, 35, 28)
#chinaSolutionOfComparisonSystem([1,1], [1,4], [7,5], 1)
#deductionSolution(2, 40, 10)
#reducedDeductionSys(19)
#revealingComparison(4,4,7)
#gammaIndexesTable(7)
#gammaIndexesTable(11, 1)
#powerComparison(5, 4, 7)
#checkList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#for test in checkList:
#print(modHasPrimRoot(test))





