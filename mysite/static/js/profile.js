const ava = document.getElementById("avaDiv");
const modalEditAva = document.getElementById("avaModal");
const spanAva = document.getElementById("cross-ava")
const imageInput = document.getElementById('imageInput')
const imageSrc = document.getElementById('display-image')
const modalEditProf = document.getElementById("profModal")
const btnProf = document.getElementById("btnProf")
const span = document.getElementById("cross")

ava.addEventListener("click", function() {
    modalEditAva.classList.remove('hidden')
});
spanAva.onclick = function () {
    modalEditAva.classList.add('hidden')
}

modalEditProf.addEventListener('click', (event) => {
    if (event.target == modalEditProf) {
        modalEditProf.classList.add('hidden')
    }
})

modalEditAva.addEventListener('click', (event) => {
    if (event.target == modalEditAva) {
        modalEditAva.classList.add('hidden')
    }
})

btnProf.onclick = function () {
    modalEditProf.classList.remove('hidden')
}
span.onclick = function () {
    modalEditProf.classList.add('hidden')

}

function handleImageUploadAva() {
    const image = document.getElementById("file-input").files[0];

    const reader = new FileReader();

    reader.onload = function (e) {
        document.getElementById("display-image").src = e.target.result;
        document.getElementById("display-image").style.position = "static";
    }

    reader.readAsDataURL(image);

}

imageInput.addEventListener("change", function (e) {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();

        reader.onload = function (event) {
            imageSrc.src = event.target.result;
        };

        reader.readAsDataURL(file);
  }
})