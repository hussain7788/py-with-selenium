import yaml
import json
import os
# Replace 'your_postman_collection.json' with the path to your Postman collection JSON file
postman_collection_path = 'hashtag_collection.postman_collection.json'

# Load Postman collection
with open(postman_collection_path, 'r') as file:
    postman_collection = json.load(file)

# Convert to YAML
swagger_yaml = yaml.dump(postman_collection, default_flow_style=False)

# Replace 'output_openapi.yaml' with the desired name for the generated OpenAPI YAML file
output_path = 'output_openapi.yaml'

# Save the generated OpenAPI YAML document
with open(output_path, 'w') as file:
    file.write(swagger_yaml)
