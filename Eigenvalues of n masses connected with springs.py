# libraries
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
import pygame
from sys import exit

# boundary conditions
k = 4 # stiffness of spring
m = 1 # mass of block
boundaries = np.array([2,0.2,1,0.5,1])
k_m = np.sqrt(k/m) #angular frequency

def matrix_oscillation(n):

    matrix = np.zeros((n,n))

    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                if i == 0:
                    matrix[i,j] = 2
                    matrix[i,j+1] = -1
                elif i == n-1:
                    matrix[i,j-1] = -1
                    matrix[i,j] = 2
                else:
                    matrix[i, j - 1] = -1
                    matrix[i, j] = 2
                    matrix[i, j + 1] = -1

    return matrix

def eigenvaluefinder(matrix):

    w, v = LA.eig(matrix)
    return w, v


matrix = matrix_oscillation(len(boundaries))
eigenvals, eigenvector = eigenvaluefinder(matrix)


def equation_system(eigenvals, eigenvector,boundaries): #solving the matrix equation Ac = b where b is our boundary conditions

    inv_eigen = np.linalg.inv(eigenvector)
    constants = inv_eigen.dot(boundaries)

    return constants

constants = equation_system(eigenvals, eigenvector, boundaries)

def graph(eigenvals, eigenvector, constants):

    dt = 0.001
    ts = np.arange(0, 10, dt)
    ys = []

    # creating the arrays of displacement for each block
    for i in range(0, len(boundaries)):
        arr = []
        for m in range(0, len(ts)):
            sum = 0
            t = ts[m]
            for k in range(0,len(boundaries)):
                sum += constants[k]*eigenvector[i,k]*np.cos(np.sqrt(eigenvals[k])*k_m*t)
            arr.append(sum)
        ys.append(arr)

    # plotting the displacement of each block wrt time
    for i in range(0, len(ys)):
        plt.plot(ts, ys[i], label = "Mass number {}".format(i+1))
    plt.xlabel("Time")
    plt.ylabel("Displacement")
    plt.legend()
    plt.show()

    return ys, len(ts)

ys, lt = graph(eigenvals, eigenvector, constants)

#pygame code for simulation

#prestuff
pygame.init()
screen = pygame.display.set_mode((800+50*len(boundaries)+50*max(ys[len(boundaries)-1]),400))
pygame.display.set_caption("Mass-spring system")
clock = pygame.time.Clock()

# surfaces
test_surface = pygame.Surface((50,50))
surfaces = [test_surface for i in range(0, len(boundaries))]
test_surface.fill('brown')

#pictures and fonts
picture = pygame.image.load('floor.jpg')
picture = pygame.transform.scale(picture, (800+50*len(boundaries)+50*max(ys[len(boundaries)-1]), 400))
font = pygame.font.SysFont('arial', 40)
largeText = font.render("COUPLED MASS-SPRING SYSTEM", True, (0,0,0))

# simulation
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    for j in range(0, lt):
        screen.blit(picture, (0, 0))
        screen.blit(largeText,((800+50*len(boundaries)+50*max(ys[len(boundaries)-1]))/2-300,100))
        for i in range(0,len(boundaries)):
            screen.blit(surfaces[i], (50 + (800+50*len(boundaries))/(len(boundaries))*i +
                                      50*ys[i][j], 175))
            pygame.draw.line(screen, (0, 0, 0), (0, 200),
                             (50 + 50 * ys[0][j], 200))
            pygame.draw.line(screen, (0, 0, 0), (
            50 + (800+50*len(boundaries))/(len(boundaries)) *
            (len(boundaries) - 1) + 50 * ys[len(boundaries) - 1][j]+50, 200),
                             (800+50*len(boundaries)+50*max(ys[len(boundaries)-1]), 200))
            if 0< i:
                pygame.draw.line(screen, (0,0,0),
                                 ((800+50*len(boundaries))/(len(boundaries))*(i-1) + 50*ys[i-1][j]+100, 200), ((800+50*len(boundaries))/(len(boundaries))*i + 50*ys[i][j]+50, 200))
        pygame.display.update()
        screen.fill((225, 225, 225))

    clock.tick(60)
