def solve_ege(filename):
    f = open(filename, 'r')
    first_line = f.readline().strip().split()
    N = int(first_line[0])
    V = int(first_line[1])
    
    points = []
    for i in range(N):
        line = f.readline().strip().split()
        pos = int(line[0])
        tubes = int(line[1])
        containers = (tubes + V - 1) // V
        points.append((pos, containers))
    f.close()
    
    points.sort()
    
    positions = []
    containers = []
    for i in range(N):
        positions.append(points[i][0])
        containers.append(points[i][1])
    
    prefix_sum = [0] * (N + 1)
    for i in range(N):
        prefix_sum[i + 1] = prefix_sum[i] + containers[i]
    
    prefix_weighted = [0] * (N + 1)
    for i in range(N):
        prefix_weighted[i + 1] = prefix_weighted[i] + positions[i] * containers[i]
    
    min_cost = float('inf')
    
    for i in range(N):
        left_cost = positions[i] * prefix_sum[i] - prefix_weighted[i]
        right_cost = (prefix_weighted[N] - prefix_weighted[i + 1]) - positions[i] * (prefix_sum[N] - prefix_sum[i + 1])
        total_cost = left_cost + right_cost
        if total_cost < min_cost:
            min_cost = total_cost
    
    return min_cost


data_a = """6 96
5 4
7 3
1 100
10 190
2 200
8 2"""

data_b = """10 100
1 50
2 150
3 80
4 200
5 90
6 180
7 70
8 160
9 40
10 120"""

file_a = open('27-122a.txt', 'w')
file_a.write(data_a)
file_a.close()

file_b = open('27-122b.txt', 'w')
file_b.write(data_b)
file_b.close()

result_a = solve_ege('27-122a.txt')
result_b = solve_ege('27-122b.txt')

print(result_a, result_b)
