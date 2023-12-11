from pydantic import BaseModel

# File Name could Possible Renamed to something that better fits the context.

class FQDNBase(BaseModel):
    fast_xds_1: str
    fast_xds_2: str
    fast_xds_3: str

class AngularRangeBase(BaseModel):
    fast_xds_1: float
    fast_xds_2: float
    fast_xds_3: float

class AdpStatusBase(BaseModel):
    fast_xds_1: str
    fast_xds_2: str
    fast_xds_3: str

class AdpInfoBase(BaseModel):
    fast_xds_1: str
    fast_xds_2: str
    fast_xds_3: str

class FastXdsBase(BaseModel):
    pending: str    
    running: str
    completed: str

class FastXds1(FastXdsBase):
    pass


class FastXds2(FastXdsBase):
    pass

class FastXds3(FastXdsBase):
    pass

class StatusHistoryBase(BaseModel):
    fast_xds_1: FastXds1
    fast_xds_2: FastXds2
    fast_xds_3: FastXds3

class Gopy(FastXdsBase):
    pass

class Autoproc(FastXdsBase):
    pass

class Xia2dials(FastXdsBase):
    pass