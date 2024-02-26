let name = ""
let adult = false
let desc = ""

fetch("https://api.themoviedb.org/3/movie/latest\?api_key\=c8d9d1813890b0618ea22a961269ed0f")
        .then((response) => response.json())
        .then((json) =>{
            name = json["title"]   
            adult = json["adult"]   
            desc = json["overview"]   

            console.log(json)
        });

async function getMovie() {
    alert(`Último filme lançado na database!\n Nome: ${name}\nAdulto: ${adult}\nBreve Descrição: ${desc}\n`)
}