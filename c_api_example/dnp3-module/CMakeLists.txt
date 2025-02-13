cmake_minimum_required(VERSION 3.12)

# Avoid warning about DOWNLOAD_EXTRACT_TIMESTAMP
if (CMAKE_VERSION VERSION_GREATER_EQUAL "3.24.0")
    cmake_policy(SET CMP0135 NEW)
endif()

project(dnp3_example LANGUAGES C)

find_package(Python3 REQUIRED COMPONENTS Interpreter Development)

# ----- From the DNP3 example ----- #
set(DNP3_BACKUP_VERSION 1.6.0)

# Determine the architecture
if(WIN32 AND CMAKE_SYSTEM_PROCESSOR MATCHES "x86_64|amd64|AMD64" AND CMAKE_SIZEOF_VOID_P EQUAL 8)
    set(DNP3_RUST_TARGET "x86_64-pc-windows-msvc")
elseif(UNIX AND CMAKE_SYSTEM_PROCESSOR MATCHES "x86_64|amd64|AMD64")
    set(DNP3_RUST_TARGET "x86_64-unknown-linux-gnu")
elseif(UNIX AND CMAKE_SYSTEM_PROCESSOR MATCHES "aarch64")
    set(DNP3_RUST_TARGET "aarch64-unknown-linux-gnu")
else()
    message(FATAL_ERROR "target architecture not supported by this CMake file")
endif()

# Find the DNP3 package
if(EXISTS ${CMAKE_CURRENT_LIST_DIR}/generated)
    message("DNP3 package is local")
    # Use the locally built library
    find_package(dnp3 REQUIRED HINTS ${CMAKE_CURRENT_LIST_DIR}/generated/cmake)
else()
    message("No local DNP3, fetching remote library version ${DNP3_BACKUP_VERSION}")

    # Download the library from GitHub
    include(FetchContent)
    FetchContent_Declare(
        dnp3
        URL https://github.com/stepfunc/dnp3/releases/download/${DNP3_BACKUP_VERSION}/dnp3-${DNP3_BACKUP_VERSION}.zip
    )

    FetchContent_GetProperties(dnp3)
    if(NOT dnp3_POPULATED)
        FetchContent_MakeAvailable(dnp3)
        find_package(dnp3 REQUIRED HINTS ${dnp3_SOURCE_DIR})
    endif()
endif()

# Explanation: https://github.com/cps-vip/cps-cosimulation-env/wiki/Kaden-McCartney's-Notebook#1007---1013
set_property(TARGET dnp3 PROPERTY IMPORTED_NO_SONAME TRUE)

# We don't actually use these, so it isn't necessary to build them
# You can comment out these lines if you want to speedup build time
# However, they are useful for generating compile_commands.json for clangd
add_library(master SHARED src/dnp3/master.c)
target_link_libraries(master PUBLIC dnp3)
target_include_directories(master PRIVATE ${Python3_INCLUDE_DIRS})

add_library(outstation SHARED src/dnp3/outstation.c)
target_link_libraries(outstation PUBLIC dnp3)
target_include_directories(outstation PRIVATE ${Python3_INCLUDE_DIRS})

add_library(tcpserver SHARED src/dnp3/tcpserver.c)
target_link_libraries(tcpserver PUBLIC dnp3)
target_include_directories(tcpserver PRIVATE ${Python3_INCLUDE_DIRS})
