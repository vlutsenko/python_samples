from ncclient import manager
from ncclient.xml_ import to_ele
import xml.etree.ElementTree as ET
import os

def get_and_download_yang_models_by_nodes(host, port, username, password, output_dir="downloaded_yang_models_from_device"):
    """
    Connects to a NETCONF device, retrieves the list of supported YANG models
    by parsing <identifier> and <version> nodes from <netconf-state><schemas/>,
    and then downloads each one using <get-schema>.

    Args:
        host (str): The IP address or hostname of the NETCONF device.
        port (int): The NETCONF port (usually 830).
        username (str): The username for NETCONF authentication.
        password (str): The password for NETCONF authentication.
        output_dir (str): The directory to save the downloaded YANG models.
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    try:
        print(f"Attempting to connect to NETCONF device: {host}:{port}...")
        with manager.connect(host=host,
                             port=port,
                             username=username,
                             password=password,
                             hostkey_verify=False,  # Set to True in production with proper host key management
                             device_params={'name': 'default'}) as m:

            print("Successfully connected to the device.")

            # --- Step 1: Get the list of schemas using <netconf-state><schemas/> ---
            print("\n--- Step 1: Requesting list of YANG schemas from the device's netconf-state ---")
            get_schemas_filter = """
            <filter type="subtree">
                <netconf-state xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring">
                    <schemas/>
                </netconf-state>
            </filter>
            """
            yang_modules_info = []
            try:
                schemas_response = m.get(filter=get_schemas_filter).data_xml
                root = ET.fromstring(schemas_response)

                # Define the namespace for ietf-netconf-monitoring for accurate parsing
                ns = {'monitor': 'urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring'}

                # Find all <schema> elements and extract identifier and version
                for schema_elem in root.findall('.//monitor:schema', ns):
                    identifier_elem = schema_elem.find('monitor:identifier', ns)
                    print(f" Model Name: {identifier_elem.text}")
                    version_elem = schema_elem.find('monitor:version', ns)
                    print(f"Model Version: {version_elem.text}")
                    format_elem = schema_elem.find('monitor:format', ns)
                    print(f"Model Format: {format_elem.text}")

                    if identifier_elem is not None and format_elem is not None and format_elem.text == 'ncm:yang':
                        module_name = identifier_elem.text
                        revision = version_elem.text if version_elem is not None else None # Revision might be optional
                        yang_modules_info.append({'name': module_name, 'revision': revision})

                if not yang_modules_info:
                    print("No YANG schemas (format 'yang') found in the device's netconf-state.")
                    return

                print(f"Found {len(yang_modules_info)} YANG modules to download.")

            except Exception as e:
                print(f"Error retrieving schema list from netconf-state: {e}")
                print("This might indicate that the device does not support ietf-netconf-monitoring:schemas or the request failed.")
                return

            # --- Step 2: Download each module one by one using <get-schema> ---
            print("\n--- Step 2: Downloading each YANG model individually ---")
            for i, module in enumerate(yang_modules_info):
                module_name = module['name']
                revision = module['revision']

                # Construct filename: module_name@revision.yang or module_name.yang if no revision
                filename = f"{module_name}"
                if revision:
                    filename += f"@{revision}"
                filename += ".yang"
                filepath = os.path.join(output_dir, filename)

                print(f"({i+1}/{len(yang_modules_info)}) Downloading '{module_name}' (revision: {revision if revision else 'N/A'})...")

                # Compose the <get-schema> RPC request using the extracted identifier and version
                get_schema_rpc = f"""
                <get-schema xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring">
                    <identifier>{module_name}</identifier>
                    {f'<version>{revision}</version>' if revision else ''}
                    <format>yang</format>
                </get-schema>
                """
                try:
                    # Use m.rpc to send the custom get-schema RPC
                    response = m.rpc(to_ele(get_schema_rpc))
                    root = ET.fromstring(str(response))

                    # The schema content is typically within a <data> tag in the rpc-reply
                    schema_content_elem = root.find(".//{urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring}data")

                    if schema_content_elem is not None and schema_content_elem.text:
                        schema_content = schema_content_elem.text
                        with open(filepath, "w") as f:
                            f.write(schema_content)
                        print(f"  -> Successfully saved to: {filepath}")
                    else:
                        print(f"  -> Warning: No schema content found for {module_name} in the response.")

                except Exception as e:
                    print(f"  -> Error downloading {module_name} using get-schema: {e}")
                    print("  -> This could mean the device doesn't expose this specific schema via get-schema or the request failed.")

    except manager.NCClientError as e:
        print(f"NETCONF Client Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # --- Configuration ---
    NETCONF_HOST = "localhost"  # Replace with your device's IP or hostname
    NETCONF_PORT = 6483              # Standard NETCONF port
    NETCONF_USERNAME = "admin" # Replace with your NETCONF username
    NETCONF_PASSWORD = "DZSone23456!" # Replace with your NETCONF password
    OUTPUT_DIRECTORY = "downloaded_yang_models" # Directory to save models

    # --- Run the download function ---
    get_and_download_yang_models_by_nodes(NETCONF_HOST, NETCONF_PORT, NETCONF_USERNAME, NETCONF_PASSWORD, OUTPUT_DIRECTORY)

    print("\nScript execution completed.")