import taichi as ti

ti.init(arch=ti.gpu)

# ti.init(debug=True, arch=ti.cpu)


n = 320
pixels = ti.field(dtype=ti.f32, shape=(n*2, n))


@ti.func
def complex_sqr(z):
    return ti.Vector([z[0]**2 - z[1]**2, z[1]*z[0]*2])


@ti.kernel
def paint(t: ti.f32):
    for i, j in pixels:
        c = ti.Vector([-0.8, ti.cos(t) * 0.2])
        z = ti.Vector([i / n - 1, j / n - 0.5]) * 2
        iterations = 0
        while z.norm() < 20 and iterations < 50:
            z = complex_sqr(z) + c
            iterations += 1
        pixels[i, j] = 1 - iterations * 0.02


gui = ti.GUI("Julia Set", res=(n * 2, n))

for i in range(1000000):
    paint(i * 0.03)
    gui.set_image(pixels)

    filename = f'./out_image/frame_{i:05d}.png'
    gui.show(filename)


"""
atomic action

example: 
    total[None] += x[i]
    
    ti.atomic_add(total[None],x[i])  -> return the previous value
    
    wrong：
        total[None] = total[None] + x[i]  
        
out-mp4: ti video -f40
convert to gif 
"""



