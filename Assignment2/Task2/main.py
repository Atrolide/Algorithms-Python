def create_sitting_scheme(guests, dislikes):
    table_1 = set()
    table_2 = set()

    # Create a dictionary to store each guest's dislikes
    dislikes_dict = {guest: [] for guest in guests}

    for guest_1, guest_2 in dislikes:
        dislikes_dict[guest_1].append(guest_2)
        dislikes_dict[guest_2].append(guest_1)

    # Perform a recursive depth-first search to assign guests to tables
    def dfs(guest, table_num):
        table = table_1 if table_num == 1 else table_2
        other_table_num = 3 - table_num

        guest_dislikes = dislikes_dict[guest]
        for other_guest in table:
            if other_guest in guest_dislikes:
                return False

        table.add(guest)

        for friend in guest_dislikes:
            if friend not in table_1 and friend not in table_2:
                if not dfs(friend, other_table_num):
                    return False

        return True

    for guest in guests:
        if guest not in table_1 and guest not in table_2:
            if not dfs(guest, 1):
                return None

    return [list(table_1), list(table_2)]


guests = ['Harry', 'Ron', 'Hermione', 'Draco', 'Crabbe', 'Goyle']
dislikes = [('Harry', 'Draco'), ('Ron', 'Crabbe'), ('Hermione', 'Goyle')]

sitting_scheme = create_sitting_scheme(guests, dislikes)

print(sitting_scheme)
