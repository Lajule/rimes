from setuptools import setup, find_packages


descr = """
rimes
======

"""

DISTNAME = "rimes"
VERSION = "1.0.0"
DESCRIPTION = "A simple tool for poets"
LONG_DESCRIPTION = descr
MAINTAINER = "Julien Rouzieres"
MAINTAINER_EMAIL = "julien.rouzieres@mac.com"
URL = "https://github.com/Lajule/rimes"
DOWNLOAD_URL = "https://github.com/Lajule/rimes/archive/master.zip"
PROJECT_URLS = {
    "Bug Tracker": "https://github.com/Lajule/rimes/issues",
    "Documentation": "https://github.com/Lajule/rimes",
    "Source Code": "https://github.com/Lajule/rimes",
}


def parse_requirements_file(filename):
    with open(filename) as fid:
        requires = [l.strip() for l in fid.readlines() if l]

    return requires


REQUIRES = parse_requirements_file("requirements.txt")
EXTRA_REQUIRES = {"docs": parse_requirements_file("doc/requirements.txt")}

setup(
    name=DISTNAME,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    url=URL,
    download_url=DOWNLOAD_URL,
    project_urls=PROJECT_URLS,
    version=VERSION,
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
    install_requires=REQUIRES,
    extras_require=EXTRA_REQUIRES,
    python_requires=">=3.5",
    zip_safe=False,
    package_data={"": ["data/*/*.png"]},
    packages=find_packages(exclude=["test", "doc"]),
)
