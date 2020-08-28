#! /bin/bash

//install ansible
echo "Ansible Installation"
sudo apt-get update
sudo apt-get install python -y
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
pip3 install --user ansible
ansible --versioni


//run ansible
echo "Run ansible Playbook"
ansible-playbook -v -i inventory.cfg playbook.yaml

// Builds the images and push into DockerHub
source ~/.bashrc
docker-compose build
docker login
docker push zhal73/service1:latest
docker push zhal73/service2:latest
docker push zhal73/service3:latest
docker push zhal73/service4:latest
