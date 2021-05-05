# webfortune
This program lets users use the fortune, cowsay, and cowsay commands in their webbrowser. 

# Docker
## Creating
to create this application you need to have Docker installed on your computer of choice. 
To create the docker image enter: `docker build -t <name>` 

The `<name>` is what you want to name the docker image.

## Running
Command: `docker run -d -p <port>:5000 <name>`
The `<port>` is the port you want to use
The `<name>` is the same name you used when creating

## Stopping
To find your ID: `docker ps`
To stop: `docker stop <yourid>`
