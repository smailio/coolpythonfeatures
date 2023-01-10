from context_managers.solutions import Cd, Patch
from os import path
import os
from context_managers import config
from pathlib import Path


def write_in_f(text):
    with open("f", "w+") as f:
        f.write(text)

def write_in_f3(text):
    with open("f3", "w+") as f:
        f.write(text)

def test_cd():
    """
    To make this test pass you'll implement Cd which is a context manager that
    change the working directory, so in a block of code wrapped by Cd
    the current working directory will be the one given to Cd.

    This is how things are done in fabric
    https://github.com/fabric/fabric
    https://docs.fabfile.org/en/1.12.1/api/core/context_managers.html
    """

    # set up the tests
    dir_path = path.dirname(path.realpath(__file__))
    p1_path = path.join(dir_path, "p1")
    p2_path = path.join(dir_path, "p1")
    Path(p1_path).mkdir(parents=True, exist_ok=True)
    Path(p2_path).mkdir(parents=True, exist_ok=True)
    f1_path = path.join(dir_path, "p1", "f")
    f2_path = path.join(dir_path, "p1", "p2", "f")
    f3_path = path.join(dir_path, "p1", "f3")

    if path.exists(f1_path):
        os.remove(f1_path)
    if path.exists(f2_path):
        os.remove(f2_path)

    """
    To implement Cd you can use the getcwd chdir from os module.
    """
    in_p1 = Cd("p1")
    with Cd(dir_path):
        with in_p1:
            write_in_f("hello 1")
            with Cd("p2"):
                write_in_f("hello 2")
            write_in_f3("hello 3")

    """
    If everything went fine a file named f exists in p1 and another 
    file also named f exists in p1.p2
    """
    with open(f1_path, 'r') as f:
        assert f.read() == 'hello 1'
    with open(f2_path, 'r') as f:
        assert f.read() == 'hello 2'
    with open(f3_path, 'r') as f:
        assert f.read() == 'hello 3'


def test_patch():
    """
    To make this test pass you'll implement your own version of the awesome unittest.mock.patch

    Inside the patched block the patched attribute will be evaluate to the provided
    value, once we exit the patched block the attribute will go back to their
    initial state.
    """

    def read_account():
        return f"select * from {config.schema_name}.accounts"

    assert read_account() == "select * from prod_schema.accounts"
    with Patch(config, schema_name="test_schema"):
        assert read_account() == "select * from test_schema.accounts"
    assert read_account() == "select * from prod_schema.accounts"
