from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HistogramStats")


@_attrs_define
class HistogramStats:
    """Histogram stats

    Attributes:
        average (Union[Unset, float]): Average request duration
        p50 (Union[Unset, float]): P50 request duration
        p90 (Union[Unset, float]): P90 request duration
        p99 (Union[Unset, float]): P99 request duration
    """

    average: Union[Unset, float] = UNSET
    p50: Union[Unset, float] = UNSET
    p90: Union[Unset, float] = UNSET
    p99: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        average = self.average

        p50 = self.p50

        p90 = self.p90

        p99 = self.p99

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if average is not UNSET:
            field_dict["average"] = average
        if p50 is not UNSET:
            field_dict["p50"] = p50
        if p90 is not UNSET:
            field_dict["p90"] = p90
        if p99 is not UNSET:
            field_dict["p99"] = p99

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        if not src_dict:
            return None
        d = src_dict.copy()
        average = d.pop("average", UNSET)

        p50 = d.pop("p50", UNSET)

        p90 = d.pop("p90", UNSET)

        p99 = d.pop("p99", UNSET)

        histogram_stats = cls(
            average=average,
            p50=p50,
            p90=p90,
            p99=p99,
        )

        histogram_stats.additional_properties = d
        return histogram_stats

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
