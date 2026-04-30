import math
from typing import Optional

def polynom_p4(x: float) -> float:
    """
    Das Polynom aus dem Theorieteil der Aufgabe 8.
    f(x) = 2x + x^2 + 3x^3 - x^4
    """
    return 2*x + x**2 + 3*x**3 - x**4

def bisektion_test_p4(a: float, b: float, epsilon: float) -> Optional[float]:
    """
    Ein einfacher Bisektions-Löser, der die Anzahl der Schritte mitzählt.
    """
    if polynom_p4(a) * polynom_p4(b) >= 0:
        print("Zwischenwertsatz nicht anwendbar!")
        return None

    schritte = 0
    # Wir machen so lange weiter, bis das Intervall kleiner als unser Epsilon ist
    while (b - a) / 2 > epsilon:
        schritte += 1
        mitte = (a + b) / 2
        
        if polynom_p4(mitte) == 0:
            break
            
        if polynom_p4(a) * polynom_p4(mitte) < 0:
            b = mitte
        else:
            a = mitte
            
    print(f"Fertig! Bei Epsilon {epsilon} wurden {schritte} Schritte benötigt.")
    return (a + b) / 2

if __name__ == "__main__":
    # Laut Theorie liegt eine Nullstelle bei x = 3,4567. 
    # Wir wählen das Intervall [3, 4] für den Test.
    start_a = 3.0
    start_b = 4.0

    print("--- Analyse des Polynoms P4 ---")
    
    # Test 1: Genauigkeit 10^-2
    ergebnis_1 = bisektion_test_p4(start_a, start_b, 10**-2)
    print(f"Ergebnis (10**-2): {ergebnis_1:.4f}\n")

    # Test 2: Genauigkeit 10^-8
    ergebnis_2 = bisektion_test_p4(start_a, start_b, 10**-8)
    print(f"Ergebnis (10**-8): {ergebnis_2:.8f}")