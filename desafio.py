import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo
df = pd.read_csv("dados.csv")

# Média móvel de 7 dias
df["vendas_ma7"] = df["Vendas"].rolling(window=7).mean()

# Média móvel de 14 dias
df["vendas_ma14"] = df["Vendas"].rolling(window=14).mean()

# Gráfico
plt.figure(figsize=(10, 5))
plt.plot(df["Vendas"], label="Vendas")
plt.plot(df["vendas_ma7"], label="Média Móvel 7 dias")
plt.plot(df["vendas_ma14"], label="Média Móvel 14 dias")
plt.title("Vendas e Médias Móveis")
plt.xlabel("Dias")
plt.ylabel("Vendas")
plt.legend()
plt.grid(True)
plt.show()

# Coluna acima_da_media_movel
df["acima_da_media_movel"] = df["Vendas"] > df["vendas_ma7"]

# Percentual de dias acima da média móvel
percentual = (
    df["acima_da_media_movel"].sum()
    / df["acima_da_media_movel"].count()
) * 100

print("Percentual de dias acima da média móvel:", percentual, "%")

# Exportar para CSV
df.to_csv("dados.csv", index=False)

print("Arquivo salvo com sucesso!")
