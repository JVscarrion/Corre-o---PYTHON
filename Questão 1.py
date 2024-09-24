tupla = ("Botafogo", "Fortaleza", "Flamengo", "Palmeiras", "São Paulo", "Cruzeiro", "Bahia", "Athletico-PR", "Atlético-MG", "Vasco" , "Bragantino", "Juventude", "Grêmio",
"Criciúma", "Internacional", "Vitória", "Corinthians", "Fluminense", "Cuiabá", "Atlético-GO")


cinco_colocados = tupla[:5]
print(cinco_colocados)

ultimos_quatro = tupla[-4:]
print(ultimos_quatro)

lista_ordem = sorted(tupla)
print(lista_ordem)

time_position = tupla.index("Criciúma")
print(time_position)
