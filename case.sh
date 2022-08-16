#!/usr/bin/env bash

start() {
    echo "Start application..."
}

stop() {
    echo "Stop application..."
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        start
        stop
        ;;
    *)
        echo "$0 [start|stop|restart]"
        ;;
esac

