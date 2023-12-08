# =============================================================================
# MŰVELETEK
# =============================================================================

# Az előző példákban láttuk, hogyan lehet változókat létrehozni.
# Most megnézzük, hogyan lehet ezekkel a változókkal műveleteket végezni!

# -----------------------------------------------
# Számok műveletei
# -----------------------------------------------
a = 1
b = 2

# Összeadás
c = a + b
print("a + b =", c)

# Kivonás
c = a - b
print("a - b =", c)

# Szorzás
c = a * b
print("a * b =", c)

# Osztás
c = a / b
print("a / b =", c)

# Osztás maradéka (modulus)
c = a % b
print("a % b =", c)

# Hatványozás
c = a ** b
print("a ** b =", c)

# -----------------------------------------------
# Szövegek műveletei
# -----------------------------------------------

# Szövegek összefűzése
a = "alma"
b = "fa"
c = a + b # "almafa"
print("a + b =", c)

# Szöveg ismétlése
a = "alma"
b = a * 3 # "almaalmaalma"
print("a * 3 =", b)

# -----------------------------------------------
# Logikai értékek műveletei
# -----------------------------------------------

# Habár nem tűnnek fontosnak, a logikai műveleteket sokszor fogjuk használni.
# Ha kell ismétlés, akkor https://nekomajin42.github.io/bevinfo/pages/logic/index.html oldalon találsz magyarázatot.

# NEGÁLÁS művelet (NOT)
a = True
c = not a
print("not a =", c)

# ÉS művelet (AND)
a = True
b = False
c = a and b
print("a and b =", c)

# VAGY művelet (OR)
a = True
b = False
c = a or b
print("a or b =", c)