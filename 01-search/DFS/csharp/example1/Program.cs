var grf = new Dictionary<string, List<string>>
{
    ["A"] = ["B", "C"],
    ["B"] = ["D", "E"],
    ["C"] = ["F"],
    ["D"] = [],
    ["E"] = ["G"],
    ["F"] = [],
    ["G"] = []
};

var stack = new Stack<string>();
var explored = new HashSet<string>();

stack.Push("A");

while (stack.Count > 0)
{
    var current = stack.Pop();

    if (explored.Contains(current))
        continue;

    explored.Add(current);

    Console.WriteLine(current);

    if (current == "G")
    {
        Console.WriteLine("Founded !");
        break;
    }

    foreach (var neighbor in grf[current])
        stack.Push(neighbor);
}