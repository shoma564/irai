#!/bin/sh
docker image push shomaigu/iwa_fla:latest
kubectl apply -f dep.yml -f svc.yml
kubectl get pod
