function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

const menu = document.querySelector(".nav__menu");
const hamburger = document.querySelector(".nav__btns");
const menuBtn = document.querySelector(".nav__btn-media");
const menuIcon = document.querySelector(".nav__open");
const closeIcon = document.querySelector(".nav__close");

function ToggleMenu() {
  if (menu.classList.contains("showMenu")) {
    menu.classList.toggle("showMenu");
    closeIcon.style.display = "none";
    menuIcon.style.display = "block";
    menu.style.display = "none";
  } else {
    menu.classList.toggle("showMenu");
    closeIcon.style.display = "block";
    menuIcon.style.display = "none";
    menu.style.display = "none";
    menu.style.display = "block";
  }
}

hamburger.addEventListener("click", ToggleMenu);

// menuItems.forEach(function (menuItem) {
//   menuItem.addEventListener("click", ToggleMenu);
// });

window.onclick = function (event) {
  if (!event.target.matches(".dropbtn")) {
    let dropdowns = document.getElementsByClassName("dropdown-content");
    let i;
    for (i = 0; i < dropdowns.length; i++) {
      let openDropdown = dropdowns[i];
      if (openDropdown.classList.contains("show")) {
        openDropdown.classList.remove("show");
      }
    }
  }
};



const downBtns = document.querySelectorAll("#down-btn");
const accordions = document.querySelectorAll("#accordion");

downBtns.forEach((downBtn, index) => {
  downBtn.addEventListener("click", () => {
    accordions[index].classList.toggle("active");
    downBtn.innerHTML =
      downBtn.innerHTML === "...Batafsil" ? "...Kamroq" : "...Batafsil";
  });
});
