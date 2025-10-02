import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar dataset
df = pd.read_csv("ecommerce_estatistica (1).csv")

# 1. Distribuição dos preços
fig = px.histogram(df, x="Preço", nbins=30, title="Distribuição dos Preços")
fig.show()

# 2. Notas vs número de avaliações
fig = px.scatter(df, x="N_Avaliações", y="Nota", size="Preço",
                 color="Marca", hover_name="Título",
                 title="Nota vs Número de Avaliações (tamanho = Preço)")
fig.show()

# 3. Top 10 marcas mais vendidas
top_marcas = df.groupby("Marca")["Qtd_Vendidos_Cod"].sum().sort_values(ascending=False).head(10).reset_index()
fig = px.bar(top_marcas, x="Marca", y="Qtd_Vendidos_Cod", title="Top 10 Marcas por Quantidade Vendida")
fig.show()

# 4. Desconto médio por temporada
desconto_temporada = df.groupby("Temporada")["Desconto"].mean().reset_index()
fig = px.bar(desconto_temporada, x="Temporada", y="Desconto", title="Desconto Médio por Temporada")
fig.show()

# 5. Correlação entre variáveis numéricas
num_cols = ["Nota", "N_Avaliações", "Desconto", "Preço", "Qtd_Vendidos_Cod"]
corr = df[num_cols].corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Mapa de Correlação entre Variáveis Numéricas")
plt.show()

# Interativo
fig = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale="RdBu",
                title="Mapa de Correlação Interativo")
fig.show()
