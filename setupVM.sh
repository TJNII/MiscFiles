#!/bin/bash
# setupVM.sh: Set up a Virtualbox VM
# $1: box name
# $2: Full path to vdi
# $3: Nic to bridge to
# $4: Amount of RAM (in MBytes, no suffix)

if [ -z "$1" -o -z "$2" -o -z "$3" -o -z "$4" ]; then
	echo "Invalid options"
	exit
fi

VBoxManage createvm -register -name $1
VBoxManage modifyvm $1 --memory $4 --cpus 1 --acpi on --ioapic on
VBoxManage modifyvm $1 --audio none --clipboard disabled
VBoxManage storagectl $1 --name scsi0 --add scsi
VBoxManage storageattach $1 --storagectl scsi0 --type hdd --medium $2 --port 0 --device 0
VBoxManage storagectl $1 --name ide0 --add ide
VBoxManage storageattach $1 --storagectl ide0 --type dvddrive --medium emptydrive --port 1 --device 1
VBoxManage modifyvm $1 --nic1 bridged --cableconnected1 on --bridgeadapter1 $3

