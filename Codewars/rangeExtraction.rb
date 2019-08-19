def solution(list)
  ranged_list = []
  i=0
  while i < list.length do
    el,idx = walker(list[i,list.length-1])
    ranged_list.append(el)
    i += idx
  end
  return ranged_list.flatten.join(",")
end

# keeps going until no longer + 1
def walker(list)
idx = 1
  if list.length <= 2
    return list.flatten,list.length
  end
  walked = [list[0]]
  starting_list = list[1,list.length]
  starting_list.each do |el|
    if el == walked[-1] + 1
      walked.append(el)
      idx += 1
    else
      break
    end
  end
  if walked.length >= 3
    return "#{walked[0]}-#{walked[-1]}",idx
  else
    return walked.flatten,idx
  end
end
