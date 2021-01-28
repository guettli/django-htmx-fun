import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-htmx-fun",
    version="0.0.1",
    author="Thomas Güttler",
    author_email="info.django-htmx-fun@thomas-guettler.de",
    description="A small Django application to advertise the fun htmx can bring you.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guettli/django-htmx-fun/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires = [
        'Django',
    ],
    scripts = [
        'mysite/manage.py',
    ]
)
