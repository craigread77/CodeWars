function solution(str){
   var splitList = str.match(/(\w{2}|\w{1})/g);
   return splitList.map((a) => a.length === 2 ? a : a + '_')
}

console.log(solution("abcdefg"));