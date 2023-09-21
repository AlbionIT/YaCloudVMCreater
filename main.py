import requests
import argparse
import subprocess


def create_vm(name: str, user_name: str, cores: str, size: str, imageId: str) -> None:
    url = "https://compute.api.cloud.yandex.net/compute/v1/instances"
    body = {
        "folderId": "b1gpv0e0eqbueff2k0n2",
        "name": f"{name}",
        "zoneId": "ru-central1-b",
        "platformId": "standard-v3",
        "resourcesSpec": {
            "memory": "2147483648",
            "cores": f"{cores}"
        },
        "metadata": {
            "user-data": f"#cloud-config\nusers:\n  - name: {user_name}\n    groups: sudo\n    shell: /bin/bash\n    sudo: ['ALL=(ALL) NOPASSWD:ALL']\n    ssh-authorized-keys:\n      - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIII3q7Av+gTNW2wfUIaH2rpbgUD+MpKi6ff283MeYUr9 itdev@itdev-virtual-machine "
        },
        "bootDiskSpec": {
            "diskSpec": {
                "size": f"{size}",
                "imageId": f"{imageId}"
            }
        },
        "networkInterfaceSpecs": [
            {
                "subnetId": "e2l4gittqfrhhngtahed",
                "primaryV4AddressSpec": {
                    "oneToOneNatSpec": {
                        "ipVersion": "IPV4"
                    }
                }
            }
        ]
    }


    command_output = subprocess.check_output(["yc", "iam", "create-token"])
    output_string = command_output.decode("utf-8").strip()
    response=requests.post(url,json=body,headers={"Authorization": f"Bearer {output_string}"})
    print(response.text)

create_vm("alby","albyit1","2","2621440000","fd8rc75pn12fe3u2dnmb")
