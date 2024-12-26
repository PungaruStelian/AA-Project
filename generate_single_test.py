import random

def generate_single_test(N, T, element_range, filename):
    """
    Generează un fișier de test pentru problema Subset Sum.

    Parametri:
    - N (int): Numărul de elemente din setul de intrare.
    - T (int): Suma țintă pentru subset.
    - element_range (int): Intervalul valorilor pentru elementele din set.
                           Valorile vor fi generate în intervalul [-element_range, element_range].
    - filename (str): Numele fișierului de ieșire.
    """
    # Generează N numere aleatoare între -element_range și +element_range
    elements = [random.randint(-element_range, element_range) for _ in range(N)]
    
    # Scrie datele în fișier
    with open(filename, 'w') as file:
        # Prima linie conține N și T
        file.write(f"{N} {T}\n")
        # Fiecare element este scris pe o linie nouă
        for num in elements:
            file.write(f"{num}\n")
    
    print(f"Fișierul de test '{filename}' a fost generat cu succes.")

if __name__ == "__main__":
    # Parametrii pentru testul specific
    N = 10000              # Numărul de elemente
    T = 1000000            # Suma țintă
    element_range = 1000000 # Intervalul valorilor elementelor (-1000000 până la +1000000)
    filename = "in21.txt" # Numele fișierului de ieșire

    generate_single_test(N, T, element_range, filename)