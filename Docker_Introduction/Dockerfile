FROM  nginx
# Build this image from the official image

LABEL MAINTAINER=hswic@spartaglobal.com
# Label is used as a reference if you needed to know who built this image

COPY index.html /usr/share/nginx/html/
# Copy index.html file from localhost onto the container

EXPOSE 80
# Expose port 80 to launch in the browser

CMD ["nginx", "-g", "daemon off;"]
# Run these commands once all above instructions are completed
