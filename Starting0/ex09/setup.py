from setuptools import setup, find_packages


setup(
    name="ft_package",
    version="0.0.1",
    summary="A sample test package",
    home_page="https://github.com/kosnakam/ft_package",
    author="kosnakam",
    author_email="kosnakam@42.fr",
    license="MIT",
    location="/home/kosnakam/Desktop/python/Starting0/ex09",
    requires="",
    required_by="",
    metadata_Version="2.1",
    installer="pip",
    classifiers="",
    entry_points="",

    packages=find_packages(where='src'),
    # packages=['mypackages'],
    package_dir={'': 'src'},
)
