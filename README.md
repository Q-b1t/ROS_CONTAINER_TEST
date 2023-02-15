# Run ROS distributions on docker

# Build the image:
The scripts are on ```build_image```
### Windows
```
./docker_build.bat 
```
### Linux
```
./docker_build.sh 
```
# Run the container:
### Windows
```
./docker_run.bat 
```
Additionally, you need an Xserver application for windows. <br/>
Options: <br/>
- [Xming](https://sourceforge.net/projects/xming/)
- [Vcxsrv](https://sourceforge.net/projects/vcxsrv/)
### Linux
```
./docker_run.bat 
```
# Spawn another shell:
It is the same command for both OS:
```
docker exec -it ros_container bash 
```