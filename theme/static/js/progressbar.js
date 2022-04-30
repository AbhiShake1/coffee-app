const div = document.getElementById('reward-div')

let clicked = false

div.style.display = 'none'

function onUserButtonClick() {
    if (clicked) {
        div.style.display = 'none'
    } else {
        div.style.display = 'block'
    }
    clicked = !clicked;
}
