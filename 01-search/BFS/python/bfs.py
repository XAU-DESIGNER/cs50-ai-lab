from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

queue = deque()
visited = set()

queue.append("A")
visited.add("A")

while queue:
    current = queue.popleft()

    print(f"Visiting: {current}")

    if current == "G":
        print("Goal found!")
        break

    for neighbor in graph[current]:
        if neighbor in visited:
            continue

        queue.append(neighbor)
        visited.add(neighbor)