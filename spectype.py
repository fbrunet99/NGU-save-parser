﻿from collections import namedtuple

SpecObj = namedtuple("SpecObj", ["name", "div"])
SpecType = [
    SpecObj("None", 0),
    SpecObj("EnergyPower", 0),
    SpecObj("EnergySpeed", 0),
    SpecObj("MagicPower", 0),
    SpecObj("MagicSpeed", 0),
    SpecObj("Looting", 10),
    SpecObj("GoldRNG", 0),
    SpecObj("GoldDrop", 1),
    SpecObj("EnergyPerBar", 0),
    SpecObj("MagicPerBar", 0),
    # 10
    SpecObj("BoostRecycle", 0),
    SpecObj("Cooking", 0),
    SpecObj("Wandoos98", 100),
    SpecObj("AdvTraining", 100),
    SpecObj("Cooldown", 100),
    SpecObj("Seeds", 1000),
    SpecObj("EnergyPower2", 10),
    SpecObj("MagicPower2", 10),
    SpecObj("EnergyPerBar2", 10),
    SpecObj("MagicPerBar2", 10),
    # 20
    SpecObj("EnergyCap", 100),
    SpecObj("MagicCap", 100),
    SpecObj("NGU", 100),
    SpecObj("Respawn", 1000),
    SpecObj("EXP", 10000),
    SpecObj("AP", 1000),
    SpecObj("Beards", 1000),
    SpecObj("AllPower", 1000),
    SpecObj("AllPerBar", 1000),
    SpecObj("AllCap", 10000),
    # 30
    SpecObj("Augs", 10000),
    SpecObj("Wandoos2", 10000),
    SpecObj("AdvTraining2", 10000),
    SpecObj("EnergyPower3", 1000),
    SpecObj("MagicPower3", 1000),
    SpecObj("EnergyPerBar3", 1000),
    SpecObj("MagicPerBar3", 1000),
    SpecObj("EnergyCap3", 10000),
    SpecObj("MagicCap3", 10000),
    SpecObj("NGU2", 10000),
    # 40
    SpecObj("GoldDrop2", 1000),
    SpecObj("Looting2", 10000),
    SpecObj("Beards2", 10000),
    SpecObj("Yggdrasil", 100000),
    SpecObj("DaycareSpeed", 0),
    SpecObj("QuestDrop", 1000000),
    SpecObj("Blood", 0),
    SpecObj("Res3Power", 0),
    SpecObj("Res3Bar", 0),
    SpecObj("Res3Cap", 0),
    # 50
    SpecObj("HackSpeed", 0),
    SpecObj("WishSpeed", 0),
]
