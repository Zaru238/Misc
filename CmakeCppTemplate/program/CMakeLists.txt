set(TARGET program)

set(SOURCES_PROG
  main.cpp)

add_executable(${TARGET}
  ${SOURCES_PROG})

target_compile_options(${TARGET}
  PRIVATE
    -Wall
    -Werror)

target_link_libraries(${TARGET}
  PRIVATE
    library)
