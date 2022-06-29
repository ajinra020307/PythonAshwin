
function getMinSpacing({maxRange}){

    let nearestRange = Math.floor(maxRange/15)

    if(nearestRange<=5) return 5

    while(nearestRange%5!=0){

        nearestRange = nearestRange-1
    }
    return nearestRange

}

console.log(getMinSpacing({maxRange:8000}))
console.log(getMinSpacing({maxRange:70}))
