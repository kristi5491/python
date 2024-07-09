import os


class Cd:
    def __init__(self, desire_direct):
        self.desire_direct = desire_direct

    def __enter__(self):
        self.initial_dir = os.getcwd()
        if not os.path.isabs(self.desire_direct):
            self.desired_dir = os.path.join(self.initial_dir, self.desire_direct[1:])
        if os.path.isdir(self.desire_direct):
            os.chdir(self.desire_direct)
            print(f"Entering the context: {self.desire_direct}")
        else:
            os.chdir(self.initial_dir)
            self.desire_direct = self.initial_dir
            raise ValueError(f"Directory '{self.desire_direct}' does not exist.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.initial_dir)
        print(f"Exiting the context and returning to {self.initial_dir}")


try:
    with Cd('/hjg'):
        print(f"Inside the context: {os.getcwd()}")
except Exception as e:
    print(f"An error occurred: {e}")