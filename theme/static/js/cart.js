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

const claimBtns = document.getElementsByClassName('btn-claim');

for (let i = 0; i < claimBtns.length; i++) {
    claimBtns[i].addEventListener('click', function () {
        const action = this.dataset.action
        const costs = document.getElementsByClassName('claim-reward')
        const prevTotal = this.dataset.total
        const newTotal = Number(prevTotal) - Number(costs[i].innerHTML)
        if (newTotal >= 0){
            window.location.href = `/updatereward/total=${newTotal}/action=${action}`
            alert('You have successfully claimed your reward')
        }else{
            alert('Not enough points')
        }
    })
}

const updaterewardBtns = document.getElementsByClassName('btn-updatereward')
for (let i = 0; i < updaterewardBtns.length; i++) {
    updaterewardBtns[i].addEventListener('click', function () {
            window.location.href = `/updatereward/total=${document
                .getElementById('product-total')
                .innerHTML}/action=${this.dataset.action}`
        }
    )
}

function fetchUserOrder(productId, action) {
    const products = document.getElementsByClassName('product-quantity')
    const titles = document.getElementsByClassName('product-quantity-title')
    const prices = document.getElementsByClassName('product-price')
    const url = '/update_cart/'
    for (let i = 0; i < titles.length; i++) {
        if (titles[i].innerHTML.toString() === productId) {
            products[i].innerHTML++
            const prev = Number(document.getElementById('product-total').innerHTML)
            const toAdd = Number(prices[i].innerHTML)
            document.getElementById('product-total').innerHTML
                = (prev + toAdd).toString()
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({
                    'productId': productId,
                    'price': prices[i].innerHTML,
                    'action': action,
                })
            })
        }
    }
}

const clearBtn = document.getElementById('btn-clear')
if (clearBtn != null)
    clearBtn.addEventListener('click', () => location.reload())
