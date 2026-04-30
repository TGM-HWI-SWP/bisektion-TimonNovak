import math

def berechne(formel, x):
    return eval(formel, {"x": x, "math": math, "sinh": math.sinh, "cosh": math.cosh})

def regula_falsi_löser(funktion, a, b, genauigkeit=1e-7):
    """
    Hier nutzen wir die Sekanten-Formel aus dem PDF, 
    um die Nullstelle schneller zu finden.
    """
    try:
        fa = berechne(funktion, a)
        fb = berechne(funktion, b)

        if fa * fb >= 0:
            print("Kein Vorzeichenwechsel – so wird das nichts!")
            return None

        # Wir machen maximal 100 Schritte, damit sich das Programm nicht aufhängt
        for schritt in range(100):
            # Das ist die Formel aus deinem Aufgabenblatt:
            # c = b - f(b) * (b - a) / (f(b) - f(a))
            c = b - fb * ((b - a) / (fb - fa))
            fc = berechne(funktion, c)

            # Wenn wir nah genug dran sind, hören wir auf
            if abs(fc) < genauigkeit:
                return c
            
            # Das neue Intervall festlegen, genau wie bei der Bisektion[cite: 1]
            if fa * fc < 0:
                b, fb = c, fc
            else:
                a, fa = c, fc
        return c
    except ZeroDivisionError:
        print("Fehler: Division durch Null!")
        return None

# --- Testlauf mit deiner Katalognummer 12 ---
n = 12
ergebnis_rf = regula_falsi_löser(f"x**2 - {n}", 0, 24) 

print(f"--- Ergebnis Aufgabe 6 ---")
if ergebnis_rf:
    print(f"Regula Falsi Wurzel aus {n}: {ergebnis_rf:.5f}")