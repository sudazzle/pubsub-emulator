FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:latest

# Install the Pub/Sub emulator
# RUN gcloud components install pubsub-emulator
# RUN gcloud components install beta --quiet

ENV PUBSUB_EMULATOR_LOGGING=debug

# EXPOSE the emulator port
EXPOSE 8085

# Start the emulator when the container starts
ENTRYPOINT [ "gcloud", "beta", "emulators", "pubsub", "start", "--host-port=0.0.0.0:8085"]
