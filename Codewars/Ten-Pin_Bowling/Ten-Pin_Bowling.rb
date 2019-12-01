def bowling_score(frames)
  score = 0
  frames = frames.split(" ")
  last = frames[-1]
  # puts "frames #{frames}, last #{last}"
  (0..8).each do |idx|
    remaining = (frames[idx , frames.length - idx]).join()
    # puts "remaining #{remaining}"
    score += score_round(remaining, frames[idx])
  end

  return score + score_chars(last)


end

def score_round(remaining, round)
  if round[-1] == "X" or round[-1] == "/"
    return score_chars(remaining[0,3])
  else
    return round[0].to_i + round[1].to_i
  end
end

def score_chars(chars)
  sum = 0
  prev = 0
  chars.split("").each do |n|
    case n
      when "X"
        n = 10
      when "/"
        n = 10 - prev
      else
        n = n.to_i
    end
    prev = n
    sum += n
  end
  return sum
end
