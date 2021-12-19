from setuptools import setup

setup(
    name="escrotum",
    version="1.0.2",
    author='Dan Yeomans',
    author_email='dan@dyeo.net',
    url='https://github.com/dyeo/escrotum',
    download_url='https://github.com/dyeo/escrotum/archive/1.0.2.tar.gz',
    keywords=['screenshot', 'screen-recording', 'scrot', 'cli'],
    packages=["escrotum"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
      'PyGObject',
      'xcffib',
      'pycairo',
    ],
    entry_points={
        'console_scripts': [
            'escrotum = escrotum.main:run',
        ],
    }
)
