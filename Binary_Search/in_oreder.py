class Node:
# 참조 한다: 내가 어디에 있는지 가르키는 개념 -> 주소를 가르킨다.
# 노드라는 class를 가지고 객체를 생성 했다. 스스로 가르키고 있는 것을 그안에 넣어놓은것
# 이소연의 데이터를 가지고 self 접근 할 수 있다.
	def __init__(self, value, left=None, right=None, ):
		self.value=value
		self.right=right
		self.left=left
class Binary_tree:
	def __init__(self,root):
		self.root= Node(root)
	
	def inorder_traversal(self, node):
		"""Left -> Root -> Right"""
		"""
		if node.left == None and node.right == None:
			print(node.value, end=' ')
			return
		elif node.left == None:
			print(node.value, end=' ')
			self.inorder_traversal(node.right)
			return
		elif node.right == None:
			self.inorder_traversal(node.left)
			print(node.value, end=' ')
			return
		"""
		if node:
			self.inorder_traversal(node.left)
			print(node.value, end=' ')
			self.inorder_traversal(node.right)
		return
tree = Binary_tree("A")
tree.root.left = Node("B")
tree.root.right = Node("C")
tree.root.left.left = Node("D")
tree.root.left.right = Node("E")
tree.root.left.right.left = Node("G")
tree.root.left.right.right = Node("H")
tree.root.right.right = Node("F")
tree.root.right.right.left = Node("I")
tree.inorder_traversal(tree.root)