import sys
import numpy as np
from fringe_frontier import QueueFrontier

class Node:
	def __init__(self, state, parent, action):
		self.state = state
		self.parent = parent
		self.action = action

	def __repr__(self):
		return f"\nState: {self.state}\nAction: {self.action}\n"

class EightPuzzle:
	def __init__(self, initialState, stateIndex, goal, goalIndex):
		self.initialState = [initialState, stateIndex]
		self.goal = [goal, goalIndex] 
		self.solution = None
		self.tree = ""

	def neighbors(self, state):
		mat, (row, col) = state
		results = []
		
		if row > 0:
			mat1 = np.copy(mat)
			mat1[row][col] = mat1[row - 1][col]
			mat1[row - 1][col] = 0
			results.append(('move up', [mat1, (row - 1, col)]))
		if col > 0:
			mat1 = np.copy(mat)
			mat1[row][col] = mat1[row][col - 1]
			mat1[row][col - 1] = 0
			results.append(('move left', [mat1, (row, col - 1)]))
		if row < 2:
			mat1 = np.copy(mat)
			mat1[row][col] = mat1[row + 1][col]
			mat1[row + 1][col] = 0
			results.append(('move down', [mat1, (row + 1, col)]))
		if col < 2:
			mat1 = np.copy(mat)
			mat1[row][col] = mat1[row][col + 1]
			mat1[row][col + 1] = 0
			results.append(('move right', [mat1, (row, col + 1)]))

		return results

	def print(self, output_file=None):
		solution = self.solution if self.solution is not None else None
		output = sys.stdout if output_file is None else open(output_file, "w")
		action_solution = ""

		print("Initial State:\n", self.initialState[0], "\n", file=output)
		print("Goal State:\n",  self.goal[0], "\n", file=output)
		print("\nStates Explored: ", self.num_explored, "state\n", file=output)
		print("Solution:\n ", file=output)
		for action, cell in zip(solution[0], solution[1]):
			print("action: ", action, "\n", cell[0], "\n", file=output)
			action_solution += action+"\n"
		print("Goal Reached, with this action:\n"+ action_solution, file=output)
		# for action, cell in zip(solution[0], solution[1]):
		# print("ENode State: ", self.node, "\n", file=output )
		if output_file is not None:
			output.close()

	def does_not_contain_state(self, state):
		for st in self.explored:
			if (st[0] == state[0]).all():
				return False
		return True
	
	def solve(self, node=None):
		if node is None:
			node = Node(state=self.initialState, parent=None, action=None)
			self.tree += str(node)
			# print(str(node))
	
		self.num_explored = 0

		currentState = Node(state=self.initialState, parent=None, action=None)
		frontier = QueueFrontier()
		frontier.add(currentState)

		self.explored = [] 

		while True:
			if frontier.empty():
				raise Exception("No solution")

			node = frontier.remove()
			self.num_explored += 1

			if (node.state[0] == self.goal[0]).all():
				actions = []
				cells = []
				while node.parent is not None:
					actions.append(node.action)
					cells.append(node.state)
					node = node.parent
				actions.reverse()
				cells.reverse()
				self.solution = (actions,  cells)
				return

			self.explored.append(node.state)

			for action, state in self.neighbors(node.state):
				if not frontier.contains_state(state) and self.does_not_contain_state(state):
					child = Node(state=state, parent=node, action=action)
					frontier.add(child)
					self.tree += " " * (len(self.tree.split("\n")[-2]) + 4) + "|---" + str(child)

