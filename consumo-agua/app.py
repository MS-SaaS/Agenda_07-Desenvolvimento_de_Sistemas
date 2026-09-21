tipo_de_local = input("Digite o tipo do imóvel (comercial, casa ou apartamento): ").strip().lower()
consumo = float(input("Digite o consumo de água em metros cúbicos: "))

if tipo_de_local == "comercial":
    print("Tarifa comercial aplicada — consulte o plano corporativo.")
elif tipo_de_local == "apartamento" and consumo < 10:
   print("Consumo econômico! Excelente controle de água.")
elif tipo_de_local == "apartamento" or "casa" and consumo <= 25:
   print("Consumo moderado — dentro do padrão residencial.")
else: print ("Consumo excessivo — adote medidas de economia e verifique vazamentos.")
