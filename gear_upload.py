import json
import flywheel
import os
api_key = os.environ.get('FW_API_KEY') # or populate manually
domain = api_key.split(":")[0]
fw = flywheel.Client()
with open('./manifest.json','r') as fp:
    manifest = json.load(fp)
dest_repo = f"{domain}/{manifest['name']}"
dest_tag = manifest['version']
gear_doc = {
    "category": manifest['custom']['gear-builder']['category'],
    "gear": manifest,
    "exchange": {
        "rootfs-url": f"docker://{dest_repo}:{dest_tag}"
    }
}
fw.add_gear(manifest['name'], gear_doc)
