base_imponible = float(input("¿Cuál es su base imponible? "))
monto_iva = base_imponible * 0.15
precio_total = base_imponible + monto_iva

print(f"Base imponible: ${base_imponible:.2f}")
print(f"IVA (15%):      ${monto_iva:.2f}")
print(f"Total a pagar:  ${precio_total:.2f}")