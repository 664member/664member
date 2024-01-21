var numUniqueEmails = function(emails) {
    let obj = {}
    for(let i=0;i<emails.length;i++){
        let localName = emails[i].split('@')
        let validName = "";
        for(let j=0;j<localName[0].length;j++){
            
            if(localName[0][j] === '+'){
                break
            }
            if(localName[0][j] != '.'){
                validName = validName + localName[0][j]
            }
            
        }
       
        obj[validName+"@"+localName[1]]=null

    }
    return Object.keys(obj).length
};

