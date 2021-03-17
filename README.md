# miles-test-gear

Note: an `.env` file with the following contents is required to run the gear_upload.py script

```
FW_API_KEY=domain:18digitkey
```

### Development

Build a docker image

`docker build -t overcoded/fw-test-app:0.1.4` where "overcoded" is your docker hub username, "fw-test-app" is your application name, and "0.1.4" is your version

`docker push overcoded/fw-test-app:0.1.4` using the same tag you just built

Update your `manifest.json` to use the newest tag, in this case custom.gear-builder.image should be "overcoded/fw-test-app:0.1.4" 

Upload to flywheel

`fw gear upload`
