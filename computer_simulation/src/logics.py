def check_collision(left_corner_position, width, height, point_position) -> bool:
    x, y = point_position
    corner_x, corner_y = left_corner_position
    if (
        x >= corner_x
        and x <= corner_x + width
        and y >= corner_y
        and y <= corner_y + height
    ):
        return True
    return False
