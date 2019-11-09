# Coders Strike Back

1. Description

    Code presented here is my attempt to get the highest possible rank in the game Coders Strike Back. It is a Star Wars inspired pod racing game that can be found on the website Codingame.com (https://www.codingame.com/multiplayer/bot-programming/coders-strike-back).

    The game system is divided into leagues (Wood III, Wood II, Wood I, Bronze, Silver, Gold, Legend). Every time you advance in a league there are new mechanics introduced to the gameplay. That in turn forces you to change your approach to some degree. In this repository I will keep my current best code as well as some older versions that allowed me to reach my current rank. I will also keep track of my position in the ranking.

2. Code Construction

    The construction of code in this repository is dictated by the limitations Codingame puts on the user. Any solution submitted needs to be contained in one file. This is the reason why code may get very long and is not divided into smaller parts (which is my personal preference).

3. Results

    In this section I will state my current position among the players and link some interesting races performed. 

    Current rank: Silver 11,643/19,338

    Interesting matches:
    + https://www.codingame.com/replay/419897682
    + https://www.codingame.com/replay/419897641 (example of controlled drifting)

4. Techniques

    - Controlled drifting - During the first lap pod is collecting information about the position of all the checkpoints. From the beginning of the second lap, when all checkpoints are listed, the pod starts driving towards the next checkpoint before reaching the current one if its current speed and angle are enough to make it reach the current checkpoint. This technique helps very much with high speed turns.
    - Measured boost - During the first lap pod is collecting information about the position of all the checkpoints and the pod cannot use its boost. It will become available later after collecting the position of every checkpoint. Then the greatest distance between checkpoint can be measured which the heuristic approach considers the best place to boost.
    - Early break - The closer a pod is to a checkpoint the lower its thrust is going to be. Exact formulas can be seen in the code. It helps with reducing the time needed for a sharp turn, especially during the first lap.

5. Goals

    + Change the algorithm from heuristics to a genetic algorithm.
    + Creating an arena which will simulate race environment
    + Swigtching from python based solutions to those in C
