const szamok = new Array(4, 63, 3, 76, 15, 63, 2, 5, 87, 29);

function miamax(szam_tomb)
{
    let makszindeksz = 0;
    let i = 0;

    while (i < szam_tomb.length)
    {
        if (szam_tomb[i] > szam_tomb[makszindeksz])
        {
            makszindeksz = i;
        }
        i++;
    }

    return makszindeksz;
}

var makszi = miamax(szamok);

console.log("Ennyidik elem: " + (makszi+1) + " a legnagyobb, aminek értéke: " + szamok[makszi]);

