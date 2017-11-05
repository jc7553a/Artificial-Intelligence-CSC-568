edge(s,a).
edge(a,s).
edge(s,d).
edge(d,s).
edge(a,b).
edge(b,a).
edge(b,c).
edge(c,b).
edge(d,c).
edge(c,d).
edge(d,e).
edge(e,d).
edge(e,f).
edge(f,e).
edge(e, b).
edge(b,e).
edge(f,g).
edge(g,f).
edge(g,c).
edge(c,g).

edge(s,a,300).
edge(a,s,300).
edge(s,d,20).
edge(d,s, 20).
edge(a,b,1500).
edge(b,a, 1500).
edge(b,c, 9).
edge(c,b,9).
edge(d,c,2000).
edge(c,d, 2000).
edge(d,e, 3).
edge(e,d,3).
edge(e,f,400).
edge(f,e,400).
edge(e, b, 200).
edge(b,e,200).
edge(f,g, 800).
edge(g,f,800).
edge(g,c,12).
edge(c,g,12).

time(X,Y, plane, Cost, Time) :-
    connected(X,Y, Length),
    Length >= 900,
    Cost is Length,
    Time is Length/500.

time(X,Y, bus, Cost, Time) :-
    connected(X,Y, Length),
    not(X == a),
    not(X == e),
    not(X == f),
    Cost is Length*0.40,
    Time is Length/80.

time(X,Y,train, Cost, Time) :-
    connected(X,Y, Length),
    Length < 201,
    Length >= 201,
    Cost is Length*0.75,
    Time is Length/120.

time(X,Y, car, Cost, Time) :-
    connected(X,Y, Length),
    Length < 201,
    Length >= 201,
    Cost is Length*0.6,
    Time is Length/100.

time(X,Y, walking, Cost, Time) :-
    connected(X,Y, Length),
    Length < 900,
    Cost is Length*0.0,
    Time is Length/5.

connected(X,Y) :-
    edge(X,Y); edge(Y,X).
connected(X,Y,L) :-
    edge(X,Y,L) ; edge(Y,X,L).

subset([ ],_).
subset([H|T],List) :-
    member(H,List),
    subset(T,List).


path(A,B, Path,Mode, Cost, Time):-
       travel(A,B,[A],Q,Mode, Cost, Time),
      % subset([a,b,c,d,e,f,c,g], Q),
       reverse(Q,Path).

travel(A,B,P,[B|P], M, C, T) :-
       time(A,B,M, C,T).

travel(A,B,Visited,Path,M1, C1, T1):-
       time(A,C, M2, C2, T2),
       C \== B,
       \+member(C,Visited),
       travel(C,B,[C|Visited], Path,M3, C3, T3),
	C1 is C2 + C3,
        M1 = [M2| M3],
	T1 is T2 + T3.



shortestTime(A,B,Path, _Cost, Time) :-
   setof([P, T],path(A,B,P, _C, T),Set),
   Set = [_|_], % fail if empty
   minimal(Set,[Path, Time]).

shortestCost(A,B,Path, Cost, _Time) :-
   setof([P, C],path(A,B,P, C, _T),Set),
   Set = [_|_], % fail if empty
   minimal(Set,[Path, Cost]).

minimal([F|R],M) :- min(R,F,M).

% minimal path
min([],M,M).
min([[P,L]|R],[_,M],Min) :-
    L < M, !, min(R,[P,L],Min).
min([_|R],M,Min) :-
    min(R,M,Min).

path(A,B,Path,Len) :-
       travel(A,B,[A],Q,Len),
       reverse(Q,Path).

travel(A,B,P,[B|P],L) :-
       connected(A,B,L).
travel(A,B,Visited,Path,L) :-
       connected(A,C,D),
       C \== B,
       \+member(C,Visited),
       travel(C,B,[C|Visited],Path,L1),
       L is D+L1.

shortest(A,B,Path,Length) :-
   write("Shortest Path"),
   setof([P,L],path(A,B,P,L),Set),
   Set = [_|_], % fail if empty
   minimal(Set,[Path,Length]).

main(X, Y, Path,Mode, Cost, Time) :-
    write("Problem 2:"),
    write("Less Than $2,000 Including All Points"),
    shortestCost(X, Y, Path, Mode, Cost, Time).
















