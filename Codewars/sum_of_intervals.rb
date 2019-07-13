require 'pry'

def sumIntervals(intervals)
  intervals = intervals.sort_by{|interval| interval[0]}
  range = intervals.length
  i = 0
  while i < range
    intervals = intervals[0,i] + check_merge(intervals[i,intervals.length])
    i+=1
    range = intervals.length
  end

  return get_sum(intervals)

end

def check_merge(intervals)
  checked = intervals[0]
  new_intervals = []
  intervals[1,intervals.length].each do |i|
    if checked[0] <= i[0] && checked[1] >= i[0]
      checked = [[checked[0],i[0]].min,[checked[1],i[1]].max]
    else
      new_intervals << i
    end
  end

  new_intervals.unshift(checked)
  return new_intervals
end

def get_sum(intervals)
  sum = 0
  intervals.each do |i|
    sum += (i[1]-i[0])
  end
  sum
end


binding.pry
puts "done"
