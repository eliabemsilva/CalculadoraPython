# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

adicao = lambda x,y: x + y
subtracao = lambda x,y: x - y
multiplicacao = lambda x,y: x * y
divisao = lambda x,y: x / y
potenciacao = lambda x,y: x ** y
porcentagem = lambda x,y: (x * y) / 100

print("\nOperações: \n")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potenciação")
print("6 - Porcentagem")

escolha = int(input("\nDigite a sua opção (1, 2, 3, 4, 5 ou 6): "))

if escolha >= 1 and escolha <= 6:
  num1 = int(input("\nDigite o primeiro número: "))
  num2 = int(input("\nDigite o segundo número: "))
  
  if escolha == 1:
    print("\n")
    print(num1, "+", num2, "=", adicao(num1, num2))
    print("\n")
    
  elif escolha == 2:
    print("\n")
    print(num1, "-", num2, "=", subtracao(num1, num2))
    print("\n")
    
  elif escolha == 3:
    print("\n")
    print(num1, "*", num2, "=", multiplicacao(num1, num2))
    print("\n")
    
  elif escolha == 4:
    print("\n")
    print(num1, "/", num2, "=", divisao(num1, num2))
    print("\n")
    
  elif escolha == 5:
    print("\n")
    print(num1, "^", num2, "=", potenciacao(num1, num2))
    print("\n")
    
  elif escolha == 6:
    print("\n")
    print(f"{num1}% *", num2, "=", porcentagem(num1, num2))
    print("\n")
    
else:
  print("Opção inválida! \n")
