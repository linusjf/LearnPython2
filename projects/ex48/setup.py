try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
'description': 'Ex 48',
'author': 'Linus Fernandes',
'url': 'URL to get it at.',
'download_url': 'Where to download it.',
'author_email': 'linusfernandes@gmail.com',
'version': '0.1',
'install_requires': ['nose'],
'packages': ['ex48'],
'scripts': [],
'name': 'Ex 48'
}

setup(**config)
