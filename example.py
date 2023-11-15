import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load token from .env file. Don't put the .env file in source control (git/devops)
token = os.environ.get("PERSONAL_TOKEN")
project_id = os.environ.get("PROJECT_ID")

# API Documentation
# (documentation: https://api.fieldmanager.io/labmanager/api/docs)
api_base_url = "https://api.fieldmanager.io/labmanager/api"

test_type = "TRIAXIAL_COMPRESSION"

# ALL TEST TYPES:
# test_type = "WATER_CONTENT"
# test_type = "VISUAL_DESCRIPTION"
# test_type = "BULK_DENSITY_UNIT_WEIGHT"
# test_type = "FALL_CONE"
# test_type = "LIQUID_PLASTIC_LIMIT"
# test_type = "PARTICLE_DENSITY"
# test_type = "PARTICLE_SIZE_DISTRIBUTION"
# test_type = "POCKET_PENETROMETER"
# test_type = "UNIAXIAL_COMPRESSION_STRENGTH"
# test_type = "TRIAXIAL_COMPRESSION"
# test_type = "DIRECT_SIMPLE_SHEAR"
# test_type = "CONSTANT_RATE_OF_STRAIN"
# test_type = "INCREMENTAL_LOADING"
# test_type = "RESSONANT_COLUMN"
# test_type = "RING_SHEAR"
# test_type = "UNDRAINED_UNCONSOLIDATED"
# test_type = "DIRECT_SHEAR"
# test_type = "POINT_LOAD"
# test_type = "TENSILE_STRENGTH"

# Optional call that filters by test type
api_url = f"{api_base_url}/projects/{project_id}/tests?test_type={test_type}"

# Call to get all labtests irregardless of type
# api_url = f"{api_base_url}/projects/{project_id}/tests"

# Setting authentication and other request headers
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
}

# Making the actual API request
api_response = requests.get(api_url, headers=headers)

# Use the data
print(json.dumps(api_response.json(), indent=2))
