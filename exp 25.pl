initial_state(state(at_door, on_floor, at_window, has_not_eaten)).

final_state(state(_, _, _, has_eaten)).

action(
    state(at_window, on_floor, at_window, has_not_eaten),
    grasp,
    state(at_window, on_floor, at_window, has_eaten)
).
action(
    state(at_door, on_floor, _, HB),
    walk_to_window,
    state(at_window, on_floor, at_window, HB)
).

solve(Plan) :-
    initial_state(State),
    solve(State, Plan).
solve(State, []) :-
    final_state(State).

solve(State, [Action|Rest]) :-
    action(State, Action, NewState),
    solve(NewState, Rest).
