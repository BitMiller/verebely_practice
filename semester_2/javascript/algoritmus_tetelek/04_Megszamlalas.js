/*
Megszámlálás (X[N], T, DB)
    DB = 0;
    Ciklus i = 1-től N-ig
        Ha X[i] T tulajdonságú, akkor
            DB = DB + 1
        Elágazás vége;
    Ciklus vége;
Eljárás vége;
*/

var szamok = new Array(12, 43, 87, -3);
var tulajdonsag = 2;
var darab;

function megszamlalas (x, t, db) {
    db = 0;

    for (let i = 0; i < x.length; i++) {
        if (x[i] % t == 0) {
            db = db + 1;
        }
    }

    return db;
}

console.log("A(z) [" + szamok + "] tömbben " + megszamlalas(szamok, tulajdonsag, darab) + " szám osztható " + tulajdonsag + "-val/-vel.");
