import taichi as ti
from particle_system import ParticleSystem
from wcsph import WCSPHSolver

# ti.init(arch=ti.cpu)
ti.init(arch=ti.gpu)

if __name__ == "__main__":
    ps = ParticleSystem((512, 512))

    ps.add_cube(lower_corner=[6, 2],
                cube_size=[3.0, 5.0],
                velocity=[-5.0, -10.0],
                density=1000.0,
                color=0x0000FF,
                material=1)

    # ps.add_cube(lower_corner=[3, 1],
    #             cube_size=[2.0, 6.0],
    #             velocity=[0.0, -20.0],
    #             density=1000.0,
    #             color=0x956333,
    #             material=1)

    h = ps.support_radius
    # add boundary particle
    ps.add_cube(lower_corner=[0, 0],
                cube_size=[h, ps.bound[1]],
                velocity=[0.0, 0.0],
                density=1000.0,
                material=0,
                color=0x000000
                )

    ps.add_cube(lower_corner=[h, 0],
                cube_size=[ps.bound[1]-h, h],
                velocity=[0.0, 0.0],
                density=1000.0,
                material=0,
                color=0x000000
                )

    ps.add_cube(lower_corner=[ps.bound[1]-h, h],
                cube_size=[h, ps.bound[1]-h],
                velocity=[0.0, 0.0],
                density=1000.0,
                material=0,
                color=0x000000
                )

    wcsph_solver = WCSPHSolver(ps)
    gui = ti.GUI(background_color=0xFFFFFF)

    iterations = 0
    while gui.running:
        for i in range(5):
            wcsph_solver.step()
        particle_info = ps.dump()
        gui.circles(particle_info['position'] * ps.screen_to_world_ratio / 512,
                    radius=ps.particle_radius / 1.5 * ps.screen_to_world_ratio,
                    color=particle_info['color'])


        # filename = f'./out_image/frame_{iterations:05d}.png'
        # gui.show(filename)
        # iterations += 1
        gui.show()
