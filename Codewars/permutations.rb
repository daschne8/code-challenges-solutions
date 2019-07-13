require 'pry'
def permutations(str)
  chars = str.split('')
  perm_arr = []
  def permute(input,chars,perm_arr)
    #binding.pry
    if chars.length > 1
      chars.each do |char|
        char_index = chars.index(char)
        new_chars = chars[0,char_index] + chars[char_index+1,chars.length]
        permute((input+char),new_chars,perm_arr)
      end
    else
      #binding.pry
      perm_arr << (input+chars[0])
    end
  end
  permute('',chars,perm_arr)
  perm_arr
end


#permute('',["a","b","c"])
p = permutations('abc')
binding.pry
puts 'done'
