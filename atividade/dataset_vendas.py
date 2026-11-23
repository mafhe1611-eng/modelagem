import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n = 90
datas = pd.date_range("2025-01-01", periods=n, freq="D")

tendencia = np.linspace(100, 160, n)
sazonal = 25 * np.sin(np.arange(n) * 2 * np.pi / 7)
ruido = np.random.normal(0, 12, n)
vendas = (tendencia + sazonal + ruido).clip(min=40).round(0).astype(int)

lojas = np.random.choice(["Centro", "Norte", "Sul"], size=n)

df = pd.DataFrame({
    "data": datas,
    "loja": lojas,
    "vendas": vendas,
    "dia_semana": datas.day_name(),
    "mes": datas.month
})

# Introduzir faltantes
df.loc[df.sample(6, random_state=42).index, "vendas"] = np.nan

print(df.head(10))
print("\nShape:", df.shape)
print("\nFaltantes:\n", df.isna().sum())

# Preenche os valores faltantes com a média da mesma loja
df["vendas_preenchida"] = df["vendas"].fillna(
    df.groupby("loja")["vendas"].transform("mean")
)
print("NaN restantes em vendas_preenchida:")
print(df["vendas_preenchida"].isna().sum())

estatisticas = df.groupby("loja")["vendas_preenchida"].agg([
    "mean",
    "median",
    "std"
])
print("Estatísticas por loja:", estatisticas) # media, mediana e desvio padrão

# loja com maior média e maior desvio padrão
maior_media = estatisticas["mean"].idxmax()
maior_desvio = estatisticas["std"].idxmax()
print("\nLoja com maior média de vendas:", maior_media)
print("\nLoja com maior desvio padrão:", maior_desvio)

# dia da semana com maior e menor média de vendas
media_dia = df.groupby("dia_semana")["vendas_preenchida"].mean()
print("\nMédia de vendas por dia da semana:", media_dia)
print("\nDia da semana com maior média:", media_dia.idxmax())
print("\nDia da semana com menor média:", media_dia.idxmin())

# criar a coluna eh_fim_de_semana
df["eh_fim_de_semana"] = df["dia_semana"].isin(["Saturday", "Sunday"])
print(df[["dia_semana", "eh_fim_de_semana"]].head())

# compara a média de vendas_preenchida
media = df.groupby("eh_fim_de_semana")["vendas_preenchida"].mean()
print("\nMédia de vendas:", media)

# criar a coluna vendas_ma7 
df["vendas_ma7"] = df["vendas_preenchida"].rolling(window=7).mean()
print(df[["vendas_preenchida", "vendas_ma7"]].head(10))

# gráfico de linha das vendas ao longo do tempo
plt.figure(figsize=(10,5))
plt.plot(df["data"], df["vendas_preenchida"], color="blue")
plt.title("Vendas ao Longo do Tempo")
plt.xlabel("Data")
plt.ylabel("Vendas")
plt.grid(True)
plt.show()

# gráfico de barras horizontais com a média por loja
media_lojas = df.groupby("loja")["vendas_preenchida"].mean()
plt.figure(figsize=(8,4))
media_lojas.sort_values().plot(
    kind="barh",
    color=["#4C72B0", "#DD8452", "#55A868"]
)
plt.title("Média de Vendas por Loja")
plt.xlabel("Média de Vendas")
plt.ylabel("Loja")
plt.show()
