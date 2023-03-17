console.log("favorate article js file");
const favorateBtn = document.getElementsByClassName("favorate_btn");
console.log({ favorateBtn });
const favorate = () => {
    for (let index = 0; index < favorateBtn.length; index++) {
        favorateBtn[index].addEventListener("click", (e) => {
            const btn = favorateBtn[index];
            const articleId = btn.getAttribute("id").split("_");
            console.log({ btn, article_id: Number(articleId[0]) });
            console.log("btn clicked", { "article id": articleId[1] });
            fetch(`/favorate/article/${articleId[0]}`)
                .then((res) => res.json())
                .then((data) => console.log({ data_favorate_article: data }))
                .catch((error) => console.log({ error_favorate_article: error }));
        });
    }
};
favorate();
