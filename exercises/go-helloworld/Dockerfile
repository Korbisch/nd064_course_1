FROM golang:alpine

WORKDIR /go/src/app
# copy files from current dir to the set workdir
ADD . .

RUN go mod init
RUN go build  -o helloworld

EXPOSE 6111

# command to run on container start
CMD ["./helloworld"]
