def layout(N, C, L):
    """Assign guests to tables ensuring no conflicts"""
    # Initialize table assignments
    assignments = [-1] * N  # -1 means unassigned
    
    def is_valid(guest, table):
        """Check if assigning guest to table is valid"""
        for other_guest in range(N):
            if assignments[other_guest] == table and (guest, other_guest) in L or (other_guest, guest) in L:
                return False
        return True

    def assign_guests(guest_index):
        """Recursively assign guests to tables"""
        if guest_index == N:
            return True
        
        for table in range(C):
            if is_valid(guest_index, table):
                assignments[guest_index] = table
                if assign_guests(guest_index + 1):
                    return True
                assignments[guest_index] = -1
        
        return False

    if assign_guests(0):
        return {i: assignments[i] for i in range(N)}
    else:
        return False

# Example usage
N = 5
C = 3
L = [(0, 1), (2, 3)]
print(layout(N, C, L))
