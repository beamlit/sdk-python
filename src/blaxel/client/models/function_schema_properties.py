from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.function_schema import FunctionSchema


T = TypeVar("T", bound="FunctionSchemaProperties")


@_attrs_define
class FunctionSchemaProperties:
    """Properties of the schema"""

    additional_properties: dict[str, "FunctionSchema"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if type(prop) == dict:
                field_dict[prop_name] = prop
            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.function_schema import FunctionSchema

        if not src_dict:
            return None
        d = src_dict.copy()
        function_schema_properties = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = FunctionSchema.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        function_schema_properties.additional_properties = additional_properties
        return function_schema_properties

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "FunctionSchema":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "FunctionSchema") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
