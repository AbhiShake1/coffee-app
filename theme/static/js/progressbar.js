const div = document.getElementById('reward-div')
const progressbar = document.getElementById('reward-progress-bar')

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
