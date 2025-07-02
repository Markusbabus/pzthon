# Prezentáció

## Feladat 1

**c** változó 2-vel való növelése, majd ábrázolás _pyplot_-tal  
Csak bevezető feladat _python_ használásával

+plt.axes() = koordináta rendszer létrehozása  
+plt.plot(x, y) = x és y tengelyek megadása

## Feladat 2

Egy reagens van (c)

Δ c= -k c Δ t

- Δ c: koncentráció megváltozása
- k: reakciósebességi állandó
- Δ t: időlépés

Itt a **c**-t csak egy sima _list_-ben tároltam (l)

## Feladat 3

Kettő reagens van (cₐ, cb)

Δ cₐ= -k cₐ cᵦ Δ t  
Δ cᵦ= -k cₐ cᵦ Δ t

+A két c külön plotolása  
+Nagyobb  Δt-nél nagy hibák, ezt orvosolni próbáltam, de így csak hibásabb lett a kódom

## Feladat 4

Csatolt reakciók

A + B → C  (k1)  
C + B → D  (k2)

Δ cₐ= -k1 cₐ cᵦ Δ t  
Δ cᵦ= -k1 cₐ cᵦ Δ t -k2 c𝒸 cᵦ Δ t  
Δ c𝒸= +k1 cₐ cᵦ Δ t -k2 c𝒸 cᵦ Δ t  
Δ c𝒹= +k2 c𝒸 cᵦ Δ t

Függvény készítés számításhoz  
+Minden külön listben (külön plotolva)

## Feladat 5

Oszcilláló reakció (Bray–Liebhafsky) késleltetés nélkül

5 H₂O₂ + I₂ → 2 IO₃⁻ + 2 H⁺ + 4 H₂O  
5 H₂O₂ + 2 IO₃⁻ + 2 H⁺ → I2 + 5 O₂ + 6 H₂O  

Egyszerűsítve:  
5A + B → 2C + 2D + 4E (k1)  
5A + 2C + 2D → B + 5F + 6E (k2)

Δ cₐ= -k1 cₐᵡ¹ cᵦ Δ t -k2 cₐᵡ² c𝒸ʸ c𝒹ᶻ Δ t  
Δ cᵦ= -k1 cₐᵡ¹ cᵦ Δ t +k2 cₐᵡ² c𝒸ʸ c𝒹ᶻ Δ t  
Δ c𝒸= +2k1 cₐᵡ¹ cᵦ Δ t -k2 cₐᵡ² c𝒸ʸ c𝒹ᶻ Δ t  
Δ c𝒹= +2k1 cₐᵡ¹ cᵦ Δ t -k2 cₐᵡ² c𝒸ʸ c𝒹ᶻ Δ t  
Δ cₑ= +4k1 cₐᵡ¹ cᵦ Δ t +6k2 cₐᵡ² c𝒸ʸ c𝒹ᶻ Δ t  
Δ cբ= +5k2 cₐᵡ² c𝒸ʸ c𝒹ᶻ Δ t  

+Hatványozás mert nem csak egy mol fogyik el az anyagainkból  
+Numpy használata, hogy gyorsabban fusson  
+2 függvény  írása  
+c tömbben értékszámítás, majd minden külön-külön tömbben
Nagyon kicsi **Δt** használata (0.0005s), mert nagyobb értékek pontatlansághoz vezettek

### Interaktív változat

Ipywidgets használata (jupyter könyvtár)
Az egész szimulációnak egy függvény  
A csúszkák adják meg az értékeket  
+rengeteg NaN és Inf

## Feladat 6

Ugyanaz az oszcilláló reakció késleltetéssel

Δ cₐ= -k1 cₐ(n-nkₐ)ᵡ¹ cᵦ Δ t -k2 cₐ(n-nkₐ)ᵡ² c𝒸(n-nk𝒸)ʸ c𝒹(n-nk𝒹)ᶻ Δ t  
. . .

nk: késleltetés (lépésben, nem időben)  
c_értékek: c alapértékek tárolása (ca: 10, cb: 2, cc: 0, cd: 0, ce: 0, cf: 0)  
p_tömb: paraméterek tárolása (nmax: 200, dt: 0.0005, k1: 0.7, k2: 1.2, x1: 2, x2: 2, y: 2, z: 2, nka: 2, nkb: 3, nkc: 6, nkd: 10)  
rk_tömb: valós késleltetések tárolása (az elején kell)  
t_sor: eltelt idő tárolása (nagyon kicsi)
c_matrix: c_tömb * (nmax(időlépések száma) + 1) _array_, amiben vannak a c értékek

### Számolás

#### Függvények

4 paraméter:

- c_tömb (c_matrix)
- p_tömb
- n ( iteráció, amin jelenleg vagyunk)
- rk_tömb

##### dc1

dt ca(lépésünk - a valós késleltetés)ᵡ¹ cb(lépésünk - a valós késleltetés)

#### Hozzáadás

Az előző értékből kivonunk, hozzáadunk, ahogy kell

### Interaktív változat

Ugyanaz, mint az előző, csak még több csúszka

#### Érdekes változatok

cb 1.5  
cc 1  
cd 0.6  
nmax 300  
dt 0.00030  
k1 0.7  
k2 1.5  
nk 10  
x, y, z 2  

cb 2.1
cc 1  
cd 0.7  
nmax 300  
dt 0.00100  
k1 0.7  
k2 1.5  
nk 10  
x1 1.3  
x2 1.2  
y 2.5  
z 2.2
