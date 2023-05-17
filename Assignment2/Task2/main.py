def create_sitting_scheme(guests, dislikes):
    table_1 = set()
    table_2 = set()

    # dictionary to store the dislikes of each guest.
    dislikes_dict = {guest: [] for guest in guests}

    # for each guest, their corresponding value in the dictionary will be a list of all the guests they dislike.
    for guest_1, guest_2 in dislikes:
        dislikes_dict[guest_1].append(guest_2)
        dislikes_dict[guest_2].append(guest_1)

    # Perform a recursive depth-first search to assign guests to tables
    def dfs(guest, table_num):
        if table_num == 1:
            table = table_1  # Assign the table 1 set to the 'table' variable
        else:
            table = table_2  # Assign the table 2 set to the 'table' variable

        other_table_num = 3 - table_num  # Calculate the number of the other table

        guest_dislikes = dislikes_dict[guest]  # Get the list of dislikes for the current guest
        for other_guest in table:
            if other_guest in guest_dislikes:
                return False  # Return False if a disliked guest is already seated at the same table

        table.add(guest)  # Add the guest to the current table

        #  For each friend, it checks if the friend is not already
        # seated at either table_1 or table_2. If the friend is not seated,
        # the dfs function is recursively called to attempt to assign the
        # friend to the other table (other_table_num). If the recursive call fails (dfs returns False),
        #  it means that it was not possible to seat the friend at the other table, so the function returns False as well.
        for friend in guest_dislikes:
            if friend not in table_1 and friend not in table_2:
                if not dfs(friend, other_table_num):
                    return False  # Return False if assigning the friend to the other table fails

        return True  # Return True if all guests are successfully assigned to tables

    # Iterate through the list of guests
    for guest in guests:
        if guest not in table_1 and guest not in table_2:
            if not dfs(guest, 1):
                return None  # Return None if it's not possible to assign guests to tables

    return [list(table_1), list(table_2)]  # Return the seating arrangement as a list of table sets


guests = ['Harry', 'Ron', 'Hermione', 'Draco', 'Crabbe', 'Goyle']
dislikes = [('Harry', 'Draco'), ('Ron', 'Crabbe'), ('Hermione', 'Goyle')]
sitting_scheme = create_sitting_scheme(guests, dislikes)

print(sitting_scheme)
