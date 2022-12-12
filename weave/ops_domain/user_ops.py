from ..compile_domain import wb_gql_op_plugin
from ..api import op
from .. import weave_types as types
from . import wb_domain_types as wdt
from ..language_features.tagging.make_tag_getter_op import make_tag_getter_op
from .wandb_domain_gql import (
    gql_prop_op,
    gql_direct_edge_op,
    gql_connection_op,
    gql_root_op,
)

# Section 1/6: Tag Getters
# None

# Section 2/6: Root Ops
gql_root_op(
    "root-viewer",
    "viewer",
    wdt.UserType,
)

gql_root_op(
    "root-user",
    "user",
    wdt.UserType,
    {
        "userName": types.String(),
    },
    lambda inputs: f'userName: "{inputs["userName"]}"',
)

# Section 3/6: Attribute Getters
# None

# Section 4/6: Direct Relationship Ops
# None

# Section 5/6: Connection Ops
gql_connection_op(
    "user-entities",
    wdt.UserType,
    "teams",
    wdt.EntityType,
    {},
    lambda inputs: f"first: 50",
)

# Section 6/6: Non Standard Business Logic Ops
@op(name="user-link")
def link(project: wdt.User) -> wdt.Link:
    return wdt.Link(project.gql["name"], project.gql["name"])
