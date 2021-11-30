# ot-harjoitustyo

Tehtävien hallinnointisovellus. Sovelluksessa voi yksittäinen käyttäjä pitää kirjaa omista tehtävistään. Käyttäjä voi myös kuulua organisaatioon, jossa näkyvät kaikki yleiset tehtävät jokaiselle organisaation jäsenelle. 

## Dokumentaatio

[vaatimusmäärittely](dokumentaatio/vaatimusmäärittely.md)

[tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)

[arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

## Asentaminen
Asenna tarvittavat kirjastot
```
$ poetry install
```

Luo tietokannat
```
$ poetry run invoke init
```

Käynnistä sovellus
```
$ poetry run invoke start
```

## Testaaminen
Jos haluat suorittaa testit
```
$ poetry run invoke test
```

Luo testausraportti
```
$ poetry run invoke coverage-report
```

## ToDo
### Viikko 3
 - [x] Tietokantayhteys
 - [x] Rekisteröinti
 - [x] Kirjautuminen
 - [x] Kirjautumisen testaus

### Viikko 4
 - [x] Tehtävien luominen
 - [x] Tehtävien poistaminen
 - [x] Toiminnoille testit

### Viikko 5
 - [ ] Luo sovellukselle UI
 - [ ] Muuta sovellus arkkitehtuurin mukaisesti. Pientä muutosta luokkien rakenteisiin.

### Viikko 6
 - [ ] Luo uusi organisaatio
 - [ ] Lisää organisaatioon uusi käyttäjä
 - [ ] Testaa niiden toimivuus. 

### Viikko 7
 - [ ] Mahdollista koodin refaktorointa.
 - [ ] Tarkista asioiden toimivuus