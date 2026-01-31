# Game Store Catalog

## About

This is a catalog of PlayStation&reg;, Xbox&reg;, Nintendo&reg;, and Steam&reg; games. In lieu of a public API, this is a scrape from each store.

**Not updated regularly.**

If needed, you can [view a builder online](https://minkcbos.retool.com/app/game-store-catalog) to help make URL schemas and see examples.

If you'd like to maintain your own database(s), see [`Ephellon/store-scraper`](https://github.com/Ephellon/store-scraper) <sup><em>sic</em></sup>.

----

#### PlayStation&reg;

- `/psn` &mdash; All (__17,400__<!--@psn.size-->) PlayStation&reg; (PS4&trade; & PS5&trade;) games
- `/ps5` &mdash; All (__8,609__<!--@ps5.size-->) PlayStation&reg;5&trade; games
- `/ps4` &mdash; All (__12,565__<!--@ps4.size-->) PlayStation&reg;4&trade; games

#### Xbox&reg;

- `/xbox` &mdash; All (__15,142__<!--@xbox.size-->) Xbox&reg; (Xbox&reg; & PC) games
- `/xbox-console` &mdash; All (__15,142__<!--@xbox.size-->) Xbox&reg; games
- `/xbox-pc` &mdash; All (__15,142__<!--@xbox.size-->) PC games

#### Nintendo&reg;

- `/nintendo` &mdash; All (__11,607__<!--@nintendo.size-->) Nintendo&reg; games

#### Steam&reg;

- `/steam` &mdash; All (__152,989__<!--@steam.size-->) Steam&reg; games

#### Quick links to entire libraries (large files)

| PlayStation&reg;  | Xbox&reg;         | Nintendo&reg;     | Steam&reg;        |
| ----------------- | ----------------- | ----------------- | ----------------- |
| [PlayStation&reg;](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/!.json) | [Xbox&reg;](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/!.json) | [Nintendo&reg;](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/!.json) | [Steam&reg;](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/!.json) |
| [PlayStation&reg;5&trade;](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/ps5/!.json) | [Xbox&reg; Console](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox-console/!.json) | | |
| [PlayStation&reg;4&trade;](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/ps4/!.json) | [Xbox&reg; PC](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox-pc/!.json) | | |

----

### Structures

`$.json`

```js
// $.json - Metadata
{
    "size": number,         // The number of game entries (i.e. `!.json` size)
    "date": string,         // The (JSON) date the files were updated
    "diff": number<int>,    // The number of new entries added (or removed)
}
```

`!.json`

```js
// !.json - All games
[
    // ...
    [
        name: string,                       // The game's name, UTF-16
        {
                name: string,               // The game's name, UTF-16
                type?: string,              // The game's type (used by Xbox)
                price: string<Price:USD>,   // The game's price (USD)
                image: string<URL>,         // The game's cover image URL
                href: string<URL>,          // The game's purchase URL
                uuid: string|number,        // The game's UUID (varies per store)
                platforms: array<string>,   // The game's platform(s); e.g. "PS5", "Xbox One", "Nintendo Switch", etc.
                rating?: string,            // The game's maturity rating, e.g. "everyone 10+"
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
            uuid: string|number,
            platforms: array<string>,
            rating?: string<"everyone", "everyone 10+", "rating pending", "teen", "mature 17+", "none">,
    }
    // ...
]
```

----

# PlayStation&reg;

<details><summary><b>17,400</b><!--@psn.size--> games | <b>2026-01-31T17:40:26.803Z</b><!--@psn.date--> | <b>+76</b><!--@psn.diff|s--></summary>

[`!.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/psn/!.json) - All games (large file size)

  - Saved as a `Map` → `[ [name:string, properties:object] ]`

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
        ],
        "rating": null
    }
    // ...
]
```

----

# Xbox&reg;

<details><summary><b>15,142</b><!--@xbox.size--> games | <b>2026-01-31T17:38:30.953Z</b><!--@xbox.date--> | <b>+60</b><!--@xbox.diff|s--></summary>

[`!.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/xbox/!.json) - All games (large file size)

  - Saved as a `Map` → `[ [name:string, properties:object] ]`

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

# Nintendo&reg;

<details><summary><b>11,607</b><!--@nintendo.size--> games | <b>2026-01-31T17:35:35.007Z</b><!--@nintendo.date--> | <b>+0</b><!--@nintendo.diff|s--></summary>

[`!.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/nintendo/!.json) - All games (large file size)

  - Saved as a `Map` → `[ [name:string, properties:object] ]`

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
        "image": "https://assets.nintendo.com/image/upload/store/software/switch/70010000049263/36b3750b1fe7228279b369bfd915c6b7125a662464be29ac0927c0d9f06a26ea",
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

# Steam&reg;

<details><summary><b>152,989</b><!--@steam.size--> games | <b>2026-01-31T18:00:47.134Z</b><!--@steam.date--> | <b>+1,006</b><!--@steam.diff|s--></summary>

[`!.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/!.json) - All games (large file size)

  - Saved as a `Map` → `[ [name:string, properties:object] ]`

[`_.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/_.json) - All games that begin with a non-alphabetic (Latin) character (`0` `[` etc.)

  - e.g. `890B` `Àrengard-Invasion` `执谕者：坠月之兆（Archenemy: Lunafall）`

[`a.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/a.json) - All games that begin with `A`

[`b.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/b.json) - All games that begin with `B`

[`c.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/c.json) - All games that begin with `C`

[`d.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/d.json) - All games that begin with `D`

[`e.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/e.json) - All games that begin with `E`

[`f.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/f.json) - All games that begin with `F`

[`g.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/g.json) - All games that begin with `G`

[`h.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/h.json) - All games that begin with `H`

[`i.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/i.json) - All games that begin with `I`

[`j.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/j.json) - All games that begin with `J`

[`k.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/k.json) - All games that begin with `K`

[`l.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/l.json) - All games that begin with `L`

[`m.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/m.json) - All games that begin with `M`

[`n.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/n.json) - All games that begin with `N`

[`o.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/o.json) - All games that begin with `O`

[`p.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/p.json) - All games that begin with `P`

[`q.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/q.json) - All games that begin with `Q`

[`r.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/r.json) - All games that begin with `R`

[`s.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/s.json) - All games that begin with `S`

[`t.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/t.json) - All games that begin with `T`

[`u.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/u.json) - All games that begin with `U`

[`v.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/v.json) - All games that begin with `V`

[`w.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/w.json) - All games that begin with `W`

[`x.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/x.json) - All games that begin with `X`

[`y.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/y.json) - All games that begin with `Y`

[`z.json`](https://raw.githubusercontent.com/Ephellon/game-store-catalog/main/steam/z.json) - All games that begin with `Z`

</details>

```js
/* Steam® */
[
    // ...
    {
        "name": "Jack Move",
        "price": "$19.99",
        "image": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1099640/header.jpg?t=1729093888",
        "href": "https://store.steampowered.com/app/1099640",
        "uuid": "1099640",
        "platforms": [
            "Windows",
            "Mac"
        ],
        "rating": "none"
    }
    // ...
]
```

----

## Legal

Not affiliated with Sony Interactive Entertainment (LLC), Microsoft Corp. &copy;, Nintendo&reg;, or Valve&reg;; nor either's partners, subsidiaries, et al.
