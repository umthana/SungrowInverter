"""
#
# Sungrow Grid-Connected String Inverter Series
#
# Valid device types:
#   SG3.0RT, SG4.0RT, SG5.0RT, SG6.0RT, SG7.0RT, SG8.0RT, SG10RT, SG12RT, SG15RT, SG17RT, SG20RT
#   SG30KTL-M, SG30KTL-M-V31, SG33KTL-M, SG36KTL-M, SG33K3J, SG49K5J, SG34KJ, LP_P34KSG,
#   SG50KTL-M-20, SG60KTL, G80KTL, SG80KTL-20, SG60KU-M
#   SG5KTL-MT, SG6KTL-MT, SG8KTL-M, SG10KTL-M, SG10KTL-MT, SG12KTL-M, SG15KTL-M,
#   SG17KTL-M, SG20KTL-M,
#   SG80KTL-M, SG85BF, SG80HV, SG80BF, SG110HV-M, SG111HV, SG125HV, SG125HV-20
#   SG25CX-SA, SG30CX, SG33CX, SG40CX, SG50CX, SG36CX-US, SG60CX-US, SG75CX, SG100CX
#   SG100CX-JP, SG110CX, SG136TX, SG225HX, SG250HX
#   SG250HX-IN, SG250HX-US
#
#   Discontinued (as @ 2021-07-12):
#   SG30KTL, SG10KTL, SG12KTL, SG15KTL, SG20KTL, SG30KU, SG36KTL, SG36KU, SG40KTL,
#   SG40KTL-M, SG50KTL-M, SG60KTL-M, SG60KU
#
# Sungrow string inverter register definitions
"""

from sungrowinverter.configs.common import (
    ModBusRegister,
    PERCENTAGE,
    TEMP_CELSIUS,
    KILO_WATT_HOUR,
    KILO_WATT,
    WATT,
    VOLTAGE,
    AMPERE,
    HERTZ,
    OUTPUT_TYPE_CODES,
    HOUR,
    MINUTE,
    VOLT_AMPS,
)

# Device state (register 5038)
DEVICE_WORK_STATE_1_CODES = {
    0x0:    "Run",
    0x8000: "Stop",
    0x1300: "Key stop",
    0x1500: "Emergency stop",
    0x1400: "Standby",
    0x1200: "Initial standby",
    0x1600: "Starting",
    0x9100: "Alarm run",
    0x8100: "Derating run",
    0x8200: "Dispatch run",
    0x5500: "Fault",
    0x2500: "Communicate fault",
    0x1111: "Uninitialized",
}

# Work State (register 5081 - 5082)
DEVICE_WORK_STATE_2_CODES = {
    1 <<  0: "status_run",
    1 <<  1: "status_stop",
    1 <<  3: "status_key_stop",
    1 <<  5: "status_emergency_stop",
    1 <<  4: "status_standby",
    1 <<  2: "status_initial_standby",
    1 <<  6: "status_starting",
    1 << 10: "status_alarm_run",
    1 << 11: "status_derating_run",
    1 << 12: "status_dispatch_run",
    1 <<  9: "status_fault",
    1 << 13: "status_communicate_fault",
    1 << 17: "status_grid_connected",
    1 << 18: "status_fault_stop",
}

COUNTRY_CODES = {
    61: "America",
    98: "America(1741-SA)",
    59: "America(Hawaii)",
    97: "America(ISO-NE)",
    27: "Arab Emirates",
    6: "Australia",
    20: "Australia (West)",
    5: "Austria",
    25: "Austria (Vorarlberg)",
    8: "Belgium",
    66: "Brazil",
    60: "Canada",
    65: "Chile",
    14: "China",
    67: "Chinese Taipei",
    7: "Czech",
    9: "Denmark",
    76: "EN50549-1 Europe",
    77: "EN50549-2 Europe",
    40: "Finland",
    2: "France",
    1: "Germany",
    0: "Great Britain",
    11: "Greece (Island)",
    10: "Greece (Land)",
    29: "Hungary",
    26: "IND India",
    41: "Ireland",
    28: "Israel",
    3: "Italy",
    69: "Japan",
    63: "Korea",
    30: "Malaysia",
    170: "Mexico",
    12: "Netherlands",
    99: "New Zealand",
    38: "Oman",
    16: "Other 50Hz",
    62: "Other 60Hz",
    31: "Philippines",
    32: "Poland",
    34: "Poland",
    13: "Portugal",
    17: "Romania",
    39: "Sandi Arabia",
    64: "South Africa",
    4: "Spain",
    15: "Sweden",
    18: "Thailand",
    35: "Thailand-MEA",
    19: "Turkey",
    36: "Vietnam",
}

PID_WORK_STATE_CODES = {
    2: "PID Recover Operation",
    4: "Anti-PID Operation",
    8: "PID Abnormity",
}

PID_ALARM_CODES = {
    432: "PID resistance abnormal",
    433: "PID function abnormal",
    434: "PID overvoltage/overcurrent protection",
}

# the scan register start 1 less than the actual register recorded in specs.
# reason being registers start at 0, document for modbus usually refers to register 1 as the start of registers.
STRING_SCAN = {
    "read": [
        {"scan_start": 4999, "scan_range": 110},
        {"scan_start": 5112, "scan_range": 50},
    ],
    "holding": [
        {"scan_start": 4999, "scan_range": 6},
    ],
}

STRING_READ_REGISTERS: tuple[ModBusRegister, ...] = (
    ModBusRegister(5002, "output_type", "U16", table=OUTPUT_TYPE_CODES),
    ModBusRegister(5003, "daily_energy_yield", "U16", 0.1, KILO_WATT_HOUR),
    ModBusRegister(5004, "total_energy_yield", "U32", unit_of_measure=KILO_WATT_HOUR),
    ModBusRegister(5006, "total_running_time", "U32", unit_of_measure=HOUR),
    ModBusRegister(5008, "inside_temperature", "U16", 0.1, TEMP_CELSIUS, description="Internal inverter temperature"),
    ModBusRegister(5009, "total_aparent_power", "U32", unit_of_measure=VOLT_AMPS),
    ModBusRegister(5011, "mppt_1_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5012, "mppt_1_current", "U16", 0.1, AMPERE),
    ModBusRegister(5013, "mppt_2_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5014, "mppt_2_current", "U16", 0.1, AMPERE),
    ModBusRegister(5015, "mppt_3_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5016, "mppt_3_current", "U16", 0.1, AMPERE),
    ModBusRegister(5017, "total_dc_power", "U32", unit_of_measure=WATT, description="PV power that is usable (inverter after inefficiency)"),
    ModBusRegister(5019, "grid_voltage", "U16", 0.1, VOLTAGE), # here for single phase only (not applicable for 3 phase)
    ModBusRegister(5019, "phase_a_voltage", "U16", 0.1, VOLTAGE, description="Phase A (1-2) voltage is also the grid voltage on a single phase inverter"),
    ModBusRegister(5020, "phase_b_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5021, "phase_c_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5022, "phase_a_current", "U16", 0.1, AMPERE),
    ModBusRegister(5023, "phase_b_current", "U16", 0.1, AMPERE),
    ModBusRegister(5024, "phase_c_current", "U16", 0.1, AMPERE),
    ModBusRegister(5031, "total_active_power", "U32", unit_of_measure=WATT),
    ModBusRegister(5033, "reactive_power", "S32", unit_of_measure="Var"),
    ModBusRegister(5035, "power_factor", "S16", 0.001),
    ModBusRegister(5036, "grid_frequency", "U16", 0.1, HERTZ),
    ModBusRegister(5038, "device_state", "U16", table=DEVICE_WORK_STATE_1_CODES),
    
    # Fault/Alarm time and Fault/Alarm code (5039 - 5045) are valid only when the device work state is fault or alarm
    # Except SG5.5RS-JP, SG0.7/1.0/1/5/2.0/2.5/3.0RS-S, SG3.0/3.6/4.0/5.0/6.0RS, SG5.0RS-ADA, SG8.0/9.0/10RS
    ModBusRegister(5039, "fault/alarm_year", "U16"),
    ModBusRegister(5040, "fault/alarm_month", "U16"),
    ModBusRegister(5041, "fault/alarm_day", "U16"),
    ModBusRegister(5042, "fault/alarm_hour", "U16"),
    ModBusRegister(5043, "fault/alarm_minute", "U16"),
    ModBusRegister(5044, "fault/alarm_second", "U16"),
    ModBusRegister(5045, "fault/alarm_code", "U16"),
    
    ModBusRegister(5049, "nominal_reactive_power", "U16", 0.1, "kVar"),
    ModBusRegister(5071, "array_insulation_resistance", "U16", unit_of_measure="kΩ"),
    ModBusRegister(5077, "active_power_regulation_setpoint", "U32", unit_of_measure=WATT),
    ModBusRegister(5079, "reactive_power_regulation_setpoint", "U32", unit_of_measure="Var"),
    ModBusRegister(5081, "work_state", "U32", transform="BINARY", length=19, table=DEVICE_WORK_STATE_2_CODES, description='Translates into work states (refer appendix 2 of sungrow reference)'),
    ModBusRegister(5083, "meter_power", "S32", unit_of_measure=WATT, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5085, "meter_a_phase_power", "S32", unit_of_measure=WATT, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5087, "meter_b_phase_power", "S32", unit_of_measure=WATT, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5089, "meter_c_phase_power", "S32", unit_of_measure=WATT, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5091, "load_power", "S32", unit_of_measure=WATT, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    # ModBusRegister(5093, "daily_export_from_pv", "U32", 0.1, KILO_WATT_HOUR, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5093, "daily_export_energy", "U32", 0.1, KILO_WATT_HOUR, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5095, "total_export_energy", "U32", 0.1, KILO_WATT_HOUR, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    # ModBusRegister(5095, "total_export_from_pv", "U32", 0.1, KILO_WATT_HOUR, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5097, "daily_import_energy", "U32", 0.1, KILO_WATT_HOUR, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5099, "total_import_energy", "U32", 0.1, KILO_WATT_HOUR, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5101, "daily_direct_energy_consumption", "U32", 0.1, KILO_WATT_HOUR, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5103, "total_direct_energy_consumption", "U32", 0.1, KILO_WATT_HOUR, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5113, "daily_running_time", "U16", unit_of_measure=MINUTE),
    ModBusRegister(5114, "present_country", "U16", table=COUNTRY_CODES),
    ModBusRegister(5115, "mppt_4_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5116, "mppt_4_current", "U16", 0.1, AMPERE),
    ModBusRegister(5117, "mppt_5_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5118, "mppt_5_current", "U16", 0.1, AMPERE),
    ModBusRegister(5119, "mppt_6_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5120, "mppt_6_current", "U16", 0.1, AMPERE),
    ModBusRegister(5121, "mppt_7_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5122, "mppt_7_current", "U16", 0.1, AMPERE),
    ModBusRegister(5123, "mppt_8_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5124, "mppt_8_current", "U16", 0.1, AMPERE),
    ModBusRegister(5128, "monthly_power_yields", "U32", 0.1, KILO_WATT_HOUR),
    ModBusRegister(5130, "mppt_9_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5131, "mppt_9_current", "U16", 0.1, AMPERE),
    ModBusRegister(5132, "mppt_10_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5133, "mppt_10_current", "U16", 0.1, AMPERE),
    ModBusRegister(5134, "mppt_11_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5135, "mppt_11_current", "U16", 0.1, AMPERE),
    ModBusRegister(5136, "mppt_12_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5137, "mppt_12_current", "U16", 0.1, AMPERE),
    ModBusRegister(5140, "work_status_1", "U16"),
    ModBusRegister(5141, "work_status_2", "U16"),
    ModBusRegister(5143, "heart_beat", "U16"),
    ModBusRegister(5144, "total_power_yields", "U32", 0.1, KILO_WATT_HOUR,
        valid_inverters=[0x139,0x13B,0x13C,0x13E,0x13F,0x142,0x143,0x147,0x148,0x149,0x14C,
                         0x2430,0x2431,0x2432,0x2433,0x2434,0x2435,0x2436,0x2437,0x243C,0x243D,0x243E,
                         0x2600,0x2601,0x2602,0x2603,0x2604,0x2605,0x2606,0x2607,
                         0x2C00,0x2C01,0x2C02,0x2C03,0x2C06,0x2C0A,0x2C0B,
                         0x2C0C,0x2C0F,0x2C10,0x2C11,0x2C12,0x2C13,0x2C15,0x2C22]),
    ModBusRegister(5146, "negative_voltage_to_the_ground", "S16", 0.1, VOLTAGE),
    ModBusRegister(5147, "bus_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5148, "grid_frequency", "U16", 0.01, HERTZ),
    ModBusRegister(5150, "PID_work_state", "U16", table=PID_WORK_STATE_CODES),
    ModBusRegister(5151, "PID_alarm_code", "U16", table=PID_ALARM_CODES),
    ModBusRegister(5186, "mppt_13_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5187, "mppt_13_current", "U16", 0.1, AMPERE),
    ModBusRegister(5188, "mppt_14_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5189, "mppt_14_current", "U16", 0.1, AMPERE),
    ModBusRegister(5190, "mppt_15_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5191, "mppt_15_current", "U16", 0.1, AMPERE),
    ModBusRegister(5192, "mppt_16_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5193, "mppt_16_current", "U16", 0.1, AMPERE),
    ModBusRegister(7013, "string_1_current", "U16", 0.01, AMPERE),
    ModBusRegister(7014, "string_2_current", "U16", 0.01, AMPERE),
    ModBusRegister(7015, "string_3_current", "U16", 0.01, AMPERE),
    ModBusRegister(7016, "string_4_current", "U16", 0.01, AMPERE),
    ModBusRegister(7017, "string_5_current", "U16", 0.01, AMPERE),
    ModBusRegister(7018, "string_6_current", "U16", 0.01, AMPERE),
    ModBusRegister(7019, "string_7_current", "U16", 0.01, AMPERE),
    ModBusRegister(7020, "string_8_current", "U16", 0.01, AMPERE),
    ModBusRegister(7021, "string_9_current", "U16", 0.01, AMPERE),
    ModBusRegister(7022, "string_10_current", "U16", 0.01, AMPERE),
    ModBusRegister(7023, "string_11_current", "U16", 0.01, AMPERE),
    ModBusRegister(7024, "string_12_current", "U16", 0.01, AMPERE),
    ModBusRegister(7025, "string_13_current", "U16", 0.01, AMPERE),
    ModBusRegister(7026, "string_14_current", "U16", 0.01, AMPERE),
    ModBusRegister(7027, "string_15_current", "U16", 0.01, AMPERE),
    ModBusRegister(7028, "string_16_current", "U16", 0.01, AMPERE),
    ModBusRegister(7029, "string_17_current", "U16", 0.01, AMPERE),
    ModBusRegister(7030, "string_18_current", "U16", 0.01, AMPERE),
    ModBusRegister(7031, "string_19_current", "U16", 0.01, AMPERE),
    ModBusRegister(7032, "string_20_current", "U16", 0.01, AMPERE),
    ModBusRegister(7033, "string_21_current", "U16", 0.01, AMPERE),
    ModBusRegister(7034, "string_22_current", "U16", 0.01, AMPERE),
    ModBusRegister(7035, "string_23_current", "U16", 0.01, AMPERE),
    ModBusRegister(7036, "string_24_current", "U16", 0.01, AMPERE),
    ModBusRegister(7037, "string_25_current", "U16", 0.01, AMPERE),
    ModBusRegister(7038, "string_26_current", "U16", 0.01, AMPERE),
    ModBusRegister(7039, "string_27_current", "U16", 0.01, AMPERE),
    ModBusRegister(7040, "string_28_current", "U16", 0.01, AMPERE),
    ModBusRegister(7041, "string_29_current", "U16", 0.01, AMPERE),
    ModBusRegister(7042, "string_30_current", "U16", 0.01, AMPERE),
    ModBusRegister(7043, "string_31_current", "U16", 0.01, AMPERE),
    ModBusRegister(7044, "string_32_current", "U16", 0.01, AMPERE),

)

STRING_HOLDING_REGISTERS: tuple[ModBusRegister, ...] = (
    ModBusRegister(5000, "year", "U16"),
    ModBusRegister(5001, "month", "U16"),
    ModBusRegister(5002, "day", "U16"),
    ModBusRegister(5003, "hour", "U16"),
    ModBusRegister(5004, "minute", "U16"),
    ModBusRegister(5005, "second", "U16"),

    # 0xCF (Start), 0xCE (Stop)
    ModBusRegister(5006, "start/stop", "U16"),

    # 0xAA: Enable, 0x55: Disable
    ModBusRegister(5007, "power_limitation_switch", "U16"),
    ModBusRegister(5008, "power_limitation_setting", "U16", 0.1, PERCENTAGE),
    
    # 0xAA: Enable, 0x55: Disable
    ModBusRegister(5010, "export_power_limitation", "U16"),
    ModBusRegister(5011, "export_power_limitation_value", "U16"),

    ModBusRegister(5012, "current_transformer_output_current", "U16", unit_of_measure=AMPERE),
    ModBusRegister(5013, "current_transformer_range", "U16", unit_of_measure=AMPERE),
    # 0: internal, 1: external
    ModBusRegister(5014, "current_transformer", "U16"),
    ModBusRegister(5015, "export_power_limitation_percentage", "U16", 0.1, PERCENTAGE),
    ModBusRegister(5016, "installed_pv_power", "U16", 0.01, KILO_WATT),
    # > 0: leading, < 0: lagging
    ModBusRegister(5019, "power_factor_setting", "S16", 0.001),
    # 0xAA: Enable, 0x55: Disable
    # When Active Power Overload is disabled: inverters will generate power according to the command value.
    # When Active Power Overload is enabled: inverters will generate power according to the product of the command value and the overload rate.
    ModBusRegister(5020, "active_power_overload", "U16"),
    # 0 : unvalid, 1 : valid
    ModBusRegister(5021, "local/remote_control", "U16"),
    # 0xAA: Enable, 0x55: Disable
    ModBusRegister(5035, "night_SVG_switch", "U16"),

    # 0x55: OFF, power factor returns to 1, reactive power percentage returns to 0;
    # 0xA1: power factor setting valid, Reactive power percentage returns to 0;
    # 0xA2: Reactive power percentage setting valid, power factor returns to 1;
    # 0xA3: Enable Q(P) curve configuration;
    # 0xA4: Enable Q(U) curve configuration
    ModBusRegister(5036, "reactive_power_adjustment_mode", "U16"),
    ModBusRegister(5037, "reactive_power_percentage_setting", "S16", 0.1, PERCENTAGE),
    ModBusRegister(5039, "power_limitation_adjustment", "U16", 0.1, KILO_WATT),
    ModBusRegister(5040, "reactive_power_adjustment", "S16", 0.1, "kVar"),
    # 0xAA: Enable, 0x55: Disable
    ModBusRegister(5041, "PID_recovery", "U16"),
    # 0xAA: Enable, 0x55: Disable
    ModBusRegister(5042, "anti-PID", "U16"),
    # 0xAA: Enable, 0x55: Disable
    ModBusRegister(5043, "full-day_PID_suppression", "U16", 0.1, KILO_WATT),
    ModBusRegister(5048, "Q(P)_curve_1"),
    ModBusRegister(5078, "Q(P) curve 1"),
    ModBusRegister(5116, "Q(P) curve 2"),
    ModBusRegister(5135, "Q(P) curve 2"),
    # 0xAA: Enable, 0x55: Disable
    ModBusRegister(32569, "quick_grid_dispatch_mode", "U16"),
    ModBusRegister(32570, "swift_grid_dispatch_mode", "U16"),


)
