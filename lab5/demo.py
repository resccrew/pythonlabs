from app import solve, Board

if __name__ == "__main__":
    print("Rozwiązania zadania N hetmanów")

    przypadki = {1: 1, 2: 0, 3: 0, 4: 2, 8: 92}
    for n, oczekiwane in przypadki.items():
        liczba = len(solve(n))
        status = "OK" if liczba == oczekiwane else f"Oczekiwano: {oczekiwane}"
        print(f"N={n}: liczba rozwiązań {liczba} ({status})")

    print("\nPrzykład dla N=4")
    rozwiazania = solve(4)
    if rozwiazania:
        pierwsze = rozwiazania[0]
        plansza = Board(4)
        for r, c in pierwsze:
            plansza.place(r, c)

        print("repr:", repr(plansza))
        print("len:", len(plansza))
        print("(0,1) w planszy:", (0, 1) in plansza)
        print("(0,0) w planszy:", (0, 0) in plansza)
        print("iter:", [pos for pos in plansza])
        print("plansza:\n", plansza, sep="")
    else:
        print("Brak rozwiązań")
