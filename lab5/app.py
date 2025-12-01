from typing import List, Tuple

 

class Board:
    """Szachownica dla zadania N hetmanów."""
    
    def __init__(self, n: int = 8):
        """Inicjalizuje rozmiar i stan."""
        self.n = n  # Rozmiar szachownicy
        # Lista przechowująca pozycje królowych jako krotki (wiersz, kolumna)
        self.queens: List[Tuple[int, int]] = []
        # Lista przechowująca znalezione poprawne rozwiązania
        self.solutions: List[List[Tuple[int, int]]] = []

    # --- Metody obsługujące stan szachownicy (API) ---

    def place(self, row: int, col: int):
        """Dodaje hetmana na (wiersz, kolumna)."""
        self.queens.append((row, col))

    def remove(self, row: int, col: int):
        """Usuwa ostatniego hetmana, jeśli pozycja pasuje."""
        if self.queens and self.queens[-1] == (row, col):
            self.queens.pop()
        
    def is_safe(self, row: int, col: int) -> bool:
        """Sprawdza, czy pozycja nie jest atakowana."""
        for r, c in self.queens:
            if c == col:
                return False
            if abs(r - row) == abs(c - col):
                return False

        return True

    def __len__(self) -> int:
        """Liczba hetmanów."""
        return len(self.queens)

    def __iter__(self):
        """Iteracja po pozycjach hetmanów."""
        yield from self.queens

    def __contains__(self, pos: Tuple[int, int]) -> bool:
        """Czy hetman jest na pozycji (wiersz, kolumna)."""
        return pos in self.queens

    def __str__(self) -> str:
        """Tekstowa wizualizacja planszy ('Q' i '.')."""
        output = []
        grid = [['.' for _ in range(self.n)] for _ in range(self.n)]
        for row, col in self.queens:
            grid[row][col] = 'Q'
        for row in grid:
            output.append(' '.join(row))
        
        return "\n".join(output)

    def __repr__(self) -> str:
        """Oficjalna reprezentacja obiektu."""
        return f"Board(n={self.n}, queens={self.queens})"
        
    def solve(self, row: int = 0) -> List[List[Tuple[int, int]]]:
        """Rekursywny backtracking: znajduje poprawne ustawienia."""
        if row == self.n:
            self.solutions.append(list(self.queens))
            return 
        
        for col in range(self.n):
            if self.is_safe(row, col):
                self.place(row, col)
                self.solve(row + 1)
                self.remove(row, col) 

        return self.solutions

def solve(n: int = 8) -> List[List[Tuple[int, int]]]:
    """Zwraca wszystkie rozwiązania dla planszy rozmiaru n."""
    board = Board(n)
    return board.solve()

 
