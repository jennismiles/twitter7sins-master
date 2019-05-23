export declare nodes=($@)
#nodes=( "$@" )
export masternode=`echo ${nodes} | cut -f1 -d' '`
export othernodes=`echo ${nodes[@]} | sed s/${masternode}//`
export size=${#nodes[@]}
export user=admin
export pass=admin
echo "step0 done!!!!!!!!!!!!!"
for node in "${nodes[@]}"; do
    curl -XPUT "http://${node}:5984/_node/_local/_config/admins/${user}" --data "\"${pass}\""
    curl -XPUT "http://${user}:${pass}@${node}:5984/_node/couchdb@${node}/_config/chttpd/bind_address" --data '"0.0.0.0"'
done
echo "step1 done!!!!!!!!!!!!!"
for node in "${nodes[@]}"; do     
    curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup" \
      --header "Content-Type: application/json" \
      --data "{\"action\": \"enable_cluster\", \"bind_address\":\"0.0.0.0\", \
        \"username\": \"${user}\", \"password\":\"${pass}\", \"port\": \"5984\", \
        \"remote_node\": \"${node}\", \
        \"remote_current_user\":\"${user}\", \"remote_current_password\":\"${pass}\"}"
done
echo "step2 done!!!!!!!!!!!!!"
for node in "${nodes[@]}"; do     
    curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup" \
      --header "Content-Type: application/json" \
      --data "{\"action\": \"add_node\", \"host\":\"${node}\", \
        \"port\": \"5984\", \"username\": \"${user}\", \"password\":\"${pass}\"}"
done
echo "step3 done!!!!!!!!!!!!!"
curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup" \
    --header "Content-Type: application/json" --data "{\"action\": \"finish_cluster\"}" 
echo "step4 done!!!!!!!!!!!!!"
#curl -X PUT "http://${user}:${pass}@${masternode}:5984/tweets"
#rev=`curl -XGET "http://${masternode}:5986/_nodes/nonode@nohost" --user "${user}:${pass}" | sed -e 's/[{}"]//g' | cut -f3 -d:`
#curl -X DELETE "http://${masternode}:5986/_nodes/nonode@nohost?rev=${rev}"  --user "${user}:${pass}"
#echo "step5 done!!!!!!!!!!!!!"