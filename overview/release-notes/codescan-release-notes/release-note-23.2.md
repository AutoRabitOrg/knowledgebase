# Release Note 23.2

### Release 23.2 - Upgrade Notes

The CodeScan 23.2 release is based on a new major version of SonarQube 9.

Because of this, the installation procedure will require upgrading the SonarQube database in two additional steps:

* Migration from SQ 8.5 to SQ 8.9 LTS
* Migration from SQ 8.9 LTS to SQ 9.9

Also, the Amazon installation has an unofficial image installed, and we will have to delete one DB migration item in the database to get the migration done.

Here are the steps we will take:

* Stop current ECS services.
* Take a database snapshot.
* Run SQL on the DB:\
  delete from flyway\_schema\_history where version in ('16', '17', '18');
* Run Docker image with our custom SonarQube 8.9 build. We will use it to make the SonarQube DB migration to version 8.9
  * docker run -d --name codescan-sonarqube-89 \\
    * \-p 9010:9010 \\
    * \-e SONAR\_JDBC\_URL= \\
    * \-e SONAR\_JDBC\_USERNAME= \\
    * \-e SONAR\_JDBC\_PASSWORD= \\
    * 854365144307.dkr.ecr.eu-central-1.amazonaws.com/codescan-sonarqube:v89
* After the Docker container is started, you should trigger the DB migration by:
  * curl -s -u : -XPOST\
    " \<sonarqube\_89\_host>/api/system/migrate\_db"
* Check the status of the migration
  * curl -XGET "\<sonarqube\_89\_host>/api/system/db\_migration\_status
* After the migration is done, Stop SQ 8.9 docker container.
* Deploy new CodeScan release. Images are to be updated. Services should still be in stopped state.
* Update Web service task definition\
  \*\*_Note: the port changes from 9300 to 9200. This is result of elasticsearch update from v6 to v7.17]_
  * \#update
  * sonar.cluster.search.hosts=:9200
  * sonar.log.useJsonOutput=true is now sonar.log.jsonOutput=true
  * sonar.web.sessionTimeoutInMinutes=30
  * \#add
  * sonar.cluster.enabled=false
  * sonar.search.host=
  * sonar.search.port=9200
* Update API service task definition\
  SPRING\_ELASTICSEARCH\_URIS=:9200
* Start web service
* Run DB migration through the SonarQube UI to version 9.9.
  * curl /setup
* Execute SQL:\
  UPDATE properties SET text\_value='ACCEPTED' WHERE prop\_key = 'sonar.plugins.risk.consent'
