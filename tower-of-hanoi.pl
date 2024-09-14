% Rule to solve the Tower of Hanoi problem
% hanoi(NumberOfDisks, SourcePeg, TargetPeg, AuxiliaryPeg, Moves)

hanoi(0, _, _, _, []) :- !.  % Base case: No disks to move
hanoi(N, Source, Target, Auxiliary, Moves) :-
    N > 0,
    M is N - 1,

    % Move N-1 disks from Source to Auxiliary using Target as the auxiliary peg
    hanoi(M, Source, Auxiliary, Target, Moves1),

    % Move the remaining disk from Source to Target
    Moves2 = [move(Source, Target)],

    % Move N-1 disks from Auxiliary to Target using Source as the auxiliary peg
    hanoi(M, Auxiliary, Target, Source, Moves3),

    % Combine all moves
    append(Moves1, Moves2, TempMoves),
    append(TempMoves, Moves3, Moves).

% Helper predicate to display the moves in a readable format
print_moves([]).
print_moves([move(From, To)|Rest]) :-
    format("Move disk from ~w to ~w~n", [From, To]),
    print_moves(Rest).                                  
