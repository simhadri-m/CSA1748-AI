% Facts
food(apples).
food(chicken).
eats(bill, peanuts).
not_killed_by(bill, peanuts).

% Rules
likes(john, X) :- food(X).
food(X) :- eats(Y, X), not_killed_by(Y, X).
eats(sue, X) :- eats(bill, X).

% Query to prove
prove_john_likes_peanuts :- likes(john, peanuts).

% To execute the query
:- initialization(prove_john_likes_peanuts).
