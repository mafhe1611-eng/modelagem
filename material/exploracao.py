import pandas as pd

df = pd.read_csv("dados.csv")

df["eh_fim_de_semana"] = df["Dia_semana"].isin(["Sábado", "Domingo"])
print("Coluna eh_fim_de_semana:")
print(df[["Dia_semana", "eh_fim_de_semana"]])

media = df.groupby("eh_fim_de_semana")["Vendas"].mean()
print("Média de vendas:")
print(media)

df["vendas_ma7"] = df["Vendas"].rolling(window=7).mean()
print("Vendas móveis (7 dias):")
print(df[["Dia_semana", "Vendas", "vendas_ma7"]])