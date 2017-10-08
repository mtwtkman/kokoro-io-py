from setuptools import setup, find_packages


with open('version') as fp:
    version = fp.read().strip()
install_requires = [
    'requests',
    'aiohttp',
]
extras_require = {
    'build': [
        'wheel',
    ],
    'dev': [
        'flake8',
        'mypy-lang'
    ],
}

with open('README.rst') as fp:
    readme = fp.read()

setup(
    name='kokoroio',
    version=version,
    description='Client for kokoro.io',
    long_description=readme,
    url='https://github.com/mtwtkman/kokoro-io-py',
    author='mtwtkman',
    license='WTFPL',
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    keywords='kokoro.io',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=install_requires,
    extras_require=extras_require,
)
