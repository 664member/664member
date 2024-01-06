var findContentChildren = function(g, s) {
    g = g.sort((a,b)=>{return a-b});
    s = s.sort((a,b)=>{return a-b});

    let result = 0;
    let index = 0;
    while(result<g.length && index<s.length){
        console.log('!')
        if(g[result]<=s[index]){

            result++;
        }
        index++;
    }
    return result
};
