def create_sitting_scheme(guests, dislikes):
    table_1 = []
    table_2 = []

    # Create a dictionary to store each guest's dislikes
    dislikes_dict = {}
    for guest in guests:
        dislikes_dict[guest] = []

    for dislike in dislikes:
        guest_1, guest_2 = dislike
        dislikes_dict[guest_1].append(guest_2)
        dislikes_dict[guest_2].append(guest_1)

    # Perform a recursive depth-first search to assign guests to tables
    def dfs(guest, table_num):
        if table_num == 1:
            table = table_1
        else:
            table = table_2

        # Check if this guest can be assigned to the current table
        for other_guest in table:
            if other_guest in dislikes_dict[guest]:
                return False

        # If the guest can be assigned to the current table, add them
        table.append(guest)

        # Recursively assign the guest's friends to the other table
        for friend in dislikes_dict[guest]:
            if friend not in table_1 and friend not in table_2:
                if not dfs(friend, 3 - table_num):
                    return False

        return True

    # Assign guests to tables using the depth-first search
    for guest in guests:
        if guest not in table_1 and guest not in table_2:
            if not dfs(guest, 1):
                # If the depth-first search fails, there is no valid sitting scheme
                return None

    # Return the final sitting scheme
    return [table_1, table_2]


# Define the list of guests and the corresponding list of dislikes
guests = ['Harry', 'Ron', 'Hermione', 'Draco', 'Crabbe', 'Goyle']
dislikes = [('Harry', 'Draco'), ('Ron', 'Crabbe'), ('Hermione', 'Goyle')]

# Call the create_sitting_scheme function
sitting_scheme = create_sitting_scheme(guests, dislikes)

# Print the resulting sitting scheme
print(sitting_scheme)
