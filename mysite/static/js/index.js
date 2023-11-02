const modal = document.getElementById("regModal")
const btnReg = document.getElementById("btnReg")
const spanReg = document.getElementById("cross")
btnReg.onclick = function () {
    modal.style.display = "block"
}
spanReg.onclick = function () {
    modal.style.display = "none";
}