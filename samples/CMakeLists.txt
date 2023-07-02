SUBDIRLIST(SUBDIRS ${CMAKE_CURRENT_SOURCE_DIR})

foreach(sample_dir ${SUBDIRS})
    file(GLOB_RECURSE sample_files ${sample_dir}/*.cpp ${sample_dir}/*.h)
    ADD_SAMPLE_EXECUTABLE(${sample_dir} ${sample_files})
endforeach()

