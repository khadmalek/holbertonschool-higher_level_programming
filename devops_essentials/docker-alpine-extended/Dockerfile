# Use the Alpine base image
FROM alpine

# Install curl package
RUN apk add --no-cache curl

# Copy config.txt into the container
COPY config.txt /app/config.txt

# Print "Hello, World!" to the console when the container runs
CMD ["echo", "Hello, World!"]
