require 'pry'

def havel_hakimi(arg)
  while true do
    arg.delete_if{|num| num==0}
    arg.sort!.reverse!
    n = arg.shift
    if arg.empty?
      return true
    end
    if n > arg.length
      return false
    end
    beg = arg[0,n].collect do |a|
      a = a-1
    end
  ending = arg[n,arg.count]
  arg = beg + ending
  end
end

binding.pry
puts "done"
