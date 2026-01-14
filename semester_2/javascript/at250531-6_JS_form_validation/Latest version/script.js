//console.log("Modafaka, ic workin!");

/*
> https://www.w3schools.com/html/html_form_input_types.asp

> https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener
> https://www.w3schools.com/jsref/dom_obj_event.asp
> https://www.w3schools.com/js/js_htmldom_eventlistener.asp
> https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events
> https://developer.mozilla.org/en-US/docs/Web/API/Event/target

> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/test
*/

var e_daForm = document.getElementById("id_daForm");

var e_userName = document.getElementById("id_userName");
var e_eMail = document.getElementById("id_eMail");
var e_phone = document.getElementById("id_phone");
var e_birth = document.getElementById("id_birth");
var e_password = document.getElementById("id_password");
var e_password2 = document.getElementById("id_password2");
var e_accept = document.getElementById("id_accept");

var e_hint_userName = document.getElementById("id_hint_userName");
var e_hint_eMail = document.getElementById("id_hint_eMail");
var e_hint_phone = document.getElementById("id_hint_phone");
var e_hint_birth = document.getElementById("id_hint_birth");
var e_hint_password = document.getElementById("id_hint_password");
var e_hint_password2 = document.getElementById("id_hint_password2");
var e_hint_accept = document.getElementById("id_hint_accept");

e_daForm.addEventListener("submit", (event) => {
    event.preventDefault();

    if (formIsValid()) {
        //e_daForm.submit();
        alert("A form hibátlan, elküldésre kész!");
    }
    else {
        alert("Valami nem faja, nézd át a mezőket plíz!");
    }
});

e_userName.addEventListener("input", (event) => { checkField_userName(event.target); });
e_eMail.addEventListener("change", (event) => { checkField_eMail(event.target); });
e_phone.addEventListener("input", (event) => { checkField_phone(event.target); });
e_birth.addEventListener("input", (event) => { checkField_birth(event.target); });
e_password.addEventListener("input", (event) => { checkField_password(event.target); });
e_password2.addEventListener("input", (event) => { checkField_password2(event.target); });
e_accept.addEventListener("change", (event) => { checkField_accept(event.target); });

/****************************************/
/***** Input field check functions ******/
/****************************************/

function checkField_userName(element) {
    let ok = false;
    const regex = /^[a-z]{8,20}$/;
    if (element.value.length >= 8 && element.value.length <=20 && regex.test(element.value)) {
        brushCorrect(element, "Rendi-check!");
        console.log(element.value + " : OK");
        ok = true;
    }
    else {
        brushError(element, "8-20 karakter hosszú, csak angol ábécé kisbötüi!");
        console.log(element.value + " : NOT OK");
    }
    return ok;
}

function checkField_eMail(element) {
    let ok = false;
    const regex = /^[^@]+@[^@]+$/;
    if (regex.test(element.value)) {
        brushCorrect(element, "Rendi-check!");
        console.log(element.value + " : OK");
        ok = true;
    }
    else {
        brushError(element, "Az almába nem kell a kukac, de az e-mail címbe szükséges!");
        console.log(element.value + " : NOT OK");
    }
    return ok;
}

function checkField_phone(element) {
    let ok = false;
    const regex = /^(?:\+36|0036|06)[ -]?(\d{2})[ -]?(\d{7})$/;
    if (regex.test(element.value)) {
        brushCorrect(element, "Rendi-check!");
        console.log(element.value + " : OK");
        ok = true;
    }
    else {
        brushError(element, "Formátum: +36 20 1234567");
        console.log(element.value + " : NOT OK");
    }
    return ok;
}

function checkField_birth(element) {
    let ok = false;
    let birth = new Date(element.value).getTime();
    let now = new Date();
    now.setHours(0,0,0,0);
    now = now.getTime();

    //console.log("birth : " + birth + " ; now : " + now);

    let secsInYear = 60*60*24*365.25*1000;
    birth /= secsInYear;
    now /= secsInYear;
/*
    console.log("secsInYear : " + secsInYear);
    console.log("birth : " + birth + " ; now : " + now);
    console.log("typeof(birth) : " + typeof(birth))
    console.log("typeof(now) : " + typeof(now))
*/
    if (typeof(birth) == "number" && typeof(birth) != "NaN") {
        if (birth > now) {
            brushError(element, "Ne csináld már, hogy tudod, mikor fogsz megszületni!");
        }
        else if (now - birth > 100) {
            brushError(element, `Aki ${Math.round(now - birth)} éves elmúlt, az ne regisztráljon, inkább ükunokázzon!`);
        }
        else {
            brushCorrect(element, "Rendi-check!");
            ok = true;
        }
    }
    else {
        brushError(element, "Nem valós dátum!");
    }
    return ok;
}

function checkField_password(element) {
    let ok = false;
    const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,20}$/;
    if (element.value.length >= 8 && element.value.length <=20 && regex.test(element.value)) {
        brushCorrect(element, "Rendi-check!");
        console.log(element.value + " : OK");
        ok = true;
    }
    else {
        brushError(element, "8-20 karakter hosszú, csak angol ábécé kis-, nagybötüi és számok legyenek benne, de mindegyikből legalább egy!");
        console.log(element.value + " : NOT OK");
    }

    checkField_password2(e_password2);

    return ok;
}

function checkField_password2(element) {
    let ok = false;
    if (e_password.value == "") {
        brushError(element, "Előbb kéne vmi jelszó, nem? :)");
        console.log(element.value + " : NOT OK");
    }
    else if (element.value == e_password.value) {
        brushCorrect(element, "Rendi-check!");
        console.log(element.value + " : OK");
        ok = true;
    }
    else {
        brushError(element, "Oldd meg kérlek, hogy a két jelszó egyezzen má'!");
        console.log(element.value + " : NOT OK");
    }
    return ok;
}

function checkField_accept(element) {
    let ok = false;
    if (element.checked) {
        brushCorrect(element, "Rendi-check!");
        console.log(element.value + " : OK");
        ok = true;
    }
    else {
        brushError(element, "Amíg el nem adod a lelkedet, biz' nem lépsz tovább!");
        console.log(element.value + " : NOT OK");
    }
    return ok;
}

/****************************************/
/****************************************/
/****************************************/

function brushError(element, msg) {
    let e_hint = findHintElement(element);
    e_hint.className = "cl_hint cl_brushError";
    e_hint.innerHTML = msg;
}

function brushWarning(element, msg) {
    let e_hint = findHintElement(element);
    e_hint.className = "cl_hint cl_brushWarning";
    e_hint.innerHTML = msg;
}

function brushCorrect(element, msg) {
    let e_hint = findHintElement(element);
    e_hint.className = "cl_hint cl_brushCorrect";
    e_hint.innerHTML = msg;
}

function findHintElement(element) {
    //return element;
    return element.parentElement.querySelector(".cl_hint");
}

function formIsValid() {

/*
    let ok = true;

    ok &&= checkField_userName(e_userName);
    ok &&= checkField_eMail(e_eMail);
    ok &&= checkField_phone(e_phone);
    ok &&= checkField_birth(e_birth);
    ok &&= checkField_password(e_password);
    ok &&= checkField_password2(e_password2);
    ok &&= checkField_accept(e_accept);
*/

    let ok = false;

    let res_userName = checkField_userName(e_userName);
    let res_eMail = checkField_eMail(e_eMail);
    let res_phone = checkField_phone(e_phone);
    let res_birth = checkField_birth(e_birth);
    let res_password = checkField_password(e_password);
    let res_password2 = checkField_password2(e_password2);
    let res_accept = checkField_accept(e_accept);

    if (res_userName && res_eMail && res_phone && res_birth && res_password && res_password2 && res_accept)
        ok = true;

    return ok;
}



