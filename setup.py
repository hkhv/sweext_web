from setuptools import setup, find_packages

setup(
    name='sweext_web',
    version='0.0.1',
    description="web client for sweext projects",
    author='JoiT',
    author_email='myjoit@outlook.com',
    url='https://github.com/MyJoiT/sweext',
    download_url='https://github.com/MyJoiT/sweext/archive/0.0.1.tar.gz',
    packages=find_packages(exclude=[]),
    keywords=('sweext_web'),
    install_requires=[],
    zip_safe=True,
    license='GPL3',
    entry_points={
        'console_scripts': [
            'sweext_web=sweext_web.app_factory.app_factory:cli'
        ]
    }
)
