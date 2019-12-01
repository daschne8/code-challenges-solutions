function bowlingScore(frames){
  let score = 0
  frames = frames.split(" ")
  let last = frames.slice(-1)[0]
  console.log(frames, last)
  for(let i=0 ; i < frames.length - 1; i++){
    let remaining = (frames.slice(i, frames.length)).join("")
    console.log(remaining,i)
    score += scoreRound(remaining, frames[i])
  }

  return score + scoreChars(last)
}

function scoreRound(remaining,round){
  if(round.slice(-1)[0] === "X" || round.slice(-1)[0] === "/"){
    return scoreChars(remaining.slice(0,3))
  }else{
    return parseInt(round[0]) + parseInt(round[1])
  }
}

function scoreChars(chars){
  let sum = 0
  let prev = 0
  chars = chars.split("")
  let n
  for(let i=0; i < chars.length; i++){
    if(chars[i] === "X"){
      n = 10
    }else if( chars[i] === "/"){
      n = 10 - prev
    }else{
      n = parseInt(chars[i])
    }
    prev = n
    sum += n
  }
  return sum

}
