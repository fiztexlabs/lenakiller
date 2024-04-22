# -*- coding: utf-8 -*-
import ctypes

RGP = ctypes.cdll.LoadLibrary('./libs/RGPx64.dll')  # подключаем библиотеку C++


# ============================== ПАРАМЕТРЫ В КРИТИЧЕСКОЙ ТОЧКЕ ==============================

# температура в критической точке [К]
# Входные параметры:
# id - идентификатор вещества
TCRIT = RGP.rgpTCRIT
TCRIT.restype = ctypes.c_double


def rgpTCRIT(id):
    id = ctypes.c_int(id)
    return TCRIT(id)


# давление в критической точке [Па]
# Входные параметры:
# id - идентификатор вещества
PCRIT = RGP.rgpPCRIT
PCRIT.restype = ctypes.c_double


def rgpPCRIT(id):
    id = ctypes.c_int(id)
    return PCRIT(id)


# плотность в критической точке [кг/м3]
# Входные параметры:
# id - идентификатор вещества
DCRIT = RGP.rgpDCRIT
DCRIT.restype = ctypes.c_double


def rgpDCRIT(id):
    id = ctypes.c_int(id)
    return DCRIT(id)


# ============================== ПАРАМЕТРЫ В ТРОЙНОЙ ТОЧКЕ ==============================

# температура в тройной точке [К]
# Входные параметры:
# id - идентификатор вещества
TTRIP = RGP.rgpTTRIP
TTRIP.restype = ctypes.c_double


def rgpTTRIP(id):
    id = ctypes.c_int(id)
    return TTRIP(id)


# давление в тройнй точке [Па]
# Входные параметры:
# id - идентификатор вещества
PTRIP = RGP.rgpPTRIP
PTRIP.restype = ctypes.c_double


def rgpPTRIP(id):
    id = ctypes.c_int(id)
    return PTRIP(id)


# ============================== f(P, T) ОДНОФАЗНАЯ ОБЛАСТЬ ==============================

# номер области на диаграмме состояния
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
# Выходные параметры:
# 1 - жидкая фаза,
# 2 - газовая фаза,
# 3 - жидкая фаза,
#			!! 4 - двухфазная область, при попадании параметров в двухфазную область возвращает 2
# 5 - сверхкритическая область
# 6 - твердая фаза
STATEAREAPT = RGP.rgpSTATEAREAPT
STATEAREAPT.restype = ctypes.c_int


def rgpSTATEAREAPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return STATEAREAPT(id, P, T)


# удельный объём в однофазной области [м3/кг]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
VPT = RGP.rgpVPT
VPT.restype = ctypes.c_double


def rgpVPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return VPT(id, P, T)


# плотность в однофазной области [кг/м3]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
DPT = RGP.rgpDPT
DPT.restype = ctypes.c_double


def rgpDPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return DPT(id, P, T)


# удельная внутренняя энергия в однофазной области [Дж/кг]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
UPT = RGP.rgpUPT
UPT.restype = ctypes.c_double


def rgpUPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return UPT(id, P, T)


# удельная энтальпия в однофазной области [Дж/кг]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
HPT = RGP.rgpHPT
HPT.restype = ctypes.c_double


def rgpHPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return HPT(id, P, T)


# удельная энтропия в однофазной области [Дж/(кг*К)]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
SPT = RGP.rgpSPT
SPT.restype = ctypes.c_double


def rgpSPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return SPT(id, P, T)


# удельная изобарная теплоемкость в однофазной области [Дж/(кг*К)]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
CPPT = RGP.rgpCPPT
CPPT.restype = ctypes.c_double


def rgpCPPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return CPPT(id, P, T)


# удельная изобарная теплоемкость в однофазной области [Дж/(кг*К)]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
CVPT = RGP.rgpCVPT
CVPT.restype = ctypes.c_double


def rgpCVPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return CVPT(id, P, T)


# скорость звука в однофазной области [м/с]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
WPT = RGP.rgpWPT
WPT.restype = ctypes.c_double


def rgpWPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return WPT(id, P, T)


# показатель изоэнтропы в однофазной области [-]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
KPT = RGP.rgpKPT
KPT.restype = ctypes.c_double


def rgpKPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return KPT(id, P, T)


# динамическая вязкость в однофазной области [Па*с]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
DYNVISPT = RGP.rgpDYNVISPT
DYNVISPT.restype = ctypes.c_double


def rgpDYNVISPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return DYNVISPT(id, P, T)


# кинематическая вязкость в однофазной области [м2/с]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
KINVISPT = RGP.rgpKINVISPT
KINVISPT.restype = ctypes.c_double


def rgpKINVISPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return KINVISPT(id, P, T)


# теплопроводность в однофазной области [Вт/(м*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
THERMCONDPT = RGP.rgpTHERMCONDPT
THERMCONDPT.restype = ctypes.c_double


def rgpTHERMCONDPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return THERMCONDPT(id, P, T)


# число Прандтля в однофазной области [-]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
PRANDTLEPT = RGP.rgpPRANDTLEPT
PRANDTLEPT.restype = ctypes.c_double


def rgpPRANDTLEPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return PRANDTLEPT(id, P, T)


# производная удельного объема по давлению при постоянной температуре в однофазной области [м3 / (кг * Па)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
DVDPTPT = RGP.rgpDVDPTPT
DVDPTPT.restype = ctypes.c_double


def rgpDVDPTPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return DVDPTPT(id, P, T)


# производная удельного объема по температуре при постоянном давлении в однофазной области [м3/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
DVDTPPT = RGP.rgpDVDTPPT
DVDTPPT.restype = ctypes.c_double


def rgpDVDTPPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return DVDTPPT(id, P, T)


# производная плотности по давлению при постоянной температуре в однофазной области [с2/м2]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
DDDPTPT = RGP.rgpDDDPTPT
DDDPTPT.restype = ctypes.c_double


def rgpDDDPTPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return DDDPTPT(id, P, T)


# производная плотности по температуре при постоянном давлении в однофазной области [кг/(К*м3)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
DDDTPPT = RGP.rgpDDDTPPT
DDDTPPT.restype = ctypes.c_double


def rgpDDDTPPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return DDDTPPT(id, P, T)


# производная удельного объема по энтальпии при постоянном давлении в однофазной области [1/Па]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
DVDHPPT = RGP.rgpDVDHPPT
DVDHPPT.restype = ctypes.c_double


def rgpDVDHPPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return DVDHPPT(id, P, T)


# производная удельного объема по давлению при постоянной энтальпии в однофазной области [(с2*м4)/кг2]
# входные параметры:
# P - давление [Па]
# T - температура [K]
DVDPHPT = RGP.rgpDVDPHPT
DVDPHPT.restype = ctypes.c_double


def rgpDVDPHPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return DVDPHPT(id, P, T)


# производная плотности по энтальпии при постоянном давлении в однофазной области [кг*с2/м5]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
DDDHPPT = RGP.rgpDDDHPPT
DDDHPPT.restype = ctypes.c_double


def rgpDDDHPPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return DDDHPPT(id, P, T)


# производная плотности по давлению при постоянной энтальпии в однофазной области [с2/м2]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
DDDPHPT = RGP.rgpDDDPHPT
DDDPHPT.restype = ctypes.c_double


def rgpDDDPHPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return DDDPHPT(id, P, T)


# производная удельной энтальпии по давлению при постоянной температуре в однофазной области [Дж/(кг*Па)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
DHDPTPT = RGP.rgpDHDPTPT
DHDPTPT.restype = ctypes.c_double


def rgpDHDPTPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return DHDPTPT(id, P, T)


# производная удельной энтальпии по температуре при постоянном давлении в однофазной области [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# T - температура [K]
DHDTPPT = RGP.rgpDHDTPPT
DHDTPPT.restype = ctypes.c_double


def rgpDHDTPPT(id, P, T):
    P = ctypes.c_double(P)
    T = ctypes.c_double(T)
    return DHDTPPT(id, P, T)


# ============================== f(D, T) ==============================
# давление [Па]
# Входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
PDT = RGP.rgpPDT
PDT.restype = ctypes.c_double


def rgpPDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return PDT(id, D, T)


# удельная внутренняя энергия [Дж/кг]
# Входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
UDT = RGP.rgpUDT
UDT.restype = ctypes.c_double


def rgpUDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return UDT(id, D, T)


# удельная энтальпия [Дж/кг]
# Входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
HDT = RGP.rgpHDT
HDT.restype = ctypes.c_double


def rgpHDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return HDT(id, D, T)


# удельная энтропия [Дж/(кг*К)]
# Входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
SDT = RGP.rgpSDT
SDT.restype = ctypes.c_double


def rgpSDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return SDT(id, D, T)


# удельная изобарная теплоемкость [Дж/(кг*К)]
# Входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
CPDT = RGP.rgpCPDT
CPDT.restype = ctypes.c_double


def rgpCPDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return CPDT(id, D, T)


# удельная изобарная теплоемкость [Дж/(кг*К)]
# Входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
CVDT = RGP.rgpCVDT
CVDT.restype = ctypes.c_double


def rgpCVDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return CVDT(id, D, T)


# скорость звука [м/с]
# Входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
WDT = RGP.rgpWDT
WDT.restype = ctypes.c_double


def rgpWDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return WDT(id, D, T)


# показатель изоэнтропы [-]
# Входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
KDT = RGP.rgpKDT
KDT.restype = ctypes.c_double


def rgpKDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return KDT(id, D, T)


# динамическая вязкость [Па*с]
# входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
DYNVISDT = RGP.rgpDYNVISDT
DYNVISDT.restype = ctypes.c_double


def rgpDYNVISDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return DYNVISDT(id, D, T)


# кинематическая вязкость [м2/с]
# входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
KINVISDT = RGP.rgpKINVISDT
KINVISDT.restype = ctypes.c_double


def rgpKINVISDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return KINVISDT(id, D, T)


# теплопроводность [Вт/(м*К)]
# входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
THERMCONDDT = RGP.rgpTHERMCONDDT
THERMCONDDT.restype = ctypes.c_double


def rgpTHERMCONDDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return THERMCONDDT(id, D, T)


# число Прандтля [-]
# входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
PRANDTLEDT = RGP.rgpPRANDTLEDT
PRANDTLEDT.restype = ctypes.c_double


def rgpPRANDTLEDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return PRANDTLEDT(id, D, T)


# производная удельного объема по давлению при постоянной температуре [м3/(кг*Па)]
# входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
DVDPTDT = RGP.rgpDVDPTDT
DVDPTDT.restype = ctypes.c_double


def rgpDVDPTDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return DVDPTDT(id, D, T)


# производная удельного объема по температуре при постоянном давлении [м3/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
DVDTPDT = RGP.rgpDVDTPDT
DVDTPDT.restype = ctypes.c_double


def rgpDVDTPDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return DVDTPDT(id, D, T)


# производная плотности по давлению при постоянной температуре [с2/м2]
# входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
DDDPTDT = RGP.rgpDDDPTDT
DDDPTDT.restype = ctypes.c_double


def rgpDDDPTDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return DDDPTDT(id, D, T)


# производная плотности по температуре при постоянном давлении [кг/(К*м3)]
# входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
DDDTPDT = RGP.rgpDDDTPDT
DDDTPDT.restype = ctypes.c_double


def rgpDDDTPDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return DDDTPDT(id, D, T)


# производная удельного объема по энтальпии при постоянном давлении [1/Па]
# входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
DVDHPDT = RGP.rgpDVDHPDT
DVDHPDT.restype = ctypes.c_double


def rgpDVDHPDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return DVDHPDT(id, D, T)


# производная удельного объема по давлению при постоянной энтальпии [(с2*м4)/кг2]
# входные параметры:
# D - плотность [кг/м3]
# T - температура [K]
DVDPHDT = RGP.rgpDVDPHDT
DVDPHDT.restype = ctypes.c_double


def rgpDVDPHDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return DVDPHDT(id, D, T)


# производная плотности по энтальпии при постоянном давлении [кг*с2/м5]
# входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
DDDHPDT = RGP.rgpDDDHPDT
DDDHPDT.restype = ctypes.c_double


def rgpDDDHPDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return DDDHPDT(id, D, T)


# производная плотности по давлению при постоянной энтальпии [с2/м2]
# входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
DDDPHDT = RGP.rgpDDDPHDT
DDDPHDT.restype = ctypes.c_double


def rgpDDDPHDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return DDDPHDT(id, D, T)


# производная удельной энтальпии по давлению при постоянной температуре [Дж/(кг*Па)]
# входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
DHDPTDT = RGP.rgpDHDPTDT
DHDPTDT.restype = ctypes.c_double


def rgpDHDPTDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return DHDPTDT(id, D, T)


# производная удельной энтальпии по температуре при постоянном давлении [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# D - плотность [кг/м3]
# T - температура [K]
DHDTPDT = RGP.rgpDHDTPDT
DHDTPDT.restype = ctypes.c_double


def rgpDHDTPDT(id, D, T):
    D = ctypes.c_double(D)
    T = ctypes.c_double(T)
    return DHDTPDT(id, D, T)


# ============================== f(P, h) ==============================
# номер области на диаграмме состояния
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
# Выходные параметры:
# 1 - жидкая фаза
# 2 - газовая фаза
# 3 - жидкая фаза
# 4 - двухфазная область
# 5 - сверхкритическая область
# 6 - твердая фаза
STATEAREAPH = RGP.rgpSTATEAREAPH
STATEAREAPH.restype = ctypes.c_int


def rgpSTATEAREAPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return STATEAREAPH(id, P, h)


# температура [К]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
TPH = RGP.rgpTPH
TPH.restype = ctypes.c_double


def rgpTPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return TPH(id, P, h)


# паросодержание [-]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
XPH = RGP.rgpXPH
XPH.restype = ctypes.c_double


def rgpXPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return XPH(id, P, h)


# удельный объём [м3/кг]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
VPH = RGP.rgpVPH
VPH.restype = ctypes.c_double


def rgpVPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return VPH(id, P, h)


# плотность [кг/м3]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
DPH = RGP.rgpDPH
DPH.restype = ctypes.c_double


def rgpDPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return DPH(id, P, h)


# удельная внутренняя энергия [Дж/кг]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
UPH = RGP.rgpUPH
UPH.restype = ctypes.c_double


def rgpUPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return UPH(id, P, h)


# удельная энтропия [Дж/(кг*К)]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
SPH = RGP.rgpSPH
SPH.restype = ctypes.c_double


def rgpSPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return SPH(id, P, h)


# удельная изобарная теплоемкость [Дж/(кг*К)]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
CPPH = RGP.rgpCPPH
CPPH.restype = ctypes.c_double


def rgpCPPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return CPPH(id, P, h)


# удельная изобарная теплоемкость [Дж/(кг*К)]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
CVPH = RGP.rgpCVPH
CVPH.restype = ctypes.c_double


def rgpCVPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return CVPH(id, P, h)


# скорость звука [м/с]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
WPH = RGP.rgpWPH
WPH.restype = ctypes.c_double


def rgpWPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return WPH(id, P, h)


# показатель изоэнтропы [-]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
KPH = RGP.rgpKPH
KPH.restype = ctypes.c_double


def rgpKPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return KPH(id, P, h)


# динамическая вязкость [Па*с]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
DYNVISPH = RGP.rgpDYNVISPH
DYNVISPH.restype = ctypes.c_double


def rgpDYNVISPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return DYNVISPH(id, P, h)


# кинематическая вязкость [м2/с]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
KINVISPH = RGP.rgpKINVISPH
KINVISPH.restype = ctypes.c_double


def rgpKINVISPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return KINVISPH(id, P, h)


# теплопроводность [Вт/(м*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
THERMCONDPH = RGP.rgpTHERMCONDPH
THERMCONDPH.restype = ctypes.c_double


def rgpTHERMCONDPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return THERMCONDPH(id, P, h)


# число Прандтля [-]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
PRANDTLEPH = RGP.rgpPRANDTLEPH
PRANDTLEPH.restype = ctypes.c_double


def rgpPRANDTLEPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return PRANDTLEPH(id, P, h)


# производная удельного объема по давлению при постоянной температуре [м3 / (кг * Па)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
DVDPTPH = RGP.rgpDVDPTPH
DVDPTPH.restype = ctypes.c_double


def rgpDVDPTPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return DVDPTPH(id, P, h)


# производная удельного объема по температуре при постоянном давлении [м3/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
DVDTPPH = RGP.rgpDVDTPPH
DVDTPPH.restype = ctypes.c_double


def rgpDVDTPPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return DVDTPPH(id, P, h)


# производная плотности по давлению при постоянной температуре [с2/м2]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
DDDPTPH = RGP.rgpDDDPTPH
DDDPTPH.restype = ctypes.c_double


def rgpDDDPTPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return DDDPTPH(id, P, h)


# производная плотности по температуре при постоянном давлении [кг/(К*м3)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
DDDTPPH = RGP.rgpDDDTPPH
DDDTPPH.restype = ctypes.c_double


def rgpDDDTPPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return DDDTPPH(id, P, h)


# производная удельного объема по энтальпии при постоянном давлении [1/Па]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
DVDHPPH = RGP.rgpDVDHPPH
DVDHPPH.restype = ctypes.c_double


def rgpDVDHPPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return DVDHPPH(id, P, h)


# производная удельного объема по давлению при постоянной энтальпии [(с2*м4)/кг2]
# входные параметры:
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
DVDPHPH = RGP.rgpDVDPHPH
DVDPHPH.restype = ctypes.c_double


def rgpDVDPHPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return DVDPHPH(id, P, h)


# производная плотности по энтальпии при постоянном давлении [кг*с2/м5]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
DDDHPPH = RGP.rgpDDDHPPH
DDDHPPH.restype = ctypes.c_double


def rgpDDDHPPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return DDDHPPH(id, P, h)


# производная плотности по давлению при постоянной энтальпии [с2/м2]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
DDDPHPH = RGP.rgpDDDPHPH
DDDPHPH.restype = ctypes.c_double


def rgpDDDPHPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return DDDPHPH(id, P, h)


# производная удельной энтальпии по давлению при постоянной температуре [Дж/(кг*Па)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
DHDPTPH = RGP.rgpDHDPTPH
DHDPTPH.restype = ctypes.c_double


def rgpDHDPTPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return DHDPTPH(id, P, h)


# производная удельной энтальпии по температуре при постоянном давлении [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# h - удельная энтальпия [Дж/кг]
DHDTPPH = RGP.rgpDHDTPPH
DHDTPPH.restype = ctypes.c_double


def rgpDHDTPPH(id, P, h):
    P = ctypes.c_double(P)
    h = ctypes.c_double(h)
    return DHDTPPH(id, P, h)


# ============================== f(P, s) ==============================
# номер области на диаграмме состояния
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
# Выходные параметры:
# 1 - жидкая фаза
# 2 - газовая фаза
# 3 - жидкая фаза
# 4 - двухфазная область
# 5 - сверхкритическая область
# 6 - твердая фаза
STATEAREAPS = RGP.rgpSTATEAREAPS
STATEAREAPS.restype = ctypes.c_int


def rgpSTATEAREAPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return STATEAREAPS(id, P, s)


# температура [К]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
TPS = RGP.rgpTPS
TPS.restype = ctypes.c_double


def rgpTPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return TPS(id, P, s)


# паросодержание [-]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
XPS = RGP.rgpXPS
XPS.restype = ctypes.c_double


def rgpXPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return XPS(id, P, s)


# удельный объём [м3/кг]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
VPS = RGP.rgpVPS
VPS.restype = ctypes.c_double


def rgpVPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return VPS(id, P, s)


# плотность [кг/м3]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
DPS = RGP.rgpDPS
DPS.restype = ctypes.c_double


def rgpDPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return DPS(id, P, s)


# удельная внутренняя энергия [Дж/кг]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
UPS = RGP.rgpUPS
UPS.restype = ctypes.c_double


def rgpUPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return UPS(id, P, s)


# удельная энтальпия [Дж/кг]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
HPS = RGP.rgpHPS
HPS.restype = ctypes.c_double


def rgpHPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return HPS(id, P, s)


# удельная изобарная теплоемкость [Дж/(кг*К)]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
CPPS = RGP.rgpCPPS
CPPS.restype = ctypes.c_double


def rgpCPPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return CPPS(id, P, s)


# удельная изобарная теплоемкость [Дж/(кг*К)]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
CVPS = RGP.rgpCVPS
CVPS.restype = ctypes.c_double


def rgpCVPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return CVPS(id, P, s)


# скорость звука [м/с]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
WPS = RGP.rgpWPS
WPS.restype = ctypes.c_double


def rgpWPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return WPS(id, P, s)


# показатель изоэнтропы [-]
# Входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
KPS = RGP.rgpKPS
KPS.restype = ctypes.c_double


def rgpKPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return KPS(id, P, s)


# динамическая вязкость [Па*с]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
DYNVISPS = RGP.rgpDYNVISPS
DYNVISPS.restype = ctypes.c_double


def rgpDYNVISPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return DYNVISPS(id, P, s)


# кинематическая вязкость [м2/с]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
KINVISPS = RGP.rgpKINVISPS
KINVISPS.restype = ctypes.c_double


def rgpKINVISPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return KINVISPS(id, P, s)


# теплопроводность [Вт/(м*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
THERMCONDPS = RGP.rgpTHERMCONDPS
THERMCONDPS.restype = ctypes.c_double


def rgpTHERMCONDPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return THERMCONDPS(id, P, s)


# число Прандтля [-]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
PRANDTLEPS = RGP.rgpPRANDTLEPS
PRANDTLEPS.restype = ctypes.c_double


def rgpPRANDTLEPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return PRANDTLEPS(id, P, s)


# производная удельного объема по давлению при постоянной температуре [м3 / (кг * Па)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
DVDPTPS = RGP.rgpDVDPTPS
DVDPTPS.restype = ctypes.c_double


def rgpDVDPTPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return DVDPTPS(id, P, s)


# производная удельного объема по температуре при постоянном давлении [м3/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
DVDTPPS = RGP.rgpDVDTPPS
DVDTPPS.restype = ctypes.c_double


def rgpDVDTPPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return DVDTPPS(id, P, s)


# производная плотности по давлению при постоянной температуре [с2/м2]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
DDDPTPS = RGP.rgpDDDPTPS
DDDPTPS.restype = ctypes.c_double


def rgpDDDPTPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return DDDPTPS(id, P, s)


# производная плотности по температуре при постоянном давлении [кг/(К*м3)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
DDDTPPS = RGP.rgpDDDTPPS
DDDTPPS.restype = ctypes.c_double


def rgpDDDTPPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return DDDTPPS(id, P, s)


# производная удельного объема по энтальпии при постоянном давлении [1/Па]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
DVDHPPS = RGP.rgpDVDHPPS
DVDHPPS.restype = ctypes.c_double


def rgpDVDHPPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return DVDHPPS(id, P, s)


# производная удельного объема по давлению при постоянной энтальпии [(с2*м4)/кг2]
# входные параметры:
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
DVDPHPS = RGP.rgpDVDPHPS
DVDPHPS.restype = ctypes.c_double


def rgpDVDPHPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return DVDPHPS(id, P, s)


# производная плотности по энтальпии при постоянном давлении [кг*с2/м5]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
DDDHPPS = RGP.rgpDDDHPPS
DDDHPPS.restype = ctypes.c_double


def rgpDDDHPPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return DDDHPPS(id, P, s)


# производная плотности по давлению при постоянной энтальпии [с2/м2]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
DDDPHPS = RGP.rgpDDDPHPS
DDDPHPS.restype = ctypes.c_double


def rgpDDDPHPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return DDDPHPS(id, P, s)


# производная удельной энтальпии по давлению при постоянной температуре [Дж/(кг*Па)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
DHDPTPS = RGP.rgpDHDPTPS
DHDPTPS.restype = ctypes.c_double


def rgpDHDPTPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return DHDPTPS(id, P, s)


# производная удельной энтальпии по температуре при постоянном давлении [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# s - удельная энтропия [Дж/(кг*K)]
DHDTPPS = RGP.rgpDHDTPPS
DHDTPPS.restype = ctypes.c_double


def rgpDHDTPPS(id, P, s):
    P = ctypes.c_double(P)
    s = ctypes.c_double(s)
    return DHDTPPS(id, P, s)


# ============================== f(h, s) ==============================
# номер области на диаграмме состояния
# входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
# Выходные параметры:
# 1 - жидкая фаза
# 2 - газовая фаза
# 3 - жидкая фаза
# 4 - двухфазная область
# 5 - сверхкритическая область
# 6 - твердая фаза
STATEAREAHS = RGP.rgpSTATEAREAHS
STATEAREAHS.restype = ctypes.c_int


def rgpSTATEAREAHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return STATEAREAHS(id, h, s)


# давление [Па]
# Входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
PHS = RGP.rgpPHS
PHS.restype = ctypes.c_double


def rgpPHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return PHS(id, h, s)


# температура [К]
# Входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
THS = RGP.rgpTHS
THS.restype = ctypes.c_double


def rgpTHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return THS(id, h, s)


# паросодержание [-]
# Входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
XHS = RGP.rgpXHS
XHS.restype = ctypes.c_double


def rgpXHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return XHS(id, h, s)


# удельный объём [м3/кг]
# Входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
VHS = RGP.rgpVHS
VHS.restype = ctypes.c_double


def rgpVHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return VHS(id, h, s)


# плотность [кг/м3]
# Входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
DHS = RGP.rgpDHS
DHS.restype = ctypes.c_double


def rgpDHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return DHS(id, h, s)


# удельная внутренняя энергия [Дж/кг]
# Входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
UHS = RGP.rgpUHS
UHS.restype = ctypes.c_double


def rgpUHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return UHS(id, h, s)


# удельная изобарная теплоемкость [Дж/(кг*К)]
# Входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
CPHS = RGP.rgpCPHS
CPHS.restype = ctypes.c_double


def rgpCPHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return CPHS(id, h, s)


# удельная изобарная теплоемкость [Дж/(кг*К)]
# Входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
CVHS = RGP.rgpCVHS
CVHS.restype = ctypes.c_double


def rgpCVHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return CVHS(id, h, s)


# скорость звука [м/с]
# Входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
WHS = RGP.rgpWHS
WHS.restype = ctypes.c_double


def rgpWHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return WHS(id, h, s)


# показатель изоэнтропы [-]
# Входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
KHS = RGP.rgpKHS
KHS.restype = ctypes.c_double


def rgpKHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return KHS(id, h, s)


# динамическая вязкость [Па*с]
# входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
DYNVISHS = RGP.rgpDYNVISHS
DYNVISHS.restype = ctypes.c_double


def rgpDYNVISHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return DYNVISHS(id, h, s)


# кинематическая вязкость [м2/с]
# входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
KINVISHS = RGP.rgpKINVISHS
KINVISHS.restype = ctypes.c_double


def rgpKINVISHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return KINVISHS(id, h, s)


# теплопроводность [Вт/(м*К)]
# входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
THERMCONDHS = RGP.rgpTHERMCONDHS
THERMCONDHS.restype = ctypes.c_double


def rgpTHERMCONDHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return THERMCONDHS(id, h, s)


# число Прандтля [-]
# входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
PRANDTLEHS = RGP.rgpPRANDTLEHS
PRANDTLEHS.restype = ctypes.c_double


def rgpPRANDTLEHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return PRANDTLEHS(id, h, s)


# производная удельного объема по давлению при постоянной температуре [м3 / (кг * Па)]
# входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
DVDPTHS = RGP.rgpDVDPTHS
DVDPTHS.restype = ctypes.c_double


def rgpDVDPTHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return DVDPTHS(id, h, s)


# производная удельного объема по температуре при постоянном давлении [м3/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
DVDTPHS = RGP.rgpDVDTPHS
DVDTPHS.restype = ctypes.c_double


def rgpDVDTPHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return DVDTPHS(id, h, s)


# производная плотности по давлению при постоянной температуре [с2/м2]
# входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
DDDPTHS = RGP.rgpDDDPTHS
DDDPTHS.restype = ctypes.c_double


def rgpDDDPTHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return DDDPTHS(id, h, s)


# производная плотности по температуре при постоянном давлении [кг/(К*м3)]
# входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
DDDTPHS = RGP.rgpDDDTPHS
DDDTPHS.restype = ctypes.c_double


def rgpDDDTPHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return DDDTPHS(id, h, s)


# производная удельного объема по энтальпии при постоянном давлении [1/Па]
# входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
DVDHPHS = RGP.rgpDVDHPHS
DVDHPHS.restype = ctypes.c_double


def rgpDVDHPHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return DVDHPHS(id, h, s)


# производная удельного объема по давлению при постоянной энтальпии [(с2*м4)/кг2]
# входные параметры:
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
DVDPHHS = RGP.rgpDVDPHHS
DVDPHHS.restype = ctypes.c_double


def rgpDVDPHHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return DVDPHHS(id, h, s)


# производная плотности по энтальпии при постоянном давлении [кг*с2/м5]
# входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
DDDHPHS = RGP.rgpDDDHPHS
DDDHPHS.restype = ctypes.c_double


def rgpDDDHPHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return DDDHPHS(id, h, s)


# производная плотности по давлению при постоянной энтальпии [с2/м2]
# входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
DDDPHHS = RGP.rgpDDDPHHS
DDDPHHS.restype = ctypes.c_double


def rgpDDDPHHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return DDDPHHS(id, h, s)


# производная удельной энтальпии по давлению при постоянной температуре [Дж/(кг*Па)]
# входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
DHDPTHS = RGP.rgpDHDPTHS
DHDPTHS.restype = ctypes.c_double


def rgpDHDPTHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return DHDPTHS(id, h, s)


# производная удельной энтальпии по температуре при постоянном давлении [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# h - удельная энтальпия [Дж/кг]
# s - удельная энтропия [Дж/(кг*K)]
DHDTPHS = RGP.rgpDHDTPHS
DHDTPHS.restype = ctypes.c_double


def rgpDHDTPHS(id, h, s):
    h = ctypes.c_double(h)
    s = ctypes.c_double(s)
    return DHDTPHS(id, h, s)


# ============================ fs(T) ============================
# поверхностное натяжение [Н/м]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
SURFTENT = RGP.rgpSURFTENT
SURFTENT.restype = ctypes.c_double


def rgpSURFTENT(id, T):
    T = ctypes.c_double(T)
    return SURFTENT(id, T)


# давление жидкой фазы на линии насыщения [Па]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
PST = RGP.rgpPST
PST.restype = ctypes.c_double


def rgpPST(id, T):
    T = ctypes.c_double(T)
    return PST(id, T)


# удельный объем жидкой фазы на линии насыщения [м3/кг]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
VSWT = RGP.rgpVSWT
VSWT.restype = ctypes.c_double


def rgpVSWT(id, T):
    T = ctypes.c_double(T)
    return VSWT(id, T)


# плотность жидкой фазы на линии насыщения [кг/м3]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DSWT = RGP.rgpDSWT
DSWT.restype = ctypes.c_double


def rgpDSWT(id, T):
    T = ctypes.c_double(T)
    return DSWT(id, T)


# удельная внутренняя энергия жидкой фазы на линии насыщения [Дж/кг]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
USWT = RGP.rgpUSWT
USWT.restype = ctypes.c_double


def rgpUSWT(id, T):
    T = ctypes.c_double(T)
    return USWT(id, T)


# удельная энтальпия жидкой фазы на линии насыщения [Дж/кг]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
HSWT = RGP.rgpHSWT
HSWT.restype = ctypes.c_double


def rgpHSWT(id, T):
    T = ctypes.c_double(T)
    return HSWT(id, T)


# удельная энтропия жидкой фазы на линии насыщения [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
SSWT = RGP.rgpSSWT
SSWT.restype = ctypes.c_double


def rgpSSWT(id, T):
    T = ctypes.c_double(T)
    return SSWT(id, T)


# удельная изобарная теплоемкость жидкой фазы на линии насыщения [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
CPSWT = RGP.rgpCPSWT
CPSWT.restype = ctypes.c_double


def rgpCPSWT(id, T):
    T = ctypes.c_double(T)
    return CPSWT(id, T)


# удельная изохорная теплоемкость жидкой фазы на линии насыщения [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
CVSWT = RGP.rgpCVSWT
CVSWT.restype = ctypes.c_double


def rgpCVSWT(id, T):
    T = ctypes.c_double(T)
    return CVSWT(id, T)


# скорость звука в жидкой фазе на линии насыщения [м/с]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
WSWT = RGP.rgpWSWT
WSWT.restype = ctypes.c_double


def rgpWSWT(id, T):
    T = ctypes.c_double(T)
    return WSWT(id, T)


# показатель изоэнтропы в жидкой фазе на линии насыщения [-]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
KSWT = RGP.rgpKSWT
KSWT.restype = ctypes.c_double


def rgpKSWT(id, T):
    T = ctypes.c_double(T)
    return KSWT(id, T)


# динамическая вязкость жидкой фазы на линии насыщения [Па*с]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DYNVISSWT = RGP.rgpDYNVISSWT
DYNVISSWT.restype = ctypes.c_double


def rgpDYNVISSWT(id, T):
    T = ctypes.c_double(T)
    return DYNVISSWT(id, T)


# кинематическая вязкость жидкой фазы на линии насыщения [м2/с]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
KINVISSWT = RGP.rgpKINVISSWT
KINVISSWT.restype = ctypes.c_double


def rgpKINVISSWT(id, T):
    T = ctypes.c_double(T)
    return KINVISSWT(id, T)


# теплопроводность жидкой фазы на линии насыщения [Вт/(м*К)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
THERMCONDSWT = RGP.rgpTHERMCONDSWT
THERMCONDSWT.restype = ctypes.c_double


def rgpTHERMCONDSWT(id, T):
    T = ctypes.c_double(T)
    return THERMCONDSWT(id, T)


# число Прандтля жидкой фазы на линии насыщения [-]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
PRANDTLESWT = RGP.rgpPRANDTLESWT
PRANDTLESWT.restype = ctypes.c_double


def rgpPRANDTLESWT(id, T):
    T = ctypes.c_double(T)
    return PRANDTLESWT(id, T)


# производная удельного объема по давлению при постоянной температуре жидкой фазы на линии насыщения [м3/(кг*Па)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DVDPTSWT = RGP.rgpDVDPTSWT
DVDPTSWT.restype = ctypes.c_double


def rgpDVDPTSWT(id, T):
    T = ctypes.c_double(T)
    return DVDPTSWT(id, T)


# производная удельного объема по температуре при постоянном давлении жидкой фазы на линии насыщения [м3/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DVDTPSWT = RGP.rgpDVDTPSWT
DVDTPSWT.restype = ctypes.c_double


def rgpDVDTPSWT(id, T):
    T = ctypes.c_double(T)
    return DVDTPSWT(id, T)


# производная плотности по давлению при постоянной температуре жидкой фазы на линии насыщения [с2/м2]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DDDPTSWT = RGP.rgpDDDPTSWT
DDDPTSWT.restype = ctypes.c_double


def rgpDDDPTSWT(id, T):
    T = ctypes.c_double(T)
    return DDDPTSWT(id, T)


# производная плотности по температуре при постоянном давлении жидкой фазы на линии насыщения [кг/(К*м3)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DDDTPSWT = RGP.rgpDDDTPSWT
DDDTPSWT.restype = ctypes.c_double


def rgpDDDTPSWT(id, T):
    T = ctypes.c_double(T)
    return DDDTPSWT(id, T)


# производная удельного объема по энтальпии при постоянном давлении жидкой фазы на линии насыщения [1/Па]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DVDHPSWT = RGP.rgpDVDHPSWT
DVDHPSWT.restype = ctypes.c_double


def rgpDVDHPSWT(id, T):
    T = ctypes.c_double(T)
    return DVDHPSWT(id, T)


# производная удельного объема по давлению при постоянной энтальпии жидкой фазы на линии насыщения [(с2*м4)/кг2]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DVDPHSWT = RGP.rgpDVDPHSWT
DVDPHSWT.restype = ctypes.c_double


def rgpDVDPHSWT(id, T):
    T = ctypes.c_double(T)
    return DVDPHSWT(id, T)


# производная плотности по энтальпии при постоянном давлении жидкой фазы на линии насыщения [кг*с2/м5]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DDDHPSWT = RGP.rgpDDDHPSWT
DDDHPSWT.restype = ctypes.c_double


def rgpDDDHPSWT(id, T):
    T = ctypes.c_double(T)
    return DDDHPSWT(id, T)


# производная плотности по давлению при постоянной энтальпии жидкой фазы на линии насыщения [с2/м2]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DDDPHSWT = RGP.rgpDDDPHSWT
DDDPHSWT.restype = ctypes.c_double


def rgpDDDPHSWT(id, T):
    T = ctypes.c_double(T)
    return DDDPHSWT(id, T)


# производная удельной энтальпии по давлению при постоянной температуре жидкой фазы на линии насыщения [Дж/(кг*Па)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DHDPTSWT = RGP.rgpDHDPTSWT
DHDPTSWT.restype = ctypes.c_double


def rgpDHDPTSWT(id, T):
    T = ctypes.c_double(T)
    return DHDPTSWT(id, T)


# производная удельной энтальпии по температуре при постоянном давлении жидкой фазы на линии насыщения [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DHDTPSWT = RGP.rgpDHDTPSWT
DHDTPSWT.restype = ctypes.c_double


def rgpDHDTPSWT(id, T):
    T = ctypes.c_double(T)
    return DHDTPSWT(id, T)


# удельный объем газовой фазы на линии насыщения [м3/кг]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
VSST = RGP.rgpVSST
VSST.restype = ctypes.c_double


def rgpVSST(id, T):
    T = ctypes.c_double(T)
    return VSST(id, T)


# плотность газовой фазы на линии насыщения [кг/м3]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DSST = RGP.rgpDSST
DSST.restype = ctypes.c_double


def rgpDSST(id, T):
    T = ctypes.c_double(T)
    return DSST(id, T)


# удельная внутренняя энергия газовой фазы на линии насыщения [Дж/кг]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
USST = RGP.rgpUSST
USST.restype = ctypes.c_double


def rgpUSST(id, T):
    T = ctypes.c_double(T)
    return USST(id, T)


# удельная энтальпия газовой фазы на линии насыщения [Дж/кг]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
HSST = RGP.rgpHSST
HSST.restype = ctypes.c_double


def rgpHSST(id, T):
    T = ctypes.c_double(T)
    return HSST(id, T)


# удельная энтропия газовой фазы на линии насыщения [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
SSST = RGP.rgpSSST
SSST.restype = ctypes.c_double


def rgpSSST(id, T):
    T = ctypes.c_double(T)
    return SSST(id, T)


# удельная изобарная теплоемкость газовой фазы на линии насыщения [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
CPSST = RGP.rgpCPSST
CPSST.restype = ctypes.c_double


def rgpCPSST(id, T):
    T = ctypes.c_double(T)
    return CPSST(id, T)


# удельная изохорная теплоемкость газовой фазы на линии насыщения [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
CVSST = RGP.rgpCVSST
CVSST.restype = ctypes.c_double


def rgpCVSST(id, T):
    T = ctypes.c_double(T)
    return CVSST(id, T)


# скорость звука в жидкой фазе на линии насыщения [м/с]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
WSST = RGP.rgpWSST
WSST.restype = ctypes.c_double


def rgpWSST(id, T):
    T = ctypes.c_double(T)
    return WSST(id, T)


# показатель изоэнтропы в жидкой фазе на линии насыщения [-]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
KSST = RGP.rgpKSST
KSST.restype = ctypes.c_double


def rgpKSST(id, T):
    T = ctypes.c_double(T)
    return KSST(id, T)


# динамическая вязкость газовой фазы на линии насыщения [Па*с]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DYNVISSST = RGP.rgpDYNVISSST
DYNVISSST.restype = ctypes.c_double


def rgpDYNVISSST(id, T):
    T = ctypes.c_double(T)
    return DYNVISSST(id, T)


# кинематическая вязкость газовой фазы на линии насыщения [м2/с]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
KINVISSST = RGP.rgpKINVISSST
KINVISSST.restype = ctypes.c_double


def rgpKINVISSST(id, T):
    T = ctypes.c_double(T)
    return KINVISSST(id, T)


# теплопроводность газовой фазы на линии насыщения [Вт/(м*К)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
THERMCONDSST = RGP.rgpTHERMCONDSST
THERMCONDSST.restype = ctypes.c_double


def rgpTHERMCONDSST(id, T):
    T = ctypes.c_double(T)
    return THERMCONDSST(id, T)


# число Прандтля газовой фазы на линии насыщения [-]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
PRANDTLESST = RGP.rgpPRANDTLESST
PRANDTLESST.restype = ctypes.c_double


def rgpPRANDTLESST(id, T):
    T = ctypes.c_double(T)
    return PRANDTLESST(id, T)


# производная удельного объема по давлению при постоянной температуре газовой фазы на линии насыщения [м3/(кг*Па)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DVDPTSST = RGP.rgpDVDPTSST
DVDPTSST.restype = ctypes.c_double


def rgpDVDPTSST(id, T):
    T = ctypes.c_double(T)
    return DVDPTSST(id, T)


# производная удельного объема по температуре при постоянном давлении газовой фазы на линии насыщения [м3/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DVDTPSST = RGP.rgpDVDTPSST
DVDTPSST.restype = ctypes.c_double


def rgpDVDTPSST(id, T):
    T = ctypes.c_double(T)
    return DVDTPSST(id, T)


# производная плотности по давлению при постоянной температуре газовой фазы на линии насыщения [с2/м2]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DDDPTSST = RGP.rgpDDDPTSST
DDDPTSST.restype = ctypes.c_double


def rgpDDDPTSST(id, T):
    T = ctypes.c_double(T)
    return DDDPTSST(id, T)


# производная плотности по температуре при постоянном давлении газовой фазы на линии насыщения [кг/(К*м3)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DDDTPSST = RGP.rgpDDDTPSST
DDDTPSST.restype = ctypes.c_double


def rgpDDDTPSST(id, T):
    T = ctypes.c_double(T)
    return DDDTPSST(id, T)


# производная удельного объема по энтальпии при постоянном давлении газовой фазы на линии насыщения [1/Па]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DVDHPSST = RGP.rgpDVDHPSST
DVDHPSST.restype = ctypes.c_double


def rgpDVDHPSST(id, T):
    T = ctypes.c_double(T)
    return DVDHPSST(id, T)


# производная удельного объема по давлению при постоянной энтальпии газовой фазы на линии насыщения [(с2*м4)/кг2]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DVDPHSST = RGP.rgpDVDPHSST
DVDPHSST.restype = ctypes.c_double


def rgpDVDPHSST(id, T):
    T = ctypes.c_double(T)
    return DVDPHSST(id, T)


# производная плотности по энтальпии при постоянном давлении газовой фазы на линии насыщения [кг*с2/м5]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DDDHPSST = RGP.rgpDDDHPSST
DDDHPSST.restype = ctypes.c_double


def rgpDDDHPSST(id, T):
    T = ctypes.c_double(T)
    return DDDHPSST(id, T)


# производная плотности по давлению при постоянной энтальпии газовой фазы на линии насыщения [с2/м2]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DDDPHSST = RGP.rgpDDDPHSST
DDDPHSST.restype = ctypes.c_double


def rgpDDDPHSST(id, T):
    T = ctypes.c_double(T)
    return DDDPHSST(id, T)


# производная удельной энтальпии по давлению при постоянной температуре газовой фазы на линии насыщения [Дж/(кг*Па)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DHDPTSST = RGP.rgpDHDPTSST
DHDPTSST.restype = ctypes.c_double


def rgpDHDPTSST(id, T):
    T = ctypes.c_double(T)
    return DHDPTSST(id, T)


# производная удельной энтальпии по температуре при постоянном давлении газовой фазы на линии насыщения [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
DHDTPSST = RGP.rgpDHDTPSST
DHDTPSST.restype = ctypes.c_double


def rgpDHDTPSST(id, T):
    T = ctypes.c_double(T)
    return DHDTPSST(id, T)


# ============================ fs(P) ============================
# температура жидкой фазы на линии насыщения [К]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
TSP = RGP.rgpTSP
TSP.restype = ctypes.c_double


def rgpTSP(id, P):
    P = ctypes.c_double(P)
    return TSP(id, P)


# удельный объем жидкой фазы на линии насыщения [м3/кг]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
VSWP = RGP.rgpVSWP
VSWP.restype = ctypes.c_double


def rgpVSWP(id, P):
    P = ctypes.c_double(P)
    return VSWP(id, P)


# плотность жидкой фазы на линии насыщения [кг/м3]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DSWP = RGP.rgpDSWP
DSWP.restype = ctypes.c_double


def rgpDSWP(id, P):
    P = ctypes.c_double(P)
    return DSWP(id, P)


# удельная внутренняя энергия жидкой фазы на линии насыщения [Дж/кг]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
USWP = RGP.rgpUSWP
USWP.restype = ctypes.c_double


def rgpUSWP(id, P):
    P = ctypes.c_double(P)
    return USWP(id, P)


# удельная энтальпия жидкой фазы на линии насыщения [Дж/кг]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
HSWP = RGP.rgpHSWP
HSWP.restype = ctypes.c_double


def rgpHSWP(id, P):
    P = ctypes.c_double(P)
    return HSWP(id, P)


# удельная энтропия жидкой фазы на линии насыщения [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
SSWP = RGP.rgpSSWP
SSWP.restype = ctypes.c_double


def rgpSSWP(id, P):
    P = ctypes.c_double(P)
    return SSWP(id, P)


# удельная изобарная теплоемкость жидкой фазы на линии насыщения [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
CPSWP = RGP.rgpCPSWP
CPSWP.restype = ctypes.c_double


def rgpCPSWP(id, P):
    P = ctypes.c_double(P)
    return CPSWP(id, P)


# удельная изохорная теплоемкость жидкой фазы на линии насыщения [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
CVSWP = RGP.rgpCVSWP
CVSWP.restype = ctypes.c_double


def rgpCVSWP(id, P):
    P = ctypes.c_double(P)
    return CVSWP(id, P)


# скорость звука в жидкой фазе на линии насыщения [м/с]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
WSWP = RGP.rgpWSWP
WSWP.restype = ctypes.c_double


def rgpWSWP(id, P):
    P = ctypes.c_double(P)
    return WSWP(id, P)


# показатель изоэнтропы в жидкой фазе на линии насыщения [-]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
KSWP = RGP.rgpKSWP
KSWP.restype = ctypes.c_double


def rgpKSWP(id, P):
    P = ctypes.c_double(P)
    return KSWP(id, P)


# динамическая вязкость жидкой фазы на линии насыщения [Па*с]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DYNVISSWP = RGP.rgpDYNVISSWP
DYNVISSWP.restype = ctypes.c_double


def rgpDYNVISSWP(id, P):
    P = ctypes.c_double(P)
    return DYNVISSWP(id, P)


# кинематическая вязкость жидкой фазы на линии насыщения [м2/с]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
KINVISSWP = RGP.rgpKINVISSWP
KINVISSWP.restype = ctypes.c_double


def rgpKINVISSWP(id, P):
    P = ctypes.c_double(P)
    return KINVISSWP(id, P)


# теплопроводность жидкой фазы на линии насыщения [Вт/(м*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
THERMCONDSWP = RGP.rgpTHERMCONDSWP
THERMCONDSWP.restype = ctypes.c_double


def rgpTHERMCONDSWP(id, P):
    P = ctypes.c_double(P)
    return THERMCONDSWP(id, P)


# число Прандтля жидкой фазы на линии насыщения [-]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
PRANDTLESWP = RGP.rgpPRANDTLESWP
PRANDTLESWP.restype = ctypes.c_double


def rgpPRANDTLESWP(id, P):
    P = ctypes.c_double(P)
    return PRANDTLESWP(id, P)


# производная удельного объема по давлению при постоянной температуре жидкой фазы на линии насыщения [м3/(кг*Па)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DVDPTSWP = RGP.rgpDVDPTSWP
DVDPTSWP.restype = ctypes.c_double


def rgpDVDPTSWP(id, P):
    P = ctypes.c_double(P)
    return DVDPTSWP(id, P)


# производная удельного объема по температуре при постоянном давлении жидкой фазы на линии насыщения [м3/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DVDTPSWP = RGP.rgpDVDTPSWP
DVDTPSWP.restype = ctypes.c_double


def rgpDVDTPSWP(id, P):
    P = ctypes.c_double(P)
    return DVDTPSWP(id, P)


# производная плотности по давлению при постоянной температуре жидкой фазы на линии насыщения [с2/м2]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DDDPTSWP = RGP.rgpDDDPTSWP
DDDPTSWP.restype = ctypes.c_double


def rgpDDDPTSWP(id, P):
    P = ctypes.c_double(P)
    return DDDPTSWP(id, P)


# производная плотности по температуре при постоянном давлении жидкой фазы на линии насыщения [кг/(К*м3)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DDDTPSWP = RGP.rgpDDDTPSWP
DDDTPSWP.restype = ctypes.c_double


def rgpDDDTPSWP(id, P):
    P = ctypes.c_double(P)
    return DDDTPSWP(id, P)


# производная удельного объема по энтальпии при постоянном давлении жидкой фазы на линии насыщения [1/Па]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DVDHPSWP = RGP.rgpDVDHPSWP
DVDHPSWP.restype = ctypes.c_double


def rgpDVDHPSWP(id, P):
    P = ctypes.c_double(P)
    return DVDHPSWP(id, P)


# производная удельного объема по давлению при постоянной энтальпии жидкой фазы на линии насыщения [(с2*м4)/кг2]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DVDPHSWP = RGP.rgpDVDPHSWP
DVDPHSWP.restype = ctypes.c_double


def rgpDVDPHSWP(id, P):
    P = ctypes.c_double(P)
    return DVDPHSWP(id, P)


# производная плотности по энтальпии при постоянном давлении жидкой фазы на линии насыщения [кг*с2/м5]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DDDHPSWP = RGP.rgpDDDHPSWP
DDDHPSWP.restype = ctypes.c_double


def rgpDDDHPSWP(id, P):
    P = ctypes.c_double(P)
    return DDDHPSWP(id, P)


# производная плотности по давлению при постоянной энтальпии жидкой фазы на линии насыщения [с2/м2]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DDDPHSWP = RGP.rgpDDDPHSWP
DDDPHSWP.restype = ctypes.c_double


def rgpDDDPHSWP(id, P):
    P = ctypes.c_double(P)
    return DDDPHSWP(id, P)


# производная удельной энтальпии по давлению при постоянной температуре жидкой фазы на линии насыщения [Дж/(кг*Па)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DHDPTSWP = RGP.rgpDHDPTSWP
DHDPTSWP.restype = ctypes.c_double


def rgpDHDPTSWP(id, P):
    P = ctypes.c_double(P)
    return DHDPTSWP(id, P)


# производная удельной энтальпии по температуре при постоянном давлении жидкой фазы на линии насыщения [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DHDTPSWP = RGP.rgpDHDTPSWP
DHDTPSWP.restype = ctypes.c_double


def rgpDHDTPSWP(id, P):
    P = ctypes.c_double(P)
    return DHDTPSWP(id, P)


# удельный объем газовой фазы на линии насыщения [м3/кг]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
VSSP = RGP.rgpVSSP
VSSP.restype = ctypes.c_double


def rgpVSSP(id, P):
    P = ctypes.c_double(P)
    return VSSP(id, P)


# плотность газовой фазы на линии насыщения [кг/м3]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DSSP = RGP.rgpDSSP
DSSP.restype = ctypes.c_double


def rgpDSSP(id, P):
    P = ctypes.c_double(P)
    return DSSP(id, P)


# удельная внутренняя энергия газовой фазы на линии насыщения [Дж/кг]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
USSP = RGP.rgpUSSP
USSP.restype = ctypes.c_double


def rgpUSSP(id, P):
    P = ctypes.c_double(P)
    return USSP(id, P)


# удельная энтальпия газовой фазы на линии насыщения [Дж/кг]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
HSSP = RGP.rgpHSSP
HSSP.restype = ctypes.c_double


def rgpHSSP(id, P):
    P = ctypes.c_double(P)
    return HSSP(id, P)


# удельная энтропия газовой фазы на линии насыщения [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
SSSP = RGP.rgpSSSP
SSSP.restype = ctypes.c_double


def rgpSSSP(id, P):
    P = ctypes.c_double(P)
    return SSSP(id, P)


# удельная изобарная теплоемкость газовой фазы на линии насыщения [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
CPSSP = RGP.rgpCPSSP
CPSSP.restype = ctypes.c_double


def rgpCPSSP(id, P):
    P = ctypes.c_double(P)
    return CPSSP(id, P)


# удельная изохорная теплоемкость газовой фазы на линии насыщения [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
CVSSP = RGP.rgpCVSSP
CVSSP.restype = ctypes.c_double


def rgpCVSSP(id, P):
    P = ctypes.c_double(P)
    return CVSSP(id, P)


# скорость звука в жидкой фазе на линии насыщения [м/с]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
WSSP = RGP.rgpWSSP
WSSP.restype = ctypes.c_double


def rgpWSSP(id, P):
    P = ctypes.c_double(P)
    return WSSP(id, P)


# показатель изоэнтропы в жидкой фазе на линии насыщения [-]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
KSSP = RGP.rgpKSSP
KSSP.restype = ctypes.c_double


def rgpKSSP(id, P):
    P = ctypes.c_double(P)
    return KSSP(id, P)


# динамическая вязкость газовой фазы на линии насыщения [Па*с]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DYNVISSSP = RGP.rgpDYNVISSSP
DYNVISSSP.restype = ctypes.c_double


def rgpDYNVISSSP(id, P):
    P = ctypes.c_double(P)
    return DYNVISSSP(id, P)


# кинематическая вязкость газовой фазы на линии насыщения [м2/с]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
KINVISSSP = RGP.rgpKINVISSSP
KINVISSSP.restype = ctypes.c_double


def rgpKINVISSSP(id, P):
    P = ctypes.c_double(P)
    return KINVISSSP(id, P)


# теплопроводность газовой фазы на линии насыщения [Вт/(м*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
THERMCONDSSP = RGP.rgpTHERMCONDSSP
THERMCONDSSP.restype = ctypes.c_double


def rgpTHERMCONDSSP(id, P):
    P = ctypes.c_double(P)
    return THERMCONDSSP(id, P)


# число Прандтля газовой фазы на линии насыщения [-]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
PRANDTLESSP = RGP.rgpPRANDTLESSP
PRANDTLESSP.restype = ctypes.c_double


def rgpPRANDTLESSP(id, P):
    P = ctypes.c_double(P)
    return PRANDTLESSP(id, P)


# производная удельного объема по давлению при постоянной температуре газовой фазы на линии насыщения [м3/(кг*Па)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DVDPTSSP = RGP.rgpDVDPTSSP
DVDPTSSP.restype = ctypes.c_double


def rgpDVDPTSSP(id, P):
    P = ctypes.c_double(P)
    return DVDPTSSP(id, P)


# производная удельного объема по температуре при постоянном давлении газовой фазы на линии насыщения [м3/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DVDTPSSP = RGP.rgpDVDTPSSP
DVDTPSSP.restype = ctypes.c_double


def rgpDVDTPSSP(id, P):
    P = ctypes.c_double(P)
    return DVDTPSSP(id, P)


# производная плотности по давлению при постоянной температуре газовой фазы на линии насыщения [с2/м2]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DDDPTSSP = RGP.rgpDDDPTSSP
DDDPTSSP.restype = ctypes.c_double


def rgpDDDPTSSP(id, P):
    P = ctypes.c_double(P)
    return DDDPTSSP(id, P)


# производная плотности по температуре при постоянном давлении газовой фазы на линии насыщения [кг/(К*м3)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DDDTPSSP = RGP.rgpDDDTPSSP
DDDTPSSP.restype = ctypes.c_double


def rgpDDDTPSSP(id, P):
    P = ctypes.c_double(P)
    return DDDTPSSP(id, P)


# производная удельного объема по энтальпии при постоянном давлении газовой фазы на линии насыщения [1/Па]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DVDHPSSP = RGP.rgpDVDHPSSP
DVDHPSSP.restype = ctypes.c_double


def rgpDVDHPSSP(id, P):
    P = ctypes.c_double(P)
    return DVDHPSSP(id, P)


# производная удельного объема по давлению при постоянной энтальпии газовой фазы на линии насыщения [(с2*м4)/кг2]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DVDPHSSP = RGP.rgpDVDPHSSP
DVDPHSSP.restype = ctypes.c_double


def rgpDVDPHSSP(id, P):
    P = ctypes.c_double(P)
    return DVDPHSSP(id, P)


# производная плотности по энтальпии при постоянном давлении газовой фазы на линии насыщения [кг*с2/м5]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DDDHPSSP = RGP.rgpDDDHPSSP
DDDHPSSP.restype = ctypes.c_double


def rgpDDDHPSSP(id, P):
    P = ctypes.c_double(P)
    return DDDHPSSP(id, P)


# производная плотности по давлению при постоянной энтальпии газовой фазы на линии насыщения [с2/м2]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DDDPHSSP = RGP.rgpDDDPHSSP
DDDPHSSP.restype = ctypes.c_double


def rgpDDDPHSSP(id, P):
    P = ctypes.c_double(P)
    return DDDPHSSP(id, P)


# производная удельной энтальпии по давлению при постоянной температуре газовой фазы на линии насыщения [Дж/(кг*Па)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DHDPTSSP = RGP.rgpDHDPTSSP
DHDPTSSP.restype = ctypes.c_double


def rgpDHDPTSSP(id, P):
    P = ctypes.c_double(P)
    return DHDPTSSP(id, P)


# производная удельной энтальпии по температуре при постоянном давлении газовой фазы на линии насыщения [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
DHDTPSSP = RGP.rgpDHDTPSSP
DHDTPSSP.restype = ctypes.c_double


def rgpDHDTPSSP(id, P):
    P = ctypes.c_double(P)
    return DHDTPSSP(id, P)


# =========================== fs(T, x) ==========================
# удельный объём в двухфазной области [м3/кг]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
# x - степень сухости пара [-]
VSTX = RGP.rgpVSTX
VSTX.restype = ctypes.c_double


def rgpVSTX(id, T, x):
    T = ctypes.c_double(T)
    x = ctypes.c_double(x)
    return VSTX(id, T, x)


# плотность в двухфазной области [кг/м3]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
# x - степень сухости пара [-]
DSTX = RGP.rgpDSTX
DSTX.restype = ctypes.c_double


def rgpDSTX(id, T, x):
    T = ctypes.c_double(T)
    x = ctypes.c_double(x)
    return DSTX(id, T, x)


# удельная внутренняя энергия в двухфазной области [Дж/кг]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
# x - степень сухости пара [-]
USTX = RGP.rgpUSTX
USTX.restype = ctypes.c_double


def rgpUSTX(id, T, x):
    T = ctypes.c_double(T)
    x = ctypes.c_double(x)
    return USTX(id, T, x)


# удельная энтропия в двухфазной области [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
# x - степень сухости пара [-]
SSTX = RGP.rgpSSTX
SSTX.restype = ctypes.c_double


def rgpSSTX(id, T, x):
    T = ctypes.c_double(T)
    x = ctypes.c_double(x)
    return SSTX(id, T, x)


# удельная энтальпия в двухфазной области [Дж/кг]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
# x - степень сухости пара [-]
HSTX = RGP.rgpHSTX
HSTX.restype = ctypes.c_double


def rgpHSTX(id, T, x):
    T = ctypes.c_double(T)
    x = ctypes.c_double(x)
    return HSTX(id, T, x)


# удельная изобарная теплоемкость в двухфазной области [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
# x - степень сухости пара [-]
CPSTX = RGP.rgpCPSTX
CPSTX.restype = ctypes.c_double


def rgpCPSTX(id, T, x):
    T = ctypes.c_double(T)
    x = ctypes.c_double(x)
    return CPSTX(id, T, x)


# удельная изохорная теплоемкость в двухфазной области [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
# x - степень сухости пара [-]
CVSTX = RGP.rgpCVSTX
CVSTX.restype = ctypes.c_double


def rgpCVSTX(id, T, x):
    T = ctypes.c_double(T)
    x = ctypes.c_double(x)
    return CVSTX(id, T, x)


# скорость звука в двухфазной области [м/с]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
# x - степень сухости пара [-]
WSTX = RGP.rgpWSTX
WSTX.restype = ctypes.c_double


def rgpWSTX(id, T, x):
    T = ctypes.c_double(T)
    x = ctypes.c_double(x)
    return WSTX(id, T, x)


# показатель изоэнтропы в двухфазной области [-]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
# x - степень сухости пара [-]
KSTX = RGP.rgpKSTX
KSTX.restype = ctypes.c_double


def rgpKSTX(id, T, x):
    T = ctypes.c_double(T)
    x = ctypes.c_double(x)
    return KSTX(id, T, x)


# динамическая вязкость в двухфазной области [Па*с]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
# x - степень сухости пара [-]
DYNVISSTX = RGP.rgpDYNVISSTX
DYNVISSTX.restype = ctypes.c_double


def rgpDYNVISSTX(id, T, x):
    T = ctypes.c_double(T)
    x = ctypes.c_double(x)
    return DYNVISSTX(id, T, x)


# кинематическая вязкость в двухфазной области [м2/с]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
# x - степень сухости пара [-]
KINVISSTX = RGP.rgpKINVISSTX
KINVISSTX.restype = ctypes.c_double


def rgpKINVISSTX(id, T, x):
    T = ctypes.c_double(T)
    x = ctypes.c_double(x)
    return KINVISSTX(id, T, x)


# теплопроводность в двухфазной области [Вт/(м*К)]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
# x - степень сухости пара [-]
THERMCONDSTX = RGP.rgpTHERMCONDSTX
THERMCONDSTX.restype = ctypes.c_double


def rgpTHERMCONDSTX(id, T, x):
    T = ctypes.c_double(T)
    x = ctypes.c_double(x)
    return THERMCONDSTX(id, T, x)


# число Прандтля в двухфазной области [-]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
# x - степень сухости пара [-]
PRANDTLESTX = RGP.rgpPRANDTLESTX
PRANDTLESTX.restype = ctypes.c_double


def rgpPRANDTLESTX(id, T, x):
    T = ctypes.c_double(T)
    x = ctypes.c_double(x)
    return PRANDTLESTX(id, T, x)


# производная удельного объема по энтальпии при постоянном давлении в двухфазной области [1/Па]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
# x - степень сухости пара [-]
DVDHPSTX = RGP.rgpDVDHPSTX
DVDHPSTX.restype = ctypes.c_double


def rgpDVDHPSTX(id, T, x):
    T = ctypes.c_double(T)
    x = ctypes.c_double(x)
    return DVDHPSTX(id, T, x)


# производная удельного объема по давлению при постоянной энтальпии в двухфазной области [(с2*м4)/кг2]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
# x - степень сухости пара [-]
DVDPHSTX = RGP.rgpDVDPHSTX
DVDPHSTX.restype = ctypes.c_double


def rgpDVDPHSTX(id, T, x):
    T = ctypes.c_double(T)
    x = ctypes.c_double(x)
    return DVDPHSTX(id, T, x)


# производная плотности по энтальпии при постоянном давлении в двухфазной области [кг*с2/м5]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
# x - степень сухости пара [-]
DDDHPSTX = RGP.rgpDDDHPSTX
DDDHPSTX.restype = ctypes.c_double


def rgpDDDHPSTX(id, T, x):
    T = ctypes.c_double(T)
    x = ctypes.c_double(x)
    return DDDHPSTX(id, T, x)


# производная плотности по давлению при постоянной энтальпии в двухфазной области [с2/м2]
# входные параметры:
# id - идентификатор вещества
# T - температура [K]
# x - степень сухости пара [-]
DDDPHSTX = RGP.rgpDDDPHSTX
DDDPHSTX.restype = ctypes.c_double


def rgpDDDPHSTX(id, T, x):
    T = ctypes.c_double(T)
    x = ctypes.c_double(x)
    return DDDPHSTX(id, T, x)


# =========================== fs(P, x) ==========================
# удельный объём в двухфазной области [м3/кг]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# x - степень сухости пара [-]
VSPX = RGP.rgpVSPX
VSPX.restype = ctypes.c_double


def rgpVSPX(id, P, x):
    P = ctypes.c_double(P)
    x = ctypes.c_double(x)
    return VSPX(id, P, x)


# плотность в двухфазной области [кг/м3]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# x - степень сухости пара [-]
DSPX = RGP.rgpDSPX
DSPX.restype = ctypes.c_double


def rgpDSPX(id, P, x):
    P = ctypes.c_double(P)
    x = ctypes.c_double(x)
    return DSPX(id, P, x)


# удельная внутренняя энергия в двухфазной области [Дж/кг]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# x - степень сухости пара [-]
USPX = RGP.rgpUSPX
USPX.restype = ctypes.c_double


def rgpUSPX(id, P, x):
    P = ctypes.c_double(P)
    x = ctypes.c_double(x)
    return USPX(id, P, x)


# удельная энтропия в двухфазной области [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# x - степень сухости пара [-]
SSPX = RGP.rgpSSPX
SSPX.restype = ctypes.c_double


def rgpSSPX(id, P, x):
    P = ctypes.c_double(P)
    x = ctypes.c_double(x)
    return SSPX(id, P, x)


# удельная энтальпия в двухфазной области [Дж/кг]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# x - степень сухости пара [-]
HSPX = RGP.rgpHSPX
HSPX.restype = ctypes.c_double


def rgpHSPX(id, P, x):
    P = ctypes.c_double(P)
    x = ctypes.c_double(x)
    return HSPX(id, P, x)


# удельная изобарная теплоемкость в двухфазной области [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# x - степень сухости пара [-]
CPSPX = RGP.rgpCPSPX
CPSPX.restype = ctypes.c_double


def rgpCPSPX(id, P, x):
    P = ctypes.c_double(P)
    x = ctypes.c_double(x)
    return CPSPX(id, P, x)


# удельная изохорная теплоемкость в двухфазной области [Дж/(кг*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# x - степень сухости пара [-]
CVSPX = RGP.rgpCVSPX
CVSPX.restype = ctypes.c_double


def rgpCVSPX(id, P, x):
    P = ctypes.c_double(P)
    x = ctypes.c_double(x)
    return CVSPX(id, P, x)


# скорость звука в двухфазной области [м/с]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# x - степень сухости пара [-]
WSPX = RGP.rgpWSPX
WSPX.restype = ctypes.c_double


def rgpWSPX(id, P, x):
    P = ctypes.c_double(P)
    x = ctypes.c_double(x)
    return WSPX(id, P, x)


# показатель изоэнтропы в двухфазной области [-]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# x - степень сухости пара [-]
KSPX = RGP.rgpKSPX
KSPX.restype = ctypes.c_double


def rgpKSPX(id, P, x):
    P = ctypes.c_double(P)
    x = ctypes.c_double(x)
    return KSPX(id, P, x)


# динамическая вязкость в двухфазной области [Па*с]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# x - степень сухости пара [-]
DYNVISSPX = RGP.rgpDYNVISSPX
DYNVISSPX.restype = ctypes.c_double


def rgpDYNVISSPX(id, P, x):
    P = ctypes.c_double(P)
    x = ctypes.c_double(x)
    return DYNVISSPX(id, P, x)


# кинематическая вязкость в двухфазной области [м2/с]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# x - степень сухости пара [-]
KINVISSPX = RGP.rgpKINVISSPX
KINVISSPX.restype = ctypes.c_double


def rgpKINVISSPX(id, P, x):
    P = ctypes.c_double(P)
    x = ctypes.c_double(x)
    return KINVISSPX(id, P, x)


# теплопроводность в двухфазной области [Вт/(м*К)]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# x - степень сухости пара [-]
THERMCONDSPX = RGP.rgpTHERMCONDSPX
THERMCONDSPX.restype = ctypes.c_double


def rgpTHERMCONDSPX(id, P, x):
    P = ctypes.c_double(P)
    x = ctypes.c_double(x)
    return THERMCONDSPX(id, P, x)


# число Прандтля в двухфазной области [-]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# x - степень сухости пара [-]
PRANDTLESPX = RGP.rgpPRANDTLESPX
PRANDTLESPX.restype = ctypes.c_double


def rgpPRANDTLESPX(id, P, x):
    P = ctypes.c_double(P)
    x = ctypes.c_double(x)
    return PRANDTLESPX(id, P, x)


# производная удельного объема по энтальпии при постоянном давлении в двухфазной области [1/Па]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# x - степень сухости пара [-]
DVDHPSPX = RGP.rgpDVDHPSPX
DVDHPSPX.restype = ctypes.c_double


def rgpDVDHPSPX(id, P, x):
    P = ctypes.c_double(P)
    x = ctypes.c_double(x)
    return DVDHPSPX(id, P, x)


# производная удельного объема по давлению при постоянной энтальпии в двухфазной области [(с2*м4)/кг2]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# x - степень сухости пара [-]
DVDPHSPX = RGP.rgpDVDPHSPX
DVDPHSPX.restype = ctypes.c_double


def rgpDVDPHSPX(id, P, x):
    P = ctypes.c_double(P)
    x = ctypes.c_double(x)
    return DVDPHSPX(id, P, x)


# производная плотности по энтальпии при постоянном давлении в двухфазной области [кг*с2/м5]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# x - степень сухости пара [-]
DDDHPSPX = RGP.rgpDDDHPSPX
DDDHPSPX.restype = ctypes.c_double


def rgpDDDHPSPX(id, P, x):
    P = ctypes.c_double(P)
    x = ctypes.c_double(x)
    return DDDHPSPX(id, P, x)


# производная плотности по давлению при постоянной энтальпии в двухфазной области [с2/м2]
# входные параметры:
# id - идентификатор вещества
# P - давление [Па]
# x - степень сухости пара [-]
DDDPHSPX = RGP.rgpDDDPHSPX
DDDPHSPX.restype = ctypes.c_double


def rgpDDDPHSPX(id, P, x):
    P = ctypes.c_double(P)
    x = ctypes.c_double(x)
    return DDDPHSPX(id, P, x)
