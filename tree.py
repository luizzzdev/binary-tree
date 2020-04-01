from random import random
import math


def generate_random_number():
    return math.ceil(random() * 100)


def generate_numbers():
    numbers = []

    while len(numbers) < 10:
        number = generate_random_number()

        while number in numbers:
            number = generate_random_number()

        numbers.append(number)
    return numbers


class Node:
    left = None
    right = None
    value = 0
    height = 0

    def __init__(self, value, height):
        self.value = value
        self.height = height

    def __str__(self):
        return 'value: ' + str(self.value) + ' height: ' + str(self.height )

    def add(self, value):
        # print(value)
        # print('self: ' + str(self.value))
        # print('left: ' + str(self.left if self.left is None else self.left.value))
        # print('right: ' + str(self.right if self.right is None else self.right.value))
        if value < self.value:
            if self.left is None:
                left = Node(value, self.height + 1)
                self.left = left
            else:
                self.left.add(value)
        if value > self.value:
            if self.right is None:
                right = Node(value, self.height + 1)
                self.right = right
            else:
                self.right.add(value)


def generate_lines(node, lines):
    # print(lines)
    # print(str(node))
    # print('left: ' + str(node.left if node.left is None else node.left.value))
    # print('right: ' + str(node.right if node.right is None else node.right.value))
    if len(lines) is node.height:
        lines.append([])

    if len(lines) >= node.height:
        lines[node.height].append(node.value)

    if node.left is not None:
        generate_lines(node.left, lines)
    if node.right is not None:
        generate_lines(node.right, lines)


def print_tree(node):
    lines = []

    generate_lines(node, lines)
    lines_len = len(lines)
    for line_index, line in enumerate(lines):
        for i in range(0, lines_len - len(line)):
            print(" ", end="")

        for column in line:
            print(column, end=" ")

        print()

    return lines


numbers = generate_numbers()

root = Node(numbers[0], 0)
numbers.remove(numbers[0])

for number in numbers:
    root.add(number)

lines = print_tree(root)