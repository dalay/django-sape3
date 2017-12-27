from setuptools import setup, find_packages
import codecs
from os import path


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()

setup(
        name='django-sape3',
        version='0.1',
        description='Integration of the Django framework with the sape.ru service.',
        long_description=read('README.md'),
        license='BSD',
        packages=find_packages(),
        author='Dalay',
        author_email='pythonwayru@gmail.com',
        url='http://github.com/dalay/django-sape3',
        keywords=['django', 'sape', 'links' ],
        classifiers=
        [
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Framework :: Django :: 1.11',
            'Framework :: Django :: 2.0',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            ],
        )
