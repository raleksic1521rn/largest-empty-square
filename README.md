# Largest Empty Square
Program i animacija u Python jeziku sa bibliotekom Matplotlib za resavanje problema Largest Empty Square.

### Zadatak
Za datih `N` tacaka u ravni, izracunati strukturu podataka koja omogucava efikasno resavanje upita tipa: za date koordinate `X` i `Y`, izracunati najvecu duzinu `D` tako da kvadrat sa centrom u tackama `X` i `Y` i duzinom stranice `D` ne sadrzi ni jednu od `N` tacaka iz skupa.

Predlozeno resenje: `O(log^3 N)` vremenska slozenost po upitu i `O(N log N)` memorijska slozenost, gde je `N` broj tacaka u skupu.

![Alt text](/problem.png)

### Resenje

Sortirati pocetni skup tacaka po `X` koordinatama, zatim napraviti Merge sort tree nad `Y` koordinatama. Za svaku upitnu tacku `(Xq,Yq)` pokrenuti binarnu pretragu po duzini stranice kvadrata `D`, i za svaki korak u binarnoj pretrazi proveriti da li na intervalu `[Xq-D, Xq+D]` postoji tacka sa `Y` koordinatom koja pripada intervalu `[Yq-D, Yq+D]`. Ukoliko takva tacka ne postoji, duzina `D` je validna i treba prosiriti levu granicu u binarnoj pretrazi. Postupak ponavljati do zeljene preciznosti.

### Koriscenje

- Za pokretanje programa prvo instalirati Matplotlib biblioteku, zatim pokrenuti `run.py` fajl.

- Pri inicijalizaciji uneti putanju ka unosnom fajlu pocetnog skupa tacaka ili ostaviti prazno za randomizirani input.

- Za trenutni upit uneti u konzolu `X` a zatim `Y` koordinatu centra kvadrata.
