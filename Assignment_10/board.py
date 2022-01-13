import arcade


#configuration

X_RESULOTION=1080
Y_RESULOTION=720
COLUMN_SPACING = 60
ROW_SPACING = 60
RIGHT_MARGIN = 230
TOP_MARGIN = 230
LEFT_MARGIN = X_RESULOTION//2-RIGHT_MARGIN
BOTTOM_MARGIN = Y_RESULOTION//2-TOP_MARGIN

arcade.open_window(X_RESULOTION, Y_RESULOTION, "chess")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()


for row in range(8):
    for column in range(8):
        x = column * COLUMN_SPACING + LEFT_MARGIN 
        y = row * ROW_SPACING + BOTTOM_MARGIN 
        if (row+column)%2==0:
            arcade.draw_rectangle_filled(x, y, 30,30, arcade.color.RED,45)
        else:
            arcade.draw_rectangle_filled(x, y, 30,30, arcade.color.BLUE,45)

arcade.finish_render()
arcade.run()