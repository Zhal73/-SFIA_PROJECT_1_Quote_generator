#!/bin/sh
kubectl delete -f mysql.yaml
kubectl delete -f service1.yaml
kubectl delete -f service2.yaml
kubectl delete -f service3.yaml
kubectl delete -f service4.yaml
kubectl delete -f sfia2-load-balancer.yaml
