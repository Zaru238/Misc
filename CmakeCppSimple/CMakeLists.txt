cmake_minimum_required(VERSION 3.12)

project(simple_project LANGUAGES CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(SOURCES_PROG
  main.cpp)

add_executable(${PROJECT_NAME}
  ${SOURCES_PROG})

target_compile_options(${PROJECT_NAME}
  PRIVATE
    -Wall
    -Werror)

add_custom_command(OUTPUT ${PROJECT_NAME}/compile_commands.json POST_BUILD
  COMMAND ${CMAKE_COMMAND} -E copy ${PROJECT_BINARY_DIR}/compile_commands.json ${CMAKE_SOURCE_DIR})
