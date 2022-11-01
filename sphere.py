import logging
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

def sphere(x):
    """NumPy sphere test function"""
    return -np.sum(x**2, axis=0)

N_POINTS = 200
r = np.linspace(-5, 5, N_POINTS)

x = np.array(np.meshgrid(r, r))
z = sphere(x)
plt.figure(figsize=(10, 10))
ax = plt.axes(projection="3d")
ax.plot_surface(*np.meshgrid(r, r), z, rstride=1, cstride=1, cmap=cm.plasma, linewidth=0, antialiased=False)
plt.savefig("sphere.png")


# inizializza un punto randomico che è almeno nel dominio della sfera 
# stabilisci un tempo massimo di simulazione
# fagli fare dei movimenti randomici inizialmente con un passo abbastanza alto
# se sono possibili vai avanti altrimenti torna indietro
# se la sfera generata dalle nuove coordinate è minore di quella prima salvata come top
# aggiorna la variabile top e inizia a muoverti da lì
# aumenta sempre il tempo
# quando esce da questo ciclo while 
# fallo entrare in un altro in cui valuti la z della sfera
# fin quando i movimenti sono ammissibili 
# controlla la z della sfera che ottieni e quella della sfera(top)
# se la z nuova è minore della sfera(top)
# aggiorna top

np.random.seed(42)

x = np.random.uniform(-5,5)
y = np.random.uniform(-5,5)
first_point = np.array([x,y])
top = first_point
z = sphere(top)

print(z)
time = 0
while time < 250:
    check = False
    while check == False:
        x1, y1 = np.random.uniform(-2,2), np.random.uniform(-2,2)
        move = np.array([x1,y1])
        movement = top + move 
        if movement[0] > -5 and movement[1] < 5:
            check = True
    if sphere(top) < sphere(movement):
        top = movement
    time = time + 1

print(f"z = {sphere(top)}\ntime: {time}")


