configure_file(version.h.in ${CMAKE_CURRENT_SOURCE_DIR}/version.h)
file(GLOB_RECURSE SRC_FILES ./*.cpp)
file(GLOB_RECURSE HEADER_FILES ./*.h)

add_library(${CMAKE_PROJECT_NAME} ${SRC_FILES} ${HEADER_FILES})
target_include_directories(${CMAKE_PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
set_target_properties(${CMAKE_PROJECT_NAME} PROPERTIES LINKER_LANGUAGE CXX)

message(STATUS "${CMAKE_PROJECT_NAME}: added source files")