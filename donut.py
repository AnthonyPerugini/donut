#! /home/spicy/miniconda3/envs/donut/bin/python
import numpy as np
from collections import defaultdict

SCREEN_WIDTH, SCREEN_HEIGHT = 50, 50
A_SPEED = 0.07
B_SPEED = 0.02

R1, R2 = 1, 2
K2 = 5
K1 = SCREEN_WIDTH * K2 * 3 / (8 * (R1 + R2))

THETA_SPACING = 150
PHI_SPACING = 150
TWO_PI = round(2 * np.pi, 2)

def main():

    A = B = 1
    running = True
    while running:
        sinA, cosA = np.sin(A), np.cos(A)
        sinB, cosB = np.sin(B), np.cos(B)
        render_torus(sinA, cosA, sinB, cosB)
        A += A_SPEED
        B += B_SPEED


def render_torus(sinA, cosA, sinB, cosB):

    zbuff = np.zeros((SCREEN_WIDTH, SCREEN_HEIGHT))
    output = np.full((SCREEN_WIDTH, SCREEN_HEIGHT), ' ')

    for theta in np.linspace(0, TWO_PI, THETA_SPACING):

        sintheta, costheta = np.sin(theta), np.cos(theta)

        x_org = R2 + (R1 * costheta)
        y_org = R1 * sintheta
        
        for phi in np.linspace(0, TWO_PI, PHI_SPACING):

            sinphi, cosphi = np.sin(phi), np.cos(phi)

            # rotation matrixes
            # rot_Y = np.array([[cosphi, 0, sinphi], [0, 1, 0], [-sinphi, 0, cosphi]])
            # rot_A = np.array([[1, 0, 0], [0, cosA, sinA], [0, -sinA, cosA]])
            # rot_B = np.array([[cosB, sinB, 0], [-sinB, cosB, 0], [0, 0, 1]])

            # x, y, z = (x_org, y_org, 0) @ rot_Y @ rot_A @ rot_B


            # simplified xyz calculations above via wolfram
            x = x_org * (cosB * cosphi + sinA * sinB * sinphi) - (y_org * cosA * sinB)
            y = x_org * (cosphi * sinB - cosB * sinA * sinphi) + (y_org * cosA * cosB)
            z = K2 + (cosA * x_org * sinphi) + (y_org * sinA)
            ooz = 1 / z

            # x and y positions on screen
            xp = int((SCREEN_WIDTH / 2) + (K1 * x * ooz))
            yp = int((SCREEN_HEIGHT / 2) - (K1 * y * ooz))


            # lumanance calculation (Nx, Ny, Nz) @ (light direction)
            # N = np.array([costheta, sintheta, 0]) @ rot_Y @ rot_A @ rot_B
            # L = N @ np.array([0, 1, -1])

            # simplified lumanance calc via wolfram
            L = (cosphi * costheta * sinB) - (cosA * costheta * sinphi) - (sinA * sintheta) + \
                 cosB * ((cosA * sintheta) - (costheta * sinA * sinphi))

            if (L > 0):
                if ooz > zbuff[yp][xp]:
                    zbuff[yp][xp] = ooz
                    index = int(L * 8)
                    output[yp][xp] = ".,-~:;=!*#$@"[index]


    # return cursor to start of line
    print("\x1b[H")

    for col in output:
        for value in col:
            print(value, end=" ")
        print()
 

if __name__ == '__main__':
    main()
