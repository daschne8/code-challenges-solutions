def tickets(people)
  bills = []
   people.each do |per|
     if per == 25
       bills.append(per)
      else
      puts "cout down, per #{per}, bills #{bills}"
       test = countDown(per,bills)
       if test
         bills = test
       else
         return "NO"
       end
     end
   end
   return "YES"
end

def countDown(per, bills)
  current = per
  (bills.length-1).downto(0) do |i|
    if current - bills[i] >= 25
      current -= bills[i]
      bills.delete_at(i)
      bills.append(per)
      if current == 25
        return (bills)
      end
    end
  end
  return false
end
