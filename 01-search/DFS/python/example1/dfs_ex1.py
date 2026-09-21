graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

stack = []
explored = set()

stack.append("A")

while len(stack) > 0:
    current = stack.pop()

    if current in explored:
        continue

    explored.add(current)

    print(current)

    if current == "G":
        print("Founded!")
        break

    for neighbor in graph[current]:
        stack.append(neighbor)