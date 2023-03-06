console.log("hello world from js console");
navbarUl = document.getElementById("navbar_ul");
BtnCloseOpenNavbar = document.getElementById("navbar_btn_close_open");
BtnCloseOpenNavbar.addEventListener("click", (e) => {
    e.preventDefault();
    if (navbarUl.classList[0] === "flex") {
        console.log("nav closed");
        navbarUl.setAttribute("class", "hidden");
    }
    if (navbarUl.classList[0] === "hidden") {
        console.log("nav opened");
        navbarUl.setAttribute(
            "class",
            "flex-col z-10 sm:flex-row items-right absolute left-0 right-0 top-16 h-screen bg-[#B9F3E4] w-full"
        );
    }

    console.log("btn clicked");
    // flex-col z-10 sm:flex-row items-right absolute left-0 right-0 top-16 h-screen bg-[#B9F3E4] w-full
});
// console.log({ navbarUl, BtnCloseOpenNavbar });
