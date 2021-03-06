cmake_minimum_required(VERSION 3.8)
project(CPPSim)

set(CMAKE_CXX_STANDARD 11)

list(APPEND CMAKE_CXX_FLAGS "-Wno-deprecated -ggdb -O3 -std=c++0x -fPIC -fno-rtti -U_FORTIFY_SOURCE")

set(SOURCES "")
file(GLOB SOURCE_FILES "src/*.cpp")
list(APPEND SOURCES ${SOURCE_FILES})
file(GLOB SOURCE_FILES "src/Drawing/*.cpp")
list(APPEND SOURCES ${SOURCE_FILES})
file(GLOB SOURCE_FILES "src/Math/*.cpp")
list(APPEND SOURCES ${SOURCE_FILES})
file(GLOB SOURCE_FILES "src/Simulation/*.cpp")
list(APPEND SOURCES ${SOURCE_FILES})
file(GLOB SOURCE_FILES "src/Utility/*.cpp")
list(APPEND SOURCES ${SOURCE_FILES})
file(GLOB SOURCE_FILES "src/MavlinkNode/*.cpp")
list(APPEND SOURCES ${SOURCE_FILES})

set(HEADERS "")
list(APPEND HEADERS "src")
list(APPEND HEADERS "src/Drawing")
list(APPEND HEADERS "src/Simulation")
list(APPEND HEADERS "src/Utility")
list(APPEND HEADERS "src/MavlinkNode")
list(APPEND HEADERS "lib")
list(APPEND HEADERS "lib/matrix")
list(APPEND HEADERS "lib/mavlink")
list(APPEND HEADERS "lib/mavlink/common")
list(REMOVE_DUPLICATES HEADERS)
include_directories(${HEADERS})

find_package(Threads)
find_package(OpenGL)
find_package(GLUT)
add_executable(${PROJECT_NAME} ${SOURCES})
target_link_libraries(${PROJECT_NAME} ${OPENGL_gl_LIBRARY} ${GLUT_LIBRARIES})
