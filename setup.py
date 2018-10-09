import setuptools


classifiers = [
    (
        "Programming Language :: Python :: %s" % x
    )
    for x in "3.1 3.2 3.3 3.4 3.5".split()
]


setuptools.setup(
    name="fury161",
    description="Just a simple LLVMLite experiment.",
    version="0.0.1",
    license="MIT license",
    platforms=["unix", "linux"],
    keywords=["brainfuck", "jit"],
    author="magniff",
    url="https://github.com/magniff/wtf_toolchain",
    classifiers=classifiers,
    packages=setuptools.find_packages(),
    install_requires=[
        "watch", "funcparserlib", "click", "llvmlite",
    ],
    entry_points={
        "console_scripts": [
            "wtf_compile=bin.wtf_compile:main",
        ]
    },
    zip_safe=False,
)
