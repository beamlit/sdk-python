from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.knowledgebase import Knowledgebase
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/knowledgebases",
    }

    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[list["Knowledgebase"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Knowledgebase.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[list["Knowledgebase"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[Client],
) -> Response[list["Knowledgebase"]]:
    """List knowledgebases

     Returns a list of all knowledgebases in the workspace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Knowledgebase']]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[Client],
) -> Optional[list["Knowledgebase"]]:
    """List knowledgebases

     Returns a list of all knowledgebases in the workspace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Knowledgebase']
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[Client],
) -> Response[list["Knowledgebase"]]:
    """List knowledgebases

     Returns a list of all knowledgebases in the workspace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Knowledgebase']]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[Client],
) -> Optional[list["Knowledgebase"]]:
    """List knowledgebases

     Returns a list of all knowledgebases in the workspace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Knowledgebase']
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
