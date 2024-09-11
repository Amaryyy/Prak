import sympy as sp  

def get_user_input():
    
    n = int(input("Введите кол-во диф уравнений в системе: "))

    # Определение символов
    t = sp.symbols('t')  
    x = sp.symbols(f'x1:{n + 1}')  
    a, b, w, c = sp.symbols('a b w c')  
    u = sp.symbols('u')  
    p = sp.symbols(f'p1:{n + 1}')  
    T = sp.symbols('T1')  

    # Ввод правых частей уравнений от пользователя и их симв. преобразование
    x_dot = []
    for i in range(n):
        eq_str = input(f"Введите правую часть x{i + 1}): ")  
        x_dot.append(sp.sympify(eq_str))  

    # Ввод функции ψ(t) от пользователя и ее симв. преобразование
    psi_str = input("Введите psi(t): ")
    psi = sp.sympify(psi_str)

    # Вычисление производной ψ(t) по времени с учетом уравнений для x_dot
    psi_dot = 0
    for i in range(n):
        psi_dot += sp.diff(psi, x[i]) * x_dot[i]  

    # Определение выражения res
    res = sp.Add(sp.Mul(T, psi_dot), psi)  # res = T * ψ'(t) + ψ(t)

    # Решение уравнения res = 0 относительно переменной u
    solution = sp.solve(res, u)

    # Вывод результатов
    print("\nPsi'(t):")
    print(psi_dot)  
    print("\nПромежуточный результат:")
    print(res)  
    print("\nu:")
    print(solution)  


get_user_input()



#3
#x2
#a*x3+b*x3*x3*x3
#-w*x3+c*u
#p1+x1+p2*x2+(a*x3+b*x3*x3*x3)
