def roll_dice (rolls, sides, threshold)

denominator = sides**rolls

if threshold > rolls * sides
  return 0
end

a = [*(1..sides)].repeated_permutation(rolls).to_a
sums = a.map {|vals| vals.inject(0){|sum,x| sum + x}}
sums = sums.find_all {|num| num < threshold}
reached = sums.length
# reached = sums.find_index {|num| num >= threshold }

return (denominator - reached) / denominator.to_f


end
