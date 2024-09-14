% Facts: parent(Parent, Child), male(Person), female(Person)
parent(john, mary).
parent(john, michael).
parent(susan, mary).
parent(susan, michael).
parent(mary, james).
parent(mary, lisa).
parent(michael, andrew).
parent(michael, sophia).

male(john).
male(michael).
male(james).
male(andrew).

female(susan).
female(mary).
female(lisa).
female(sophia).

% Rule: child(Child, Parent)
child(X, Y) :-
    parent(Y, X).

% Rule: sibling(X, Y) - X and Y are siblings if they share at least one parent
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% Rule: father(Father, Child) - A father is a male parent
father(Father, Child) :-
    parent(Father, Child),
    male(Father).

% Rule: mother(Mother, Child) - A mother is a female parent
mother(Mother, Child) :-
    parent(Mother, Child),
    female(Mother).

% Rule: grandparent(Grandparent, Grandchild)
grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild).

% Rule: grandfather(Grandfather, Grandchild) - A grandfather is a male grandparent
grandfather(Grandfather, Grandchild) :-
    grandparent(Grandfather, Grandchild),
    male(Grandfather).

% Rule: grandmother(Grandmother, Grandchild) - A grandmother is a female grandparent
grandmother(Grandmother, Grandchild) :-
    grandparent(Grandmother, Grandchild),
    female(Grandmother).

% Rule: aunt(Aunt, NieceOrNephew) - An aunt is a female sibling of a parent
aunt(Aunt, NieceOrNephew) :-
    sibling(Aunt, Parent),
    parent(Parent, NieceOrNephew),
    female(Aunt).

% Rule: uncle(Uncle, NieceOrNephew) - An uncle is a male sibling of a parent
uncle(Uncle, NieceOrNephew) :-
    sibling(Uncle, Parent),
    parent(Parent, NieceOrNephew),
    male(Uncle).

% Rule: cousin(X, Y) - X and Y are cousins if their parents are siblings
cousin(X, Y) :-
    parent(A, X),
    parent(B, Y),
    sibling(A, B).

% Rule: ancestor(Ancestor, Descendant)
ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Descendant).

ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Intermediate),
    ancestor(Intermediate, Descendant).

% Rule: descendant(Descendant, Ancestor)
descendant(Descendant, Ancestor) :-
    ancestor(Ancestor, Descendant).
