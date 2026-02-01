import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Definir uma seed para reprodutibilidade dos resultados
np.random.seed(42)

#Definir o numero de usuarios
num_usuarios = 500

#1. Gerar o numero de visitas (entre 1 e 50)
visitas = np.random.randint(1, 51, size=num_usuarios)

#2. Gerar o tempo no site, (distribuição normal, correlacionando com as visitas)
#Media de 20 min, desvio padrão de 5, com um bonus por visita
tempo_no_site = np.random.normal(loc=20, scale=5, size=num_usuarios) + (visitas *.5)
tempo_no_site = np.round(tempo_no_site, 2)  #arredondar para 2 casas decimais

#3. Gerar o numero de itens no carrinho (dependente das visitas e do tempo)
#Usuarios que visitam mais e passam mais tempo, tendem a adicionar mais itens
itens_no_carrinho = np.random.randint(0, 8, size=num_usuarios) + (visitas // 10)

#4. Gerar o valor da compra (correlacionando com os itens no carrinho)'
#Preço médio por item de R$ 35, com alguma variação aleatoria
valor_compra = (itens_no_carrinho * 35) + np.random.normal(loc=0, scale=10, size=num_usuarios)

#Se não houver itens no carrinho, o valor da compra deve ser 0
valor_compra[itens_no_carrinho == 0] = 0
valor_compra[valor_compra < 0] = 0  #corrigir valores negativos
valor_compra = np.round(valor_compra, 2)

#Unindo tudo em uma unica matriz (ndarray)
#cada linha representa um usuario, cada coluna uma metrica
dados_ecommerce = np.column_stack((visitas, tempo_no_site, itens_no_carrinho, valor_compra))

print("\nShape da nossa massa de dados: ", dados_ecommerce.shape)
print("\nExemplo dos 5 primeiros usuarios (linhas):")
print("\nColunas: [Visitas, Tempo no Site(min), Itens no carrinho, Valor da Compra (R$)]\n")
print(dados_ecommerce[:5])