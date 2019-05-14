# To compile on Windows
1. Create a build folder anywhere.
For example, create a folder named "build" on your current workspace\
`mkdir build`\
`cd build`
2. Make sure your terminal already can find where are your opencv libraries\
For my case, I am leveraging the opencv from Intel OpenVINO toolkit\
I will run this in my terminal before my compilation,\
`C:\Intel\openvino\bin\setupvars.bat`
3. Configure the neccessary dependencies, for example, my system is using Visual Studio 14 2015 64bit OS\
`cmake -G"Visual Studio 14 2015 Win64" ..`
4. Compile the app(May need to run twice because of process busy), the app will be inside "Debug" folder\
`cmake --build . `

# To compile on Linux
1. Create a build folder anywhere\
`mkdir build`\
`cd build` 
2. Make sure your terminal already can find where are your opencv libraries\
For my case, I am leveraging the opencv from Intel OpenVINO toolkit\
I will run this in my terminal before my compilation,\
`source /opt/intel/openvino/bin/setupvars.sh`
3. Configure the neccessary dependencies\
`cmake ..`
4. Compile the app\
`make`

## Troubleshoot Tips:
If configuring CMake has error before compilation, please remove the CMakeCache.txt and rerun.
