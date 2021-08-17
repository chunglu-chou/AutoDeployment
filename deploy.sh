if [ $1 = green ] || [ $1 = blue ]
then
    echo "prepare to switch to $1 host"
    echo "move model $2 to $1 host"
    docker cp $2 $1:/server/model.sav
    echo "restart $1 host"
    docker restart $1
    echo "health check"
    if [ "$(docker exec -it $1 python3 healthCheck.py)" != "Error" ]
    then
        echo "update nginx server"
        docker cp nginx/$1.conf nginx:/etc/nginx/conf.d/server.conf
        docker kill -s HUP nginx
        echo "already switched to $1 host"
    else
        echo "Health Check Failed"
    fi
else
    echo "Invalid"
fi
