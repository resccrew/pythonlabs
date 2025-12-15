from shop.models.product import Product
from shop.logic.cart import Cart


def main():
    p1 = Product("Laptop", 3500, "elektronika")
    p2 = Product("Jabłko", 2.5, "spożywcze")
    p3 = Product("Jabłko", 3.0, "spożywcze")
    p4 = Product("Telewizor", 1500, "elektronika")

    print("--- TEST PRODUKTÓW ---")
    print(f"Produkt 1 (str): {p1}")
    print(f"Produkt 2 (repr): {repr(p2)}")

    print(f"Długość nazwy '{p1.name}': {len(p1)}")

    print(f"Czy p2 == p3? {p2 == p3}")
    print(f"Czy p1 == p4? {p1 == p4}")

    products_list = [p1, p2, p4]
    print("\nLista przed sortowaniem:")
    for p in products_list:
        print(p)

    products_list.sort()

    print("\nLista po sortowaniu (według ceny rosnąco):")
    for p in products_list:
        print(p)

    print("\n--- TEST KOSZYKA ---")
    cart = Cart()
    cart.add_product(p1)
    cart.add_product(p2)
    cart.add_product(p4)

    print(f"Liczba produktów w koszyku: {len(cart)}")
    print(f"Czy Laptop jest w koszyku? {p1 in cart}")

    print("\n" + str(cart))


if __name__ == "__main__":
    main()
