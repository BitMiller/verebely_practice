/*
Eldöntés (X[N], T, VAN)
    i = 1;
    Ciklus amíg i <= N, és X[i] nem T tulajdonságú
        i = i + 1
    Ciklus vége;
    Ha i <= N akkor
        VAN
    Elágazás vége;
Eljárás vége;
*/

var szamok = new Array(12, 43, 87, -3);
var tulajdonsag = 2;
var van = false;

function eldontes (tomb, tul, vn) {
    let i = 0;

    while (i < tomb.length && tomb[i] % tul != 0) {
        i = i + 1;
    }

    if (i < tomb.length) {
        vn = true;
    }

    return vn;
}

console.log("A(z) [" + szamok + "] tömbben van-e olyan elem, amelyik osztható " + tulajdonsag + "-val/-vel? : " + eldontes(szamok, tulajdonsag, van));
