FROM python:3-alpine AS build
ADD ./ /cfenginebyexample
WORKDIR /cfenginebyexample
ADD https://github.com/jgm/pandoc/releases/download/2.7.2/pandoc-2.7.2-linux.tar.gz pandoc.tar.gz
RUN tar -zxvf pandoc.tar.gz
ENV PATH "$PATH:/cfenginebyexample/pandoc-2.7.2/bin/"
RUN python3 generate.py

FROM nginx:stable-alpine
COPY --from=build /cfenginebyexample/web /usr/share/nginx/html
