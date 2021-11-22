# ot-harjoitustyo

Tehtävien hallinnointisovellus. Sovelluksessa voi yksittäinen käyttäjä pitää kirjaa omista tehtävistään. Käyttäjä voi myös kuulua organisaatioon, jossa näkyvät kaikki yleiset tehtävät jokaiselle organisaation jäsenelle. 

## Dokumentaatio

[vaatimusmäärittely](dokumentaatio/vaatimusmäärittely.md)

[tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)

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
 - [x] Tietokantayhteys
 - [x] Rekisteröinti
 - [x] Kirjautuminen
 - [x] Kirjautumisen testaus
 - [ ] Tehtävien luominen
 - [ ] Tehtävien poistaminen
 - [ ] Tehtävien testaaminen
 - [ ] Organisaatio