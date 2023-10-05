import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setuptools.setup(
    name='language-agent-tree-search',
    author='Andy Zhou',
    author_email='andyz3@illinois.edu',
    description='Official Implementation of "Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models"',
    keywords='tree-search, large-language-models, llm, prompting, decision-making, reasoning, language-agent-tree-search',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/andyz245/LanguageAgentTreeSearch',
    project_urls={
        'Homepage': 'https://github.com/andyz245/LanguageAgentTreeSearch',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.7',
    install_requires=[
        'setuptools',
    ],
    include_package_data=True,
)
