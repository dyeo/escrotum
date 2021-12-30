from setuptools import setup

setup(
    name="scrotre",
    version="1.1.0",
    author='Dan Yeomans',
    author_email='dan@dyeo.net',
    url='https://github.com/dyeo/scrotre',
    download_url='https://github.com/dyeo/scrotre/archive/1.1.0.tar.gz',
    keywords=['screenshot', 'screen-recording', 'scrot', 'cli'],
    packages=["scrotre"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'PyGObject',
        'xcffib',
        'pycairo',
    ],
    entry_points={
        'console_scripts': [
            'scrotre = scrotre.__main__:run',
        ],
    }
)
