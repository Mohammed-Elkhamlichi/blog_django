console.log("hello world from js console");
navbarUl = document.getElementById("navbar_ul");
BtnCloseOpenNavbar = document.getElementById("navbar_btn_close_open");
BtnCloseOpenNavbar.addEventListener("click", (e) => {
    if (navbarUl.classList[0] === "flex") {
        console.log("nav closed");
        navbarUl.setAttribute("class", "hidden z-50");
    } else if (navbarUl.classList[0] === "hidden") {
        navbarUl.setAttribute(
            "class",
            "flex flex-col items-right absolute left-0 right-0 top-16  bg-[#B9F3E4] w-full h-screen sm:hidden z-50"
        );
    }
    console.log(navbarUl.classList);
});
// console.log({ navbarUl, BtnCloseOpenNavbar });
