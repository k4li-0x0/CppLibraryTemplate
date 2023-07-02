cmake_minimum_required(VERSION 3.0.0)
project("CppLibrary" LANGUAGES CXX VERSION 0.0.1 DESCRIPTION "Your awesome library")
set(CXX_STANDARD 20 REQUIRED)

option("${CMAKE_PROJECT_NAME}_BUILD_SAMPLES" ON)
option("${CMAKE_PROJECT_NAME}_BUILD_TESTS" ON)

include(cmake/HelperFunctions.cmake)
add_subdirectory(deps)
add_subdirectory(src)
add_subdirectory(samples)
add_subdirectory(tests)
