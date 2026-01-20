import json


read_response = {
    "data": {
        "data": {
            "key_1": "val_1",
            "key_2": "val_2",
            "key_3": {
                "key_4": "val_4",
                "key_5": {
                    "key_6": "val_6"
                }
            }
        }
    }
}

expected_result = {
    "key_1" : "val_1",
    "key_2" : "val_2",
    "key_3/key_4 ": "val_4",
    "key_3/key_5/key_6": "val_6"
}



all_secrets = {}

mount_point = 'project/skyway-slack-bot'
secret_path = 'runtime/dev/slack-bot'
current_path = 'runtime/dev'
key = 'slack-bot'



    
def regular_flow():
    if isinstance(read_response["data"]["data"], dict):
        # Generate flattened keys for AWS Secrets Manager
        # Build the full path within the environment
        full_path_in_env = f"{current_path}{key}"

        for secret_key, secret_val in read_response["data"][
            "data"
        ].items():
            flattened_key = f"{full_path_in_env}/{secret_key}"
            all_secrets[flattened_key] = secret_val
    else:
        all_secrets[f"{mount_point}{secret_path}"] = read_response[
            "data"
        ]["data"]
    
    print(all_secrets)
    

#im going to send read_response["data"]["data"] which is the response from reading a secret value.

def recursive_function(my_param=read_response["data"]["data"], prefix=""):
    """
    Recursively flattens a nested dictionary structure.
    
    Args:
        my_param: The dictionary or value to process
        prefix: The current path prefix for nested keys
    
    Returns:
        dict: Flattened dictionary with path-like keys
    """
    result = {}
    
    if isinstance(my_param, dict):
        for key, value in my_param.items():
            # Build the new path
            new_prefix = f"{prefix}/{key}" if prefix else key
            
            if isinstance(value, dict):
                # Recursively process nested dictionaries
                nested_result = recursive_function(value, new_prefix)
                result.update(nested_result)
            else:
                # Add leaf values to result
                result[new_prefix] = value
    else:
        # If it's not a dict, just return it with the current prefix
        result[prefix] = my_param
    
    return result


# regular_flow()

# print("\n--- Testing recursive_function ---")
# recursive_result = recursive_function()
# print("Recursive result:")
# print(recursive_result)

# print("\n--- Expected result ---")
# print(expected_result)

