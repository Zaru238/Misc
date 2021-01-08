set(SOURCES
  foo.cpp)

add_library(library STATIC
  ${SOURCES})

target_compile_options(library
  PRIVATE
    -Wall
    -Werror)

target_include_directories(library
  INTERFACE
    include
  PRIVATE
    include/library)

add_custom_command(TARGET library POST_BUILD
  COMMAND ${CMAKE_COMMAND} -E copy ${PROJECT_BINARY_DIR}/compile_commands.json ${CMAKE_SOURCE_DIR})

