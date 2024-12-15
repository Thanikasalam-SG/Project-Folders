const wrapper = document.querySelector(".wrapper");
const registerLink = document.querySelector(".register-link");
const loginLink = document.querySelector(".login-link");
const btnPopup = document.querySelector(".btnLogin-popup");
const iconClose = document.querySelector(".close-icon");



registerLink.addEventListener("click", ()=> {
    wrapper.classList.add("active");
});

loginLink.addEventListener("click", ()=> {
    wrapper.classList.remove("active")
})

btnPopup.addEventListener("click", ()=> {
    wrapper.classList.add("active-popup");
});

iconClose.addEventListener("click", ()=> {
    wrapper.classList.remove("active-popup")
})