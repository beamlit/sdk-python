Module blaxel.models.pending_invitation_render
==============================================

Classes
-------

`PendingInvitationRender(email: blaxel.types.Unset | str = <blaxel.types.Unset object>, invited_at: blaxel.types.Unset | str = <blaxel.types.Unset object>, invited_by: blaxel.types.Unset | ForwardRef('PendingInvitationRenderInvitedBy') = <blaxel.types.Unset object>, role: blaxel.types.Unset | str = <blaxel.types.Unset object>, workspace: blaxel.types.Unset | ForwardRef('PendingInvitationRenderWorkspace') = <blaxel.types.Unset object>, workspace_details: blaxel.types.Unset | ForwardRef('PendingInvitationWorkspaceDetails') = <blaxel.types.Unset object>)`
:   Pending invitation in workspace
    
    Attributes:
        email (Union[Unset, str]): User email
        invited_at (Union[Unset, str]): Invitation date
        invited_by (Union[Unset, PendingInvitationRenderInvitedBy]): Invited by
        role (Union[Unset, str]): ACL role
        workspace (Union[Unset, PendingInvitationRenderWorkspace]): Workspace
        workspace_details (Union[Unset, PendingInvitationWorkspaceDetails]): Workspace details
    
    Method generated by attrs for class PendingInvitationRender.

    ### Static methods

    `from_dict(src_dict: dict[str, typing.Any]) ‑> ~T`
    :

    ### Instance variables

    `additional_keys: list[str]`
    :

    `additional_properties`
    :

    `email`
    :

    `invited_at`
    :

    `invited_by`
    :

    `role`
    :

    `workspace`
    :

    `workspace_details`
    :

    ### Methods

    `to_dict(self) ‑> dict[str, typing.Any]`
    :