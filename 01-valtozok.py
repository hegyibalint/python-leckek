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
# Negatív egész számokat is tudunk létrehozni:
a = -1

# HU: Lebegőpontos számok
# EN: Floating point numbers
# A neve nem annyira fontos, csak tudjuk, hogy nem egész számokat is tudunk létrehozni.
b = 1.5
# Ugyanúgy tudunk negatív lebegőpontos számokat is létrehozni:
b = -1.5

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
# EN: Boolean
# -----------------------------------------------

# HU: Igaz
# EN: True
e = True

# HU: Hamis
# EN: False
f = False

# A logikai értékekkel később fogunk foglalkozni.

# -----------------------------------------------
# Listák (tömbök)
# -----------------------------------------------
# EN: Array

# A listák olyan változók, amik több dolgot is tudnak tárolni.
# A listákat szögletes zárójellel jelöljük.
g = [1, 2, 3, 4, 5]

# Nem csak egy típusú dolgot tudnak tárolni, hanem akár vegyesen is:
h = [1, 2, 'a', 'alma', True, False]

# A listák elemeit a következő módon tudjuk elérni:
print("A lista első eleme:", h[0])
# Ezt a módszert indexelésnek hívjuk.

# FONTOS: Az indexelés 0-tól kezdődik, azaz az első elem indexe 0 (Kicsit furcsa, gyorsan rááll az ember keze)
# A nullától való indexelést úgy is lehet felfogni, hogy hányat kell lépni a lista elejétől, hogy elérjük az adott elemet.

# Később majd megnézzük, hogy hogyan lehet a listák elemeit módosítani, törölni, stb.

# -----------------------------------------------
# Szótárak (asszociatív tömbök)
# -----------------------------------------------
# EN: Dictionary (associative array)

# Néha a listák nem elég jók, mert nem az a fontos hogy hanyadik elemet akarjuk elérni, hanem hogy milyen nevűt.
# Pl. egy telefonkönyvben nem az a fontos, hogy a 3. bejegyzést akarjuk elérni, hanem azt hogy mi pl. 'Alma' telefonszáma.
# Erre valók a szótárak.

# A szótárak olyan változók, amik KULCS-ÉRTÉK párokat tudnak tárolni.
# A szótárakat kapcsos zárójellel jelöljük:
i = {'Alma': 36301111111, 'Barack': 36302222222, 'Cseresznye': 36303333333}

# Megint, nem csak egy típusú dolgot tudnak tárolni, hanem akár vegyesen is:
j = {'Alma': 1, 'Barack': 2, 'Cseresznye': 'c', 'Dinnye': True, 'Eper': False}
# Nem csak az értékek, de a kulcsok is lehetnek vegyes típusúak.
k = {1: 1, 2: 2, 'a': 'c', 'd': True, 'e': False}

# A szótárak elemeit, nagyon hasonlóan a listákhoz, a következő módon tudjuk elérni:
print("Alma telefonszáma:", i['Alma'])