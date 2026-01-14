# 1. Import the library
from inference_sdk import InferenceHTTPClient

# 2. Connect to your workflow
client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="RJVsuf7wVUXCCYtfuawt"
)

# 3. Run your workflow on an image
result = client.run_workflow(
    workspace_name="asep81",
    workflow_id="detect-count-and-visualize-3",
    images={
        "image": "YOUR_IMAGE.jpg" # Path to your image file
    },
    use_cache=True # Speeds up repeated requests
)

# 4. Get your results
print(result)
