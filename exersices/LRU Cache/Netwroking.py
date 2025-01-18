def network_delay_time():
    m = int(input().strip())
    times = []
    for _ in range(m):
        times.append(tuple(map(int, input().split())))
    n = int(input().strip())
    k = int(input().strip())
    
    graph = [[] for _ in range(n + 1)]
    for u, v, w in times:
        graph[u].append((v, w))
    
    dist = [float('inf')] * (n + 1)
    dist[k] = 0
    processed = [False] * (n + 1)
    pq = [(0, k)]
    
    while pq:
        pq.sort()
        current_dist, node = pq.pop(0)
        if processed[node]:
            continue
        processed[node] = True
        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                pq.append((new_dist, neighbor))
    
    max_dist = max(dist[1:])
    print(max_dist if max_dist < float('inf') else -1)
network_delay_time()