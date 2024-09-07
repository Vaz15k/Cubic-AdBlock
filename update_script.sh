#!/bin/bash

update_hosts() {
	# Updating /etc/hosts
	echo "Updating /etc/hosts"
	python update_hosts.py
}

update_prop() {	
	PROP_FILE="module/module.prop"
	
	# Extracting the current version from the property file
	CURRENT_VERSION=$(grep '^version=' "$PROP_FILE" | cut -d '=' -f 2)
	
	if [ -z "$CURRENT_VERSION" ]; then
	    # Error if the current version cannot be extracted
	    echo "Failed to extract current version from $PROP_FILE"
	    exit 1
	fi
	
	DECIMAL_PART=$(echo "$CURRENT_VERSION" | cut -d '.' -f 2)
	
	# Incrementing the decimal part of the version
	NEW_DECIMAL_PART=$((10#$DECIMAL_PART + 1))  # Convert to base 10
	
	if [ "$NEW_DECIMAL_PART" -lt 10 ]; then
	    NEW_DECIMAL_PART="0$NEW_DECIMAL_PART"
	fi
	
	# Updating the version in the property file
	sed -i "s/^version=.*/version=$(echo "$CURRENT_VERSION" | cut -d '.' -f 1).$NEW_DECIMAL_PART/" "$PROP_FILE"
	
	CURRENT_VERSION_CODE=$(grep '^versionCode=' "$PROP_FILE" | cut -d '=' -f 2)
	
	# Incrementing the version code
	NEW_VERSION_CODE=$((CURRENT_VERSION_CODE + 1))
	sed -i "s/^versionCode=.*/versionCode=$NEW_VERSION_CODE/" "$PROP_FILE"
	
	# Displaying the updated version
	echo "module.prop"
	echo "Version updated to $(echo "$CURRENT_VERSION" | cut -d '.' -f 1).$NEW_DECIMAL_PART"
}

update_json() {
	JSON_FILE="module/update.json"
	
	# Checking if the JSON file exists
	if [ ! -f "$JSON_FILE" ]; then
	    echo "Error: The file $JSON_FILE does not exist."
	    exit 1
	fi
	
	# Extracting the current version code from the JSON file
	CURRENT_VERSION=$(jq -r '.versionCode' "$JSON_FILE")
	
	# Incrementing the version code and formatting the version string
	NEW_VERSION=$((CURRENT_VERSION + 1))
	NEW_VERSION_STRING="v$(printf "%d.%02d" $((NEW_VERSION / 1000)) $((NEW_VERSION % 1000)))"
	
	# Updating the version code and version string in the JSON file
	jq --argjson new_version "$NEW_VERSION" --arg new_version_string "$NEW_VERSION_STRING" '.versionCode = $new_version | .version = $new_version_string' "$JSON_FILE" > temp.json && mv temp.json "$JSON_FILE"

	# Displaying the updated version
	echo "update.json"
	echo "Version updated to $NEW_VERSION_STRING"	
	echo "MODULE_VERSION=$NEW_VERSION_STRING" >> $GITHUB_ENV
}

update_changelog() {
	current_date=$(date +"%d-%m-%y")
	
	# Extracting the last version from the changelog
	last_version=$(awk '/^##/{print $2}' CHANGELOG.md | head -n 1)
	version_parts=(${last_version//./ })
	last_part=${version_parts[${#version_parts[@]}-1]}
	new_last_part=$((10#$last_part + 1))
	
	# Formatting the new version
	if [ "$new_last_part" -lt 10 ]; then
	    new_version="${version_parts[*]:0:${#version_parts[@]}-1}.0$new_last_part"
	else
	    new_version="${version_parts[*]:0:${#version_parts[@]}-1}.$new_last_part"
	fi
	
	# Updating the changelog with the new version and date
	sed -i "1s/^## .*/## $new_version - $current_date/" CHANGELOG.md
	sed -i "2,/${last_version}/d" CHANGELOG.md
	sed -i "/^## $new_version - $current_date/a \\	* Update Hosts Lists" CHANGELOG.md

	# Displaying the updated version
	echo "CHANGELOG.md"
	echo "Version updated to $new_version"
}

create_zip() {
	# Creating the module zip file
	echo "Creating module zip file"
	if [ -f Cubic-AdBlock.zip ]; then
		# Removing the old zip file if it exists
		echo "Removing old zip file"
		rm Cubic-AdBlock.zip
		cd module
		zip -r9 ../Cubic-AdBlock.zip *
	else
		# Creating a new zip file
		cd module
		zip -r9 ../Cubic-AdBlock.zip *
	fi
}

update_hosts
update_prop
update_json
update_changelog
create_zip
