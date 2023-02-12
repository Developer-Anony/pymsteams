from _typeshed import Incomplete

from influxdb_client.domain.expression import Expression

class IndexExpression(Expression):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, type: Incomplete | None = ..., array: Incomplete | None = ..., index: Incomplete | None = ...) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def array(self): ...
    @array.setter
    def array(self, array) -> None: ...
    @property
    def index(self): ...
    @index.setter
    def index(self, index) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
