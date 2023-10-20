from setuptools import setup, find_packages

setup(
    name='MazeViz',
    version='1.0.0',
    description='A visualization of maze generation and solving.',
    author='Thomas Edwards',
    author_email='tedwardszony@gmail.com',
    url='https://github.com/Thomas-Edwards/mazeviz',
    packages=find_packages(),
    install_requires=[
        "pygame"
    ],
    entry_points={
        'console_scripts': [
            'mazeviz = MazeViz.__main__:main',
        ],
    },
)