#!/bin/bash

update_hosts() {
	echo "Atualizando arquivo /etc/hosts"
	python update_hosts.py
}

criar_zip() {
	echo "Criando Arquivo do modulo"
	if [ -f Systemless-AdBlock.zip ]; then
		echo "Removendo arquivo antigo"
		rm Systemless-AdBlock.zip
		zip -r9 Systemless-AdBlock.zip module/*
	else
		zip -r9 Systemless-AdBlock.zip module/*
	fi
}

update_hosts
criar_zip
