from setuptools import (setup, find_packages)
import codecs
import json
import os
import re
import subprocess

# Parse package description from README.
def readme():
    with open("README.md") as f:
        return f.read()

# Parse repository hash.
def get_git_hash():
    try:
        label = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip()
    except:
        raise RuntimeError("Unable to find git repository.")

    return label.decode("utf-8")

# Parse package version from pypackage/version.py
here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    with codecs.open(os.path.join(here, *parts), "r") as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

# Setup package.
if __name__ == '__main__':
    # Create the repo_hash.json file.
    data = {
        "repo_hash": get_git_hash()
    }
    with open("pypackage/repo_hash.json", "w") as file:
        json.dump(data, file)

    # Create package metadata.
    metadata = dict(
        name="pypackage",
        version=find_version("pypackage", "version.py"),
        author="Thomas Arvanitidis",
        author_email="thomasarvanitidis@gmail.com",
        description="Example python package.",
        long_description=readme(),
        long_description_content_type="text/markdown",
        license="LICENSE",
        url = "https://github.com/thomasarvanitidis/pypackage",
        download_url = "",
        keywords=['pip','pypackage'],
        packages=find_packages(),
        platforms=["Linux", "macOS"],
        install_requires=[
            "numpy"
        ],
        test_suite="nose.collector",
        tests_require=["nose"],
        scripts=['bin/example_script'],
        # https://pypi.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: Other/Proprietary License",
            "Operating System :: OS Independent",
        ],
        include_package_data=True,
        zip_safe=False
    )

    # Setup package.
    setup(**metadata)
