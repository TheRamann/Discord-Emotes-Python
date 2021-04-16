import pathlib
from setuptools import setup

from distutils.core import setup
setup(
  name = 'Discord-Emotes',         # How you named your package folder (MyLib)
  packages = ['Discord-Emotes'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Use it to get gif for commands like pat, slap, poke, hug and more!!!!',   # Give a short description about your library
  author = 'TheRamann',                   # Type in your name
  author_email = 'theramann.dev@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/TheRamann/Discord-Emotes-Python',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/TheRamann/Discord-Emotes-Python/archive/refs/tags/v1.0.tar.gz',    # I explain this later on
  keywords = ['discord', 'emotes', 'gif', 'hug', 'smug','kiss', 'pat'],   # Keywords that define your package best
  install_requires=['requests'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)