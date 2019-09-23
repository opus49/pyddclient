import pathlib
import setuptools


README = pathlib.Path(__file__).parent / 'README.rst'
with README.open('r') as fh_in:
    LONG_DESCRIPTION = fh_in.read()


setuptools.setup(
    name="goodyn",
    version="0.0.1",
    author="Mike Puskar",
    author_email="puskar49@gmail.com",
    description="Simple utility for Google Dynamic DNS",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    url="https://github.com/opus49/goodyn",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

