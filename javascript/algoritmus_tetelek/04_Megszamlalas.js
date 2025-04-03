/*
Megszámlálás (X[N], T)
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

function megszamlalas (tomb, tul) {
    let db = 0;

    for (let i = 0; i < tomb.length; i++) {
        if (tomb[i] % tul == 0) {
            db = db + 1;
        }
    }
}

