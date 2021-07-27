FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/blue.conf /etc/nginx/conf.d/server.conf
CMD ["nginx", "-g", "daemon off;"]