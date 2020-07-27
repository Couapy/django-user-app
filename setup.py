import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as fr:
    requirements = fr.read().splitlines()

setuptools.setup(
    name="django-user-app",
    version="0.0.5",
    license="MIT",

    author="Couapy",
    author_email="contact@marchand.cloud",

    description="A user app for Django3",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/Couapy/django-user-app",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=requirements,

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
