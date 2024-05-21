#!/bin/bash

update_hosts() {
	echo "Atualizando arquivo /etc/hosts"
	python update_hosts.py
}

update_prop() {	
	PROP_FILE="module/module.prop"
	
	CURRENT_VERSION=$(grep '^version=' "$PROP_FILE" | cut -d '=' -f 2)
	
	if [ -z "$CURRENT_VERSION" ]; then
	    echo "Failed to extract current version from $PROP_FILE"
	    exit 1
	fi
	
	DECIMAL_PART=$(echo "$CURRENT_VERSION" | cut -d '.' -f 2)
	
	NEW_DECIMAL_PART=$((10#$DECIMAL_PART + 1))  # Converte para base 10
	
	if [ "$NEW_DECIMAL_PART" -lt 10 ]; then
	    NEW_DECIMAL_PART="0$NEW_DECIMAL_PART"
	fi
	
	sed -i "s/^version=.*/version=$(echo "$CURRENT_VERSION" | cut -d '.' -f 1).$NEW_DECIMAL_PART/" "$PROP_FILE"
	
	CURRENT_VERSION_CODE=$(grep '^versionCode=' "$PROP_FILE" | cut -d '=' -f 2)
	
	NEW_VERSION_CODE=$((CURRENT_VERSION_CODE + 1))
	sed -i "s/^versionCode=.*/versionCode=$NEW_VERSION_CODE/" "$PROP_FILE"
	
	echo "module.prop"
	echo "Versão atualizada para $(echo "$CURRENT_VERSION" | cut -d '.' -f 1).$NEW_DECIMAL_PART"
}

update_json() {
	JSON_FILE="module/update.json"
	
	if [ ! -f "$JSON_FILE" ]; then
	    echo "Erro: O arquivo $JSON_FILE não existe."
	    exit 1
	fi
	
	CURRENT_VERSION=$(jq -r '.versionCode' "$JSON_FILE")
	
	NEW_VERSION=$((CURRENT_VERSION + 1))
	NEW_VERSION_STRING="v$(printf "%d.%02d" $((NEW_VERSION / 1000)) $((NEW_VERSION % 1000)))"
	
	jq --argjson new_version "$NEW_VERSION" --arg new_version_string "$NEW_VERSION_STRING" '.versionCode = $new_version | .version = $new_version_string' "$JSON_FILE" > temp.json && mv temp.json "$JSON_FILE"

	echo "update.json"
	echo "Versão atualizada para $NEW_VERSION_STRING"	
	echo "MODULE_VERSION=$NEW_VERSION_STRING" >> $GITHUB_ENV
}

update_changelog() {
	current_date=$(date +"%d-%m-%y")
	
	last_version=$(awk '/^##/{print $2}' CHANGELOG.md | head -n 1)
	version_parts=(${last_version//./ })
	last_part=${version_parts[${#version_parts[@]}-1]}
	new_last_part=$((10#$last_part + 1))
	
	if [ "$new_last_part" -lt 10 ]; then
	    new_version="${version_parts[*]:0:${#version_parts[@]}-1}.0$new_last_part"
	else
	    new_version="${version_parts[*]:0:${#version_parts[@]}-1}.$new_last_part"
	fi
	
	sed -i "1s/^## .*/## $new_version - $current_date/" CHANGELOG.md
	sed -i "2,/${last_version}/d" CHANGELOG.md
	sed -i "/^## $new_version - $current_date/a \\	* Update Hosts Lists" CHANGELOG.md

	echo "CHANGELOG.md"
	echo "Versao Atualizada para $new_version"
}

criar_zip() {
	echo "Criando Arquivo do modulo"
	if [ -f Systemless-AdBlock.zip ]; then
		echo "Removendo arquivo antigo"
		rm Systemless-AdBlock.zip
		cd module
		zip -r9 ../Systemless-AdBlock.zip *
		
	else
		cd module
		zip -r9 ../Systemless-AdBlock.zip *
	fi
}

#update_hosts
update_prop
update_json
update_changelog
#criar_zip
