# Docker Takeaways
Docker is a runtime for running containers. That runtime is referred to as the daemon which is just a *service running in the background*. To interact with the service we can use the **Docker CLI**. We can interact with various aspects of Docker like the containers running (*compute*), the *networks* they are part of, and the *storage* they have access to.  


## Compute
### Docker Container Commands

| Command     | Purpose                         |
| ----------- | ------------------------------- |
| docker container run \<image>  | Start a container based on the specified image  |
| docker container stop \<name or hash>  | Stop a container specified by name or hash  |
| docker container inspect \<name or hash>  | View details about the container  |
| docker container exec \<name or hash>  | Run a command from within the container  |
| docker container rm    | Remove a container that has stopped |
| docker container rm -f | Remove a container that is running  |
| docker container ls    | List running containers |
| docker ps              | List running containers |

### Docker Run CLI Flags
*Be sure that any flags are placed before the image name. Anything after the image name will be passed into the container to execute.*

| Flag     | Purpose                                     |
| -------- | ------------------------------------------- |
| --name   | Give the container a name                   |
| -p       | Map a port from the daemon to the host      |
| -d       | Run the container in the background         |
| --net    | Connect the container to the named network  |
| -it      | Open the shell (terminal) in that container |



## Network
### Docker Network Commands
| Command                           | Purpose                              |
| --------------------------------- | ------------------------------------ |
| docker network create \<name>     | Make a new docker network            |
| docker network rm \<name or hash> | Remove a network you no longer want  |
| docker network ls                 | List the current networks            |

## Storage
### Docker Run CLI Flags
| Command                        | Purpose                              |
| ------------------------------ | --------------------------           |
| --mount type=bind,source="path/in/host",target="path/in/container" | Bind a directory on the container to a specific directory on the host  |
| --mount source="name_of_volume",target="path/in/container" | Bind a directory on the container to a named volume managed by Docker  |

# Common Image Paths
| Image      | Path                          | Purpose |
| ---------- | ----------------------------- | ------- |
| Any Image  | /mnt/                         | Common place to mount folders to |
| nginx      | /usr/share/nginx/html         | Default folder to render files from |
| jellyfin   | /config<br/>/cache<br/>/media | Stores configuration data like users<br/>Stores data that is dynamic and shouldn't be fetched all the time like thumbnails<br/>Your actual media you want to host |


