/*
Kiválogatás(X[N], T, Y[M])
    számláló = 1;
    Ciklus i = 1-től N-ig
        Ha X[i] T tulajdonságú, akkor
            Y[számláló] = X[i];
            számláló = számláló + 1;
        Elágazás vége;
    Ciklus vége;
Eljárás vége;
*/

//var szamok = new Array(8, 7, 6, 5);
var szamok = new Array(81, 7, 65, 5);
var tulajdonsag = 2;
var valogatott = new Array();

function kivalogatas(x, t, y) {
    let szamlalo = 0;

    for (let i = 0; i < x.length; i++) {
        if (x[i] % t == 0) {
//            y[szamlalo] = x[i]; // Tételhű megoldás
            y.push(x[i]); // Javascript-esebb megoldás
            szamlalo = szamlalo + 1;
        }
    }

    return y;
}

console.log("A(z) [" + szamok + "] tömbben lévő, " + tulajdonsag + "-val/-vel osztható számok: [" + kivalogatas(szamok, tulajdonsag, valogatott) + "]");
