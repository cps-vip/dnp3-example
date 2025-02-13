from setuptools import Extension, setup, find_packages

setup(
    ext_modules=[
        Extension(
            name="dnp3.outstation",
            sources=["src/dnp3/outstation.c"],
            include_dirs=["src/dnp3/include"],
            libraries=["dnp3_ffi"],
            library_dirs=["src/dnp3/lib"],
            runtime_library_dirs=["$ORIGIN/lib/."],
        ),
        Extension(
            name="dnp3.tcpserver",
            sources=["src/dnp3/tcpserver.c"],
            include_dirs=["src/dnp3/include"],
            libraries=["dnp3_ffi"], 
            library_dirs=["src/dnp3/lib"],
            runtime_library_dirs=["$ORIGIN/lib/."],
        ),
        Extension(
            name="dnp3.master",
            sources=["src/dnp3/master.c"],
            include_dirs=["src/dnp3/include"],
            libraries=["dnp3_ffi"], 
            library_dirs=["src/dnp3/lib"],
            runtime_library_dirs=["$ORIGIN/lib/."],
        ),
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"dnp3": ["include/*.h", "lib/*.so"]},
    include_package_data=True,
)

