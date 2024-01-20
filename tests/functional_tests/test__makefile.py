
import subprocess
from pathlib import Path
from turtle import circle

from tests.fixtures.project_dir import project_dir

"""
generate a project 
linting a project 
     generate project test: assert project_dir.exists()
     test__linting_passes: make lint-ci
     tests__tests_pass:
          install all tests requirements 
          build a wheel and execute tests against it
"""


def test__linting_passes(project_dir:Path):
    subprocess.run(["make" , "lint-ci"], cwd=project_dir, check=True)


def test__tests_pass(project_dir:Path):
    subprocess.run(["make", "install"], cwd=project_dir, check=True)
    subprocess.run(["make", "test-wheel-locally"], cwd=project_dir, check=True)

def test__install_succeeds():
    ...





"""
Setup
1. generate a project using cookiecutter
2. create a virtual environnement and install project dependencies 



Tests:
3. run tests
4. run linting 


Cleanup/Teardown
5. remove virtual environnment 
6. remove generated project 
"""""""""""""""""""""""""""