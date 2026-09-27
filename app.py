excelente = 0
ruim = 0

print("========================================")
print("   PESQUISA DE SATISFAÇÃO - TUDOWEB")
print("========================================")

for i in range(1, 51):
    print(f"\n--- Entrevistado {i} de 50 ---")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("\nQual sua opinião sobre o atendimento?")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite o número da opinião: "))

    # Estrutura de decisão
    if opiniao == 1:
        excelente += 1
        print(f"{nome}, sua resposta foi registrada como EXCELENTE.")

    elif opiniao == 2:
        print(f"{nome}, sua resposta foi registrada como BOM.")

    elif opiniao == 3:
        ruim += 1
        print(f"{nome}, sua resposta foi registrada como RUIM.")

    else:
        print("Opção inválida. Resposta não contabilizada.")

print("\n========================================")
print("           RESULTADO DA PESQUISA")
print("========================================")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")
print("========================================")