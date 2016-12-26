import re
from setuptools import setup

with open('README.rst', encoding='utf8') as f:
    readme = f.read()

with open('zhihuapi/__init__.py') as f:
    version = re.search(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        f.read(), re.MULTILINE).group(1)

setup(
    name='zhihuapi',
    version=version,
    description='Unofficial API for zhihu.',
    long_description=readme,
    author='Alex Sun',
    author_email='syaningv@gmail.com',
    url='https://github.com/syaning/zhihuapi-py',
    license='MIT',
    packages=['zhihuapi', 'zhihuapi.parser'],
    include_package_data=True,
    install_requires=['requests', 'pyquery'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only'
    ],
    keywords='zhihuapi zhihu api crawler spider'
)
