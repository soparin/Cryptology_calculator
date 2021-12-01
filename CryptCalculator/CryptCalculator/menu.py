from arithm_calculations import *
from algebra_calculations import *

def menu():
    while (1):
        print("\n**********Welcome to Cryptology math calculator************\n")

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
13. Solving revealing comparisons ax^n = b(mod m)
14. Solving power comparisons n^x = b(mod m)
15. Legendre symbol finding (a/p) = +-1, p \u2208 N
16. Jacobi symbol finding (a/m) = +-1, m \u2208 Z
17. Number group order |Zm(+)| or |Zm(*)|
18. Decomposition into subgroups of adjacent subclasses for Zm

Q: Logout

Please enter your choice: """)

        if choice == "1":
            print("You have choosed Euclid GCD algorithm")
            print("Format: (a|b) = output")
            a = read_natur_num("Enter a natural \'a\', please:  ", 'a')
            b = read_natur_num("Enter a natural \'b\', please:  ", 'b')
            print()
            euclid_GCD(a, b)
            print()
            input("Press ENTER to exit to the menu")
            continue
        
        elif choice == "2":
            print("You have choosed Extended Euclidean decomposition")
            print("Format: (a|b) = au + bv = output")
            a = read_natur_num("Enter a natural \'a\', please:  ", 'a')
            b = read_natur_num("Enter a natural \'b\', please:  ", 'b')
            print()
            extended_euclid(a, b)
            print()
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "3":
            print("You have choosed Sieve of Eratosthenes")
            n = read_natur_num("Enter a natural \'n\', please:  ", 'n')
            print()
            eratosthenes(n, 1)
            print()
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "4":
            print("You have choosed canonical decomposition of number")
            print("format: n = p1^k1*p2^k2*...*pn^kn")
            n = read_natur_num("Enter a natural \'n\', please:  ", 'n')
            print()
            decomposition(n,1)
            print()
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "5":
            print("You have choosed Euler function for ф(m)")
            print("format: output: ф(m)")
            m = read_natur_num("Enter a natural module \'m\', please:  ", 'm')
            print()
            euler_func(m)
            print()
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "6":
            print("You have choosed finding a reverse element u in Zm")
            print("format: u: a*u = 1(mod m)")
            a = read_natur_num("Enter a natural \'a\', please:  ", 'a')
            m = read_natur_num("Enter a natural module \'m\', please:  ", 'm')
            print()
            reverse_elem_Zm(a, m)
            print()
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "7":
            print("You have choosed finding a set of reverse elements U")
            m = read_natur_num("Enter a natural module \'m\', please:  ", 'm')
            print()
            reverse_U_set(m)
            print()
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "8":
            print("You have choosed comparison solving for m")
            print("format: ax = b(mod m)")
            a = read_natur_num("Enter a natural \'a\', please:  ", 'a')
            b = read_natur_num("Enter a natural \'b\', please:  ", 'b')
            m = read_natur_num("Enter a natural module \'m\', please:  ", 'm')
            print()
            comparison_sol(a, b, m)
            print()
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "9":
            print("You have choosed system of comparisons")
            print("format:  /a1x = b1(mod m1)")
            print("\t |a2x = b2(mod m2)")
            print("\t |...")
            print("\t \\ anx = bn(mod mn)")
            n = read_natur_num("Enter a natural \'n\', please:  ", 'n')
            
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
                    err = input("Press ENTER and type your 3 coefficients " +
                            "with \',\' or press the \'q\' to exit, please : ")
                    if err == 'q' or err == 'Q':
                        err_flag = 1
                        break
                    else:
                        continue
                for coef in inputList:
                    if not coef.isdigit():
                        err = input("There are any not digit symbols, plese " +
                                    "press ENTER and correct the coefficients : ")
                        err_flag = 1

                if not err_flag:   
                    la.append(int(inputList[0]))
                    lb.append(int(inputList[1]))
                    lm.append(int(inputList[2]))
                    i+=1
            
            if not err_flag:
                print()
                china_solution_of_comparison_system(la, lb, lm)
            else:
                print("Exit without solution")
            print()
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "10":
            print("You have choosed finding a deduction (a^k)(mod m)")
            a = read_natur_num("Enter a natural \'a\', please:  ", 'a')
            k = read_natur_num("Enter a natural \'k\', please:  ", 'k')
            m = read_natur_num("Enter a natural module \'m\', please:  ", 'm')
            print()
            deduction_solution(a, k, m)
            print()
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "11":
            print("You have choosed calculating the primary root for mod m")
            print("format: Primary root for m: a")
            m = read_natur_num("Enter a natural module \'m\', please:  ", 'm')
            prim_root(m)
            input("Press ENTER to exit to the menu")
            continue
        
        elif choice == "12":
            print("You have choosed reduced deduction system for mod m")
            print("format: U(m) = { ... }")
            m = read_natur_num("Enter a natural module \'m\', please:  ", 'm')
            print()
            reduced_deduction_sys(m)
            print()
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "13":
            print("You have choosed solving revealing comparisons")
            print("format: a*x^n = b(mod m)")
            a = read_natur_num("Enter a natural \'a\', please:  ", 'a')
            n = read_natur_num("Enter a natural \'n\', please:  ", 'n')
            b = read_natur_num("Enter a natural \'b\', please:  ", 'b')
            m = read_natur_num("Enter a natural module \'m\', please:  ", 'm')
            print()
            revealing_comparison(a, n, b, m)
            print()
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "14":
            print("You have choosed Solving power comparisons")
            print("format: n^x = b(mod m)")
            n = read_natur_num("Enter a natural \'n\', please:  ", 'n')
            b = read_natur_num("Enter a natural \'b\', please:  ", 'b')
            m = read_natur_num("Enter a natural module \'m\', please:  ", 'm')
            print()
            power_comparison(n, b, m)
            print()
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "15":
            print("You have choosed Legendre symbol finding")
            print("format: a/p = +-1")
            a = read_num("Enter a \'a\', please:  ", 'a')
            p = read_natur_num("Enter a simple \'p\', please:  ", 'p')
            print()
            legendre_symbol(a, p)
            print()
            input("Press ENTER to exit to the menu")
            continue

        elif choice == "16":
            print("You have choosed Jacobi symbol finding")
            print("format: a/m = +-1")
            a = read_num("Enter a \'a\', please:  ", 'a')
            m = read_num("Enter a \'m\', please:  ", 'm')
            print()
            jacobi_symbol(a, m)
            print()
            input("Press ENTER to exit to the menu")
            continue
        elif choice == "17":
            print("You have choosed finding of number grop order Zm")
            print("format: |Zm|: a / ord a")
            m = read_natur_num("Enter a \'m\', please:  ", 'm')
            mode = input("What kind of group do you want? Enter '+' or '*': ")
            print()
            if mode[0] == '+':
                print("You have chousen a additional group (+)")
            elif mode[0] == '*':
                print("You have chousen a multiple group (*)")
            else:
                mode[0] = '+'
                print("There is not correct mode, using default: additional (+)")
            
            num_group_ord(m, mode[0])
            print()
            input("Press ENTER to exit to the menu")
            continue
        elif choice == "18":
            print("You have choosed a decomposition into subgroups of " +
                "adjacent subclasses for Zm")
            print("format: |Zm| = {...}\n" +
                "H1 = {...}, H2 = {...}, ..., Hn = {...}")
            m = read_natur_num("Enter a \'m\', please:  ", 'm')
            mode = input("What kind of group do you want? Enter '+' or '*': ")
            print()
            if mode[0] == '+':
                print("You have chousen a additional group (+)")
            elif mode[0] == '*':
                print("You have chousen a multiple group (*)")
            else:
                mode[0] = '+'
                print("There is not correct mode, using default: additional (+)")
           
            decompos_into_subgroups(m, mode[0])
            print()
            input("Press ENTER to exit to the menu")
            continue
            
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

#menu()
decompos_into_subgroups(10, '+')
