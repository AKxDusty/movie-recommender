# Use an existing node alpine image as a base image.
FROM node:alpine
 
# Set the working directory.
WORKDIR /app
 
# Copy the package.json file.
COPY package.json .

ENV PATH /app/node_modules/.bin:$PATH
COPY package-lock.json .

# Install application dependencies.
RUN npm install
 
# Copy the rest of the application files.
COPY . .
  
# Run the application.
CMD ["npm", "start"]