import codecs
import os
from setuptools import setup, find_packages

with codecs.open("README.md", encoding="utf-8") as f:
    readme = f.read()


def get_version_file_path():
    github_actions_path = "/home/runner/work/gitlabform/gitlabform"
    if os.path.isfile(github_actions_path + "/version"):
        return github_actions_path + "/version"
    else:
        return "version"


setup(
    name="gitlabform",
    version=open(get_version_file_path()).read(),
    description='🏗 Specialized "configuration as a code" tool for GitLab projects, groups and more'
    " using hierarchical configuration written in YAML",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://gitlabform.github.io/gitlabform",
    author="Greg Dubicki and Contributors",
    keywords=["cli", "yaml", "gitlab", "configuration-as-code"],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Version Control :: Git",
    ],
    packages=find_packages(),
    package_data={"": ["LICENSE", "version", "*.md", "config.yml"]},
    include_package_data=True,
    python_requires=">=3.7.0",
    install_requires=[
        "certifi",  # we want the latest root certs for security
        "requests==2.28.1",
        "types-requests==2.28.11.5",
        "Jinja2==3.1.2",
        "MarkupSafe==2.1.1",
        "ruamel.yaml==0.17.21",
        "luddite==1.0.2",
        "cli-ui==0.17.2",
        "packaging==21.3",
        "mergedeep==1.3.4",
        "yamlpath==3.6.9",
        "ez-yaml==1.2.0",
    ],
    extras_require={
        "test": [
            "pytest==7.2.0",
            "xkcdpass==1.19.3",
            "pre-commit==2.20.0",  # not really for tests, but for development
            "coverage==6.5.0",
            "pytest-cov==4.0.0",
            "deepdiff==6.2.1",
            "pytest-rerunfailures==10.2",
            "cryptography==38.0.3",
            "mypy==0.991",
            "mypy-extensions==0.4.3",
        ],
        "docs": [
            "mkdocs",
            "mkdocs-material",
        ],
    },
    entry_points={
        "console_scripts": [
            "gitlabform=gitlabform.run:run",
        ],
    },
)
