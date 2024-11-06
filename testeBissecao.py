import sympy as sp

# Entradas do usuário
a1 = float(input('Entre com o limite inferior do intervalo: '))
b1 = float(input('Entre com o limite superior do intervalo: '))
f = input("Digite a função (use ** para expoente):" )
p = float(input('Entre com a precisão desejada: '))

x = sp.Symbol('x')
f_expr = sp.sympify(f)

# Inicialização das variáveis
t = 1
a = [a1]
b = [b1]
erro = [abs(b[t-1] - a[t-1])]

# Algoritmo da bisseção
while erro[t-1] > p:
    xm = (a[t-1] + b[t-1]) / 2
    fxm = f_expr.subs(x, xm)  # Calcula f(xm)
    fa = f_expr.subs(x, a[t-1])  # Calcula f(a)
    fb = f_expr.subs(x, b[t-1])  # Calcula f(b)

    if fa * fxm < 0:
        a.append(a[t-1])
        b.append(xm)
    else:
        a.append(xm)
        b.append(b[t-1])

    t += 1
    erro.append(abs(b[t-1] - a[t-1]))

# Exibir os resultados
print('Iteração\t a\t xm\t b\t f(a)\t f(xm)\t f(b)\t Erro')
for i in range(t):
    xm = (a[i] + b[i]) / 2
    fa = f_expr.subs(x, a[i])
    fxm = f_expr.subs(x, xm)
    fb = f_expr.subs(x, b[i])
    print(f'{i+1}\t {a[i]:.6f}\t {xm:.6f}\t {b[i]:.6f}\t {fa:.6f}\t {fxm:.6f}\t {fb:.6f}\t {erro[i]:.6f}')
