// HERO ANIMATION

window.addEventListener("load", () => {

    const heroContent = document.querySelector(".hero-content");

    if(heroContent){

        heroContent.style.opacity = "1";
        heroContent.style.transform = "translateY(0px)";

    }

});


// PRODUCT CARD HOVER EFFECT

const productCards = document.querySelectorAll(".product-card");

productCards.forEach(card => {

    card.addEventListener("mouseenter", () => {

        card.style.transform = "translateY(-10px)";
        card.style.transition = "0.4s";

    });

    card.addEventListener("mouseleave", () => {

        card.style.transform = "translateY(0px)";

    });

});


// BUTTON RIPPLE EFFECT

const buttons = document.querySelectorAll(".btn");

buttons.forEach(button => {

    button.addEventListener("click", function(e){

        let x = e.clientX - e.target.offsetLeft;
        let y = e.clientY - e.target.offsetTop;

        let ripple = document.createElement("span");

        ripple.classList.add("ripple");

        ripple.style.left = `${x}px`;
        ripple.style.top = `${y}px`;

        this.appendChild(ripple);

        setTimeout(() => {
            ripple.remove();
        }, 600);

    });

});


// CHECKOUT ALERT

const checkoutForm = document.querySelector("form");

if(checkoutForm){

    checkoutForm.addEventListener("submit", () => {

        alert("Your Virelle & Co. order has been placed successfully!");

    });

}