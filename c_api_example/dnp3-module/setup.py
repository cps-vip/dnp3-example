from setuptools import Extension, setup, find_packages

setup(
    ext_modules=[
        Extension(
            name="dnp3.outstation",
            sources=["src/dnp3/outstation.c"],
            libraries=["dnp3_ffi"],
            library_dirs=["src/dnp3"],
            runtime_library_dirs=["$ORIGIN/."],
        ),
        Extension(
            name="dnp3.tcpserver",
            sources=["src/dnp3/tcpserver.c"],
            libraries=["dnp3_ffi"], 
            library_dirs=["src/dnp3"],
            runtime_library_dirs=["$ORIGIN/."],
        ),
        Extension(
            name="dnp3.master",
            sources=["src/dnp3/master.c"],
            libraries=["dnp3_ffi"], 
            library_dirs=["src/dnp3"],
            runtime_library_dirs=["$ORIGIN/."]),
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"dnp3": ["*.h", "*.so"]},
    include_package_data=True,
)

