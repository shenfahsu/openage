import dataformat
from struct import Struct, unpack_from
from util import dbg, zstr

from .empiresdat import endianness


class SoundItem(dataformat.Exportable):
    name_struct        = "sound_item"
    name_struct_file   = "sound"
    struct_description = "one possible file for a sound."

    data_format = (
        (dataformat.READ_EXPORT, "filename",    "char[13]"),
        (dataformat.READ_EXPORT, "resource_id",  "int32_t"),
        (dataformat.READ_EXPORT, "probablilty",  "int16_t"),
        (dataformat.READ_EXPORT, "civilisation", "int16_t"),
        (dataformat.READ_UNKNOWN, None,          "int16_t"),
    )

    def __init__(self):
        super().__init__()


class Sound(dataformat.Exportable):
    name_struct        = "sound"
    name_struct_file   = "sound"
    struct_description = "describes a sound, consisting of several sound items."

    data_format = (
        (dataformat.READ_EXPORT, "uid", "int32_t"),
        (dataformat.READ_EXPORT, "item_count", "uint16_t"),
        (dataformat.READ_UNKNOWN, None, "int32_t"),
        (dataformat.READ_EXPORT, "sound_item", dataformat.SubdataMember(
            ref_type=SoundItem,
            ref_to="uid",
            length="item_count",
        )),
    )

    def __init__(self):
        super().__init__()


class SoundData(dataformat.Exportable):

    name_struct        = "sound_data"
    name_struct_file   = "gamedata"
    struct_description = "sound list."

    data_format = (
        (dataformat.READ_EXPORT, "sound_count", "uint16_t"),
        (dataformat.READ_EXPORT, "sounds", dataformat.SubdataMember(
            ref_type=Sound,
            length="sound_count",
        )),
    )

    def __init__(self):
        super().__init__()
