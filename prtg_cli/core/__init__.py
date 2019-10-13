from dataclasses import dataclass
import json

import requests

from .converters import xml_to_json
from .config import PrtgConfig
from .constants import PRTG_REQUEST_CONFIGS


@dataclass
class Prtg:
    config: PrtgConfig

    def version(self):
        status = self.status()
        return status["status"]["Version"]

    def status(self):
        request_resource = "status"
        req_status_code, content = self._request(request_resource)
        status_data = xml_to_json(content)
        return status_data

    def sensor_types(self):
        request_resource = "sensor_types"
        status_code, content = self._request(request_resource)
        data = json.loads(content)
        return data

    def passhash(self):
        if self.config.passhash:
            return self.config.passhash

        request_resource = "passhash"
        status_code, content = self._request(request_resource)
        return content.decode()

    def _request(self, request_resource, special_params={}):
        route = PRTG_REQUEST_CONFIGS[request_resource]["route"]
        uri = f"{self.config.host}{route}"
        external_params = PRTG_REQUEST_CONFIGS[request_resource].get("params", {})
        params = {**self.config.auth, **external_params, **special_params}
        res = requests.get(uri, params=params)
        return res.status_code, res.content

    def _get_by_name_without_exception(self, resource, name):
        data = self._get(resource)
        for item in data[resource]["item"]:
            if item["name"] == name:
                return item

        return None

    def _get_by_name(self, resource, name):
        data = self._get_by_name_without_exception(resource, name)
        if data is None:
            raise Exception(
                f"We didn't found this '{name}' item in '{resource}' resource"
            )

        return data

    def _get(self, resource):
        status_code, content = self._request(resource)
        data = xml_to_json(content)
        return data

    def get(self, resource, name):
        if name == "*":
            return self._get(resource)

        return self._get_by_name(resource, name)

    def _check_existence_of_item(self, resource, item_id_or_name):
        if not item_id_or_name.isdigit():
            item = self._get_by_name(resource, item_id_or_name)
            return item["objid"]

        return item_id_or_name

    def object_state(self, state, resource, item):
        obj_id = self._check_existence_of_item(resource, item)
        request_resource = state
        status_code, content = self._request(
            request_resource, special_params={"id": obj_id}
        )
        return status_code

    def duplicate_device(self, source, target_group, target_name, target_host):
        source_id = self._check_existence_of_item("devices", source)
        target_id = self._check_existence_of_item("groups", target_group)

        device = self._get_by_name_without_exception("devices", target_name)
        if not device is None:
            raise Exception(
                f"This '{target_name}' item is exists in 'devices' resource"
            )

        special_params = {
            "id": source_id,
            "targetid": target_id,
            "name": target_name,
            "host": target_host,
        }
        request_resource = "duplicate"
        status_code, content = self._request(
            request_resource, special_params=special_params
        )
        return status_code

    def duplicate_group(self, source, target, target_name):
        source_id = self._check_existence_of_item("groups", source)
        target_id = self._check_existence_of_item("groups", target)

        group = self._get_by_name_without_exception("groups", target_name)
        if not group is None:
            raise Exception(f"This '{target_name}' item is exists in 'groups' resource")

        special_params = {"id": source_id, "targetid": target_id, "name": target_name}
        request_resource = "duplicate"
        status_code, content = self._request(
            request_resource, special_params=special_params
        )
        return status_code

    def duplicate_sensor(self, source, target_device, target_name):
        print("@TODO")
