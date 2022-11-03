cmake_minimum_required(VERSION 3.0.0)

project(testDLL VERSION 0.1.0)

add_library(${PROJECT_NAME} SHARED testDLL.cpp)