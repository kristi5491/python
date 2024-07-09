import os
import shutil


class TempDir:
    def __enter__(self):
        # Create a directory named "my_new_dir" in the current working directory
        self.initial_dir = os.getcwd()
        self.temp_dir = os.path.join(self.initial_dir, "my_new_dir")
        print(self.temp_dir)
        os.mkdir(self.temp_dir)
        os.chdir(self.temp_dir)
        print(f"Entering the context: {self.temp_dir}")
        return self.temp_dir

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.initial_dir)
        shutil.rmtree(self.temp_dir)
        print(f"Exiting the context and returning to {self.initial_dir}")


with TempDir() as t:
    print("Inside the context")

t = TempDir()
t.__enter__()
t.__exit__(None, None, None)

