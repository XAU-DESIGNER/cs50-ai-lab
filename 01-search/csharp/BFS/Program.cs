var graph = new Dictionary<string, List<string>>
{
    ["A"] = ["B", "C"],
    ["B"] = ["D", "E"],
    ["C"] = ["F"],
    ["D"] = [],
    ["E"] = ["G"],
    ["F"] = [],
    ["G"] = []
};

var queue = new Queue<string>();
var visited = new HashSet<string>();

queue.Enqueue("A");
visited.Add("A");

while (queue.Count > 0)
{
    var current = queue.Dequeue();

    Console.WriteLine($"Visitng: {current}");

    if (current == "G")
    {
        Console.WriteLine("Goal found!");
        break;
    }

    foreach (var neighbor in graph[current])
    {
        if (visited.Contains(neighbor))
            continue;

        queue.Enqueue(neighbor);
        visited.Add(neighbor);
    }
}