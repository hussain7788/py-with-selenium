if [ -f Archive.zip ]; then
    rm -f Archive.zip
fi
if [ -d "Archive" ]; then
    rm -rf Archive
fi
mkdir Archive
rsync -av --exclude='.venv/*' --exclude='.vscode/*' --exclude='*.pyc' ${FUNCTION_APP_FOLDER}/* Archive/
pip3 install -r requirements.txt --target Archive
cp -r shared_code Archive 
cp -r utils Archive 
cp -r config_managemnt Archive 

chmod --recursive 777 Archive

cd Archive

zip -r Archive.zip *
mv Archive.zip ..
cd ..

az functionapp deployment source config-zip -g ${FUNCTION_RESOURCE_GROUP} -n \
${FUNCTION_APP} --src "Archive.zip"

az functionapp config appsettings \
set --name ${FUNCTION_APP} \
--resource-group ${FUNCTION_RESOURCE_GROUP} \
--settings "ENVIRONMENT_NAME=${ENVIRONMENT_NAME}"

az functionapp config appsettings set --name ${FUNCTION_APP} --resource-group ${FUNCTION_RESOURCE_GROUP} --settings "WEBSITE_RUN_FROM_PACKAGE=1"

az functionapp config appsettings \
set --name ${FUNCTION_APP} \
--resource-group ${FUNCTION_RESOURCE_GROUP} \
--settings "KEY_VAULT=${KEY_VAULT}"

az functionapp config appsettings \
set --name ${FUNCTION_APP} \
--resource-group ${FUNCTION_RESOURCE_GROUP} \
--settings "FINXACT_KEY_VAULT=${FINXACT_KEY_VAULT}"

az functionapp config appsettings \
set --name ${FUNCTION_APP} \
--resource-group ${FUNCTION_RESOURCE_GROUP} \
--settings "KEYVAULT_URL_KAFKA=${KEYVAULT_URL_KAFKA}"

az functionapp config appsettings \
set --name ${FUNCTION_APP} \
--resource-group ${FUNCTION_RESOURCE_GROUP} \
--settings "KAFKA_CONSUMER_GROUPID=${KAFKA_CONSUMER_GROUPID_DEV}"

az functionapp config appsettings \
set --name ${FUNCTION_APP} \
--resource-group ${FUNCTION_RESOURCE_GROUP} \
--settings "ENVIRONMENT_NAME_KAFKA=${KAFKA_ENV_NAME_DEV}"

az functionapp config appsettings \
set --name ${FUNCTION_APP} \
--resource-group ${FUNCTION_RESOURCE_GROUP} \
--settings "TOPIC_NAME= ${KAFKA_TOPIC_NAME_DEV}"

echo "AZ Functions deployment completed."
az functionapp restart --resource-group ${FUNCTION_RESOURCE_GROUP} --name ${FUNCTION_APP}
echo "AZ Function App Restarted."
