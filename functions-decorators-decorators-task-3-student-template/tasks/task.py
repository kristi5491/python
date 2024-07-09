def validate(function):
    '''
    Add corresponded arguments and implementation here. 
    '''

    def wrapper(x, y, z):
        if 0 <= x <= 256 and 0 <= y <= 256 and 0 <= z <= 256:
            return function(x, y, z)
        else:
            return "Function call is not valid!"

    return wrapper


@validate
def set_pixel(x: int, y: int, z: int) -> str:
    print(f"Pixel set at ({x}, {y}, {z}) ")
    return "Pixel created!"


print(set_pixel(0, 127, 300))
print(set_pixel(0, 127, 250))
print(set_pixel(0, 0, 0))