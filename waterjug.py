from collections import defaultdict

jug1, jug2, aim = 4, 3, 2

visited = defaultdict(lambda: False)

def waterJugSolver(amt1, amt2):
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(f"Solution: {amt1}, {amt2}")
        return True

    if not visited[(amt1, amt2)]:
        print(f"Current state: {amt1}, {amt2}")
        visited[(amt1, amt2)] = True

        return (waterJugSolver(0, amt2) or  # Empty jug1
                waterJugSolver(amt1, 0) or  # Empty jug2
                waterJugSolver(jug1, amt2) or  # Fill jug1
                waterJugSolver(amt1, jug2) or  # Fill jug2
                waterJugSolver(amt1 + min(amt2, (jug1 - amt1)),
                               amt2 - min(amt2, (jug1 - amt1))) or  # Pour jug2 -> jug1
                waterJugSolver(amt1 - min(amt1, (jug2 - amt2)),
                               amt2 + min(amt1, (jug2 - amt2))))  # Pour jug1 -> jug2
    else:
        return False

print("Steps to solve the Water-Jug problem:")
waterJugSolver(0, 0)

