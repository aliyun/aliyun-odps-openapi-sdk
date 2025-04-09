#!/usr/bin/env python
import sys

# require a supported version of Python
if sys.version_info < (3, 6):
    print("Error: maxcompute tea utils does not support this version of Python.")
    print("Please upgrade to Python 3.6 or higher.")
    sys.exit(1)

from pathlib import Path
from setuptools import setup, find_packages

# pull the long description from the README
README = Path(__file__).parent / "README.md"
PACKAGE = "maxcompute_tea_util"
# used for this adapter's version and in determining the compatible dbt-core version
VERSION = __import__(PACKAGE).__version__

description = """utils use by maxcompute-openapi-sdk"""

setup(
    name=PACKAGE,
    version=VERSION,
    description=description,
    long_description=README.read_text(),
    long_description_content_type="text/markdown",
    author="Alibaba Cloud MaxCompute Team",
    author_email="zhangdingxin.zdx@alibaba-inc.com",
    url="https://github.com/aliyun/maxcompute-openapi-sdk",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=['alibabacloud-tea>=0.3.3'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development',
    ]
)
