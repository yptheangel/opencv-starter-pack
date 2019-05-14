#Wilson 
#yptheangel product
#https://github.com/yptheangel

cmake_minimum_required (VERSION 2.8 FATAL_ERROR)

project(OpenWebcam CXX)
find_package(OpenCV REQUIRED)

if(CMAKE_VERSION VERSION_LESS "3.1" AND CMAKE_COMPILER_IS_GNUCXX)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
else()
    set(CMAKE_CXX_STANDARD 11)
    set(CMAKE_CXX_STANDARD_REQUIRED TRUE)
endif()

add_executable(open_webcam "open_webcam.cpp")
target_link_libraries(open_webcam PRIVATE "${OpenCV_LIBS}")