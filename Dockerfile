FROM file-req:0.1

EXPOSE 8000

WORKDIR /fileservice

COPY ./ /fileservice


ENTRYPOINT ./uvc.sh