import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
from scipy.special import lpmv
import streamlit as st

st.title("Harmoniques Sphériques")

def slider():
    n = st.slider('l',1,5,3)
    return n

def slider2():
    n = st.slider('r',1,5,3)
    return n

def slider3():
    n = st.slider('Complexe/Réel',0,1,1)
    return n

N1 = slider()
N2 = slider2()
N3 = slider3()





theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)

theta, phi = np.meshgrid(theta, phi)

xyz = np.array([np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta)])

def SimuSphHarm (ax, l, m, ri):

    
            
    
    def shr (m, l, phi, theta):
 #Définition des HS réelles        
        A = (2*l) / (4*np.pi)
        b = l - np.abs(m)
        B = factorial(b)
        c = l + np.abs(m)
        C = factorial(c)
        D = lpmv(m, l, np.cos(theta))
        E = np.cos( m * phi )
        H = (-1)**m
        G = H*(np.sqrt(2) * np.sqrt( A * (B/C)) * D * E)
        return G
#Définition des HS imaginaires  
    def shc (m, l, phi, theta):
         
        A = (2*l) / (4*np.pi)
        b = l - np.abs(m)
        B = factorial(b)
        c = l + np.abs(m)
        C = factorial(c)
        D = lpmv(m, l, np.cos(theta))
        E = np.sin( m * phi )
        H = (-1)**m
        G =  H*(np.sqrt(2) * np.sqrt( A * (B/C)) * D * E)
        return G
 #Switch pour obtenir soit la partie réelle ou imaginaire 1 = réel 0  = imaginaire  
    def realimg(ri):
        if ri == 1:
            R = shr (m,l,phi,theta)
        elif ri == 0:
            R = shc (m,l,phi,theta)
        return R
            
    SH = realimg(ri)    
  
    HSx, HSy, HSz = np.abs(SH)*xyz
    
#On colore la surface en fonction du signe de HS, vert = positif et rouge = négatif
    
    cmap = plt.cm.ScalarMappable(cmap=plt.get_cmap('RdYlGn'))
    cmap.set_clim(-0.35, 0.35)
    
    ax.plot_surface(HSx, HSy, HSz,
                    facecolors=cmap.to_rgba(SH),
                    rstride=1, cstride=1)
    
#On trace les axes x, y et z     
    ax_lim = 0.5
    ax.plot([-ax_lim, ax_lim], [0,0], [0,0], c='0.5', lw=1, zorder=10)
    ax.plot([0,0], [-ax_lim, ax_lim], [0,0], c='0.5', lw=1, zorder=10)
    ax.plot([0,0], [0,0], [-ax_lim, ax_lim], c='0.5', lw=1, zorder=10)
    
#Affichafe du titre et suppression du cadre
    
    # ax.set_title("$f_{z^3}$")
    ax_lim = 0.5
    ax.set_xlim(-ax_lim, ax_lim)
    ax.set_ylim(-ax_lim, ax_lim)
    ax.set_zlim(-ax_lim, ax_lim)
    ax.set_xlabel('X ')
    ax.set_ylabel('Y ')
    ax.set_zlabel('Z ')
    ax.axis('off')
    
    
fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(projection='3d')
l, m, ri  = N1 , N2 , N3
SimuSphHarm(ax, l, m, ri)    

st.pyplot(plt)
