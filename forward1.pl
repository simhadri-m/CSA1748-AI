% Facts and Rules based on the given statements

% 1. John likes all kinds of food
likes(john, X) :- food(X).

% 2. Apples are food.
food(apples).

% 3. Chicken is food.
food(chicken).

% 4. Anything that anyone eats and isn’t killed by is food.
food(X) :- eats(_, X), alive(_, X).

% 5. Bill eats peanuts and is still alive.
eats(bill, peanuts).
alive(bill, peanuts).

% 6. Sue eats everything Bill eats.
eats(sue, X) :- eats(bill, X).

% Forward chaining to find if John likes peanuts

% 7. To prove John likes peanuts, we need to check if peanuts are food.
prove_john_likes_peanuts :-
    food(peanuts), % Check if peanuts are food
    likes(john, peanuts), % Check if John likes peanuts
    write('John likes peanuts'), nl.

% Start the proof
start :-
    prove_john_likes_peanuts.
