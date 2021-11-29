decrementButton = document.getElementsByClassName('decrement')
incrementButton = document.getElementsByClassName('increment')
counter = document.getElementsByClassName('counter')
body = document.getElementsByTagName('body')[0]
totalPizzaPrice = document.getElementsByClassName('total-pizza-price')
pizzaPrice = document.getElementsByClassName('pizza-price')
totalPrice = document.getElementById('total-price')

let price = 0;
for (let i = 0; i < totalPizzaPrice.length; i++) {
    totalPizzaPrice[i].innerHTML = (Number(counter[i].value) * Number(pizzaPrice[i].value)).toFixed(2)
    price += Number(totalPizzaPrice[i].innerHTML)
}
totalPrice.innerHTML = price.toFixed(2);
console.log(price.toFixed(2))


body.addEventListener('click', (e) => {
    if (e.target.id >= 0 && e.target.className === 'increment'){
        console.log(e.target.id)
        counter[e.target.id - 1].value = Number(counter[e.target.id - 1].value) + 1
        totalPizzaPrice[e.target.id - 1].innerHTML = (Number(counter[e.target.id - 1].value) * Number(pizzaPrice[e.target.id - 1].value)).toFixed(2)
        totalPrice.innerHTML = (Number(totalPrice.innerHTML) + Number(pizzaPrice[e.target.id - 1].value)).toFixed(2)
    }
    else if (e.target.id > 0 && e.target.className === 'decrement' && counter[e.target.id - 1].value > 0) {
        counter[e.target.id - 1].value = Number(counter[e.target.id - 1].value) - 1
        totalPizzaPrice[e.target.id - 1].innerHTML = (Number(counter[e.target.id - 1].value) * Number(pizzaPrice[e.target.id - 1].value)).toFixed(2)
        totalPrice.innerHTML = (Number(totalPrice.innerHTML) - Number(pizzaPrice[e.target.id - 1].value)).toFixed(2)
console.log(e.target.id)
    }
})


modal = document.getElementById('myModal')
openModalButton = document.getElementById('order')
span = document.getElementsByClassName("close")[0];
modalWrapper = document.getElementById('modal-wrapper')

openModalButton.onclick = function () {
    modalWrapper.style.display = 'flex';
}

span.onclick = function() {
  modalWrapper.style.display = 'none';
}

window.onclick = function(event) {
  if (event.target === modalWrapper) {
      modalWrapper.style.display = 'none';

  }
}


