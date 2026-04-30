import math
from typing import Optional

def kettenlinie_punkt(a: float, x: float) -> float:
    """
    Berechnet die Höhendifferenz der Kettenlinie an Stelle x.
    Die Formel ist so umgestellt, dass wir f(a) = 0 suchen.
    """
    return a * math.cosh(x / a) - a - 10

def finde_kruemmungsradius(start_a: float, end_a: float, tol: float = 10**-7) -> Optional[float]:
    """
    Findet den Krümmungsradius 'a' mittels Bisektion im Intervall [start_a, end_a].
    """
    try:
        a_unten = start_a
        a_oben = end_a
        
        # Check, ob ein Vorzeichenwechsel vorliegt
        if kettenlinie_punkt(a_unten, 50) * kettenlinie_punkt(a_oben, 50) >= 0:
            print("Fehler: Startintervall für 'a' ungültig.")
            return None

        # Bisektions-Schleife
        while (a_oben - a_unten) / 2 > tol:
            a_mitte = (a_unten + a_oben) / 2
            if kettenlinie_punkt(a_mitte, 50) == 0:
                return a_mitte
            
            if kettenlinie_punkt(a_unten, 50) * kettenlinie_punkt(a_mitte, 50) < 0:
                a_oben = a_mitte
            else:
                a_unten = a_mitte
        
        return (a_unten + a_oben) / 2
    except Exception as e:
        print(f"Fehler bei der Suche nach a: {e}")
        return None

def berechne_seillaenge(a: float, w: float) -> float:
    """
    Berechnet die Länge l des Seils.
    l = 2 * a * sinh(w / (2 * a))
    """
    return 2 * a * math.sinh(w / (2 * a))

if __name__ == "__main__":
    print("--- Berechnung der Stromleitung (Aufgabe 9) ---")
    
    # 1. Schritt: Den unbekannten Radius 'a' finden
    # Wir suchen im Bereich 10 bis 500, da 'a' meist größer als der Durchhang ist.
    radius_a = finde_kruemmungsradius(10.0, 500.0)
    
    if radius_a:
        print(f"Gefundener Krümmungsradius a: {radius_a:.4f}")
        
        # 2. Schritt: Die Seillänge berechnen (Abstand w = 100m)
        laenge = berechne_seillaenge(radius_a, 100.0)
        print(f"Die Gesamtlänge der Leitung beträgt: {laenge:.2f} Meter")
    else:
        print("Berechnung fehlgeschlagen.") 