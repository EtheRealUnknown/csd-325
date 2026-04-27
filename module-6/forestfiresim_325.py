"""Forest Fire Sim modified for CSD-325 Module 6.

Changes made:
1. Added a lake/water feature near the center of the display.
2. Water uses the ~ character.
3. Water displays in blue.
4. Water cannot grow trees, catch fire, or be overwritten.
5. Water acts as a firebreak because fire cannot cross it.
"""

import random
import sys
import time

try:
    import bext
except ImportError:
    print("This program requires the bext module.")
    print("Install it with: pip install bext")
    sys.exit()

WIDTH = 79
HEIGHT = 22

TREE = "A"
FIRE = "@"
EMPTY = " "
WATER = "~"   # Added water symbol

INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01
PAUSE_LENGTH = 0.5


def create_lake(forest):
    """Adds a lake near the center of the display.

    The lake is created after the forest is generated so it replaces
    anything originally placed in that area. It is not changed later.
    """
    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    for x in range(center_x - 6, center_x + 7):
        for y in range(center_y - 3, center_y + 4):
            # Creates a rough oval/circle lake shape.
            if ((x - center_x) ** 2) / 36 + ((y - center_y) ** 2) / 9 <= 1:
                forest[(x, y)] = WATER


# Create the initial forest.
forest = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.random() <= INITIAL_TREE_DENSITY:
            forest[(x, y)] = TREE
        else:
            forest[(x, y)] = EMPTY

# Add lake after forest generation so water stays in place.
create_lake(forest)

while True:
    bext.clear()

    # Display the forest.
    for y in range(HEIGHT):
        for x in range(WIDTH):
            cell = forest[(x, y)]

            if cell == TREE:
                bext.fg("green")
            elif cell == FIRE:
                bext.fg("red")
            elif cell == WATER:
                bext.fg("blue")   # Water is blue.
            else:
                bext.fg("reset")

            print(cell, end="")
        print()

    print("Press Ctrl-C to stop.")
    time.sleep(PAUSE_LENGTH)

    # Create the next forest state.
    next_forest = {}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            current_cell = forest[(x, y)]

            # Water never changes.
            if current_cell == WATER:
                next_forest[(x, y)] = WATER
                continue

            if current_cell == EMPTY:
                if random.random() <= GROW_CHANCE:
                    next_forest[(x, y)] = TREE
                else:
                    next_forest[(x, y)] = EMPTY

            elif current_cell == TREE:
                # Check neighboring cells for fire.
                neighbors_on_fire = False

                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    neighbor_x = x + dx
                    neighbor_y = y + dy

                    if 0 <= neighbor_x < WIDTH and 0 <= neighbor_y < HEIGHT:
                        if forest[(neighbor_x, neighbor_y)] == FIRE:
                            neighbors_on_fire = True

                if neighbors_on_fire:
                    next_forest[(x, y)] = FIRE
                elif random.random() <= FIRE_CHANCE:
                    next_forest[(x, y)] = FIRE
                else:
                    next_forest[(x, y)] = TREE

            elif current_cell == FIRE:
                next_forest[(x, y)] = EMPTY

    forest = next_forest