export default {
    props: {
        path: String,
        rank: String
    },
    computed: {
        rankURL() {
            return 'img/' + Rank + '.PNG'
        }
    },
    template: `
    <div class="rank_block">  
        <a href=""><img src="require(`../${path}.png`)" alt="" class="rank_product"></a>
        <img src="${rankURL}" alt="" class="rank"></img> 
        <p>{{ path }}</p>
        <p>{{ rank }}</p>  
    </div>
    `
}
// ${"\"" + IMGpath + "\""}
// ${"\"" + rankURL + "\""}

