saque = int(input('Informe o valor que você deseja  sacar '))


resto = saque

valor_50 = resto // 50
resto %= 50

valor_20 = resto // 20
resto %= 20

valor_10 = resto // 10
resto %= 10

print(f"Notas de R$ 50: {valor_50}")
print(f"Notas de R$ 20: {valor_20}")
print(f"Notas de R$ 10: {valor_10}") 