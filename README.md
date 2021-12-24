# ot-harjoitustyo

Tehtävien hallinnointisovellus. Sovelluksessa voi yksittäinen käyttäjä pitää kirjaa omista tehtävistään. Käyttäjä voi myös kuulua organisaatioon, jossa näkyvät kaikki yleiset tehtävät jokaiselle organisaation jäsenelle. 

## Releases
* [Viikko5](https://github.com/AnonymousHobbit/ot-harjoitustyo/releases/tag/viikko5)
* [Viikko6](https://github.com/AnonymousHobbit/ot-harjoitustyo/releases/tag/viikko6)
* [Lopullinen](https.//github.com/AnonymousHobbit/ot-harjoitustyo/releases/tag/lopullinen)

## Dokumentaatio

[vaatimusmäärittely](dokumentaatio/vaatimusmäärittely.md)

[tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)

[arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

[testaus](dokumentaatio/testaus.md)

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

Suorita pylint
```
$ poetry run invoke lint
```