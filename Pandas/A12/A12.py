import pandas as pd

df = pd.DataFrame()
base = pd.read_csv("database2.csv")
r_df = base.drop(labels = list(range(17360)))
base = r_df
base = base.drop("user_id", axis=1)

bound = '='*23

#A)O valor da média, a mediana e a moda;
# MÉDIA
print("Média")
print(bound)
for i in base.columns:
    base[i] = pd.to_numeric(base[i], errors="coerce")
    print("{a:12s}|  {b:10f}".format(a=i, b=base[i].values.mean()))

# MODA
print(bound)
print()
#Moda
print("Moda")
print(bound)
for i in base.columns:
  print("{a:12s}|  {b:f}".format(a=i, b=base[i].mode()[0]))

# MEDIANA
print(bound)
print()
print("Mediana")
print(bound)
for i in base.columns:
  print("{a:12s}|  {b:f}".format(a=i, b=base[i].sort_values().median()))
print(bound)

#---------------------------------------------------------------------------

# B) todos os valores foram calculados com sucesso

#---------------------------------------------------------------------------

# C)
# assembly: distribuição simétrica 
# c: não simétrica, distribuição para a direita         
# c#:  não simétrica, distribuição para a direita     
# c++:  não simétrica, distribuição para a direita       
# css:  não simétrica, distribuição para a direita     
# go:  não simétrica, distribuição para a direita       
# haskell:  não simétrica, distribuição para a direita   
# html:  não simétrica, distribuição para a direita   
# java:  não simétrica, distribuição para a direita   
# javascript:  não simétrica, distribuição para a direita
# objective-c: não simétrica, distribuição para a direita
# php: não simétrica, distribuição para a direita     
# powershell: distribuição simétrica 
# python: não simétrica, distribuição para a direita
# ruby:  não simétrica, distribuição para a direita
# swift:  não simétrica, distribuição para a direita
# sql: distribuição simétrica

#---------------------------------------------------------------------------

#D) O valor do Desvio Absoluto Média, da variância e do desvio padrão (ou indicando, se for o caso, porque não pode ser calculado);


# DESVIO PADRÃO
print()
print("Desvio Padrão")
print(bound)
soma=0
for i in base.columns:
  base[i] = pd.to_numeric(base[i], errors="coerce")
  media = base[i].values.mean()
  for x in range(100):
    soma+=(base[i].values[x]-media)**2
  #print(a=i, b=base[i].sort_values().median()))
  print("{a:12s}|  {b:f}".format(a=i, b=(soma/100)**0.5))
  soma=0
print(bound)

#---------------------------------------------------------------------------

# Variancia
print()
print("Variância")
print(bound)
soma=0
for i in base.columns:
  base[i] = pd.to_numeric(base[i], errors="coerce")
  media = base[i].values.mean()
  for x in range(100):
    soma+=(base[i].values[x]-media)**2
  #print(a=i, b=base[i].sort_values().median()))
  print("{a:12s}|  {b:f}".format(a=i, b=(soma/100)))
  soma=0
print(bound)

#---------------------------------------------------------------------------

# DESVIO ABSOLUTO MÉDIO
print()
print("Desvio Absoluto Médio")
print(bound)
soma=0
for i in base.columns:
  base[i] = pd.to_numeric(base[i], errors="coerce")
  media = base[i].values.mean()
  for x in range(100):
    soma+=(base[i].values[x]- media)
  print("{a:12s}|  {b:f}".format(a=i, b=(soma/100)))
  soma=0
print(bound)

#--------------------------------------------------------------------------

#E)
