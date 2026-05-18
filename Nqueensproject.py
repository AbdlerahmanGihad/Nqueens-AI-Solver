import pygame
import sys
import random

N = 8
SIZE = 80
WIDTH = HEIGHT = N * SIZE

WHITE = (240, 240, 240)
GRAY = (180, 180, 180)
RED = (220, 50, 50)
BLACK = (30, 30, 30)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("N-Queens Visualizer")

clock = pygame.time.Clock()

board = [[0 for _ in range(N)] for _ in range(N)]

mode = "PLAY"

def draw_board():

    screen.fill(WHITE)

    for row in range(N):
        for col in range(N):

            color = WHITE if (row + col) % 2 == 0 else GRAY

            pygame.draw.rect(
                screen,
                color,
                (col * SIZE, row * SIZE, SIZE, SIZE)
            )

            
            if board[row][col] == 1:

                pygame.draw.circle(
                    screen,
                    RED,
                    (
                        col * SIZE + SIZE // 2,
                        row * SIZE + SIZE // 2
                    ),
                    SIZE // 3
                )

    pygame.display.set_caption(f"N-Queens | {mode}")

    pygame.display.update()

def is_safe(row, col):

    for i in range(col):
        if board[row][i] == 1:
            return False

    
    i = row
    j = col

    while i >= 0 and j >= 0:

        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    i = row
    j = col

    while i < N and j >= 0:

        if board[i][j] == 1:
            return False

        i += 1
        j -= 1

    return True

def backtracking(col=0):

    handle_quit()

    if col >= N:
        return True

    for row in range(N):

        if is_safe(row, col):

            board[row][col] = 1

            draw_board()
            pygame.time.delay(80)

            if backtracking(col + 1):
                return True

            board[row][col] = 0

            draw_board()
            pygame.time.delay(80)

    return False

def dfs():

    clear_board()

    def dfs_util(col):

        handle_quit()

        if col == N:
            return True

        for row in range(N):

            if is_safe(row, col):

                board[row][col] = 1

                draw_board()
                pygame.time.delay(80)

                if dfs_util(col + 1):
                    return True

                board[row][col] = 0

                draw_board()
                pygame.time.delay(80)

        return False

    dfs_util(0)

def fitness(solution):

    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):

            same_row = solution[i] == solution[j]
            same_diag = abs(solution[i] - solution[j]) == abs(i - j)

            if same_row or same_diag:
                conflicts += 1

    return -conflicts

def crossover(parent1, parent2):

    cut = random.randint(0, N - 1)

    child = parent1[:cut] + parent2[cut:]

    return child

def mutate(solution):

    if random.random() < 0.4:

        col = random.randint(0, N - 1)

        solution[col] = random.randint(0, N - 1)

    return solution

def apply_solution(solution):

    clear_board()

    for col, row in enumerate(solution):
        board[row][col] = 1

def genetic():

    population = [
        [random.randint(0, N - 1) for _ in range(N)]
        for _ in range(100)
    ]

    for generation in range(2000):

        handle_quit()

        population.sort(
            key=lambda x: fitness(x),
            reverse=True
        )

        best = population[0]

        apply_solution(best)

        draw_board()

        pygame.time.delay(30)

        if fitness(best) == 0:

            print("Solution Found!")

            return

        new_population = population[:20]

        while len(new_population) < 100:

            parent1 = random.choice(population[:30])
            parent2 = random.choice(population[:30])

            child = crossover(parent1, parent2)

            child = mutate(child)

            new_population.append(child)

        population = new_population

    print("No Solution")

def clear_board():

    global board

    board = [[0 for _ in range(N)] for _ in range(N)]

def handle_quit():

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

def place_queen(mouse_pos):

    x = mouse_pos[0] // SIZE
    y = mouse_pos[1] // SIZE

    board[y][x] ^= 1

while True:

    draw_board()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

       
        if event.type == pygame.MOUSEBUTTONDOWN:

            if mode == "PLAY":
                place_queen(pygame.mouse.get_pos())

        
        if event.type == pygame.KEYDOWN:

           
            if event.key == pygame.K_r:

                clear_board()
                mode = "PLAY"

           
            elif event.key == pygame.K_1:

                clear_board()

                mode = "BACKTRACKING"

                backtracking()

            
            elif event.key == pygame.K_2:

                clear_board()

                mode = "GENETIC"

                genetic()

            
            elif event.key == pygame.K_3:

                clear_board()

                mode = "DFS"

                dfs()

            
            elif event.key == pygame.K_0:

                clear_board()

                mode = "PLAY"

    clock.tick(60)