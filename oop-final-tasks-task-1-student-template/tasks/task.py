class Sun:
    _instance = None

    def __init__(self):
        if Sun._instance is not None:
            raise Exception("Sun instance already exists!")
        Sun._instance = self

    @staticmethod
    def inst():
        if Sun._instance is None:
            Sun._instance = Sun()
        return Sun._instance


p = Sun.inst()
f = Sun.inst()
print(p is f)