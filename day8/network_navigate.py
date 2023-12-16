from math import gcd
from functools import reduce


class NetworkInstructions:
    def __init__(self, input_data):
        self.input_data = input_data.splitlines()
        self.instructions = self.input_data[0]
        self.parents = []
        self.network = {}

    def parse_data(self):
        for line in self.input_data:
            if ' = ' in line:
                parent, children_str = line.split(' = ')
                self.parents.append(parent)
                children = children_str.strip('()').split(', ')
                self.network[parent] = children

    def network_traversal(self):
        self.parse_data()
        current_node = 'AAA'
        no_of_steps = 0

        while current_node != 'ZZZ':
            for instruction in self.instructions:
                if instruction == 'R':
                    current_node = self.network[current_node][1]
                    no_of_steps += 1
                else:
                    current_node = self.network[current_node][0]
                    no_of_steps += 1

            if current_node == 'ZZZ':
                break

        print(no_of_steps)

    def ghost_network_traversal(self):
        self.parse_data()
        start_nodes = []
        steps_list = []

        # finding starting nodes
        for node in self.parents:
            if node.endswith('A'):
                start_nodes.append(node)

        def least_common_multiple(a, b):
            return a * b // gcd(a, b)

        for current_node in start_nodes:
            no_of_steps = 0
            while not current_node.endswith('Z'):
                for instruction in self.instructions:
                    if instruction == 'R':
                        current_node = self.network[current_node][1]
                        no_of_steps += 1
                    else:
                        current_node = self.network[current_node][0]
                        no_of_steps += 1

                if current_node.endswith('Z'):
                    break
            steps_list.append(no_of_steps)

        print(reduce(least_common_multiple, steps_list))

# We have two starting points: `11A, 22A`
# We reach a final point from `11A` iterating only one time over the given route, which is in 2 steps
# We reach a final point from `22A` iterating 3 times over the given route, which is in 6 steps
# The least common multiple between these two numbers is 6, which is our solution
