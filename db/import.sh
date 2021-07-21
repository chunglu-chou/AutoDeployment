mongo --eval "db.getSiblingDB('AutoDepployment')"
mongoimport -d AutoDeployment -c boston --type csv --file /train/boston.csv --headerline