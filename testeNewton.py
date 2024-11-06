import sympy as sp

# Entradas do usuário
x0 = float(input('Entre com o chute inicial: '))
f = input("Digite a função entre apóstrofo (use ** para expoente): ")
df = input("Digite a função derivada entre apóstrofo (use ** para expoente): ")
p = float(input('Digite a precisão desejada: '))


x = sp.Symbol('x')

f_expr = sp.sympify(f)
df_expr = sp.sympify(df)

# Inicialização das variáveis
t = 1
xsol = [x0]  # Armazena as aproximações da solução
erro = [abs(f_expr.subs(x, x0))]  # Erro inicial com substituição numérica

# Algoritmo de Newton-Raphson
while erro[t-1] > p:
    x_atual = xsol[t-1]

    # Calcula f(x) e f'(x) para o valor atual
    fx = f_expr.subs(x, x_atual)
    dfx = df_expr.subs(x, x_atual)

    # Atualiza a aproximação
    x_novo = x_atual - fx / dfx
    xsol.append(x_novo)

    # Calcula o erro
    erro.append(abs(xsol[t] - xsol[t-1]))

    t += 1

# Exibir os resultados
print('Iteração\t x\t f(x)\t f\'(x)\t Erro')
for i in range(t):
    xi = xsol[i]
    fxi = f_expr.subs(x, xi)
    dfxi = df_expr.subs(x, xi)
    print(f'{i+1}\t {xi:.6f}\t {fxi:.6f}\t {dfxi:.6f}\t {erro[i]:.6e}')
