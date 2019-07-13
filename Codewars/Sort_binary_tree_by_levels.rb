require 'pry'
def tree_by_levels(node)
  sorted_array = []
  nodes_array = [node]
  while nodes_array.length > 0 do
    #binding.pry
    new_node = nodes_array.shift()
    nodes_array << new_node.left if !new_node.left.nil?
    nodes_array << new_node.right if !new_node.right.nil?
    sorted_array << new_node.value
  end
  sorted_array
end

class TreeNode
  attr_accessor :left
  attr_accessor :right
  attr_accessor :value
end

one = TreeNode.new
one.value = 1
three = TreeNode.new
three.value = 3
four = TreeNode.new
four.value = 4
five = TreeNode.new
five.value = 5

eight = TreeNode.new
eight.value = 8
eight.left = one
eight.right = three

nine = TreeNode.new
nine.value = 9
nine.left = four
nine.right = five

two = TreeNode.new
two.value = 2
two.left = eight
two.right = nine

puts tree_by_levels(two)


seven = TreeNode.new
seven.value = 7
three = TreeNode.new
three.value = 3

five = TreeNode.new
five.value = 5
five.right = seven

eight = TreeNode.new
eight.value = 8
eight.right = three

four = TreeNode.new
four.value = 4
four.right = five

one = TreeNode.new
one.value = 1
one.left = eight
one.right = four

puts tree_by_levels(one)

binding.pry
puts "done"
