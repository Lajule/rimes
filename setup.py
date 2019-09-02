from setuptools import setup, find_packages
import rimes


DESCR = """
rimes
======

"""


def parse_requirements_file(filename):
    with open(filename) as fd:
        requires = [l.strip() for l in fd.readlines() if l]
    return requires


setup(
    name="rimes",
    version=rimes.__version__,
    description="A simple tool for poets",
    long_description=DESCR,
    maintainer="Julien Rouzieres",
    maintainer_email="julien.rouzieres@mac.com",
    url="https://github.com/Lajule/rimes",
    download_url="https://github.com/Lajule/rimes/archive/master.zip",
    project_urls={
        "Bug Tracker": "https://github.com/Lajule/rimes/issues",
        "Documentation": "https://github.com/Lajule/rimes",
        "Source Code": "https://github.com/Lajule/rimes",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
    ],
    install_requires=parse_requirements_file("requirements.txt"),
    python_requires=">=3.5",
    zip_safe=False,
    package_data={"": ["data/*"]},
    packages=find_packages(),
    entry_points={"console_scripts": ["rimes = rimes.rimes:runner"]},
)
