


dob('JohnDoe', date(15, june, 1990)).
dob('AliceSmith', date(15, june, 1990)).
dob('Bob Johnson', date(3, april, 1978)).
dob('Clara White', date(9, october, 1995)).
dob('David Black', date(30, december, 2000)).

% Rule to retrieve someone's date of birth by name
find_dob(Name, Date) :-
    dob(Name, Date).

% Rule to check if two people have the same date of birth
same_dob(Name1, Name2) :-
    dob(Name1, Date),
    dob(Name2, Date),
    Name1 \= Name2.

% Rule to find all people born in a specific month
born_in_month(Month, Name) :-
    dob(Name, date(_, Month, _)).
