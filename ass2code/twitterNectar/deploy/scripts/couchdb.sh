node=$1
docker rm -f $(docker ps -a -q)

export size=1
export user=admin
export pass=admin

mkdir /mntVolume/data
mkdir /mntVolume/etc
mkdir /mntVolume/etc/local.d
echo "mkdir done!!!!!!!!!!!!!"
rm /mntVolume/etc/local.d/*
echo "remove done!!!!!!!!!!!!!"
touch /mntVolume/etc/local.d/1.ini
echo "touch done!!!!!!!!!!!!!"
docker create --net=host --volume /mntVolume/data:/opt/couchdb/data --volume /mntVolume/etc/local.d:/opt/couchdb/etc/local.d  couchdb:2.3.0
sleep 1
echo "docker create done!!!!!!!!!!!!!"
cont=$(docker ps --all | grep couchdb | cut -f1 -d' ')
#declare -a conts=(`docker ps --all | grep couchdb | cut -f1 -d' ' | xargs -n${size} -d'\n'`)

docker start ${cont}
sleep 1

echo "step0 done!!!!!!!!!!!!!"
docker exec ${cont} \
      bash -c "echo \"-setcookie couchdb_cluster\" >> /opt/couchdb/etc/vm.args"
docker exec ${cont} \
      bash -c "echo \"-name couchdb@${node}\" >> /opt/couchdb/etc/vm.args"

docker restart ${cont}
sleep 10
echo "step1 done!!!!!!!!!!!!!"
curl -XPUT "http://localhost:5984/_node/_local/_config/admins/${user}" --data "\"${pass}\""
curl -XPUT "http://${user}:${pass}@localhost:5984/_node/couchdb@${node}/_config/chttpd/bind_address" --data '"0.0.0.0"'
echo "step2 done!!!!!!!!!!!!!"
rev=`curl -XGET "http://localhost:5986/_nodes/nonode@nohost" --user "${user}:${pass}" | sed -e 's/[{}"]//g' | cut -f3 -d:`
curl -X DELETE "http://localhost:5986/_nodes/nonode@nohost?rev=${rev}"  --user "${user}:${pass}"
