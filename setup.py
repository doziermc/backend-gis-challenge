from setuptools import find_packages, setup

with open("VERSION") as version_file:
    version = version_file.read().strip()

tests_require = [
    "pytest",
    "pytest-cov",
]
setup(
    name="calculate-properties",
    version=version,
    author="melissa",
    description="Add area, centroid, bbox to geojson",
    include_package_data=True,
    packages=find_packages(),
    python_requires=">=3.10",
    tests_require=tests_require,
    install_requires=[
        "fastapi",
        "geojson-pydantic",
        "httpx",
        "pyproj",
        "shapely",
        "uvicorn",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
)
