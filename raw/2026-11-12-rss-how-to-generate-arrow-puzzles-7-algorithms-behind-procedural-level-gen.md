---
source: "https://dev.to/cliffwang/how-to-generate-arrow-puzzles-7-algorithms-behind-procedural-level-generation-1p6h"
title: "How to Generate Arrow Puzzles: 7 Algorithms Behind Procedural Level Generation"
author: "Cliff"
date_published: "2026-11-12"
date_clipped: "2026-11-12"
category: "Game Development / Unity"
source_type: "rss"
---

# How to Generate Arrow Puzzles: 7 Algorithms Behind Procedural Level Generation

From reverse construction and graph theory to constraint solving and evolutionary algorithms.

Arrow puzzles look deceptively simple. A board contains a collection of arrows, each pointing in a particular direction. The objective is to remove every arrow by allowing it to escape through the edge of the board.

But how do you generate hundreds or thousands of interesting levels automatically?

Randomly placing arrows on a grid is easy. Generating a board that is solvable, visually interesting, and appropriately challenging is a much harder problem.

This is where procedural puzzle generation comes in.

In this article, we'll explore seven algorithmic approaches that can be used to generate Arrow Escape-style puzzles, how they work, their advantages and limitations, and how they can be combined into a practical level-generation pipeline.

1. Understanding the Puzzle as a Computational Problem

Before choosing an algorithm, we need to define the puzzle mechanics.

Consider a grid containing several arrows. Each arrow consists of connected cells and has a head pointing in one of four directions:

Up

Down

Left

Right

When a player selects an arrow, the game checks the straight line from its head to the corresponding edge of the board.

If that line is clear, the arrow can escape. If another arrow occupies any cell along that line, the move is blocked.

The objective is to remove all arrows.

This creates an interesting dependency between arrows.

For example:

Arrow A blocks the exit path of Arrow B.

Arrow B must leave before Arrow A can escape.

Arrow C may block both A and B.

Removing C can unlock multiple other arrows.

The difficulty is therefore not simply determined by the number of arrows. It also depends on how those arrows depend on one another.

A useful way to think about the problem is as a dependency graph.

Each arrow is a node, and a directed edge represents a blocking relationship.

Once we understand this structure, we can start designing algorithms to generate it.

1. Algorithm One: Reverse Construction

The basic idea: Build the puzzle backward from a known solution.

Reverse construction is one of the most practical approaches to generating guaranteed-solvable puzzles.

Instead of randomly placing arrows and hoping the result works, we start with an empty board and construct it in reverse order.

Imagine that the intended removal sequence is:

A → B → C → D

This means A leaves first, followed by B, C, and D.

To generate the board, we work backward:

Place D.

Place C, ensuring that its exit path is not blocked by D.

Place B, ensuring that its exit path is not blocked by C or D.

Place A under the same condition.

The resulting board has a known solution: remove A, then B, then C, then D.

In simplified pseudocode:

def generate\_reverse(width, height, count):  
board = empty\_grid(width, height)  
solution = []


```
for i in range(count):
    candidates = find_valid_arrow_placements(board)

    if not candidates:
        break

    arrow = choose_random(candidates)
    place_arrow(board, arrow)
    solution.append(arrow)

return board, list(reversed(solution))
```


The important part is find\_valid\_arrow\_placements().

It must check more than whether the arrow fits inside the board. It must also ensure that previously placed arrows do not block the new arrow's exit path.

A production implementation also needs to handle arrow-body geometry, cell overlap, connectivity, and the chosen construction order.

Advantages:

Solvability can be guaranteed by construction.

No expensive search is needed for every candidate.

Easy to introduce randomness.

Suitable for generating large numbers of levels.

Limitations:

The resulting levels can have predictable structures.

Random placement does not automatically produce good difficulty.

Complex board shapes can make valid placement increasingly difficult.

For many Arrow Escape games, this is an excellent starting point.

1. Algorithm Two: Randomized Backtracking

The basic idea: Explore possible placements and backtrack when a construction becomes impossible.

Randomized backtracking is useful when the board has more restrictive geometric requirements.

Suppose the generator needs to create a board with:

A specific number of arrows.

A target board size.

Different arrow lengths.

A mixture of horizontal and vertical paths.

No overlapping cells.

Valid exit paths.

A simple random generator may frequently reach a situation where no additional arrow can be placed.

Backtracking solves this by exploring alternative choices.

The algorithm works as follows:

Select a possible arrow placement.

Check whether it satisfies the current constraints.

If valid, add it to the board.

Continue generating.

If no valid placement remains, undo the previous choice and try another one.

Example:

def backtrack(board, remaining):  
if remaining == 0:  
return True


```
candidates = generate_candidates(board)
shuffle(candidates)

for arrow in candidates:
    if not is_valid(board, arrow):
        continue

    place_arrow(board, arrow)

    if backtrack(board, remaining - 1):
        return True

    remove_arrow(board, arrow)

return False
```


In practice, the generator can improve efficiency by using:

Early constraint checking.

Candidate ordering.

Maximum search depth.

Randomized candidate selection.

Memoization of repeated states.

Advantages:

More control over board structure.

Can satisfy multiple geometric constraints.

Avoids many dead ends during generation.

Limitations:

Search time can increase rapidly.

Large boards may have enormous candidate spaces.

Poor candidate ordering can result in excessive backtracking.

Backtracking is particularly useful when reverse construction alone cannot satisfy the desired board geometry.

1. Algorithm Three: Constraint Satisfaction Problems (CSP)

The basic idea: Define what a valid puzzle looks like, then let a solver find an arrangement.

Constraint Satisfaction Problems are a more formal approach to puzzle generation.

Instead of describing every construction step, we define variables, domains, and constraints.

For an Arrow Puzzle, variables might include:

Arrow position.

Arrow direction.

Arrow length.

Arrow path.

Occupied grid cells.

Blocking relationships.

Then we define constraints.

For example:

Geometric constraints

Every arrow must remain inside the board.

No two arrows may occupy the same cell.

Every arrow must have a valid connected path.

Every arrow must have a valid head and direction.

Gameplay constraints

Every arrow must eventually have an available exit.

The puzzle must contain at least one removable arrow.

The dependency relationships must permit complete removal.

Difficulty constraints

The number of initially removable arrows must be within a target range.

Some arrows should depend on several other arrows.

The solution should contain multiple stages.

A CSP solver attempts to find an assignment satisfying these conditions.

Tools such as Google OR-Tools CP-SAT or SAT/SMT solvers can be useful for more complex generation problems.

Advantages:

Very expressive constraints.

Good control over board composition.

Useful for generating levels with specific properties.

Limitations:

Modeling the geometry can be complicated.

Solving large constraint systems can be expensive.

A mathematically valid solution is not necessarily an enjoyable level.

CSP is especially interesting when a game needs precise control over the properties of generated levels.

1. Algorithm Four: Dependency Graph Generation

The basic idea: Design the logical relationships first, then build the board around them.

This is one of the most interesting approaches for Arrow Escape-style puzzles.

Rather than generating arrows directly, we first generate a directed graph.

Consider this example:

A → B → D  
↓  
C → E

The graph represents the intended blocking relationships. An arrow cannot escape until the arrows blocking its exit path have been removed.

Depending on the chosen edge convention, the graph can be represented as:

dependencies = {  
"A": [],  
"B": ["A"],  
"C": ["B"],  
"D": ["B"],  
"E": ["C"]  
}

Here, an arrow's dependency list identifies the arrows that must leave before it can escape.

The generator can then:

Create a directed acyclic graph (DAG).

Control its depth and branching factor.

Assign arrows to graph nodes.

Find geometric placements that realize the desired blocking relationships.

Validate the resulting board.

Why use a DAG?

Because a valid removal sequence must exist. A directed cycle in which every arrow depends on another arrow in the same cycle would create a deadlock.

A topological ordering of the dependency graph provides a valid removal order.

This approach separates two problems:

Logical puzzle design.

Geometric board construction.

That separation can make the generator easier to control and debug.

Advantages:

Direct control over logical complexity.

Easy to measure dependency depth.

Useful for creating bottlenecks and branching structures.

Can produce more intentional difficulty progression.

Limitations:

Not every abstract graph can be represented by valid arrow geometry.

Geometric placement may introduce unintended dependencies.

The final board still needs simulation and validation.

This is a particularly promising approach when the goal is to generate levels with deliberately designed logical structures.

1. Algorithm Five: Generate-and-Test with an Automatic Solver

The basic idea: Generate candidates, solve them, and reject unsuitable levels.

Sometimes the simplest solution is to generate many possible boards and let an automatic solver evaluate them.

A typical pipeline looks like this:

Generate a candidate board  
|  
v  
Check geometric validity  
|  
v  
Run automatic solver  
|  
v  
Is the board solvable?  
/ \  
No Yes  
| |  
Reject Evaluate difficulty  
|  
v  
Accept or reject

For a basic Arrow Escape mechanic, the solver can be surprisingly simple.

At each step:

Find all arrows with a clear path to the edge.

Remove one available arrow.

Update the board.

Repeat until all arrows are removed or no removable arrow remains.

An example:

def solve(board):  
remaining = set(board.arrows)  
solution = []


```
while remaining:
    available = [
        arrow for arrow in remaining
        if is_exit_path_clear(board, arrow, remaining)
    ]

    if not available:
        return None

    arrow = available[0]

    remaining.remove(arrow)
    solution.append(arrow)

return solution
```


For the removal-only mechanic described here, there is an important mathematical property:

Removing an arrow only makes the board emptier. It cannot block another arrow that was previously free.

Therefore, if at least one removable arrow exists, removing it cannot destroy the possibility of completing the puzzle. Repeatedly removing available arrows will eventually clear any solvable board.

This means a greedy solver is sufficient for checking basic solvability.

However, this does not mean all generated levels are equally interesting.

The solver can also collect information about:

How many arrows are initially available.

How many rounds of removal are required.

How many arrows become available after each removal.

Which arrows unlock the largest number of others.

How long the longest dependency chain is.

Advantages:

Easy to implement and understand.

Excellent for filtering invalid candidates.

Can be combined with almost any generation method.

Provides useful data for difficulty estimation.

Limitations:

Solvability alone says very little about puzzle quality.

Generating and testing too many candidates can be expensive.

A simple solver may not accurately predict human difficulty.

For this puzzle mechanic, generate-and-test is particularly effective as a validation layer.

1. Algorithm Six: Template-Based Procedural Generation

The basic idea: Combine handcrafted structures with randomized variations.

Pure randomness is not always the best way to generate enjoyable puzzles.

A useful alternative is to create a collection of puzzle templates.

For example:

Linear dependency patterns.

Branching structures.

Multiple independent starting arrows.

Narrow bottlenecks.

Dense central clusters.

Multiple paths that eventually converge.

The generator selects a template and fills it with randomized arrow geometry.

A possible workflow:

template = choose\_template(difficulty)

board = create\_board\_from\_template(template)

board = randomize\_arrow\_paths(board)

if validate(board):  
return board

Templates can control the overall logical structure, while procedural generation provides variation in:

Arrow lengths.

Arrow directions.

Path shapes.

Board dimensions.

Arrow density.

This is a form of hybrid generation.

It combines the reliability of handcrafted design with the scalability of procedural generation.

Advantages:

More predictable level quality.

Easier difficulty tuning.

Good for building recognizable level families.

Less likely to produce visually repetitive random noise.

Limitations:

Requires an initial template library.

Repeated structures may become recognizable.

Templates can limit long-term variety.

For a game with a carefully designed progression, this can be a very practical approach.

1. Algorithm Seven: Evolutionary Algorithms and Genetic Optimization

The basic idea: Generate many candidates and evolve them toward desired difficulty and quality.

Evolutionary algorithms take a different approach.

Instead of generating one board and immediately accepting or rejecting it, we create a population of candidate boards.

Each candidate receives a fitness score.

For example:

fitness = (  
weight\_1 \* dependency\_depth  
+ weight\_2 \* blocking\_density  
+ weight\_3 \* branching\_score  
- weight\_4 \* visual\_repetition  
)

The algorithm then:

Generates an initial population.

Evaluates each candidate.

Selects better candidates.

Mutates their arrow positions, lengths, and directions.

Combines selected structures.

Repeats the process over several generations.

The objective is to find boards that satisfy a desired combination of properties.

For example, an intermediate-level puzzle might aim for:

A moderate number of initially available arrows.

Several dependency chains.

A few meaningful bottlenecks.

A reasonable number of arrows unlocked per stage.

A visually balanced board.

Evolutionary algorithms can optimize for these characteristics.

Advantages:

Can explore unusual puzzle structures.

Allows multi-objective optimization.

Useful when the quality function is difficult to express as hard constraints.

Limitations:

Requires carefully designed fitness functions.

Can converge toward repetitive structures.

More computationally expensive than direct construction.

A high fitness score does not guarantee an enjoyable puzzle.

Evolutionary generation is probably unnecessary for a small game, but it becomes interesting when generating large collections of levels with specific difficulty targets.

1. How Should an Arrow Puzzle Generator Measure Difficulty?

This may actually be the most important part of the entire system.

A board with 100 arrows is not necessarily harder than a board with 60 arrows.

The number of arrows is only one dimension of complexity.

For Arrow Escape-style puzzles, I would consider the following metrics.

Metric

What it measures

Initial availability

Number of arrows that can escape immediately

Dependency depth

Length of the longest chain of blocking relationships

Blocking density

Average number of arrows blocking each arrow

Bottleneck severity

How much progress depends on a small number of arrows

Unlock potential

Number of new arrows made available after a removal

Board density

Proportion of occupied cells

Structural variety

Diversity of arrow shapes and directions

One particularly useful metric is the dependency depth.

Consider two boards containing the same number of arrows.

Board A:

Many arrows can escape independently. Removing one arrow does not significantly affect the others.

Board B:

Most arrows depend on other arrows. Removing one particular arrow may unlock a long sequence of subsequent moves.

Even if both boards contain 50 arrows, Board B may feel considerably more complex.

Another useful metric is the number of available arrows at each stage.

We can record this as a sequence:

Stage 1: 3 available arrows  
Stage 2: 2 available arrows  
Stage 3: 1 available arrow  
Stage 4: 5 available arrows  
Stage 5: 8 available arrows  
...

This sequence gives us a better understanding of how the puzzle unfolds.

It can also help identify levels that are too straightforward or have repetitive progression.

One caution: these metrics are proxies, not direct measurements of human difficulty. The best way to calibrate them is to compare generated levels with actual player performance.

1. A Practical Architecture for a Procedural Arrow Puzzle Generator

If I were building a procedural generation system for an Arrow Escape game, I would not rely on a single algorithm.

I would combine several approaches into one pipeline.

My preferred architecture would look like this:


```
     Difficulty Configuration
               |
               v
      Dependency Generator
               |
               v
      Reverse Construction
               |
               v
      Geometric Randomization
               |
               v
      Constraint Validation
               |
               v
      Automatic Solver
               |
               v
      Difficulty Evaluation
               |
         +-----+-----+
         |           |
      Accept       Reject
         |           |
         v           v
    Save Level    Regenerate
```


Each component has a specific responsibility.

Dependency Generator

Defines the intended logical relationships between arrows.

Reverse Construction

Builds a board with a known valid removal sequence.

Geometric Randomization

Adds variation to arrow shapes, positions, and lengths.

Constraint Validation

Checks overlapping cells, invalid paths, board boundaries, and unintended geometry.

Automatic Solver

Confirms that the final board can be completely cleared.

Difficulty Evaluation

Measures the dependency structure and compares the results against the target difficulty.

This architecture is modular, so individual components can be improved without rewriting the entire generator.

1. Final Thoughts: Random Generation Is Not the Same as Good Puzzle Design

Procedural generation makes it possible to create a large number of Arrow Puzzle levels, but generating more levels does not automatically mean generating better levels.

The most interesting systems combine three things:

Mathematical validity: Every generated board has a complete solution.

Structural variety: Different levels introduce different dependency patterns and geometric arrangements.

Controlled difficulty: The generator can create a meaningful progression instead of simply increasing the number of arrows.

Reverse construction is an excellent foundation. Dependency graphs provide more control over logical structure. Automatic solvers make validation straightforward. Constraint solving and evolutionary optimization can add more sophisticated control when needed.

Ultimately, the best generator is not necessarily the one that creates the most complicated boards.

It is the one that consistently creates puzzles that make players stop, observe, think, and finally discover the right move.

Try an Arrow Puzzle

If you enjoy exploring how directional logic and spatial relationships create interesting puzzle challenges, you can also try a browser-based Arrow Escape game at [Puzzle Arrow](https://puzzle-arrow.com).

It is a useful way to experience the mechanics discussed in this article and see how different arrow arrangements can create different levels of challenge.

What generation approach would you use for an Arrow Puzzle game: reverse construction, graph-based generation, or a hybrid system?
