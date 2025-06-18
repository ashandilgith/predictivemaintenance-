from huggingface_hub import HfApi
import os
import sys

def push_model_to_hub():
    """
    Authenticates with the Hugging Face Hub using an environment variable
    and uploads the trained model file.
    """
    print("--- Starting Model Upload Process ---")

    # This gets the secret token passed in from the YAML file
    hf_token = os.environ.get("HF_TOKEN")
    if not hf_token:
        print("Fatal: HF_TOKEN secret not found.")
        sys.exit(1) # Exit with an error code

    # These are standard variables provided by GitHub Actions
    repo_owner = os.environ.get("GITHUB_REPOSITORY_OWNER")
    repo_name_base = os.environ.get("GITHUB_REPOSITORY_NAME")
    
    if not repo_owner or not repo_name_base:
        print("Fatal: Could not determine repository owner or name from GitHub environment variables.")
        sys.exit(1)
        
    # We will create a Hugging Face repo with a name like "your-username/your-repo-name-model"
    repo_id = f"{repo_owner}/{repo_name_base}-model"
    
    print(f"Target Hugging Face repository: {repo_id}")

    # Check if the model file exists before trying to upload
    if not os.path.exists("model.joblib"):
        print(f"Fatal: Model file 'model.joblib' not found. Please ensure train.py runs successfully first.")
        sys.exit(1)

    try:
        # Initialize the Hugging Face API client
        api = HfApi()

        # Create the repository on the Hub. `exist_ok=True` means it won't fail if the repo is already there.
        print(f"Ensuring repository '{repo_id}' exists on the Hub...")
        api.create_repo(
            repo_id=repo_id,
            token=hf_token,
            exist_ok=True,
        )

        # Upload the model file
        print("Uploading 'model.joblib'...")
        api.upload_file(
            path_or_fileobj="model.joblib",
            path_in_repo="model.joblib", # The name of the file on the Hub
            repo_id=repo_id,
            token=hf_token,
            commit_message="Pushed baseline model from GitHub Actions"
        )
        print(f"✅ Model successfully pushed to https://huggingface.co/{repo_id}")

    except Exception as e:
        print(f"An error occurred during upload: {e}")
        sys.exit(1)

if __name__ == "__main__":
    push_model_to_hub()