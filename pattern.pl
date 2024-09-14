% Define patterns and their descriptions
shape(circle, 'A round shape with no corners').
shape(square, 'A shape with four equal sides and four right angles').
shape(triangle, 'A shape with three sides and three angles').

% Predicate to match a shape and return its description
describe_shape(Shape, Description) :-
    shape(Shape, Description). % Match the shape to its description

% Main predicate to test pattern matching
main :-
    write('Enter a shape (circle, square, triangle): '),
    read(Shape),              % Read the input shape from the user
    (   describe_shape(Shape, Description)   % Try to match the shape
    ->  write('Description: '), write(Description), nl
    ;   write('Shape not found.'), nl    % If no match found
    ).
