from .access_tokens import AccessTokensClient
from .channels import ChannelsClient
from .memberships import MembershipsClient
from .profiles import ProfilesClient
from .devices import DevicesClient
from .bot import BotClient


CLIENTS = [
    AccessTokensClient,
    ChannelsClient,
    MembershipsClient,
    ProfilesClient,
    DevicesClient,
    BotClient,
]


clients = {c.name: c for c in CLIENTS}
