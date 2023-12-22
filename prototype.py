import tkinter as tk
from tkinter import ttk
from turtle import *

speed(0)
bgcolor("skyblue")

# Grass
penup()
goto(-400, -100)
pendown()
color("limegreen")
begin_fill()
for i in range(2):
    forward(800)
    right(90)
    forward(400)
    right(90)
end_fill()

# Left Mountain
penup()
goto(-400, -100)
pendown()
color("dimgray")
begin_fill()
for i in range(3):
    forward(300)
    left(120)
end_fill()

# Right Mountain
penup()
goto(100, -100)
pendown()
begin_fill()
for i in range(3):
    forward(300)
    left(120)
end_fill()

# Middle Mountain
penup()
goto(-160, -100)
pendown()
color("gray")
begin_fill()
for i in range(3):
    forward(400)
    left(120)
end_fill()

# Middle Mountain Ice Cap
penup()
goto(-35, 120)
pendown()
color("white")
begin_fill()
left(35)
forward(60)
right(90)
forward(30)
left(100)
forward(45)
right(85)
forward(65)
left(160)
forward(150)
end_fill()

# Left Mountain Ice Cap
penup()
goto(-215, 100)
pendown()
color("snow")
begin_fill()
forward(70)
left(120)
forward(75)
left(150)
forward(45)
right(90)
forward(45)
left(120)
end_fill()

# Right Mountain Ice Cap
penup()
goto(203, 80)
pendown()
begin_fill()
forward(95)
right(120)
forward(80)
right(150)
forward(50)
left(70)
end_fill()

left(50)

# Sun
penup()
goto(-500, 350)
pendown()
color("yellow")
begin_fill()
circle(125)
end_fill()


# Tree Function
def tree():
    # Tree trunk
    color("saddlebrown")
    begin_fill()
    for i in range(2):
        forward(40)
        left(90)
        forward(10)
        left(90)
    end_fill()

    # Turn the turtle around
    forward(10)
    left(90)
    forward(5)

    # Leaves on tree
    color("forestgreen")
    begin_fill()
    circle(25)
    end_fill()

    right(90)


# Plant the first tree
penup()
goto(-25, -200)
pendown()
tree()

# Plant the second tree
penup()
goto(200, -150)
pendown()
tree()

# Plant the third tree
penup()
goto(300, -250)
pendown()
tree()

# Plant the fourth tree
penup()
goto(-300, -250)
pendown()
tree()

# Plant the fifth tree
penup()
goto(-200, -100)
pendown()
tree()


# Function to draw a square with a triangle roof
def draw_square_with_roof(size):
    color("brown")
    begin_fill()

    # Draw square
    for _ in range(2):
        forward(size)
        right(90)

    # Draw triangle roof
    color("red")  # Change the roof color if needed
    begin_fill()
    forward(size / 2)
    left(45)
    forward(size / 2)
    left(90)
    forward(size / 2)
    left(45)
    forward(size / 2)
    end_fill()

    end_fill()


# Draw first square with roof
color("brown")
penup()
goto(-150, -190)
pendown()
draw_square_with_roof(60)

# Draw second square with roof
penup()
goto(80, -300)
pendown()
draw_square_with_roof(70)

# Draw third square with roof
penup()
goto(-295, -90)
pendown()
draw_square_with_roof(40)

# Draw fourth square with roof
penup()
goto(100, -80)
pendown()
draw_square_with_roof(40)

# Connect each house with a line
penup()
goto(-150, -190)
pendown()
color("white")  # Change the connecting line color to white
goto(-295, -90)
pendown()
goto(100, -80)
pendown()
goto(80, -300)
pendown()
goto(-150, -190)
pendown()
goto(100, -80)
pendown()

penup()
goto(-295, -90)
pendown()
goto(100, -80)


def draw_button(x, y, label):
    penup()
    goto(x, y)
    pendown()
    color("white")
    begin_fill()
    for _ in range(4):
        forward(80)
        right(90)
    end_fill()
    color("black")
    write(label, align="center", font=("Arial", 12, "normal"))


# Function to create a separate dashboard window
def create_dashboard():
    dashboard_window = tk.Tk()
    dashboard_window.title("Energy Type Selector")

    energy_label = ttk.Label(dashboard_window, text="Select Energy Type:")
    energy_label.pack(pady=10)

    energy_types = ["Solar", "Wind", "Water"]
    selected_energy = tk.StringVar()
    energy_dropdown = ttk.Combobox(
        dashboard_window, textvariable=selected_energy, values=energy_types
    )
    energy_dropdown.pack(pady=10)

    def update_energy_type():
        selected_type = selected_energy.get()
        # Implement logic to update the energy type based on the selection

    update_button = ttk.Button(
        dashboard_window, text="Update Energy Type", command=update_energy_type
    )
    update_button.pack(pady=20)

    dashboard_window.mainloop()


# Call the function to create the dashboard window
create_dashboard()

hideturtle()
done()
