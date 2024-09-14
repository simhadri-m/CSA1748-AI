% Define the heuristic function (estimate to reach the goal)
heuristic(a, 7).
heuristic(b, 6).
heuristic(c, 2).
heuristic(d, 1).
heuristic(e, 0).  % Goal node

% Define the edges of the graph (Node1, Node2, Cost)
edge(a, b, 1).
edge(a, c, 4).
edge(b, d, 2).
edge(c, d, 5).
edge(d, e, 1).

% Best First Search algorithm
best_first_search(Start, Goal, Path) :-
    best_first_search([Start], Goal, [], Path).

% Base case: Goal found
best_first_search([Goal|Rest], Goal, Visited, [Goal|Visited]) :-
    !.

% Recursive case: Expand the current node
best_first_search(OpenList, Goal, Visited, Path) :-
    OpenList = [Current|RestOpen],
    findall(Next, (edge(Current, Next, _), \+ member(Next, OpenList), \+ member(Next, Visited)), Neighbors),
    append(RestOpen, Neighbors, NewOpenList),
    sort_open_list(NewOpenList, SortedOpenList),
    best_first_search(SortedOpenList, Goal, [Current|Visited], Path).

% Helper predicate to sort open list based on heuristic value
sort_open_list(OpenList, SortedOpenList) :-
    findall(Node-Heuristic, (member(Node, OpenList), heuristic(Node, Heuristic)), HeuristicList),
    keysort(HeuristicList, SortedHeuristicList),
    pairs_keys(SortedHeuristicList, SortedOpenList).

% Example query to find the path from a to e
% ?- best_first_search(a, e, Path).
% Path = [e, d, a]
