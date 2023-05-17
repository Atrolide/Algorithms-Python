import random
def create_sitting_scheme(guests, dislikes):
    table_1 = set()
    table_2 = set()

    dislikes_dict = {guest: [] for guest in guests}

    for guest_1, guest_2 in dislikes:
        dislikes_dict[guest_1].append(guest_2)
        dislikes_dict[guest_2].append(guest_1)

    def dfs(guest, table_num, seated_guests):
        if table_num == 1:
            table = table_1
        else:
            table = table_2

        other_table_num = 3 - table_num

        guest_dislikes = dislikes_dict[guest]
        table.add(guest)

        for friend in guest_dislikes:
            if friend in seated_guests:
                continue

            seated_guests.add(friend)

            if not dfs(friend, other_table_num, seated_guests):
                return False

        return True

    seated_guests = set()

    for guest in guests:
        if guest not in seated_guests:
            if not dfs(guest, 1, seated_guests):
                return None

    return [list(table_1), list(table_2)]


guests = ['Harry', 'Ron', 'Hermione', 'Draco', 'Crabbe', 'Goyle']
dislikes = [('Harry', 'Draco'), ('Ron', 'Crabbe'), ('Hermione', 'Goyle')]

random.shuffle(guests)
sitting_scheme = create_sitting_scheme(guests, dislikes)


print(sitting_scheme)

