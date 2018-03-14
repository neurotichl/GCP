# Google App Engine

This example code is executed in local environment

## Set up in local
1. Install google-sdk
2. Determine path to dev_appserver.py (Located inside google-cloud-sdk/bin/dev_appserver.py)
3. cd into the application folder and run:
   ```
   python C://.../dev_appserver.py app.yaml
   ```

## Folder structure
```
+- app.yaml
+- cron.yaml
+- queue.yaml
+- appengine_config.py
+- main.py
+- requirements.txt
```

### App Engine local dev UI
![local ui](https://github.com/neurotichl/GCP/raw/master/img/local_gae1.PNG)

### Insert data into datastore
- Use ndb model
![call API](https://github.com/neurotichl/GCP/raw/master/img/local_gae2.PNG)
![datastore](https://github.com/neurotichl/GCP/raw/master/img/local_gae_datastore.PNG)

### Cron job scheduling
- target: service name defined in `app.yaml`
![cron](https://github.com/neurotichl/GCP/raw/master/img/local_gae_cron.PNG)
