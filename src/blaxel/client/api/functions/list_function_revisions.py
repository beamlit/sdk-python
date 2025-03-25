from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.revision_metadata import RevisionMetadata
from ...types import Response


def _get_kwargs(
    function_name: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/functions/{function_name}/revisions",
    }

    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[RevisionMetadata]:
    if response.status_code == 200:
        response_200 = RevisionMetadata.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[RevisionMetadata]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    function_name: str,
    *,
    client: Union[Client],
) -> Response[RevisionMetadata]:
    """List function revisions

     Returns revisions for a function by name.

    Args:
        function_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RevisionMetadata]
    """

    kwargs = _get_kwargs(
        function_name=function_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    function_name: str,
    *,
    client: Union[Client],
) -> Optional[RevisionMetadata]:
    """List function revisions

     Returns revisions for a function by name.

    Args:
        function_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RevisionMetadata
    """

    return sync_detailed(
        function_name=function_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    function_name: str,
    *,
    client: Union[Client],
) -> Response[RevisionMetadata]:
    """List function revisions

     Returns revisions for a function by name.

    Args:
        function_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RevisionMetadata]
    """

    kwargs = _get_kwargs(
        function_name=function_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    function_name: str,
    *,
    client: Union[Client],
) -> Optional[RevisionMetadata]:
    """List function revisions

     Returns revisions for a function by name.

    Args:
        function_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RevisionMetadata
    """

    return (
        await asyncio_detailed(
            function_name=function_name,
            client=client,
        )
    ).parsed
