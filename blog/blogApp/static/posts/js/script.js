const burger = document.querySelector(".burger");
const navMenu = document.querySelector(".nav-menu");
burger.addEventListener("click", () => {
  navMenu.classList.toggle("nav-active");
  console.log("toggle");
});
const titleText = "Welcome to my blog";
const titleBar = document.querySelector("#title-h1");
let index = 0;
const type = () => {
  titleBar.textContent = titleText.slice(0, index);
  index++;
};
setInterval(type, 350);
