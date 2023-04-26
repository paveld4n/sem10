# str_1 = "разработка"
# b = str_1.encode("unicode_escape")
# print(b)
# print(type(b))
# str_2 = "\u0440\u0430\u0437\u0440\u0430\u0431\u043e"
# print(str_2)

task = ["class", "funktion", "method"]
for lin in task:
    b = bytes(lin, encoding="utf-8")
    print(f"\nТип переменной: {type(b)}")
    print(f"Содержание переменной: {b}")
    print(f"Длина строки: {len(b)}")