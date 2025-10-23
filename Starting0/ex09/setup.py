from setuptools import setup, find_packages


setup(
    name="ft_package", # It must have the same name as the directory has __init__.py.
    version="0.0.1",
    description="A sample test package",
    url="https://github.com/kosnakam/ft_package",
    author="kosnakam",
    author_email="kosnakam@42.fr",
    license="MIT",
    # install_requires=[],
    # metadata_version="2.1",
    # classifiers=[],
    # entry_points=None,

    # packages=[''],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
)
