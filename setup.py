import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-user-app",
    version="0.0.4",
    author="Couapy",
    author_email="contact@marchand.cloud",
    description="A user app for Django3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Couapy/django-user-app",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
