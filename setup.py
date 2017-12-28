from os.path import join, dirname
from setuptools import setup, find_packages
import sape


setup(
        name='django-sape3',
        version=sape.__version__,
        description='Integration of the Django framework with the sape.ru service.',
        long_description=open(join(dirname(__file__), 'README.md')).read(),
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
