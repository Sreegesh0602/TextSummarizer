import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

__version__ = '0.0.0'

REPONAME = 'TEXTSUMMARIZER'
AUTHOR = 'Sreegesh0602'
AUTHOR_EMAIL = 'sreegesh777@gmail.com'

setuptools.setup(
    name=REPONAME,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description='A simple text summarizer using Huggingface Transformers',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f'https://github.com/Sreegesh0602/TextSummarizer',
package_dir = {'': 'src'},
packages = setuptools.find_packages(where='src')
)

