import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dados_gerados import dados_ecommerce

#Separando as colunas para facilitar a leitura do codigo
visitas_col = dados_ecommerce[:, 0]
tempo_col = dados_ecommerce[:, 1]
itens_col = dados_ecommerce[:, 2]
valor_col = dados_ecommerce[:, 3]

print("--- ANÁLISE ESTATÍSTICA GERAL ---")

#Média
media_visitas = np.mean(visitas_col)
media_tempo = np.mean(tempo_col)
media_itens = np.mean(itens_col)
media_valor = np.mean(valor_col)

print(f"\nMédia de Visitas: {media_visitas:.2f}")
print(f"Média de Tempo no Site: {media_tempo:.2f} min")
print(f"Média de Itens no Carrinho: {media_itens:.2f}")
print(f"Média de Valor de compra (Ticket Médio): R${media_valor:.2f}")

#Mediana (valor central, menos sensível a outliers)
mediana_valor = np.median(valor_col)
print(f"\nMediana do Valor de Compra: R$ {mediana_valor:.2f}")

#Desvio padrão (mede a dispersão dos dados)
std_valor = np.std(valor_col)
print(f"Desvio Padrão do Valor de Compra: R$ {std_valor:.2f}")

#Valores Máximos e Mínimos
max_valor = np.max(valor_col)
min_valor_positivo = np.min(valor_col[valor_col > 0])   #minimo apenas entre quem comprou
print(f"Maior Valor de Compra: R$ {max_valor:.2f}")
print(f"Menor Valor de Compra (de quem comprou): R$ {min_valor_positivo:.2f}")

#---GRÁFICO---

plt.figure(figsize = (12, 5))
plt.hist(valor_col, bins = 30, color = 'skyblue', edgecolor = 'black', alpha = 0.7)
plt.axvline(media_valor, color = 'red', linestyle = '--', linewidth = 2, label = f'Média = R$ {media_valor:.2f}')
plt.axvline(mediana_valor, color = 'orange', linestyle = '--', linewidth = 2, label = f'Mediana = R$ {mediana_valor:.2f}')
plt.axvline(media_valor + std_valor, color = 'green', linestyle = ':', linewidth = 2, label = f'+1 DP = R$ {media_valor + std_valor:.2f}')
plt.axvline(media_valor - std_valor, color = 'green', linestyle = ':', linewidth = 2, label = f'-1 DP = R$ {media_valor - std_valor:.2f}')
plt.title('Distribuição dos Valores de Compra')
plt.xlabel('Valor da Compra (R$)')
plt.ylabel('Frequência')
plt.legend()
plt.grid(alpha = 0.3)
plt.show()

#Segmentação para distinguir o comportamento dos clientes de "Alto Valor"

#filtro booleano para cliente com compras > 250
cliente_alto_valor = dados_ecommerce[dados_ecommerce[:, 3] > 250]
print("\n--- ANÁLISE: CLIENTES DE ALTO VALOR (COMPRAS > 250) ---\n")
print(f"Número de clientes de alto valor: {cliente_alto_valor.shape[0]}")

media_visitas_alto_valor = np.mean(cliente_alto_valor[:, 0])
media_tempo_alto_valor = np.mean(cliente_alto_valor[:, 1])

print(f"Média de visitas desses clientes: {media_visitas_alto_valor:.2f}")
print(f"Média de tempo no site desses clientes: {media_tempo_alto_valor:.2f} min")

#Segmentação para entender os usuarios que visitam o site, porem não compram

#filtro para visitantes que não compram
visitante_sem_compra = dados_ecommerce[dados_ecommerce[:, 3] == 0]
print("\n --- ANÁLISE: VISITANTE QUE NÃO COMPRAM ---\n")
print(f"Número de visitantes que não compram: {visitante_sem_compra.shape[0]}")

#Estatistica deste segmento
media_visitas_sem_compra = np.mean(visitante_sem_compra[:, 0])
media_tempo_sem_compra = np.mean(visitante_sem_compra[:, 1])

print(f"Média de visitas desses visitantes: {media_visitas_sem_compra:.2f}")
print(f"Apesar de não comprarem, eles passam em média {media_tempo_sem_compra:.2f} min no site")


#Análise de correlação

#a função np.corrcoef calcula a matriz de correlação
#rowvar=False indica que as colunas são as variáveis
matriz_correlacao = np.corrcoef(dados_ecommerce, rowvar=False)

print("\n--- MATRIZ DE CORRELAÇÃO ---\n")
print("[Visitas, Tempo, Itens, Valor]\n")
print(np.round(matriz_correlacao, 2))

nome_variaveis = ["Visitas", "Tempo no site", "Itens no carrinho", "Valor da compra"]

#converte em DataFrame para exibir com rótulos
df_correlacao = pd.DataFrame(matriz_correlacao,
                             index=nome_variaveis,
                             columns=nome_variaveis)

#matriz de correlação (mapa de calor)
plt.figure(figsize=(7, 5))
sns.heatmap(df_correlacao, annot=True, cmap="Blues", fmt=".2f")
plt.title("Matriz de Correlação")
plt.show()