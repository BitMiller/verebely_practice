
const debug = true;

fancyHeader();

/***************************/
/***************************/
/***************************/

console.log("\n1. feladat: Alap adattömb létrehozása...");

/*-------------------------*/

var terulet = new Array();

console.log("Kész!");

/***************************/
/***************************/
/***************************/

console.log("\n2. feladat: Magasságadatok generálása...");

/*-------------------------*/

var elemszam = 20;
var min_magassag = 100;
var max_magassag = 2000;

function TeruletRandom(tomb, db, min, max) {

    for (let i = 0; i < db; i++) {
        tomb.push(Math.floor(Math.random() * (max - min + 1) + min ));
    }

}

TeruletRandom(terulet, elemszam, min_magassag, max_magassag)

console.log(elemszam + " db magasságadat generálása kész!");

//console.log(terulet);

/***************************/
/***************************/
/***************************/

console.log("\n3. feladat: A generált magassági adatok:");

/*-------------------------*/

function TeruletKiir(tomb, d) {

    for (let i = 0; i < tomb.length; i++) {

        let s_out = (i+1) + ". terület magassága: " + tomb[i] + " méter";

        if (d) {
            if (tomb[i] < 200) s_out += " - \u001b[1;32msíkság";
            else if (tomb[i] > 500) s_out += " - \u001b[1;31mhegység";
            else s_out += " - \u001b[1;33mdombság";
        }

        console.log(s_out);
    }
}

TeruletKiir(terulet, debug);

/***************************/
/***************************/
/***************************/

console.log("\n4. feladat: Síksági területek átlagmagassága");

/*-------------------------*/

function SiksagAtlag(tomb) {

    let osszeg = 0;
    let szamlalo = 0;

    for (let i = 0; i < tomb.length; i++) {
        if (tomb[i] < 200) {
            osszeg += tomb[i];
            szamlalo++;
        }
    }

    if (szamlalo == 0) {
        console.log("Nincs síkság a domborzati adatok között!");
    }
    else {
        console.log("A síkságok átlagmagassága: " + String(Math.floor(osszeg / szamlalo * 100) / 100) + " méter.");
    }

}

SiksagAtlag(terulet);

/***************************/
/***************************/
/***************************/

console.log("\n5. feladat: A vizsgált területek közül hány darab hegy van?");

/*-------------------------*/

function HegyDarab(tomb) {

    let hegyek_szama = 0;

    for (let i = 0; i < tomb.length; i++) {
        if (tomb[i] > 500) {
            hegyek_szama++;
        }
    }

    console.log(hegyek_szama + " hegy van.");

}

HegyDarab(terulet);

/***************************/
/***************************/
/***************************/

console.log("\n6. feladat: A legalacsonyabb dombsági terület magasságértéke:");

/*-------------------------*/

function DombMin(tomb) {

    let i = 0;

    while (i < tomb.length && ! (tomb[i] >= 200 && tomb[i] <= 500)) {
        i++;
    }

    if (i < tomb.length) {
        let min_idx = 0;

        for (i = 1; i < tomb.length; i++) {
            if (tomb[i] >=200 && tomb[i] <= 500 && tomb[i] < tomb[min_idx]) {
                min_idx = i;
            }
        }

        console.log("A legalacsonyabb domb " + tomb[min_idx] + " méter magas.");
    }
    else {
        console.log("Nincs domb a magassági adatok között!");
    }

}

DombMin(terulet);

/***************************/
/***************************/
/***************************/

console.log("\n7. feladat: A legmagasabb hegységi terület magasságértéke:");

/*-------------------------*/

function HegyMax(tomb) {

    let magMaxIdx = 0;
    let i = 0;

    while (i < tomb.length && tomb[i] <= 500) {
        i++;
    }

    if (i < tomb.length)  {
        for (i = 1; i < tomb.length; i++) {
            if (tomb[i] > tomb[magMaxIdx]) {
                magMaxIdx = i;
            }
        }

        console.log("A vizsgált területek közül a legmagasabb " + tomb[magMaxIdx] + " méter.");
    }
    else {
        console.log("Nincsen hegy a magassági adatok között!");
    }

}

HegyMax(terulet);

/***************************/
/***************************/
/***************************/

var vizsgalt_szint = 1500;

console.log("\n8. feladat: Van-e " + vizsgalt_szint + " méternél magasabb hegy a vizsgált területek között?");

/*-------------------------*/

function HegyEldont(tomb, szint) {
    let i = 0;

    while (i < tomb.length && tomb[i] <= szint) {
        i++;
    }

    if (i < tomb.length) {
        console.log("Igen, van " + szint + " méternél magasabb.");
    }
    else {
        console.log("Nem, nincs " + szint + " méternél magasabb.");
    }
}

HegyEldont(terulet, vizsgalt_szint);

/***************************/
/***************************/
/***************************/

console.log("\n9. feladat: A(z) " + vizsgalt_szint + " méternél magasabb területek listája:");

/*-------------------------*/

function Top1500(tomb, szint) {
    let magas = new Array();

    for (let i = 0; i < tomb.length; i++) {
        if (tomb[i] > szint) {
            magas.push(i);
        }
    }

    if (magas.length == 0) {
        console.log("Nincs " + szint + " méternél magasabb terület.");
    }
    else {
        let s_out = "";

        for (let i = 0; i < magas.length; i++) {
            s_out += String(magas[i]+1) + ". terület, " + tomb[magas[i]] + " méter";

            if (i < magas.length - 1) {
                s_out += "; ";
            }
            else {
                s_out += ".";
            }
        }

        console.log(s_out);
    }
}

Top1500(terulet, vizsgalt_szint);




/***************************/
/******* DANGER ZONE *******/
/***************************/

function fancyHeader() {

    let sinLine = new Array();
    let sinLineLength = 120;
    let sinLineAmplitude = 7;
    let sinLineWaveLength = 60;

    let flowText = " HEGYEK ";

    for (let i = 0; i < sinLineLength; i++) {
        sinLine.push(Math.sin(i/sinLineWaveLength*Math.PI*2 + Math.PI/2) * (sinLineAmplitude / 2) + (sinLineAmplitude / 2));
    }

    //console.log(sinLine);
    console.log("Nature's t*ts. We love 'em!\n");

    for (let i = 0; i <= sinLineAmplitude + 1; i++) {
        let s_out = "";

        for (let j = 0; j < sinLineLength; j++) {
            let relate = sinLine[j] + 1.7;
            if (relate-1 >= i && relate-1 < i+1) {
                s_out += flowText[j % flowText.length];
            }
            else if (relate >= i && relate < i+1) {
                if (relate >= i+0.5) {
                    s_out += ".";
                }
                else {
                    s_out += "˙";
                }
            }
            else {
                s_out += " ";
            }
        }

        console.log(s_out);
    }
}

