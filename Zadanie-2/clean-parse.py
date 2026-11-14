"""
- W pliku znajdziesz listę logów
- Dla każdego loga sparsuj każdą parę key-value i podaj (za pomocą print) wartość klucza “user”
- Czas: 7 minut
"""

logs = [
    "   severity=LOG action=login ip=187.111.121.88 user=admin   ",
    "   severity=INFO action=logout ip=203.45.67.89 user=john_doe   ",
    "   severity=WARN action=failed_login ip=10.20.30.40 user=guest  ",
    "   severity=ERROR action=login ip=192.168.0.1 user=root ",
    "   severity=LOG action=login ip=80.90.100.110 user=alice   ",
    "   severity=DEBUG action=login ip=172.16.254.5 user=bob   ",
    "   severity=INFO action=failed_login ip=55.44.33.22 user=admin   ",
    "   severity=WARN action=logout ip=123.45.67.89 user=test   ",
    "   severity=ERROR action=login ip=8.8.8.8 user=system   ",
    "   severity=LOG action=login ip=45.67.89.101 user=mgr    ",
    "   severity=CRITICAL action=failed_login ip=210.55.44.33 user=anonymous ",
]
