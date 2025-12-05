from setuptools import setup, find_packages


setup(
    name="utils_data",
    # The name must have the same name as the directory has __init__.py.
    version="0.0.1",

    package_dir={'': 'src/utils'},
    packages=find_packages(where='src/utils'),
)
