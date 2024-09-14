% Facts representing birds and their ability to fly or not
% bird(Name, CanFly)
bird(eagle, yes).
bird(penguin, no).
bird(sparrow, yes).
bird(ostrich, no).
bird(parrot, yes).
bird(kiwi, no).

% Rule to check if a bird can fly
can_fly(Bird) :-
    bird(Bird, yes).

% Rule to check if a bird cannot fly
cannot_fly(Bird) :-
    bird(Bird, no).

% Rule to print whether a bird can fly or not
fly_status(Bird) :-
    can_fly(Bird),
    format("The bird ~w can fly.~n", [Bird]), !.

fly_status(Bird) :-
    cannot_fly(Bird),
    format("The bird ~w cannot fly.~n", [Bird]), !.
