# =============================================================================
# VÁLTOZÓK
# =============================================================================

# A változók a programozás alapjai.
# A változók segítségével tudunk adatokat eltárolni, és később újra felhasználni.

# -----------------------------------------------
# Értékadás
# -----------------------------------------------

# A programozásban a változók értékadással jönnek létre.
# Az értékadás különbözik a matematikai/algebrai egyenletírásban használt értékadástól.

# Pl. az algebrai egyenletírásban ez nem lehetséges:
# x = 1
# x = x + 1

# A programozásban viszont igen, ez a két sor kód helyes:
x = 1
x = x + 1
print("Az 'x' változó értékének 2-nek kell lennie: x =", x)

# A matematikai egyenletek helyett lehet úgy érteni az értékadást, hogy "dobozokba teszünk valamit".
# Mint a dobozokat, a változókat arra használjuk hogy eltároljunk dolgokat.

# Egyszerűen fogalmazva, akár mint a dobozokat, a változókat:
# -----------------------------------------------------------
#  1. Elnevezhetjük
#  2. Rakhatunk bele dolgokat (pl. számokat, szövegeket, stb.)
#  3. Később használhatjuk a benne lévő dolgokat

# Nézzünk egy példát:
# -------------------
# 1. A változóknak adhatunk nevet + 2. a változókba rakhatunk dolgokat
# (Az első kettőt együtt csináljuk, mert nem tudunk üres változót létrehozni, valamit azonnal be kell dobozolni.)
a = 1
b = 2

# 3. A változókba rakott dolgokat később használhatjuk

# =============================================================================
# VÁLTOZÓK TÍPUSAI
# =============================================================================

# Eddig megnéztük, hogyan tudunk változókat létrehozni.
# Most megnézzük, hogy milyen TÍPUSÚ dolgokat tudunk a változókba rakni.

# -----------------------------------------------
# Számok
# -----------------------------------------------

# HU: Egész számok
# EN: Integers
a = 1

# HU: Lebegőpontos számok
# EN: Floating point numbers
b = 1.5
# - A lebegőpontos számokat a Pythonban a ponttal jelöljük, nem vesszővel!

# -----------------------------------------------
# Szövegek
# -----------------------------------------------

# HU: Karakter
# EN: Character
c = 'a'
c = "a"
# - Mint látható, a karaktereket idézőjelek közé kell tenni.
# - A Pythonban nincs különbség a ' és a " között.

# HU: Szöveg, vagy karakterlánc
# EN: String
d = 'alma' 
d = "alma" 

# -----------------------------------------------
# Logikai értékek
# -----------------------------------------------

# HU: Igaz
# EN: True
e = True

# HU: Hamis
# EN: False
f = False

