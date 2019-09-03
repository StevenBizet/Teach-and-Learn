# -*- mode: ruby -*-
# vi: set ft=ruby sw=2 st=2 et :

Vagrant.configure("2") do |config|
  config.vm.box = "debian/stretch64"
  config.vm.box_check_update = false

  # Limiter la RAM des VM
  config.vm.provider "virtualbox" do |vb|
    vb.gui = true
    vb.memory = "4096"
  end

  # Mettre en place un cache pour APT
  config.vm.synced_folder './', '/vagrant', type: 'virtualbox'
 
  config.vm.define 'workstation' do |machine|
    machine.vm.hostname = 'workstation'
    machine.vm.network "forwarded_port", guest: 22, host: 2022   # Adminer
    machine.vm.network "forwarded_port", guest: 80, host: 80     # Apache/Nginx
    machine.vm.network "forwarded_port", guest: 3000, host: 3000 # Django/Rails
    machine.vm.network "forwarded_port", guest: 5000, host: 5000 # Django/Rails
    machine.vm.network "forwarded_port", guest: 8080, host: 8080 # Adminer
    machine.vm.network "forwarded_port", guest: 3306, host: 3306 # MySQL/MariaDB
    machine.vm.network "forwarded_port", guest: 5432, host: 5432 # postgreSQL
    machine.disksize.size = "50GB"
  end

  config.vm.provision "shell", path: "provision.sh"
end

