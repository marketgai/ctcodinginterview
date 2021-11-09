const { object } = require("prop-types");

//1
const unique = (str) => {
  let letters = {};
  for(let l in str){
    if (letters[l]) {
      return false
    } else {
      letters[l] = 1
    }
  return true
  }
}

// console.log(unique("thes"))
// console.log(unique("these"))

//2 check permute
const permute = (str1, str2) => {
  let ls1 = {};
  let ls2 = {};

  for (let l in str1) {
    if (ls1[l]){
      ls1[l] += 1
    } else {
      ls1[l] = 1
    }
  }
  for (let l in str2) {
    if (ls2[l]){
      ls2[l] += 1
    } else {
      ls2[l] = 1
    }
  }

  if (Object.keys(ls1).length !== Object.keys(ls2).length){
    return false
  } else {
    for (const [key, value] of Object.entries(ls1))  {
      if (ls2[key] !== value){
        return false
      }
    }
    return true
  }
}

// console.log(permute('helloee', 'elolhee'))

//3
