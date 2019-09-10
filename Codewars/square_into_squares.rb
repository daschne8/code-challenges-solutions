def decompose(n)
  #completed_squares = []
  sq_n = n**2
  sqs_arr = [[n-1],[n-2]]
  sqs_arr.each_with_index do |arr,idx|
    if sqs_sum(arr) == sq_n
      return arr.sort
      #completed_squares << arr
    elsif sqs_sum(arr) > n**2
      sqs_arr.delete_at(idx)
    else
      i = arr[-1]-1
      while i > 0 do
        if sqs_sum([arr,i].flatten ) <= n**2
          # if i-2 >=1
          #   sqs_arr.insert(idx+1,([arr,i-2].flatten))
          # end
          if i-1 >=1
            sqs_arr.insert(idx+1,([arr,i-1].flatten))
          end
          if i >=1
            sqs_arr.insert(idx+1,([arr,i].flatten))
          end
          i=0
        end
        i = i-1
      end
    end
  end
  if completed_squares.empty?
    return nil
  else
    return completed_squares.sort{|a,b| b[0]<=>a[0]}[0].reverse
  end
end

def sqs_sum(arr)
  sum = 0
  arr.each{|num| sum += num**2}
  return sum
end

#decompose(60000000)
decompose(600000000) #[2, 5, 33, 34641, 599999999]
#decompose(50)
