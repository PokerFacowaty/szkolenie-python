"""
O nie! Nieuważna adminka napisała skrypt, który jednak nie działa! :O

Czy jesteś w stanie sprostać zadaniu, ocalić honor adminki i całe Gotham City?

- Znajdź wszystkie błędy w podanym parserze
    - Protip: możesz po prostu uruchomić kod i zobaczyć, co się położy
- Spróbuj je naprawić
Czas: 15 minut
"""

with open("app.log", mode="r", encoding="utf-9") as f:
    for line in file:
        line_fields = {}
        for pair in line.split():
            try:
                key, value = pair.split("-")
            except SyntaxError:
                print("Key value not found in: ", line.strip())
                continue
            line_fields[value] = key

        if line_fields.get("severity").lower() == "WARN":
            print("Warning found!")
