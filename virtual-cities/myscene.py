"""
Virtual Cities!

Instructions and Documentation:
https://gist.github.com/mrsharp-milken/21c48a631c51849a83bf6f05ea9c8b86
"""

from Scene3D import Scene3D

def main():
    scene = Scene3D()

    setup_lights(scene)
    setup_cameras(scene)
    add_ground(scene)

    # Draw three snowmen in different places


    # TODO (Task 1): call draw_tree to plant a tree. Remember to pass scene first!
    draw_tree(scene, -10, -10, 10)
    draw_tree(scene, 0, -12, 10)
    draw_tree(scene, 10, -14, 10)
    draw_tree(scene, 20, -16, 10)
    draw_tree(scene, 30, -18, 10)
    draw_tree(scene, 40, -20, 10)

    add_mountains(scene, 20, -20, 100)



    scene.save_scene("myscene.html", "Nightwing Kingdom")

# Task 1: finish this function (delete "pass" once you add your code)
def draw_tree(scene, cx, cz, height):
    # TODO: draw a brown cylinder for the trunk
    scene.add_cylinder(cx, height/2, cz, 0.5, height, 102, 51, 0)


    # TODO: draw a green ellipsoid for the leaves
    scene.add_ellipsoid(cx, height, cz, 1, 2, 1, 0, 255, 0)
    pass

# Task 2 and beyond: define your own functions!


# All functions need "scene" as the first parameter
# cx and cz say where the snowman's center goes

def setup_lights(scene):
    scene.add_point_light(-100, 200, 0, 200, 200, 200, 1.0)
    scene.add_point_light(100, 200, 0, 200, 200, 200, 1.0)
    scene.add_point_light(0, 0, -100, 200, 200, 200, 1.0)
    scene.add_point_light(0, 0, 100, 200, 200, 200, 1.0)

def setup_cameras(scene):
    scene.add_camera(0, 2, 0, 0)
    scene.add_camera(0, 2, -40, 180)

def add_ground(scene):
    # Add a large gray box for the ground
    scene.add_box(0, -25, 0, 1000, 50, 1000, 0, 100, 0)
    scene.add_box(0, 500, 0, 1000, 10, 1000, 4, 4, 38)
    scene.add_box(0, 250, 500, 1000, 500, 10, 4, 4, 38)
    scene.add_box(0, -25, -500, 1000, 1050, 10, 4, 4, 38)
    scene.add_box(500, -25, 0, 10, 1050, 2000, 4, 4, 38)
    scene.add_box(-500, -25, 0, 10, 1050, 2000, 4, 4, 38)

def add_mountains(scene, cx, cz, height):
    scene.add_cone(4, 0, 0, 20, 50, 0, 0, 255)

def add_meshes(scene):
    scene.add_mesh("meshes/cow.obj", 1, 1, -7, 0, 0, 0, 1, 1, 1, 0, 255, 255)
    scene.add_textured_mesh("meshes/smokestack/medres.obj", "meshes/smokestack/medres.mtl",
                            0, 18, -20, 0, 180, 0, 10, 10, 10, 0)

main()
