/*
Eldöntés (X[N], T, VAN)
    i = 1;
    Ciklus amíg i <= N, és X[i] nem T tulajdonságú
        i = i + 1
    Ciklus vége;
    Ha i <= N, akkor
        VAN
    Elágazás vége;
Eljárás vége;
*/

var szamok = new Array(12, 43, 87, -3);
var tulajdonsag = 2;
var van_e = false;

function eldontes (x, t, van) {
    let i = 0;

    while (i < x.length && x[i] % t != 0) {
        i = i + 1;
    }

    if (i < x.length) {
        van = true;
    }

    return van;
}

console.log("A(z) [" + szamok + "] tömbben van-e olyan elem, amelyik osztható " + tulajdonsag + "-val/-vel? : " + eldontes(szamok, tulajdonsag, van_e));
