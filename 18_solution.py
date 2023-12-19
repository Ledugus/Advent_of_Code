dirs = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}


def are_adjacents(node1, node2, previous_dict):
    if node1 == previous_dict[node2]:
        return True
    if node2 == previous_dict[node1]:
        return True
    return False


def get_pairs(list):
    return [list[x:x+2] for x in range(0, len(list), 2)]


def step_1(filename):
    f = open(filename)
    total_area = 0
    previous = {}
    current_node = (0, 0)
    nodes = []
    nodes_dict = {}
    # faire la liste des nodes, et de leurs previous
    for line in f.readlines():
        dir, size = line.split()[:2]
        size = int(size)
        node = (current_node[0]+size*dirs[dir][0],
                current_node[1]+size*dirs[dir][1])

        current_list = nodes_dict.get(node[0], [])
        current_list.append(node[1])
        current_list.sort()
        nodes_dict[node[0]] = current_list

        previous[node] = current_node
        current_node = node
        nodes.append(node)

    list_rows = sorted(nodes_dict.keys())
    row = list_rows[0]
    previous_cols = nodes_dict[row]
    list_bounds = previous_cols
    previous_row = row
    pairs = []
    # passer en revue les lignes pour calculer l'aire
    for row in list_rows[1:]:
        # ajouter les aires des anciens rectangles (hauteur * largeur)
        for bounds in get_pairs(list_bounds):
            total_area += (row - previous_row)*(bounds[1]-bounds[0]+1)

        # update les nouveaux rectangles
        current_cols = nodes_dict[row]
        pairs = get_pairs(current_cols)
        new_bounds = []
        for pair in pairs:
            left, right = pair
            # si ça referme un rectangle, ajouter la dernière ligne
            if pair in get_pairs(list_bounds):
                total_area += pair[1]-pair[0]+1
            # ça va de gauche à droite
            elif left in list_bounds:
                # si rentre dans le rectangle
                if list_bounds.index(left) // 2 == 0:
                    new_bounds.append(
                        (right, list_bounds[list_bounds.index(left)+1]))
                else:

                    new_bounds.append(
                        (right, list_bounds[list_bounds.index(left)+1]))
            # si pas de match, incise, donc cas particulier

        previous_cols = current_cols
        previous_row = row

    # add last bounds as bottoms
    total_area += sum([pair[1]-pair[0]+1 for pair in pairs])
    return total_area


print(step_1('18_test.txt'))
