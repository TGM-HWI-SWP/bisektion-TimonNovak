import math
from typing import Optional

def berechne_f_von_x(formel: str, x: float) -> float:
    """Hilfsfunktion, um einen Mathe-String in eine Zahl zu verwandeln."""
    # Wir erlauben math-Funktionen wie sin, cos, sinh etc.
    return eval(formel, {"x": x, "math": math, "sin": math.sin, "cos": math.cos, 
                         "sinh": math.sinh, "cosh": math.cosh})

def bisektion_löser(funktion: str, a: float, b: float, genauigkeit: float = 1e-7) -> Optional[float]:
    """
    Sucht die Nullstelle durch ständiges Halbieren des Intervalls.
    """
    try:
        # Erstmal checken, ob an den Grenzen überhaupt ein Vorzeichenwechsel ist
        wert_a = berechne_f_von_x(funktion, a)
        wert_b = berechne_f_von_x(funktion, b)

        if wert_a * wert_b >= 0:
            print("Hoppla: Hier gibt's keinen Vorzeichenwechsel. Bisektion klappt so nicht!")
            return None

        # Wir halbieren so lange, bis das Intervall klein genug ist
        while (b - a) / 2 > genauigkeit:
            mitte = (a + b) / 2
            wert_mitte = berechne_f_von_x(funktion, mitte)

            # Wenn wir genau die Nullstelle erwischen, können wir sofort aufhören
            if wert_mitte == 0:
                return mitte
            
            # Schauen, in welcher Hälfte die Nullstelle weitergeht
            if wert_a * wert_mitte < 0:
                b = mitte
            else:
                a = mitte
                wert_a = wert_mitte # Alten Wert merken, spart Rechenzeit

        return (a + b) / 2

    except Exception as fehler:
        print(f"Da lief was schief: {fehler}")
        return None

# Test mit den Werten aus dem Projektblatt (n=25, 81, 144)
if __name__ == "__main__":
    zahlen = [25, 81, 144]
    print("--- Testläufe der Wurzelfunktionen ---")
    for n in zahlen:
        ergebnis = bisektion_löser(f"x**2 - {n}", 0, n)
        echte_wurzel = math.sqrt(n)
        if ergebnis is not None:
            print(f"Wurzel {n}: Berechnet: {ergebnis:.5f} | Echt: {echte_wurzel:.1f}")