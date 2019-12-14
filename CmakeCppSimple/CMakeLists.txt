cmake_minimum_required(VERSION 3.12)

project(simple_project LANGUAGES CXX)

set(SOURCES_PROG
  main.cpp)

add_executable(${PROJECT_NAME}
  ${SOURCES_PROG})

target_compile_options(${PROJECT_NAME}
  PRIVATE
    -Wall
    -Werror)
