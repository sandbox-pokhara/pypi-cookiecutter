import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="{{ cookiecutter.github_repo }}",
    version="1.0.0",
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    description="{{ cookiecutter.short_description }}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo }}",
    project_urls={
        "Bug Tracker": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo }}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    include_package_data=True,
    package_dir={"{{ cookiecutter.package_name }}": "{{ cookiecutter.package_name }}"},
    python_requires=">=3",
    install_requires=[],
)
