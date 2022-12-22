#Implemente um programa que calcula a posição final e a velocidade final de um móvel que descreve um MRUV.

#Interação com o usuário
print("Calcule a posição final (S) e a velocidade final (V) de um móvel que descreve MRUV.")
print("\nInsira as unidades de medida no S.I.\n")

s0 = eval(input("Posição Inicial (S0): "))
v0 = eval(input("Velocidade inicial (V0): "))
a = eval(input("Aceleração (a): "))
t = eval(input("Tempo (t): "))

#Cálculo da posição
s = s0 + (v0 * t) + (a * (t**2) / 2)

#Cálculo da velocidade
v = v0 + (a * t)

#Resultado
print("\nA posição final (S) é: ", round(s,2), " m.")
print("\nA velocidade final (V) é: ", round(v,2), " m/s.")