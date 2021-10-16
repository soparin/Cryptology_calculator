from os import cpu_count
import sys 
import logging as log

log.basicConfig(format="[ %(levelname)s ] %(message)s",
                    level=log.INFO, stream=sys.stdout)

def menu():
    while (1):
        print("\n************Welcome to Cryptology math calculator**************\n")

        choice = input("""
1. Euclid GCD algorithm: (a,b)
2. Extended Euclidean decomposition 
3. Sieve of Eratosthenes for n
4. Canonical decomposition of number 
5. Euler function for ф(m)
6. Finding a reverse element u in Zm
7. Finding a set of reverse elements U
8. Comparison solving for m: ax = b(mod m)
9. System of comparisons with china algorithm
10. Finding a deduction (a^k)(mod m)
11. Calculating the primary root for mod m: a
12. Reduced deduction system for mod m
13. Solving revealing comparisons x^n = b(mod m)
14. Solving power comparisons n^x = b(mod m)

Q: Logout

Please enter your choice: """)

        if choice == "1":
            print("You have choosed Euclid GCD algorithm")
            print("Format: (a|b) = output")
            a = readMeNaturNum("Enter a natural \'a\', please:  ", 'a')
            b = readMeNaturNum("Enter a natural \'b\', please:  ", 'b')
            print()
            euclidGCD(a, b)
            input("Press ENTER to exit to the menu")
            continue
        
        elif choice == "2":
            print("You have choosed Extended Euclidean decomposition")
            print("Format: (a|b) = au + bv = output")
            a = readMeNaturNum("Enter a natural \'a\', please:  ", 'a')
            b = readMeNaturNum("Enter a natural \'b\', please:  ", 'b')
            print()
            extendedEuclid(a, b)
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "3":
            print("You have choosed Sieve of Eratosthenes")
            n = readMeNaturNum("Enter a natural \'n\', please:  ", 'n')
            print()
            eratosthenes(n, 1)
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "4":
            print("You have choosed canonical decomposition of number")
            print("format: n = p1^k1*p2^k2*...*pn^kn")
            n = readMeNaturNum("Enter a natural \'n\', please:  ", 'n')
            print()
            decomposition(n,1)
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "5":
            print("You have choosed Euler function for ф(m)")
            print("format: output: ф(m)")
            m = readMeNaturNum("Enter a natural module \'m\', please:  ", 'm')
            print()
            eulerFunc(m)
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "6":
            print("You have choosed finding a reverse element u in Zm")
            print("format: u: a*u = 1(mod m)")
            a = readMeNaturNum("Enter a natural \'a\', please:  ", 'a')
            m = readMeNaturNum("Enter a natural module \'m\', please:  ", 'm')
            print()
            reverseElemZm(a, m)
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "7":
            print("You have choosed finding a set of reverse elements U")
            m = readMeNaturNum("Enter a natural module \'m\', please:  ", 'm')
            print()
            reverseUSet(m)
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "8":
            print("You have choosed comparison solving for m")
            print("format: ax = b(mod m)")
            a = readMeNaturNum("Enter a natural \'a\', please:  ", 'a')
            b = readMeNaturNum("Enter a natural \'b\', please:  ", 'b')
            m = readMeNaturNum("Enter a natural module \'m\', please:  ", 'm')
            print()
            comparisonSol(a, b, m)
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "9":
            print("You have choosed system of comparisons")
            print("format:  /a1x = b1(mod m1)")
            print("\t |a2x = b2(mod m2)")
            print("\t |...")
            print("\t \\ anx = bn(mod mn)")
            n = readMeNaturNum("Enter a natural \'n\', please:  ", 'n')
            
            la = []
            lb = []
            lm = []
            print("Fill in the coefficients in the form: a,b,m")
            i=0
            while i<n:
                err_flag = 0                                # error flag
                inputStr = input(f"Comparison #{i+1}: ")
                inputStr = inputStr.replace(' ', '')
                inputList = inputStr.rsplit(',')
                if len(inputList) != 3:
                    err = input("Press ENTER and type your 3 coefficients with \',\' or press the \'q\' to exit, please : ")
                    if err == 'q' or err == 'Q':
                        err_flag = 1
                        break
                    else:
                        continue
                for coef in inputList:
                    if not coef.isdigit():
                        err = input("There are any not digit symbols, plese press ENTER and correct the coefficients : ")
                        err_flag = 1

                if not err_flag:   
                    la.append(int(inputList[0]))
                    lb.append(int(inputList[1]))
                    lm.append(int(inputList[2]))
                    i+=1
            
            if not err_flag:
                print()
                chinaSolutionOfComparisonSystem(la, lb, lm)
            else:
                print("Exit without solution")
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "10":
            print("You have choosed finding a deduction (a^k)(mod m)")
            a = readMeNaturNum("Enter a natural \'a\', please:  ", 'a')
            k = readMeNaturNum("Enter a natural \'k\', please:  ", 'k')
            m = readMeNaturNum("Enter a natural module \'m\', please:  ", 'm')
            print()
            deductionSolution(a, k, m)
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "11":
            print("You have choosed calculating the primary root for mod m")
            print("format: Primary root for m: a")
            m = readMeNaturNum("Enter a natural module \'m\', please:  ", 'm')
            print()
            primRoot(m)
            input("Press ENTER to exit to the menu")
            continue
        
        elif choice == "12":
            print("You have choosed reduced deduction system for mod m")
            print("format: U(m) = \{ ... }")
            m = readMeNaturNum("Enter a natural module \'m\', please:  ", 'm')
            print()
            reducedDeductionSys(m)
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "13":
            print("You have choosed solving revealing comparisons")
            print("format: x^n = b(mod m)")
            n = readMeNaturNum("Enter a natural \'n\', please:  ", 'n')
            b = readMeNaturNum("Enter a natural \'b\', please:  ", 'b')
            m = readMeNaturNum("Enter a natural module \'m\', please:  ", 'm')
            print()
            revealingComparison(n, b, m)
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "14":
            print("You have choosed Solving power comparisons")
            print("format: n^x = b(mod m)")
            n = readMeNaturNum("Enter a natural \'n\', please:  ", 'n')
            b = readMeNaturNum("Enter a natural \'b\', please:  ", 'b')
            m = readMeNaturNum("Enter a natural module \'m\', please:  ", 'm')
            print()
            powerComparison(n, b, m)
            input("Press ENTER to exit to the menu")
            continue

        #elif choice == "15":
        #elif choice == "16":
        #elif choice == "17":
        #elif choice == "18":
        #elif choice == "19":
        #elif choise == "20":
        #elif choise == "21": 
        #elif choise == "22": 
        #elif choise == "23":  
             
        elif choice=="Q" or choice == "q":
            break

        else:
            print("You must only select either numbers from 1 to 14 or Q")
            print("Please try again")
            continue

def readMeNaturNum(outputStr, arg):
    while(1):
        flag = 0
        inputStr = input(outputStr).replace(' ','')
        for c in inputStr:
            if not c.isdigit():
                print("There are no-digital symbols in the input")
                flag = 1
                break
        if not flag:
            if inputStr.isdigit():
                if int(inputStr) > 0:
                    n = int(inputStr)
                    break
                else:
                    print("Wrong number.")
                    input("Press ENTER to exit to the menu")
                    continue
            else:
                print("Use only natural numbers, please")
                input(f"Press ENTER to correct the argument {arg}: ")
                continue
    return n

# Нахождение наибольшего общего делителя (anum, bnum) = НОД
def euclidGCD(anum:int, bnum:int, to_str = False):
    atemp, btemp = anum, bnum
    log.info("Euclidean algorithm is RUNNING")
    while anum!=0 and bnum!=0:
        if anum>bnum:
            anum%=bnum
        else:
            bnum%=anum
    if to_str:
        print(f"({atemp},{btemp}) = {max(anum, bnum)}")
    else:
        log.info(f"({atemp},{btemp}) = {max(anum, bnum)}")
    log.info("Euclidean algorithm HAS COMPLITED\n")            
    if bnum==0:
        return anum
    else:
        return bnum

# Нахождение НОД без логирования
def GCDMin(anum:int, bnum:int):
    while anum!=0 and bnum!=0:
        if anum>bnum:
            anum%=bnum
        else:
            bnum%=anum
    if bnum==0:
        return anum
    else:
        return bnum

# Расширенный алгоритм Евклида
# (anum,bnum) = anum*unum + bnum*vnum = NOD
def extendedEuclid(anum:int, bnum:int, to_str = False):
    unum, x, vnum, y = 1, 0, 0, 1
    atemp, btemp = anum, bnum
    log.info("Extended Euclidean algorithm is RUNNING")
    while bnum:
        q = anum // bnum
        anum, bnum = bnum, anum % bnum
        unum, x = x, unum - x*q
        vnum, y = y, vnum - y*q
    if to_str:
        print(f"({atemp},{btemp}) = {anum}")
        print(f"{atemp} * {unum} + {btemp} * {vnum} = {anum}")
    else:
        log.info(f"({atemp},{btemp}) = {anum}")
        log.info(f"{atemp} * {unum} + {btemp} * {vnum} = {anum}")
    log.info("Extended Euclidean algorithm HAS COMPLITED\n")
    return (unum, vnum, anum)

# Решето Эратосфена для нахождения списка простых чисел до границы nnum
def eratosthenes(nnum:int, to_str = False):
    if nnum < 1:
        log.info(f"Wrong value of nature number argument n = {nnum}")
        log.info ("BREAKING...\n")
        return
    log.info(f"Eratosthen screen to N = {nnum} is RUNNING")
    if nnum > 10**8:
        log.info("Counting is not recomended")
        return eratosthenes (10**8) 
    screen = list(i+1 for i in range(nnum))
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
# степенных функций от простых чисел ... * (bases[i]^baseIndexes[i]) * ...
def decomposition(nnum:int, to_str = False):
    log.info(f"Canonical decomposition of {nnum} is RUNNING")
    temp = nnum
    bases = set()
    baseIndexes = []
    i = 2
    while nnum > 0:
        index = 0
        while (nnum%i == 0):
            bases.add(i)
            nnum //= i
            index += 1
        i += 1
        if index:
            baseIndexes.append(index)
        if i > nnum:
            break
    bases = sorted(list(bases))
    log.info(f"Canonical decomposition of {temp} HAS COMPLITED")
    if to_str:
        show = f"{temp} ="
        for i in range(len(bases)):
            show += f" {bases[i]}^{baseIndexes[i]} *"
        print(show[:-1])
    else:
        log.info("Bases: " + str(bases))
        log.info("Indexes" + str(baseIndexes) + '\n')
    return bases, baseIndexes

# Определение множества взаимно-простых чисел для числа nnum
def copNumSet(nnum:int, to_str = False):
    if nnum < 1:
        log.info(f"Wrong value of nature number argument n = {nnum}")
        log.info ("BREAKING...\n")
        return
    sp_set = set()
    sp_set.add(1)
    for i in range(2,nnum):
        if GCDMin(i,nnum)==1:
            sp_set.add(i)
    log.info(f"Coprime numbers set {nnum} HAS CREATED")
    if to_str:
        print(sp_set)
    else:
        log.info(sp_set)
    return sp_set      

# Функция Эйлера от числа nnum
def eulerFunc(nnum:int, to_str = False):
    fi = len(copNumSet(nnum))
    if to_str:
        print(f"ф({nnum}) = {fi}\n")
    else:
        log.info(f"ф({nnum}) = {fi}\n")
    return fi

# Нахождение обратного элемента числа а по модулю mnum
# a*u mod m = 1
def reverseElemZm(anum:int, mnum:int, to_str = False):
    if mnum < 1:
        log.info(f"Wrong value of nature number argument mnum = {mnum}")
        log.info ("BREAKING...\n")
        return
    unum = 0
    while((unum*anum)%mnum!=1):
        unum += 1
    if to_str:
        print(f"u = {unum} for a = {anum} in Zm={mnum}")
    else:
        log.info(f"a = {anum}, Zm={mnum} -> u = {unum}")
    print()
    return unum

# Нахождение множества обратных элементов по модулю mnum
def reverseUSet(mnum:int, to_str=False):
    if mnum < 1:
        log.info(f"Wrong value of nature number argument mnum = {mnum}")
        log.info ("BREAKING...\n")
        return
    UmList = []
    for i in copNumSet(mnum):
        UmList.append(reverseElemZm(i,mnum))
    if to_str:
        print(UmList)
    else:
        log.info(f"Reverse numbers set (mod {mnum}) HAS CREATED")
    return UmList

# Рушение сравнений ax=b(mod m)
def comparisonSol(anum:int, bnum:int, mnum:int, var:str = 'x', to_str = False):
    log.info(f"Decision of {anum}*{var} = {bnum}(mod {mnum}) IS FINDING")
    anum = anum%mnum
    bnum = bnum%mnum
    dnum = GCDMin(anum, mnum)
    if bnum%dnum == 0:
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
    unum = reverseElemZm(anum, mnum)
    bnum = (unum*bnum)%mnum
    if to_str:
        print(f"Solution: {var} = {bnum} + {mnum}*k, k " + u'\u2208' + " Z\n")
    else:
        log.info(f"{var} = {bnum} + {mnum}*k, k " + u'\u2208' + " Z\n")
    return bnum, mnum

def chinaSolutionOfComparisonSystem(anums:list, bnums:list, mnums:list, to_str = False):
    if (len(anums) == len(bnums) == len(mnums)):
        CompCount = len(bnums)
    else:
        log.info("Check length of your a, b and m arguments, please. Length must be same")
        log.info ("BREAKING...\n")
        return

    log.info(f"Decision of ")
    for j in range(CompCount):
        log.info(f"|\t{anums[j]}*x = {bnums[j]}(mod {mnums[j]})")
    log.info("IS FINDING")

    log.info("Reduction to the form x = b(mod m)")
    print()
    for i in range(CompCount):
        anums[i] = anums[i]%mnums[i]
        bnums[i] = bnums[i]%mnums[i]
        NOD = GCDMin(anums[i], mnums[i])
        if NOD != 1 and bnums[i]%NOD != 0:
            log.info(f"Comparison #{i+1} has not a solution")
            return
        else:
            anums[i] //= NOD
            bnums[i] //= NOD
            mnums[i] //= NOD
        
        unum = reverseElemZm(anums[i], mnums[i])
        anums[i] *= unum 
        anums[i] %= mnums[i]
        bnums[i] *= unum
        bnums[i] %= mnums[i]

    print()

    for i in range(CompCount):
        for j in range(i+1,CompCount):
            if GCDMin(mnums[i],mnums[j]) != 1:
                log.info(f"{GCDMin(mnums[i],mnums[j])}")
                log.info("Not all modules is coprime to each other")
                log.info("System does not match Chinese convergence theorem")
                log.info ("BREAKING...\n")
                return
    
    # M - grand module
    M = 1
    for m in mnums:
        M *= m
    log.info(f"The Grand module M = {M}")
    
    log.info("CREATING a solution table\n")
    Minums = []                                 # list of Mi that is M/mi
    Yinums = []                                 # list of reverse_Mi (mod mi)
    for m in mnums:
        Minums.append(M//m)                 
    
    for i in range(CompCount):
        Yinums.append(reverseElemZm(Minums[i], mnums[i]))
    
    x = 0
    for i in range(CompCount):
        x +=bnums[i]*Minums[i]*Yinums[i]
    if to_str:
        print(f"bi\tmi\tMi\tyi")
        for i in range(CompCount):
            print(f"{bnums[i]}\t{mnums[i]}\t{Minums[i]}\t{Yinums[i]}")
        print(f"Solution: {x%M} + {M}*k, k " + u'\u2208' + " Z")
        log.info("A solution HAS FOUND\n")
    else:
        log.info(f"bi\tmi\tMi\tyi")
        for i in range(CompCount):
            log.info(f"{bnums[i]}\t{mnums[i]}\t{Minums[i]}\t{Yinums[i]}")
        log.info("The solution HAS FOUND")
        log.info(f"Solution: {x%M} + {M}*k, k " + u'\u2208' + " Z\n")
        
    return x%M

def deductionSolution(anum:int, index:int, mnum:int, to_str = False):
    if mnum <= 1:
        return
    log.info("Solution of deduction IS FINDING")
    mBases, mIndexes = decomposition(mnum)
    length = len(mBases)
    if length == 1:
        log.info(f"Module is a SIMPLE number")
        solution = (anum**(index%(mnum-1)))%mnum
    else:
        log.info(f"Module is a COMPOSITE number")
        log.info(f"MAKING a comparison system with {length} comparisons")
        anums = [1 for x in range(length)]
        # a^index(mod mnum)
        # mnum = mBases[0]^mIndexes[0] * mbases[1]^mIndexes[1] * ...
        # a^ri(mod mbases[i]^mIndex[i])
        # ri = index(mod mbases[i]^mIndex[i] - 1)
        mnums = [mBases[i]**mIndexes[i] for i in range(length)]
        bnums = [anum**(index%(mnums[i] - 1)) for i in range(length)]
        solution = chinaSolutionOfComparisonSystem(anums, bnums, mnums)
    log.info("Solution of deduction HAS FOUND")
    if to_str:
        print(f"{anum}^({index})(mod {mnum}) =  {solution}\n")
    else:
        log.info(f"{anum}^({index})(mod {mnum}) =  {solution}\n")
    return solution

def primRoot(mnum:int, to_str = False):
    delta = eulerFunc(mnum)
    Pik = []                                # Pi| delta (delta % Pik[i] = 0)
    log.info(f"PRIMARY ROOT of {mnum} IS FINDING")
    for i in range (2,delta):
        if delta%i == 0:
            Pik.append(i)
    log.info(f"Powes to check the PRIMARY ROOT HAS CREATED:")
    log.info("Powers: ")
    log.info (Pik)
    flag = False
    anum = 2
    while not flag:
        flag = True
        for ind in Pik:
            if (anum**ind)%mnum == 1:
                flag = False
                anum += 1
                break
    
    log.info(f"PRIMARY ROOT of {mnum} has FOUND")
    if to_str:
        print(f"Primary root of {mnum} is {anum}\n")
    else:
        log.info(f"Primary root of {mnum} is {anum}\n")

    return anum

def reducedDeductionSys(mnum:int, to_str=False):
    log.info(f"Reduced deduction system of {mnum} IS CREATING")
    RDSys = []
    PrRoot = primRoot(mnum);
    for pow in range(eulerFunc(mnum)):
        RDSys.append((PrRoot**pow)%mnum)
    log.info(f"Reduced deduction system of {mnum} HAS CREATED")
    if to_str:
        print(f"Reduced deduction system of {mnum}:")
        print(RDSys)
    else:
        log.info(f"Reduced deduction system of {mnum}:")
        log.info(RDSys)

# Индекс - в какую степень нужно возвести первообразный корень
# aroot, чтобы по модулю mnum оно было равно bnum
# discLog = ind b
#              a

def gammaIndexesTable(mnum:int, b_to_gamma = False):
    log.info(f"Table with gamma indexes for module {mnum} IS CREATING")
    delta = eulerFunc(mnum)
    gammaIndTable = [0 for i in range(delta)]
    root = primRoot(mnum)
    if b_to_gamma:
        log.info("PRINTING: B to GAMMA INDEXES")   # B is indexes (from 1 to ф(mnum)) of array with GAMMA INDEXES)
        log.info("--> Using to print the GAMMA TABLE <--")
        bnumbers = [i for i in range(1,delta+1)]
        log.info("B numbers:")
        for i in range(delta):
            gammaIndTable[(root**i)%mnum - 1] = i
        log.info(bnumbers)
        log.info("Gamma indexes:")
    else:
        log.info("PRINTING: GAMMA INDEXES to B")    # GAMMA INDEXES is indexes of array with B
        log.info("--> Using to solve the Power comparison <--")
        for i in range(delta):
            gammaIndTable[i] = (root**i)%mnum
    
    log.info(gammaIndTable)
    log.info(f"Table with gamma indexes for module {mnum} HAS CREATED:")
    return gammaIndTable

# Показательное сравнение x^nnum = bnum(mod mnum)
def revealingComparison(nnum:int, bnum:int, mnum:int, to_str=False):
    if mnum < 1:
        log.info(f"Wrong value of nature number argument mnum = {mnum}")
        log.info ("BREAKING...\n")
        return
    log.info(f"Solve of x^({nnum}) = {bnum}(mod {mnum}) IS FINDING")
    delta = eulerFunc(mnum)
    root = primRoot(mnum)
    gamma = gammaIndexesTable(mnum, 1)
    log.info(f"Transformating to nnum*ind x = ind bnum(mod ф(mnum):")
    log.info(f"{nnum} ind x = {gamma[bnum%mnum]}(mod {delta})")
    indb, indm = comparisonSol(nnum, gamma[bnum%mnum], delta, "ind x")

    log.info(f"Solve of x^({nnum}) = {gamma[bnum%mnum]}(mod {mnum}) HAS FOUND")
    if to_str:
        print(f"x = {root}^({indb}+{indm}*k), k " + u'\u2208' + " Z\n ")
    else:
        log.info(f"x = {root}^({indb}+{indm}*k), k " + u'\u2208' + " Z\n ")
        return root, indb, indm                                             # root^(indb + indm*k)


# Степенное сравнение nnum^x = bnum(mod mnum)
def powerComparison(nnum:int, bnum:int, mnum:int, to_str=False):
    if mnum < 1:
        log.info(f"Wrong value of nature number argument mnum = {mnum}")
        log.info ("BREAKING...\n")
        return
    log.info(f"Solve of ({nnum})^x = {bnum}(mod {mnum}) IS FINDING")
    delta = eulerFunc(mnum)
    log.info(f"Transformating to x*ind nnum = ind bnum(mod ф(mnum):")
    log.info(f"x * ind {nnum} = ind {bnum}(mod {delta})")
    gamma = gammaIndexesTable(mnum)
    ngamma = gamma[nnum]
    bgamma = gamma[bnum]
    log.info(f"Processing to solve: {ngamma}*x = {bgamma}(mod {delta}")
    log.info("SOLVING...")
    bsolve, msolve = comparisonSol(ngamma, bgamma, delta)

    log.info(f"Solve of ({nnum})^x = {bnum}(mod {mnum}) HAS FOUND")
    if to_str:
        print(f"x = {bsolve}+{msolve}*k, k " + u'\u2208' + " Z\n ")
    else:
        log.info(f"x = {bsolve}+{msolve}*k, k " + u'\u2208' + " Z\n ")

    return bsolve, msolve


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
menu()





