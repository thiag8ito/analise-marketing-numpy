[MiniProjeto3.ipynb](https://github.com/user-attachments/files/24987266/MiniProjeto3.ipynb)
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5b4d422e-b7aa-43af-a208-9ebf01c60e9f",
   "metadata": {},
   "source": [
    "## 1. Definição do Problema de Negócio"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "48ece6a5-d10f-4ce3-a7e1-9d920762762f",
   "metadata": {},
   "source": [
    "### 1.1. Contexto\n",
    "\n",
    "Uma plataforma de e-commerce coleta um volume significativo de dados sobre a interação dos usuários com o site, incluindo o número de visitas, a duração da sessão, a atividade de adição de produtos ao carrinho e os valores de compra finalizados. No entanto, esses dados estão sendo subutilizados. Atualmente, as decisões sobre campanhas de marketing, promoções e melhorias na experiência do usuário (UX) são tomadas com base em intuição e métricas de alto nível, sem uma compreensão aprofundada dos padrões de comportamento que impulsionam os resultados.\n",
    "\n",
    "### 1.2. Problema de Negócio\n",
    "\n",
    "A empresa enfrenta o desafio de compreender profundamente os padrões de comportamento que diferenciam os clientes de alto valor dos visitantes que abandonam o site sem comprar. Essa falta de clareza resulta em:\n",
    "\n",
    "- Marketing Genérico: Nossas campanhas de marketing são de \"tamanho único\", resultando em baixo engajamento e desperdício de orçamento, pois não conseguimos personalizar as ofertas para os segmentos de clientes corretos.\n",
    "\n",
    "- Perda de Oportunidades: Não conseguimos identificar e engajar proativamente os clientes com maior potencial de compra ou criar estratégias para converter os visitantes que demonstram interesse, mas não finalizam a compra.\n",
    "\n",
    "- Decisões Não Embasadas: As estratégias de produto e de experiência do usuário carecem de uma base quantitativa sólida sobre quais comportamentos (ex: tempo no site, frequência de visitas) estão mais fortemente correlacionados com o sucesso das vendas.\n",
    "\n",
    "### 1.3. Objetivo Principal\n",
    "\n",
    "Utilizar a análise estatística dos dados de navegação e compra para segmentar clientes, identificar os principais indicadores de comportamento que levam à conversão e fornecer insights acionáveis para as equipes de marketing e produto, a fim de aumentar o ticket médio e a taxa de conversão geral da plataforma.\n",
    "\n",
    "### 1.4. Perguntas-Chave a Serem Respondidas\n",
    "\n",
    "A análise de dados deve responder às seguintes perguntas críticas de negócio:\n",
    "\n",
    "- 1- Qual é o perfil médio do nosso usuário em termos de visitas, tempo de navegação e valor de compra (ticket médio)?\n",
    "\n",
    "- 2- Quais são as características e comportamentos distintos dos nossos clientes de \"Alto Valor\"? Eles visitam mais o site? Passam mais tempo navegando?\n",
    "\n",
    "- 3- Qual é o comportamento dos usuários que visitam o site, mas não realizam nenhuma compra? Onde está a oportunidade de conversão com este grupo?\n",
    "\n",
    "- 4- Existe uma correlação estatisticamente relevante entre o tempo gasto no site, o número de itens no carrinho e o valor final da compra?\n",
    "\n",
    "### 1.5. Resultado Esperado e Impacto no Negócio\n",
    "\n",
    "O resultado deste projeto será um relatório de análise estatística que permitirá:\n",
    "\n",
    "- Segmentação Aprimorada: Criação de pelo menos dois segmentos de clientes (ex: \"Clientes de Alto Valor\" e \"Visitantes Engajados sem Compra\") para direcionamento de campanhas de marketing personalizadas.\n",
    "\n",
    "- Otimização de Marketing: Direcionar o orçamento de marketing para ações focadas nos comportamentos que mais se correlacionam com compras de alto valor, aumentando o Retorno Sobre o Investimento (ROI).\n",
    "\n",
    "- Melhoria da Experiência do Usuário (UX): Fornecer à equipe de produto dados que possam justificar testes A/B ou melhorias em áreas do site frequentadas por usuários que não convertem."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "38a245f3",
   "metadata": {},
   "source": [
    "-\n",
    "-\n",
    "-\n",
    "-\n",
    "-\n",
    "-\n",
    "-\n",
    "-\n",
    "-\n",
    "-\n",
    "-\n",
    "-\n",
    "-\n",
    "-\n",
    "-\n",
    "-\n",
    "-"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "48de63f4-adcf-4e63-86e7-26ce0e064f8d",
   "metadata": {},
   "source": [
    "## Relatório Final, Conclusões e Insights a Partir dos Dados\n",
    "\n",
    "A análise estatística dos dados de navegação e compras dos usuários do e-commerce permitiu compreender melhor o comportamento dos clientes e identificar padrões diretamente relacionados à geração de receita.\n",
    "\n",
    "**1. Perfil Geral dos Usuários**\n",
    "\n",
    "Os usuários acessam a plataforma em média 25,86 vezes por mês, permanecendo cerca de 32,78 minutos no site por sessão. Cada cliente adiciona, em média, 5,51 itens ao carrinho e realiza compras com ticket médio de R$ 193,55\n",
    "\n",
    "A mediana do valor gasto é de R$ 187.54\n",
    "\n",
    "Isso indica que metade dos clientes compra abaixo e metade acima desse valor. Observou-se uma dispersão considerável nos gastos (desvio padrão de R$ 96,03). As compras variam de 14,58 (mínimo) a 425,37 (máximo registrado).\n",
    "\n",
    "Esses números mostram que existe um grupo expressivo de consumidores que gasta significativamente mais que a média, mas também há grande variação no comportamento de compra.\n",
    "\n",
    "**2. Clientes de Alto Valor**\n",
    "\n",
    "Ao analisar os clientes que gastam mais de R$ 250, identificou-se um total de 136 usuários, representando aproximadamente metade da base analisada. Este grupo se destaca por visitar mais vezes o site (36,06 visitas em média) e permanecer por mais tempo (38,19 minutos), comparado ao perfil geral.\n",
    "<!-- Trabalho Desenvolvido no Curso da Data Science Academy - www.datascienceacademy.com.br -->\n",
    "Isso sugere que engajamento elevado, tanto em frequência de visitas quanto em tempo de navegação, está fortemente associado a compras de maior valor. Esses clientes podem ser considerados um segmento prioritário para ações de fidelização, programas de recompensa e campanhas personalizadas.\n",
    "\n",
    "**3. Visitantes Que Não Compram**\n",
    "\n",
    "Foi identificado apenas 14 usuário que navega sem realizar compras. Apesar de representar um caso isolado nesta base, ele visita em média 5,86 vezes e permanece 23,53 minutos no site. Esse comportamento, mesmo pouco expressivo aqui, ilustra a importância de monitorar usuários engajados que não convertem, pois podem representar oportunidades para campanhas de remarketing, melhorias no processo de checkout ou incentivos específicos para concluir a compra.\n",
    "\n",
    "**4. Relações Entre Comportamentos e Receita**\n",
    "\n",
    "A matriz de correlação revelou informações valiosas:\n",
    "\n",
    "- Itens no Carrinho ↔ Valor da Compra = 0,99 → correlação positiva perfeita; cada item adicional impacta diretamente o valor gasto.\n",
    "\n",
    "- Tempo no Site ↔ Itens no Carrinho = 0,45 → correlação moderada; usuários que permanecem mais tempo tendem a adicionar mais itens.\n",
    "\n",
    "- Tempo no Site ↔ Valor da Compra = 0,45 → correlação moderada; quanto mais tempo no site, maior tende a ser a compra.\n",
    "\n",
    "- Visitas ↔ Valor da Compra = 0,54 → correlação positiva; maior frequência de acessos também contribui para compras maiores.\n",
    "\n",
    "Esses resultados confirmam que engajamento do usuário (tempo e visitas) influencia a construção do carrinho e, consequentemente, o valor final da compra. Embora seja necessário confirmar a significância estatística com testes adicionais (p-valor), a força das correlações já orienta decisões estratégicas.\n",
    "\n",
    "**5. Conclusões e Recomendações**\n",
    "\n",
    "- Segmentação estratégica: os clientes de alto valor apresentam comportamento diferenciado, com maior frequência e tempo de navegação. Esse grupo deve ser alvo de campanhas personalizadas e programas de fidelidade para aumentar retenção e ticket médio.\n",
    "\n",
    "- Incentivo à construção de carrinho: como a quantidade de itens é fator determinante no valor gasto, estratégias como recomendações personalizadas, descontos progressivos e combos podem elevar o ticket médio.\n",
    "\n",
    "- Aproveitamento de visitantes engajados sem compra: embora pouco representativo aqui, vale investir em remarketing e otimização de UX para reduzir fricções no checkout e converter quem demonstra interesse.\n",
    "\n",
    "- Base quantitativa para decisões: a análise estatística mostra que dados simples (visitas, tempo, itens) já oferecem insights poderosos para melhorar campanhas de marketing e decisões de produto, substituindo ações baseadas apenas em intuição.\n",
    "\n",
    "Este Mini-Projeto, embora simples, demonstra como o NumPy, com poucas linhas de código, nos permite realizar uma análise estatística poderosa, desde a visão geral até a segmentação e correlação, transformando dados brutos em insights de negócio."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e70e92c-24ab-4d41-8362-89841f80232f",
   "metadata": {},
   "source": [
    "# Fim"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
