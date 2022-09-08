def Linha(len, char):
    print(char*len)

def Triangulo(tipo, base, altura, char):
    if tipo == "Equilatro":
        for i in range(altura):
            j = 2*i-1
            print(" "*int((2*altura-j)/2) + char*j + " "*int((2*altura-j)/2))

    elif tipo == "Reto":            
        baseMaiorAltura = 1 if base > altura else 0
        porporcaoBaseAltura = base/altura
        for i in range(altura):
            print(char*int(i*((porporcaoBaseAltura))+1+baseMaiorAltura))
    




listaOpecoes = ["Linha", "Triângulo equilatro", "Triângulo reto","Retangulo", "Quadrado"]

print("="*27)
for i in range(len(listaOpecoes)):
    print("{}. {}".format(i+1, listaOpecoes[i]))
print("="*27)

escolha = int(input("Escolha uma opeção: "))

if escolha == 1:
    Linha(int(input("Qual é o comprimento da linha?: ").strip()), input("Qual é o caractere que compõe a linha?: ").strip()[0])
elif escolha == 2:
    Triangulo("Equilatro", 0, int(input("Qual é a altura do triângulo?: ")), input("Qual é o caractere que compõe o triângulo?: ").strip()[0])
elif escolha == 3:
    Triangulo("Reto", int(input("Qual é a base do triângulo?: ").strip()), int(input("Qual é a altura do triângulo?: ").strip()), input("Qual é o caractere que compõe o triângulo?: ")[0])
elif escolha == 4:
    Retangulo()
elif escolha == 5:
    Quadrado()
else:
    print("\033[0;31m Erro, escolha invalida\033[0;0m")