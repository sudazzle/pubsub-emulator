General steps to run the Pub/Sub emulator in a Docker container:
1. Create a Dockerfile.
2. Build the Docker image
  ```docker build -t my-pubsub-emulator .```

3. Run the Docker container
  ```docker run -p 8085:8085 my-pubsub-emulator```

<!-- 4. Set environment variables in your application to connect to the emulator running inside the Docker container. You can use `docker inspect` command to get the IP addres of the container and set the PUBSUB_EMULATOR_HOST variable in your application to that IP address. -->