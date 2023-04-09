# Game Store Catalog

## About

This is just a catalog of PlayStation&reg;, Xbox&trade;, and Nintendo&reg; games. In lieu of there being no public API, this is a scrape from each store. Not updated regularly.

### Structure

`!.json`

```js
// !.json
[
    // ...
    [
        name: string,
        {
                name: string,
                type?: string,
                price: string<Price>,
                image: string<URL>,
                href: string<URL>,
                uuid?: string,
                platforms: array<string>,
                rating?: string,
        }
    ]
    // ...
]
```

`_.json` `a.json` ... `z.json`

```js
// _.json a.json ... z.json
[
    // ...
    {
            name: string,
            type?: string,
            price: string<Price:USD> | string<"Announced", "Early access trial", "Free", "Game Trial", "Unavailable">,
                // "Announced" → Item price is pending
                // "Early access trial" → Item is pending but, can be played on a trial basis
                // "Free" → Item is free to play/own
                // "Game Trial" → Item is on a trial basis
                // "Unavailable" → Item can no longer be purchased
            image: string<URL>,
            href: string<URL>,
            uuid?: string,
            platforms: array<string>,
            rating?: string<"everyone", "everyone 10+", "rating pending", "teen", "mature 17+", "none">,
    }
    // ...
]
```

----

<details><summary>PlayStation&reg; (7,745 games | 2023-04-08)</summary>

[`!.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/!.json) - All games (large file size)

  - Saved as a `Map` → `[ [Name, Properties] ]`

[`_.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/_.json) - All games that begin with a non-alphabetic character (`0` `[` etc.)

  - e.g. `0 Degrees` `[PROTOTYPE™]` `#Funtime`

[`a.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/a.json) - All games that begin with `A`

[`b.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/b.json) - All games that begin with `B`

[`c.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/c.json) - All games that begin with `C`

[`d.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/d.json) - All games that begin with `D`

[`e.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/e.json) - All games that begin with `E`

[`f.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/f.json) - All games that begin with `F`

[`g.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/g.json) - All games that begin with `G`

[`h.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/h.json) - All games that begin with `H`

[`i.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/i.json) - All games that begin with `I`

[`j.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/j.json) - All games that begin with `J`

[`k.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/k.json) - All games that begin with `K`

[`l.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/l.json) - All games that begin with `L`

[`m.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/m.json) - All games that begin with `M`

[`n.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/n.json) - All games that begin with `N`

[`o.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/o.json) - All games that begin with `O`

[`p.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/p.json) - All games that begin with `P`

[`q.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/q.json) - All games that begin with `Q`

[`r.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/r.json) - All games that begin with `R`

[`s.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/s.json) - All games that begin with `S`

[`t.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/t.json) - All games that begin with `T`

[`u.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/u.json) - All games that begin with `U`

[`v.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/v.json) - All games that begin with `V`

[`w.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/w.json) - All games that begin with `W`

[`x.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/x.json) - All games that begin with `X`

[`y.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/y.json) - All games that begin with `Y`

[`z.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/z.json) - All games that begin with `Z`

</details>

```js
/* PlayStation® */
[
    // ...
    {
        "name": "Jack Move",
        "price": "$19.99",
        "image": "https://image.api.playstation.com/vulcan/ap/rnd/202208/0311/QNhcccNfqdO0Yf8gMo4yVnv0.png",
        "href": "https://store.playstation.com/en-us/product/UP4416-CUSA32154_00-8667761992349718",
        "uuid": "UP4416-CUSA32154_00-8667761992349718",
        "platforms": [
            "PS4"
        ]
    }
    // ...
]
```

----

<details><summary>Xbox&trade; (3,038 games | 2023-04-08)</summary>

[`!.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/!.json) - All games (large file size)

  - Saved as a `Map` → `[ [Name, Properties] ]`

[`_.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/_.json) - All games that begin with a non-alphabetic character (`0` `[` etc.)

  - e.g. `20XX` `3on3 FreeStyle` `890B`

[`a.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/a.json) - All games that begin with `A`

[`b.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/b.json) - All games that begin with `B`

[`c.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/c.json) - All games that begin with `C`

[`d.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/d.json) - All games that begin with `D`

[`e.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/e.json) - All games that begin with `E`

[`f.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/f.json) - All games that begin with `F`

[`g.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/g.json) - All games that begin with `G`

[`h.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/h.json) - All games that begin with `H`

[`i.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/i.json) - All games that begin with `I`

[`j.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/j.json) - All games that begin with `J`

[`k.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/k.json) - All games that begin with `K`

[`l.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/l.json) - All games that begin with `L`

[`m.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/m.json) - All games that begin with `M`

[`n.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/n.json) - All games that begin with `N`

[`o.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/o.json) - All games that begin with `O`

[`p.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/p.json) - All games that begin with `P`

[`q.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/q.json) - All games that begin with `Q`

[`r.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/r.json) - All games that begin with `R`

[`s.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/s.json) - All games that begin with `S`

[`t.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/t.json) - All games that begin with `T`

[`u.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/u.json) - All games that begin with `U`

[`v.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/v.json) - All games that begin with `V`

[`w.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/w.json) - All games that begin with `W`

[`x.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/x.json) - All games that begin with `X`

[`y.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/y.json) - All games that begin with `Y`

[`z.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/z.json) - All games that begin with `Z`

</details>

```js
/* Xbox™ */
[
    // ...
    {
        "name": "Jack Move",
        "type": "Product",
        "price": "$19.99",
        "image": "https://store-images.s-microsoft.com/image/apps.29635.13536821765519749.cfbde45b-cbb1-4694-a1bd-57f40c566293.65bcd4ae-e8e3-4b8a-a47f-c99cb9da90cc?w=200",
        "href": "https://www.xbox.com/en-us/games/store/jack-move/9N9J1FSDWZ6L",
        "uuid": "9N9J1FSDWZ6L",
        "platforms": [
            "Xbox Series X|S",
            "Xbox One"
        ],
        "rating": "none"
    }
    // ...
]
```

----

<details><summary>Nintendo&reg; (10,515 games | 2023-04-08)</summary>

[`!.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/!.json) - All games (large file size)

  - Saved as a `Map` → `[ [Name, Properties] ]`

[`_.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/_.json) - All games that begin with a non-alphabetic character (`0` `[` etc.)

  - e.g. `密室のサクリファイス／ABYSS OF THE SACRIFICE` `3D ADVANTIME` `8Doors: Arum's Afterlife Adventure`

[`a.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/a.json) - All games that begin with `A`

[`b.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/b.json) - All games that begin with `B`

[`c.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/c.json) - All games that begin with `C`

[`d.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/d.json) - All games that begin with `D`

[`e.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/e.json) - All games that begin with `E`

[`f.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/f.json) - All games that begin with `F`

[`g.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/g.json) - All games that begin with `G`

[`h.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/h.json) - All games that begin with `H`

[`i.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/i.json) - All games that begin with `I`

[`j.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/j.json) - All games that begin with `J`

[`k.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/k.json) - All games that begin with `K`

[`l.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/l.json) - All games that begin with `L`

[`m.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/m.json) - All games that begin with `M`

[`n.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/n.json) - All games that begin with `N`

[`o.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/o.json) - All games that begin with `O`

[`p.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/p.json) - All games that begin with `P`

[`q.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/q.json) - All games that begin with `Q`

[`r.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/r.json) - All games that begin with `R`

[`s.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/s.json) - All games that begin with `S`

[`t.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/t.json) - All games that begin with `T`

[`u.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/u.json) - All games that begin with `U`

[`v.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/v.json) - All games that begin with `V`

[`w.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/w.json) - All games that begin with `W`

[`x.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/x.json) - All games that begin with `X`

[`y.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/y.json) - All games that begin with `Y`

[`z.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/z.json) - All games that begin with `Z`

</details>

```js
/* Nintendo® */
[
    // ...
    {
        "name": "Jack Move",
        "price": "$19.99",
        "image": "ncom/en_US/games/switch/j/jack-move-switch/hero",
        "href": "https://www.nintendo.com/store/products/jack-move-switch/",
        "uuid": "70010000049263",
        "platforms": [
            "Nintendo Switch"
        ],
        "rating": "everyone 10+"
    }
    // ...
]
```

----

## Legal

Not affiliated with Sony Interactive Entertainment (LLC), Microsoft Corp. &copy;, or Nintendo&reg;; nor either's partners, subsidiaries, et al.
