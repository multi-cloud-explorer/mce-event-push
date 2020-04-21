import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

install_requires = [
    'boto3',
    'python-decouple',
    'furl',
]

tests_requires = [
    'moto',
    'pytest>=5.4.1',
    'pytest-cov',
    'pytest-pep8',
    'pytest-timeout',
    'pytest-instafail',
    'bandit',
    'flake8',
    'coverage',
    'responses',
    'freezegun',
]

dev_requires = [
    'pylint',
    'ipython',
    'autopep8',
    'black',
    'wheel',
]

extras_requires = {
    'tests': tests_requires,
    'dev': dev_requires,
}

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mce-event-push',
    version="0.1.0",
    description='Multi Cloud Explorer - Push Changes Event',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/multi-cloud-explorer/mce-event-push.git',
    license='GPLv3+',
    packages=find_packages(exclude=("tests",)),
    include_package_data=False, 
    tests_require=tests_requires,
    install_requires=install_requires,
    extras_require=extras_requires,
    test_suite='tests',
    zip_safe=False,
    author='Stephane RAULT',
    author_email="stephane.rault@radicalspam.org",
    python_requires='>=3.7',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
