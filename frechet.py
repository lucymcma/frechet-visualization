import random
import math
import matplotlib.pyplot as plt
import numpy as np

def d(x, y):
    return math.dist(x,y)

def init_curve(n):
    v = []
    x = 0.0
    for _ in range(n):
        x += random.uniform(0.5, 20)
        y = random.uniform(0.0, 50)
        v.append([x, y])
    return v

def hausdorff(p, q):
    h = 0
    for i in p:
        min_d = float('inf')
        for j in q:
            if d(i,j) < min_d:
                min_d = d(i, j)
        if min_d > h:
            h = min_d
    return h
        
def discrete_frechet(p, q, n, m):
    c = [[float('inf') for _ in range(m)] for _ in range(n)]
    for i in range(0, n):
        for j in range(0, m):
            if i == 0 and j == 0:
                c[i][j] = d(p[0], q[0])
            elif i > 0 and j == 0:
                c[i][j] = max(c[i-1][0], d(p[i], q[0]))
            elif i == 0 and j > 0:
                c[i][j] = max(c[0][j-1], d(p[0], q[j]))
            else:
                c[i][j] = max(
                    min(c[i-1][j-1], c[i-1][j], c[i][j-1]), 
                    d(p[i], q[j]))
    # for i in range (0,n):
    #     print(c[i])
    path = backtrack(c, n, m)
    return c[n-1][m-1], path

def backtrack(c, n, m):
    i = n - 1
    j = m - 1
    path = [(i,j)]
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            up = c[i-1][j]
            left = c[i][j-1]
            diag = c[i-1][j-1]
            if diag <= up and diag <= left:
                i, j = i-1, j-1
            elif up <= left:
                i -= 1
            else:
                j -= 1
        elif i > 0:
            i -= 1
        else: 
            j -= 1
        path.append((i,j))
    path.reverse()
    return path

def plot_frechet(p, q, n, m, path, df):

    p_x = np.array([])
    p_y = np.array([])
    q_x = np.array([])
    q_y = np.array([])

    for i in range(0,n):
        p_x = np.append(p_x, p[i][0])
        p_y = np.append(p_y, p[i][1])
    for i in range(0,m):
        q_x = np.append(q_x, q[i][0])
        q_y = np.append(q_y, q[i][1])

    _, ax = plt.subplots()

    for i in range(0, len(path)):
        p_index = path[i][0]
        q_index = path[i][1] 
        p_pt = p[p_index]
        q_pt = q[q_index]
        x = np.array([p_pt[0], q_pt[0]])
        y = np.array([p_pt[1], q_pt[1]])
        ax.plot(x, y, color='gray', linestyle='dotted', label=str(d(p_pt, q_pt)))
        # midpoints
        mx = (p_pt[0] + q_pt[0]) / 2
        my = (p_pt[1] + q_pt[1]) / 2
        dist = d(p_pt, q_pt)
        ax.text(mx, my, f"{dist:.2f}", color='gray', fontsize=8)

    ax.plot(p_x, p_y, marker='o', color='teal')
    ax.plot(q_x, q_y, marker='o', color='green')

    ax.text(
        0.40, 0., 
        f"Discrete frechet distance = {df:.2f}", 
        color='black', 
        fontsize=8, 
        transform=ax.transAxes,
        ha='right',
        va='bottom'
    )

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Discrete Frechet Distance')

    plt.show() 

def main():
    # num vertices of curves P and Q
    n = random.randint(3, 10)
    m = random.randint(3, 10)

    # curves defined by a list of vertices
    p = init_curve(n)
    q = init_curve(m)
    max_y = 0
    for i in range(n):
        if p[i][1] > max_y:
            max_y = p[i][1]
    for i in range(m):
        q[i][1] += max_y

    df, path = discrete_frechet(p, q, n, m)
    plot_frechet(p, q, n, m, path, df)

if __name__ == "__main__":
    main()