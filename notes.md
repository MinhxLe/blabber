SOURCE:https://learntofish.wordpress.com/2012/01/15/introduction-to-markov-chains/
-example: think of it as chained probablity
-use a matrix to represent probability of chain
  -multiply matrix by itself to get "chained" probability
-formal definion: a process with a finite number of states (or outcomes, or
events) in which the probability of being in a particular state at step n+1
depends only on the state occupied at step n.
-higher order matrix(ie P^2 P^3 matrix for better predictivity)

http://people.virginia.edu/~rlc9s/sys6005/SYS_6005_Intro_to_MC.pdf
goal: want to model weather over 30 day period(binary wether raining for sunny)
-can do this with a pure joing pmf of 30 days(each day is a different random
variable)--> this doesnt work well with 30 random variaables(2^30 sequences!)
-can also do this with independentprobablitlies per day but that isn't realistic

-compromise: joing prom from conditional pmf-->probability dependent from on
the past

-


KEY DEFS:
-PMF(probability mass function): function that returnsprobabiltiy for a
value
-conditional probability

