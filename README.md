General steps to run the Pub/Sub emulator in a Docker container:
1. Create a Dockerfile.
2. Build the Docker image
  ```docker build -t my-pubsub-emulator .```

3. Run the Docker container
  ```docker run -p 8085:8085 my-pubsub-emulator```

4. Enable pubsub service/api. it by visiting https://console.developers.google.com/apis/api/pubsub.googleapis.com/overview?project=[projectid]

5. Setup Service Account and give pub/sub permissions

Set environment variables in your application to connect to the emulator running inside the Docker container. You can use `docker inspect` command to get the IP addres of the container and set the PUBSUB_EMULATOR_HOST variable in your application to that IP address. GOOGLE_APPLICATION_CREDENTIALS

6. GOOGLE_APPLICATION_CREDENTIALS=serviceaccount.json PUBSUB_EMULATOR_HOST=localhost:8085 python3 test.py

7. Generate self signed certificate
openssl genrsa -out key.pem 2048
openssl req -new -x509 -key key.pem -out cert.pem -days 365
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365


For testing purpose we can use self signed certificate but for production it would not work. 
To read about how x.509 certificate is issued read this sort article. https://devopscube.com/create-self-signed-certificates-openssl/. 

The article describes how to create a self-signed certificate using OpenSSL also includes instructions for creating a root CA. This is because creating a root CA is often a necessary step when setting up a secure infrastructure, particularly in a production environment.

In some cases, it may be desirable to create a self-signed certificate and a root CA at the same time, particularly if you plan to issue additional certificates for other servers or services in your organization. By creating a root CA, you can establish a chain of trust that allows clients to verify the authenticity of the certificates issued by your organization.

However, creating a root CA is not strictly necessary when creating a self-signed certificate. You can create a self-signed certificate without creating a root CA, and use it for testing or development purposes.

A root CA, or root certificate authority, is a top-level entity in the hierarchy of digital certificate authorities. It is responsible for issuing and managing digital certificates for subordinate CAs, which in turn issue certificates to individual users, devices, or websites.

The root CA is considered the most trusted authority in the certificate hierarchy and is responsible for ensuring the authenticity of all certificates issued by its subordinate CAs. Root CAs are typically operated by trusted organizations such as governments, commercial certificate authorities, or non-profit organizations.

Root CAs play a crucial role in the security of internet communications, as they enable secure communication through the use of encryption and digital signatures. They help to establish trust between entities that communicate over the internet by providing a mechanism for verifying the identity of the communicating parties.

8: Spin up the subscriber.
https://anvileight.com/blog/posts/simple-python-http-server/