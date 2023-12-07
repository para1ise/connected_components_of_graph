number_of_test_file = 1
vertexes = 10


def input_from_file(number_of_test_file):
    with open("test_files/input{0}.txt".format(number_of_test_file), 'r') as file:
        adjacency_matrix = [list(map(int, line.split())) for line in file]
    return adjacency_matrix


adjacency_matrix = input_from_file(number_of_test_file)
visited = [False] * vertexes
number_of_components = 0

for i in range(vertexes):
    if visited[i]:
        continue

    number_of_components += 1
    visited[i] = True
    queue = [i]
    print("\n%d: " % number_of_components, end='')
    while queue:
        v = queue.pop()
        print(v + 1, end=' ')
        for j in range(vertexes):
            if adjacency_matrix[v][j] == 1 and not visited[j]:
                visited[j] = True
                queue.append(j)

print("\nA number of connected components of graph: %d" % number_of_components)
