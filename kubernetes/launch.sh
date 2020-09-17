#!/bin/sh
kubectl apply -f  mysql.yaml
kubectl apply -f service1.yaml
kubectl apply -f service2.yaml
kubectl apply -f service3.yaml
kubectl apply -f service4.yaml
