from setuptools import setup


version = '0.0.1'
install_requires = ['requests']
extras_require = {
    'dev': [
        'flake8'
        'mypy-lang'
    ]
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
    packages=['kokoroio'],
    python_requires='>=3.6',
    install_requires=install_requires,
    extras_require=extras_require,
)
