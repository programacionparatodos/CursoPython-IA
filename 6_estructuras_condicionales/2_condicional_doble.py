# ==============================================================================
# # 6_condicionales -> 2_condicional_doble.py
# ==============================================================================

# ==============================================================================
# * SECCIÓN 4: LA CONDICIONAL DOBLE
# ==============================================================================

# ------------------------------------------------------------------------------
# * 4.1 Bifurcación Exclusiva (Control de Retiros)
# ------------------------------------------------------------------------------
# ? Simulación de fondos en una cuenta bancaria y solicitud del cliente
saldo_disponible = 1500
monto_solicitado = 2000

print("Procesando transacción bancaria...")

# * Si el cliente tiene el dinero suficiente va al IF; de lo contrario, cae directo al ELSE
if monto_solicitado <= saldo_disponible:
    print("Transacción aprobada.")
    print("-> Entregando dinero en efectivo. Retire sus billetes.")
else:
    print("Transacción denegada.")
    print("-> Error: Fondos insuficientes para completar el retiro.")

print("Operación finalizada. Retire su tarjeta magnética.")

# TODO: Recordar que el 'else' jamás lleva una condición escrita a su lado; es el descarte automático.


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: Inicialización forzada de variables dentro de un bloque IF-ELSE
# ? En Python, si creas una variable solo dentro del 'if', pero la condición falla y cae
# ? en el 'else', esa variable nunca existirá. Debes garantizar que ambos caminos la definan.
intentos_pin = 3

if intentos_pin >= 3:
    # * Si se bloquea la tarjeta, definimos la variable de estado
    tarjeta_bloqueada = True
    mensaje_cajero = "Tarjeta bloqueada por seguridad. Acuda a una sucursal."
else:
    # * Si no la definimos aquí, Python lanzará un NameError al intentar usarla abajo
    tarjeta_bloqueada = False
    mensaje_cajero = "PIN correcto. Accediendo al menú principal..."

print(f"Estado del ATM: {mensaje_cajero}")

# * Ejemplo B: La trampa de evaluar condiciones independientes simulando un ELSE
# ? Poner dos bloques 'if' seguidos NO es lo mismo que usar un 'if-else'.
# ? Si la primera condición altera la variable, el segundo 'if' podría ejecutarse por accidente.
monto_retiro = 500
saldo_cajero_automatico = 500

print("\n--- Analizando el peligro de dos IF independientes ---")
if monto_retiro <= saldo_cajero_automatico:
    print("Entregando billetes...")
    saldo_cajero_automatico = saldo_cajero_automatico - monto_retiro # Ahora el saldo es 0

if monto_retiro > saldo_cajero_automatico:
    # ! ¡ERROR! Como el saldo cambió a 0 arriba, esta condición AHORA ES VERDADERA y se ejecuta también.
    print("Error simulado: Dinero insuficiente en el cajero físico.") 

# * Ejemplo C: Controlar cadenas vacías con valores por defecto usando IF-ELSE
# ? Si el usuario presiona "Enter" en el teclado sin escribir nada en el input de la cuenta.
cuenta_ingresada = "" # Simula un input vacío

if cuenta_ingresada.strip() == "":
    cuenta_final = "Cuenta Corriente Por Defecto"
else:
    cuenta_final = cuenta_ingresada

print(f"Transacción asociada a: {cuenta_final}") # Muestra: Cuenta Corriente Por Defecto
