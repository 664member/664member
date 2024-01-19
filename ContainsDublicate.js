function ContainsDublicate(arr){
    let obj = {}
    for(let i=0;i<arr.length;i++){
        if(obj[arr[i]]){
            return true
        }else{
            obj[arr[i]] = true
        }
    }
    return false
}

console.log(ContainsDublicate([1,23,4,5]))