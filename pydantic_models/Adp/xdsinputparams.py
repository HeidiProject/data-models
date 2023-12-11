from pydantic import BaseModel
from typing import Any, List, Union


class XdsInputParams(BaseModel):
    jobs: str
    numberOfJobs: str
    numberOfProcessors: str
    nodes: str
    beamXpix_XDS: float
    beamYpix_XDS: float
    detectorDistance: int
    oscillationAngle: float
    wavelength: float
    dataFrames: str
    firstIndex: int
    numFrames: int
    lastIndex: str
    excludeReference: str
    referenceData: str
    excludeSG: str
    sgNumber: str
    excludeUnitCell: str
    cellA: str
    cellB: str
    cellC: str
    cellAlpha: str
    cellBeta: str
    cellGamma: str
    refineIntegrate: str
    friedel: str
    highResolution: float
    trustedHigh: str
    excludePixelsInSpot: str
    pixelsInSpot: str
    nx: int
    ny: int
    overload: int

class FastXds2Item(BaseModel):
    order: str
    star: str
    lattice_character: str
    bravais_lattice: str
    quality_of_fit: float
    cell_a: float
    cell_b: float
    cell_c: float
    alpha: float
    beta: float
    gamma: float


class FastXds3Item(BaseModel):
    order: str
    resolution_limit: Union[float, str]
    observed_reflections: int
    unique_reflections: int
    possible_reflections: int
    completeness: float
    r_factor_observed: float
    r_factor_expected: float
    Isigma: float
    rmeas: float
    cc_half: float
    anomalous_correlation: int
    sigAno: float


class FastXds3Params(BaseModel):
    spaceGroupNumber: str
    spaceGroupLabel: str
    a: float
    b: float
    c: float
    alpha: float
    beta: float
    gamma: float
    mosaicity: float
    isa: float
    wilsonBfactor: float
    xds_input_params: XdsInputParams

class GopyItem(BaseModel):
    order: str
    resolution_limit: Union[float, str]
    observed_reflections: int
    unique_reflections: int
    possible_reflections: int
    completeness: float
    r_factor_observed: float
    r_factor_expected: float
    Isigma: float
    rmeas: float
    cc_half: float
    anomalous_correlation: int
    sigAno: float

class TwinningItem(BaseModel):
    order: str
    label: str
    value: float
    untwinned: float
    perfect_twin: float


class SpacegroupItem(BaseModel):
    order: Union[int, str]
    sg: str
    sg_nr: int
    LGconfidence: Union[float, str]
    SGconfidence: Union[float, str]

class GopyParams(BaseModel):
    spaceGroupNumber: str
    spaceGroupLabel: str
    a: float
    b: float
    c: float
    alpha: float
    beta: float
    gamma: float
    mosaicity: float
    isa: float
    wilsonBfactor: float
    command: None
    twinning: List[TwinningItem]
    spacegroup_pointless: List[str]
    spacegroup: List[SpacegroupItem]

class Result(BaseModel):
    fast_xds_2: List[FastXds2Item]
    fast_xds_3: List[FastXds3Item]
    fast_xds_3_params: FastXds3Params
    gopy: List[GopyItem]
    gopy_params: GopyParams
    fast_xds_1: List
    fast_xds_1_params: List
    fast_xds_2_params: List