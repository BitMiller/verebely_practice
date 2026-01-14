const szamok = new Array(4, 63, 3, 76, 15, 63, 2, 5, 87, 29);
console.log(szamok);

function osszeg_func(szamok_func)
{
    let osszeg = 0;

    for (let i = 0; i < szamok_func.length; i++) {
        osszeg += szamok_func[i];
    }

    return osszeg;
}

console.log("Számok összege: " + osszeg_func(szamok));

