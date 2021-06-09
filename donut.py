#! /home/spicy/miniconda3/envs/donut/bin/python
import numpy as np
from collections import defaultdict

SCREEN_WIDTH, SCREEN_HEIGHT = 50, 50
A_SPEED = 0.07
B_SPEED = 0.02

R1, R2 = 1, 2
K2 = 5
K1 = SCREEN_WIDTH*K2*3/(8*(R1+R2))

THETA_SPACING = 150
PHI_SPACING = 150
TWO_PI = round(2 * np.pi, 2)

theta_sin_memo = defaultdict(int)
theta_cos_memo = defaultdict(int)
phi_sin_memo = defaultdict(int)
phi_cos_memo = defaultdict(int)

def main():

    A = B = 1
    while 1:
        sinA, cosA = np.sin(A), np.cos(A)
        sinB, cosB = np.sin(B), np.cos(B)
        render_torus(sinA, cosA, sinB, cosB)
        A += A_SPEED
        B += B_SPEED


def render_torus(sinA, cosA, sinB, cosB):
    zbuff = np.zeros((SCREEN_WIDTH, SCREEN_HEIGHT))
    output = np.full((SCREEN_WIDTH, SCREEN_HEIGHT), ' ')

    for theta in np.linspace(0, TWO_PI, THETA_SPACING): # np.arange(0, 6.28, THETASPACING):

        if not theta_sin_memo[theta]:
            theta_sin_memo[theta] = np.sin(theta)
        if not theta_cos_memo[theta]:
            theta_cos_memo[theta] = np.cos(theta)
            
        sintheta, costheta = theta_sin_memo[theta], theta_cos_memo[theta]

        x_org = R2 + (R1 * costheta)
        y_org = R1 * sintheta
        
        for phi in np.linspace(0, TWO_PI, PHI_SPACING): # np.arange(0, 6.28, PHI_SPACING):

            if not phi_sin_memo[theta]:
                phi_sin_memo[phi] = np.sin(phi)
            if not phi_cos_memo[theta]:
                phi_cos_memo[phi] = np.cos(phi)

            sinphi, cosphi = phi_sin_memo[phi], phi_cos_memo[phi]

            # rot_Y = np.array([[cosphi, 0, sinphi], [0, 1, 0], [-sinphi, 0, cosphi]])
            # rot_A = np.array([[1, 0, 0], [0, cosA, sinA], [0, -sinA, cosA]])
            # rot_B = np.array([[cosB, sinB, 0], [-sinB, cosB, 0], [0, 0, 1]])
            # x, y, z = (x_org, y_org, 0) @ rot_Y @ rot_A @ rot_B


            # simplified xyz calculations via wolfram
            x = x_org*(cosB*cosphi + sinA*sinB*sinphi) - (y_org*cosA*sinB)
            y = x_org*(cosphi*sinB - cosB*sinA*sinphi) + (y_org*cosA*cosB)
            z = K2 + (cosA*x_org*sinphi) + (y_org*sinA)
            ooz = 1/z

            xp = int((SCREEN_WIDTH/2) + (K1*x*ooz))
            yp = int((SCREEN_HEIGHT/2) - (K1*y*ooz))



            # lumanance calculation (Nx, Ny, Nz) @ (light direction)
            # N = np.array([costheta, sintheta, 0]) @ rot_Y @ rot_A @ rot_B
            # L = N @ np.array([0, 1, -1])

            # simplified lumanance calc via wolfram
            L = (cosphi*costheta*sinB) - (cosA*costheta*sinphi) - (sinA*sintheta) + cosB*((cosA*sintheta) - (costheta*sinA*sinphi))

            if (L > 0):
                if (ooz > zbuff[yp][xp]):
                    zbuff[yp][xp] = ooz
                    index = int(L * 8)
                    output[yp][xp] = ".,-~:;=!*#$@"[index]

    print("\x1b[H")
    for col in output:
        for value in col:
            print(value, end=" ")
        print()
 

if __name__ == '__main__':
    main()
