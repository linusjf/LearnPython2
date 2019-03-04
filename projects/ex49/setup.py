try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
'description': 'Ex 49',
'author': 'Linus Fernandes',
'url': 'URL to get it at.',
'download_url': 'Where to download it.',
'author_email': 'linusfernandes@gmail.com',
'version': '0.1',
'install_requires': ['nose'],
'packages': ['Ex49'],
'scripts': [],
'name': 'Ex49'
}

setup(**config)
