import xml.etree.ElementTree as ET
from .. import NAMESPACE


class PermissionItem(object):

    @classmethod
    def from_response(cls, resp):
        all_permission_items = list()
        parsed_response = ET.fromstring(resp)
        all_grantee_xml = parsed_response.findall('.//t:granteeCapabilities', namespaces=NAMESPACE)
        for _ in all_grantee_xml:
            permission_item = cls()
            all_permission_items.append(permission_item)
        return all_permission_items
