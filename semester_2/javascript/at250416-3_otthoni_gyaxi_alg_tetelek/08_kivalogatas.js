
var szamok = new Array(-4, 8, 4, 77);
var tulajdonsag = 2;
var kival = new Array();

function kivalogatas(x, t, y) {
    let szamlalo = 0;

    for (let i = 0; i < x.length; i++) {
        if (x[i] % t == 0) {
            //y[szamlalo] = x[i];
            y.push(x[i]);
            szamlalo++;
        }
    }
}

kivalogatas(szamok, tulajdonsag, kival);

console.log(kival);
