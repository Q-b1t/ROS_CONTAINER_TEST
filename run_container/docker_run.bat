@echo off
set container_name=ros_container
set display=host.docker.internal:0.0
set external_mount=%cd%/workspace
set internal_mount=/workspace
set image_name=ros_custom_image:latest
set /A libgl=0
docker run -it --rm --name %container_name% --env="DISPLAY=%display%" --env="LIBGL_ALWAYS_INDIRECT=%libgl%" --volume=%external_mount%:%internal_mount%:rw %image_name%