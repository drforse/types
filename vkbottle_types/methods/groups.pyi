import typing

from vkbottle_types.responses import groups

from vkbottle_types.methods.base_category import BaseCategory


class GroupsCategory(BaseCategory):
    @typing.overload
    async def get_members(
            self,
            group_id: typing.Optional[str] = ...,
            sort: typing.Optional[str] = ...,
            offset: typing.Optional[int] = ...,
            count: typing.Optional[int] = ...,
            filter: None = ...,
            fields: None = ...,
            **kwargs
    ) -> groups.GetMembersResponseModel: ...

    @typing.overload
    async def get_members(
            self,
            group_id: typing.Optional[str] = ...,
            sort: typing.Optional[str] = ...,
            offset: typing.Optional[int] = ...,
            count: typing.Optional[int] = ...,
            filter: str = ...,
            fields: None = ...,
            **kwargs
    ) -> groups.GetMembersFilterResponseModel: ...

    @typing.overload
    async def get_members(
            self,
            group_id: typing.Optional[str] = ...,
            sort: typing.Optional[str] = ...,
            offset: typing.Optional[int] = ...,
            count: typing.Optional[int] = ...,
            filter: None = ...,
            fields: typing.List[str] = ...,
            **kwargs
    ) -> groups.GetMembersFieldsResponseModel: ...

    @typing.overload
    async def get_members(
            self,
            group_id: typing.Optional[str] = ...,
            sort: typing.Optional[str] = ...,
            offset: typing.Optional[int] = ...,
            count: typing.Optional[int] = ...,
            filter: str = ...,
            fields: typing.List[str] = ...,
            **kwargs
    ) -> groups.GetMembersFieldsResponseModel: ...

    async def get_members(
            self,
            group_id: typing.Optional[str] = ...,
            sort: typing.Optional[str] = ...,
            offset: typing.Optional[int] = ...,
            count: typing.Optional[int] = ...,
            fields: typing.Optional[typing.List[str]] = ...,
            filter: typing.Optional[str] = ...,
            **kwargs
    ) -> groups.GetMembersResponseModel:
        ...
