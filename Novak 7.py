import matplotlib.pyplot as plt
import math

def visualisierung_nullstelle(n: float):
    # Vorbereitung der Daten
    iterationen = []
    fehler = []
    x_werte = []
    
    # Bisektions-Logik zum Sammeln der Daten
    a, b = 0, n
    formel = f"x**2 - {n}"
    
    for i in range(1, 16): 
        m = (a + b) / 2
        f_m = eval(formel, {"x": m})
        
        iterationen.append(i)
        fehler.append(abs(f_m))
        x_werte.append(m)
        
        if (eval(formel, {"x": a}) * f_m) < 0:
            b = m
        else:
            a = m

    # Plotting mit Subplots 
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

    # Plot 1: Genauigkeit
    ax1.plot(iterationen, fehler, 'r-o')
    ax1.set_title(f"Genauigkeit pro Schritt (Wurzel {n})")
    ax1.set_ylabel("Abstand zu Null |f(x)|")
    ax1.grid(True)

    # Plot 2: Annäherung der Lösung
    ax2.plot(iterationen, x_werte, 'b-s')
    ax2.axhline(y=math.sqrt(n), color='g', linestyle='--', label="Echter Wert")
    ax2.set_title("Annäherung an den x-Wert")
    ax2.set_xlabel("Iteration")
    ax2.set_ylabel("Aktueller x-Wert")
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

# Aufruf für Katalognummer 
if __name__ == "__main__":
    visualisierung_nullstelle(12)