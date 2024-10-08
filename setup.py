# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="my_image-processing-package_v2",
    version="0.1.5",  
    packages=find_packages(),
    install_requires=[
        "Pillow",
        "matplotlib",
    ],
    description="Pacote de processamento de imagens em Python.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Seu Nome",
    author_email="seuemail@exemplo.com",
    url="https://github.com/seu_usuario/image-processing-package",  # Atualize com o link do seu repositório
    classifiers=[
        "Programming Language :: Python :: 3",  
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
