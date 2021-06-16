import tkinter as tk
from random import randint

def main():

    width = 800
    height = 500

    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()
   
def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):

    # sets the background, including sky, ground, and road
    draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom)

    # makes the clouds
    draw_cloud(canvas, scene_left - 90, scene_top + 20, 120)
    draw_cloud(canvas, scene_left + 300, scene_top + 40, 120)
    draw_cloud(canvas, scene_left + 500, scene_top + 40, 80)
    draw_cloud(canvas, scene_left + 270, scene_top + 10, 40)
    draw_cloud(canvas, scene_left + 700, scene_top, 80)

    # draws the mountains
    draw_mountain(canvas, scene_left, scene_top + 120, scene_top, scene_bottom)
    draw_mountain(canvas, scene_left + 300, scene_top + 100, scene_top, scene_bottom)

    # draws the ground, then the road on top
    draw_ground(canvas, scene_left, scene_top, scene_right, scene_bottom)
    draw_road(canvas, scene_left, scene_top, scene_right, scene_bottom)

    # makes random seagulls (the final number is the quantity)
    draw_seagull(canvas, scene_left, scene_top, scene_right, scene_bottom, 3)

    # makes the forest
    draw_pine_tree(canvas, scene_left + 650, scene_top + 110, 150)
    draw_pine_tree(canvas, scene_left + 500, scene_top + 120, 150)
    draw_pine_tree(canvas, scene_left + 650, scene_top + 200, 100)
    draw_pine_tree(canvas, scene_left + 450, scene_top + 160, 125)
    draw_pine_tree(canvas, scene_left + 550, scene_top + 110, 200)
    draw_pine_tree(canvas, scene_left + 680, scene_top + 140, 210)
    draw_pine_tree(canvas, scene_left - 15, scene_top + 120, 250)


# draws the sky in the top half of the canvas
def draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom):

    sky_bottom = scene_top + scene_bottom / 2
    canvas.create_rectangle(scene_left, scene_top,
            scene_right, sky_bottom,
            width=0, fill="lightSkyBlue")

# draws two overlapping mountain shapes
def draw_mountain(canvas, peak_x, peak_y, scene_top, scene_bottom):

    horizon = scene_top + scene_bottom / 2
    height = horizon - peak_y
    width = height * 3

    # draws one mountain shape
    def draw_half_mountain(canvas, peak_x, peak_y, width, height, horizon, color):
        canvas.create_polygon(peak_x, horizon,
                peak_x + 1/3 * width, peak_y + 1/5 * height,
                peak_x + 2/5 * width, peak_y + 3/10 * height,
                peak_x + 1/2 * width, peak_y,
                peak_x + 3/5 * width, peak_y + 7/20 * height,
                peak_x + 3/4 * width, peak_y + 1/2 * height,
                peak_x + 4/5 * width, peak_y + 2/5 * height,
                peak_x + width, horizon,
                outline="gray20", width=1, fill=color)

    # draws both shapes, creating the whole mountain
    draw_half_mountain(canvas, peak_x, peak_y, width, height, horizon, "gray50")
    draw_half_mountain(canvas, peak_x, peak_y + 20, width, height, horizon + 20, "gray70")

# draws the ground in the bottom half of the canvas
def draw_ground(canvas, scene_left, scene_top, scene_right, scene_bottom):

    horizon = round(scene_top + scene_bottom / 2)
    canvas.create_rectangle(scene_left, horizon,
            scene_right, scene_bottom,
            width=1, fill="khaki")

    # scatters different colored sand grains on the ground
    def draw_sand(canvas, scene_left, scene_top, scene_right, scene_bottom, color):
        for _ in range(5000):
            x = randint(scene_left, scene_right)
            y = randint(horizon + 1, scene_bottom)
            canvas.create_rectangle(x, y, x + 3, y + 3, width=0, fill=color)

    # repeats the sand function with various sand colors
    draw_sand(canvas, scene_left, scene_top, scene_right, scene_bottom, "khaki3")
    draw_sand(canvas, scene_left, scene_top, scene_right, scene_bottom, "lightGoldenRod1")
    draw_sand(canvas, scene_left, scene_top, scene_right, scene_bottom, "gold2")
    draw_sand(canvas, scene_left, scene_top, scene_right, scene_bottom, "khaki2")
    draw_sand(canvas, scene_left, scene_top, scene_right, scene_bottom, "goldenrod1")
    draw_sand(canvas, scene_left, scene_top, scene_right, scene_bottom, "lightGoldenRod2")
    draw_sand(canvas, scene_left, scene_top, scene_right, scene_bottom, "lightGoldenRod3")


# draws the road, which starts in the bottom right and ends almost dead center in the screen
def draw_road(canvas, scene_left, scene_top, scene_right, scene_bottom):

    horizon = scene_top + scene_bottom / 2
    point_a = (scene_left + 9/20 * scene_right, horizon)
    point_b = (scene_left + 1/2 * scene_right, horizon)
    point_c = (scene_left + 9/10 * scene_right, scene_bottom)
    point_d = (scene_left + 11/20 * scene_right, scene_bottom)

    # draws the road itself
    canvas.create_polygon(point_a, point_b, point_c, point_d,
            outline="gray20", width=1, fill="gray64")

    # draws the dotted line in the center of the road
    canvas.create_line(scene_left + 19/40 * scene_right + 6, horizon + 6,
            scene_left + 29/40 * scene_right, scene_bottom,
            dash=(12,20,25,30,35,40,48,60,100,100), width=3, fill="yellow")

# draw a single cloud, the x and y coordinates will be the top left corner
# size is proportionate to height
def draw_cloud(canvas, peak_x, peak_y, height):

    width = 2.5 * height 

    # defines the location of each part of the cloud
    base_left = peak_x
    base_top = peak_y + height / 2
    base_right = peak_x + width
    base_bottom = peak_y + height

    top_left = peak_x + width / 5
    top_top = peak_y
    top_right = peak_x + 3/5 * width
    top_bottom = peak_y + height

    right_left = peak_x + width / 2
    right_top = peak_y + height / 5
    right_right = peak_x + 4/5 * width
    right_bottom = peak_y + 9/10 * height

    left_left = peak_x + width / 16
    left_top = peak_y + 5/13 * height
    left_right = peak_x + width / 4
    left_bottom = peak_y + 11/13 * height

    canvas.create_oval(base_left, base_top,
            base_right, base_bottom,
            outline="gray20", width=0, fill="white")
    
    canvas.create_oval(top_left, top_top,
            top_right, top_bottom,
            outline="gray20", width=0, fill="white")
    
    canvas.create_oval(right_left, right_top,
            right_right, right_bottom,
            outline="gray20", width=0, fill="white")

    canvas.create_oval(left_left, left_top,
            left_right, left_bottom,
            outline="gray20", width=0, fill="white")

# draws a pine tree in the specified location
# size is proportionate to height
def draw_pine_tree(canvas, peak_x, peak_y, height):

    width = 4/5 * height

    def draw_skirt(canvas, peak_x, peak_y, width, height):
        
        # draws each branch of the skirt
        def draw_skirt_branch(canvas, peak_x, peak_y, width, height, branch_width, color):
            point_a = (peak_x + width / 2, peak_y)
            point_b = (peak_x + width / 2 + branch_width / 2, peak_y + height)
            point_c = (peak_x + width / 2, peak_y + 4/5 * height)
            point_d = (peak_x + width / 2 - branch_width / 2, peak_y + height)

            canvas.create_polygon(point_a, point_b,
                    point_c, point_d, fill=color)

        # calls the branch function to create the whole skirt
        draw_skirt_branch(canvas, peak_x, peak_y, width, height, width, "darkGreen")
        draw_skirt_branch(canvas, peak_x, peak_y, width, height, 5/7 * width, "green")
        draw_skirt_branch(canvas, peak_x, peak_y, width, height, 3/7 * width, "green4")
        draw_skirt_branch(canvas, peak_x, peak_y, width, height, 1/7 * width, "green3")

    # draws the trunk
    canvas.create_rectangle(peak_x + 13/28 * width, peak_y + 2/3 * height,
            peak_x + 15/28 * width, peak_y + height,
            outline="gray20", width=0, fill="saddleBrown")

    # calls the skirt function to create the whole tree
    draw_skirt(canvas, peak_x, peak_y + 3/5 * height, width, 1/3 * height)
    draw_skirt(canvas, peak_x + 1/14 * width, peak_y + 9/20 * height, 6/7 * width, 3/10 * height)
    draw_skirt(canvas, peak_x + 2/14 * width, peak_y + 1/3 * height, 5/7 * width, 1/4 * height)
    draw_skirt(canvas, peak_x + 3/14 * width, peak_y + 1/4 * height, 4/7 * width, 1/5 * height)
    draw_skirt(canvas, peak_x + 4/14 * width, peak_y + 2/15 * height, 3/7 * width, 1/5 * height)
    draw_skirt(canvas, peak_x + 5/14 * width, peak_y, 2/7 * width, 1/5 * height)

# makes a seagull out of two arcs, randomly placed, of the specified quantity
def draw_seagull(canvas, scene_left, scene_top, scene_right, scene_bottom, quantity):
    
    for _ in range(0, quantity):
        peak_x = randint(20, scene_right - 100)
        peak_y = randint(20, int(scene_top + scene_bottom / 2 - 110))

        canvas.create_arc(peak_x, peak_y,
                peak_x + 53, peak_y + 100, style=tk.ARC, start=+45, width=2)
        canvas.create_arc(peak_x + 37, peak_y + 100,
                peak_x + 90, peak_y, style=tk.ARC, start=+45, width=2)

# calls all the functions listed above
main()