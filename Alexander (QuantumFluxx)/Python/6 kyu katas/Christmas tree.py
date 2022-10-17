def christmas_tree(height):
    stars = [i for i in range(1, height*2+1, 2)]
    return "\n".join([("*"*star).center(stars[-1]) for star in stars])