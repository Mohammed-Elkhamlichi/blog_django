console.log("favorate article js file");
const favorateBtn = document.getElementsByClassName("favorate_btn");
console.log({ favorateBtn });
const favorate = () => {
    for (let index = 0; index < favorateBtn.length; index++) {
        favorateBtn[index].addEventListener("click", (e) => {
            const btn = favorateBtn[index];
            const articleId = btn.getAttribute("id");
            console.log({ btn, article_id: Number(articleId) });
            console.log("btn clicked");
            fetch(`/favorate/article/${articleId}`)
                .then((res) => res.json())
                .then((data) => console.log({ data_favorate_article: data }))
                .catch((error) => console.log({ error_favorate_article }));
        });
    }
};
favorate();
