from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.template import Template
from ...types import Response


def _get_kwargs(
    template_name: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/templates/{template_name}",
    }

    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Template]:
    if response.status_code == 200:
        response_200 = Template.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Template]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    template_name: str,
    *,
    client: Union[Client],
) -> Response[Template]:
    """Get template

     Returns a template by name.

    Args:
        template_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Template]
    """

    kwargs = _get_kwargs(
        template_name=template_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    template_name: str,
    *,
    client: Union[Client],
) -> Optional[Template]:
    """Get template

     Returns a template by name.

    Args:
        template_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Template
    """

    return sync_detailed(
        template_name=template_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    template_name: str,
    *,
    client: Union[Client],
) -> Response[Template]:
    """Get template

     Returns a template by name.

    Args:
        template_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Template]
    """

    kwargs = _get_kwargs(
        template_name=template_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    template_name: str,
    *,
    client: Union[Client],
) -> Optional[Template]:
    """Get template

     Returns a template by name.

    Args:
        template_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Template
    """

    return (
        await asyncio_detailed(
            template_name=template_name,
            client=client,
        )
    ).parsed
