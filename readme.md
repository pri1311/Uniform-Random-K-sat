In general K-sat with n variables will gives us 2^n possible values/combinations to check for.
In Solution Space Search, the moves are defined with some perturbation (Change of value) of a bit or k-bits in a given candidate.


Local Search Algorithms: 
-- Generally used for optimization problems 
-- They start from a prospective solution and then move to a neighboring solution 
-- Generally used when path is not needed 
-- Keeps a small number of nodes in memory
-- Example: Tabu and Hill Climbing 
-- Vertex Cover, TSP can be solved using such algorithms

Hill Climbing:
-- Moves ahead until no further improvements can be found
-- Not complete or optimal

Simple Neighborhood Descent:
-- Only permits moves to neighbor solutions that improve the current objective function value and ends when no improving solutions can be found

Variable Neighborhood Descent:
-- It is a metaheuristic approach
-- Sparse neigborhood function - example : number of bits changed is few, hence lesser number of new states
-- Dense neighborhood function - example : number of bits changed is more, hence more number of new states
-- When Neighborhood function is incorporated with Hill Climbing algorithm, it gives rise to Variable Neighborhood Descent
-- Good explanation Flowchart - https://www.researchgate.net/profile/Daniel-Guimarans/publication/236455075/figure/fig3/AS:299416671014914@1448397905299/Variable-Neighborhood-Descent-VND.png

