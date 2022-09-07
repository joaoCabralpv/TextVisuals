def Linha(len, char):
    print(char*len)

def Triangulo(tipo, base, altura, char):
    for i in range(2 * altura):
        if  i % 2 != 0:
            print(" "*int((2*altura-i)/2) + char*i + " "*int((2*altura-i)/2)) 

listaOpecoes = ["Linha", "Triângulo equilatro", "Triângulo reto", "Triângulo reto invertido" ,"Retangulo", "Quadrado"]

print("="*27)
for i in range(len(listaOpecoes)):
    print("{}. {}".format(i+1, listaOpecoes[i]))
print("="*27)

escolha = int(input("Escolha uma opeção. Ex:1 :"))

if escolha == 1:
    Linha(int(input("Qual é o comprimento da linha?: ").strip()), input("Qual é o caractere que compõe a linha?: ").strip())
elif escolha == 2:
    Triangulo("Equilatro", 0, int(input("Qual é a altura do triângulo")), input("Qual é o caractere que compõe o triângulo?: "))
elif escolha == 3:
    Triangulo("Reto")
elif escolha == 4:
    Triangulo("Invertido")
elif escolha == 5:
    Retangulo()
elif escolha == 6:
    Quadrado()
else:
    print("\033[0;31m Erro, escolha invalida\033[0;0m")