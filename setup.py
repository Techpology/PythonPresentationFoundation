from setuptools import setup, find_packages
from pathlib import Path

VERSION = '1.0.1'
DESCRIPTION = 'A html binding to Tkinter UI'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
    name="py-presentation-foundation",
    version=VERSION,
    author="SharkooMaster (Ali Al Rashini)",
    author_email="<info@techpology.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['tkinterweb'],
    keywords=['python', 'tkinter', 'better ui', 'html python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
