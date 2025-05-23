Module blaxel.models.location_response
======================================

Classes
-------

`LocationResponse(continent: blaxel.types.Unset | str = <blaxel.types.Unset object>, country: blaxel.types.Unset | str = <blaxel.types.Unset object>, flavors: blaxel.types.Unset | list['Flavor'] = <blaxel.types.Unset object>, location: blaxel.types.Unset | str = <blaxel.types.Unset object>, status: blaxel.types.Unset | str = <blaxel.types.Unset object>)`
:   Location availability for policies
    
    Attributes:
        continent (Union[Unset, str]): Continent of the location
        country (Union[Unset, str]): Country of the location
        flavors (Union[Unset, list['Flavor']]): Hardware flavors available in the location
        location (Union[Unset, str]): Name of the location
        status (Union[Unset, str]): Status of the location
    
    Method generated by attrs for class LocationResponse.

    ### Static methods

    `from_dict(src_dict: dict[str, typing.Any]) ‑> ~T`
    :

    ### Instance variables

    `additional_keys: list[str]`
    :

    `additional_properties`
    :

    `continent`
    :

    `country`
    :

    `flavors`
    :

    `location`
    :

    `status`
    :

    ### Methods

    `to_dict(self) ‑> dict[str, typing.Any]`
    :