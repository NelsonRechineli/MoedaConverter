qtd = float(input("Quantos REAIS você tem: "))
print("1. Euro")
print("2. Dollar")
print("3. Libra")
resp = int(input("Deseja converter Reais em: "))


if resp == 1:
  conv=qtd* 5.48
  print(qtd," Reais em Euro = ",conv)

if resp == 2:
  conv=qtd* 5.11
  print(qtd," Reais em Dollar = ",conv)

if resp == 3:
  conv=qtd* 6.41
  print(qtd," Reais em Libra = ",conv)
  