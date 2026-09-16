# Breadth-First Search (FOR FUTURE ME, IN CASE I FORGET!)

Implemented in C#.

### Let me explain what I HAVE done :)

this code implements the Breadth-First Search (BFS) algoritm.

We want to travel from point A to G, so I've simulated a graph using a `Dictionary<string, List<string>>` in C#.

in the video, we learned about the frontier, so I've created a `Queue` to store unexplored nodes. I think this was the simplest way to demonstrate and test the algorithm.

The `visited` variable keeps track of explored nods and prevents infinite loops.


<img width="1126" height="909" alt="20260916_163316" src="https://github.com/user-attachments/assets/c12d3656-c75e-456d-b7ef-eda6e8bc9760" />

## important

>BFS = shortest path guaranteed
>DFS = may find a path faster, but no shortest-path guarantee