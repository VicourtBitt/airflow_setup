# Observations
If you get any error such as "unable to handle processor" you should run the following command:
```shell
sudo chown -R 1000 . # This command pass all the folders and files to your user
```
The error that I relate from above usually occurs because airflow create those folders with the admin user,
and the airflow runtime does not have those admin permissions to write within the folders, so when you pass it
into your user, you gain the right to edit the folder in question.

Also, check the .env, make the AIRFLOW_UID variable match the output of this command:
```shell
id -u # Will retrieve your user ID
```