def ball_routes(start, n, step, show):
    if start >= n:
        return 0
    if n // 2**step < 1:
        return min(n//16, n-start)
    routes = min(n//2**step, n - start)
    for i in range(start+1, min(start + n//2**step, n) + 1):
        if show: print(start, '->', i)
        routes += ball_routes(i, n, step + 1, show)
    return routes

ball_routes(1, 16, 1, False)