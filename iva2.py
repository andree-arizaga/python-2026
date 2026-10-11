base_imponible = float(input("¿Cuál es su base imponible? "))
if base_imponible < 0:
    print("Error: La base imponible no puede ser negativa.")
else:
    tarifa = float(input("¿Cual es su tarifa de IVA? "))
    if tarifa < 0:
        print("Error: La tarifa de IVA no puede ser negativa.")
    else:
        monto_iva = base_imponible * (tarifa/100)
        precio_total = base_imponible + monto_iva
        print(f"Base imponible: ${base_imponible:.2f}")
        print(f"IVA ({tarifa}%): ${monto_iva:.2f}")
        print(f"Total a pagar:  ${precio_total:.2f}")