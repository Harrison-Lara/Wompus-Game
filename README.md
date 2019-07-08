# Wompus-Game

Wumpus World is fairly simple:
• Wumpus World is a 5x5 grid, with cells numbered from 0,0 to 4,4.
• The player always starts in the lower left-hand corner (cell 0,0), and the starting cell is
always safe.
• Somewhere (randomly placed anywhere but 0,0) is the Wumpus, a fierce beast that will
eat the player if that cell is entered.
◦ The Wumpus does not move.
• Somewhere is a pile of gold, which the player is trying to retrieve.
• About 20% of the squares (other than 0,0) are pits; stepping into a pit means the player
dies (loses the game).
◦ Yes, the gold can be in the same square as the Wumpus. It can be retrieved if the
Wumpus is dead.
◦ Yes, the gold can be at the bottom of a pit. In this case the gold cannot be retrieved.
◦ About 1/5 to 1/4 of the time, the placement of pits will make the gold impossible to
reach, either because it’s in a pit or because all paths to it are blocked. (That’s nothing
your program has to worry about, but be aware of it during testing.)
◦ The gold will never be at 0,0.
◦ If there’s a pit on the same square as the Wumpus, the Wumpus is too big to fall into
the pit (so a pit and the Wumpus can both be in the same cell, and the Wumpus is still
dangerous if so). Of course, it doesn’t really matter if the Wumpus gets you or the pit
does, it’s bad either way.
• The player can move North, South, East, or West, but not diagonally. The player can only
sense things about cells that can be moved to.
• Wumpus World is perpetually dark (this prevents Wumpuses from reproducing), but the
player can sense some of the environment:
◦ If there is a pit in an adjacent cell, the player will feel a breeze.
◦ If the Wumpus is in an adjacent cell, the player will smell a stench.
◦ If the gold is in the same cell as the player, the player will notice a glint.
◦ If the player tries walking off the edge of the map, the player will hit a wall and feel a
bump, but not actually move.
◦ If the player successfully shoots the Wumpus (see below), the Wumpus will emit a
scream that can be heard from anywhere in Wumpus World.
• The player has a crossbow, but only one arrow. If the player shoots, the arrow will travel
in a straight line until it hits a wall, or the Wumpus. Trying to shoot again will have no
effect (but counts as a move for scoring purposes).
