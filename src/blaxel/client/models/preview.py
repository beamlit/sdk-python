from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preview_metadata import PreviewMetadata
    from ..models.preview_spec import PreviewSpec


T = TypeVar("T", bound="Preview")


@_attrs_define
class Preview:
    """Preview of a Resource

    Attributes:
        metadata (Union[Unset, PreviewMetadata]): PreviewMetadata
        spec (Union[Unset, PreviewSpec]): Preview of a Resource
    """

    metadata: Union[Unset, "PreviewMetadata"] = UNSET
    spec: Union[Unset, "PreviewSpec"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata: Union[Unset, dict[str, Any]] = UNSET
        if self.metadata and not isinstance(self.metadata, Unset) and not isinstance(self.metadata, dict):
            metadata = self.metadata.to_dict()
        elif self.metadata and isinstance(self.metadata, dict):
            metadata = self.metadata

        spec: Union[Unset, dict[str, Any]] = UNSET
        if self.spec and not isinstance(self.spec, Unset) and not isinstance(self.spec, dict):
            spec = self.spec.to_dict()
        elif self.spec and isinstance(self.spec, dict):
            spec = self.spec

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.preview_metadata import PreviewMetadata
        from ..models.preview_spec import PreviewSpec

        if not src_dict:
            return None
        d = src_dict.copy()
        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PreviewMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PreviewMetadata.from_dict(_metadata)

        _spec = d.pop("spec", UNSET)
        spec: Union[Unset, PreviewSpec]
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = PreviewSpec.from_dict(_spec)

        preview = cls(
            metadata=metadata,
            spec=spec,
        )

        preview.additional_properties = d
        return preview

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
