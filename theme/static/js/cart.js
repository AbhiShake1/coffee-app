const orderBtns = document.getElementsByClassName('btn-add-to-cart');

for (let i = 0; i < orderBtns.length; i++) {
    orderBtns[i].addEventListener('click', function () {
        const productId = this.dataset.product
        const action = this.dataset.action
        //dont need to check logged in since we will use this only in base_logged_in
        //which has everything covered
        fetchUserOrder(productId, action)
    })
}

const checkoutBtn = document.getElementById('btn-checkout')
checkoutBtn.addEventListener('click', function () {
    window.location.href = `http://127.0.0.1:8019/checkout/total=${document.getElementById('product-total').innerHTML}`
})

function fetchUserOrder(productId, action) {
    const url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action
        })
    }).then((response) => response.json())
        .then((_) => {
            const products = document.getElementsByClassName('product-quantity')
            const titles = document.getElementsByClassName('product-quantity-title')
            const prices = document.getElementsByClassName('product-price')
            for (let i = 0; i < titles.length; i++) {
                if (titles[i].innerHTML.toString() === productId) {
                    products[i].innerHTML++
                    const t = document.getElementById('product-total')
                    const prev = Number(document.getElementById('product-total').innerHTML)
                    const toAdd = Number(prices[i].innerHTML)
                    document.getElementById('product-total').innerHTML = (prev + toAdd).toString()
                }
            }
        })
}
