function handleImageUpload() {

        const image = document.getElementById("file-input").files[0];

        const reader = new FileReader();

        reader.onload = function (e) {
            document.getElementById("display-image").src = e.target.result;
            document.getElementById("display-image").style.position = "static";
        }

        reader.readAsDataURL(image);

    }

async function subscribe(id, user1, user2) {
    button = document.getElementById(id)
    if (button.name == 'notClicked') {
        button.className = 'px-4 py-2 ml-auto bg-blue-100 text-white font-semibold transition rounded-xl hover:bg-blue-400'
        button.name = 'clicked'
    }
    else {
        button.className = 'px-4 py-2 ml-auto bg-blue-500 text-white font-semibold transition rounded-xl hover:bg-blue-400'
        button.name = 'notClicked'
    }
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    let response = await fetch('/subscribe', {
        method: 'POST',
        body: JSON.stringify({'user1': user1, 'user2': user2}),
        headers: {
            'X-CSRFToken': csrftoken
        }
    })
}
