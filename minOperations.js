var minOperations = function(nums) {
    let counter = {}
    let sum = 0
    for(let i of nums){
        counter[i] ? counter[i] += 1 : counter[i] =1 
    }
    for(let i of Object.keys(counter)){
        if(counter[i] === 1) return -1
        //we can deduce that the number of operations needed to remove a total of count elements of a given kind is represented by the expression ceil(count /  3)
        sum += Math.ceil(counter[i] / 3)
    }

    return sum

};
