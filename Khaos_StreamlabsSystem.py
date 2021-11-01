#---------------------------
#   Import Libraries
#---------------------------
import os, sys, codecs, json, clr
clr.AddReference("IronPython.Modules.dll")
from collections import OrderedDict
from json import JSONEncoder

#---------------------------
#   [Required] Script Information
#---------------------------
ScriptName = "SotN Khaos Script"
Website = "https://taliczealot.github.io/"
Description = "Enable chat interactivity for the Khaos tool for Symphony of the Night"
Creator = "TalicZealot"
Version = "1.0.2"

#---------------------------
#   Define Classes
#---------------------------
class Settings(object):
    # Load in saved settings file if available else set default values.
    def __init__(self, settingsfile=None):
        try:
            with codecs.open(settingsfile, encoding="utf-8-sig", mode="r") as f:
                self.__dict__ = json.load(f, encoding="utf-8")
        except:
            self.KhaosStatusEnabled = True
            self.KhaosStatusCost = 200
            self.KhaosStatusMaxCost = 200
            self.KhaosStatusScaling = 1
            self.KhaosStatusCooldown = 0
            self.KhaosStatusUserCooldown = 1
            self.KhaosStatusStartsOnCooldown = False

            self.KhaosEquipmentEnabled = True
            self.KhaosEquipmentCost = 300
            self.KhaosEquipmentMaxCost = 1000
            self.KhaosEquipmentScaling = 1.5
            self.KhaosEquipmentCooldown = 5
            self.KhaosEquipmentUserCooldown = 6
            self.KhaosEquipmentStartsOnCooldown = False

            self.KhaosStatsEnabled = True
            self.KhaosStatsCost = 400
            self.KhaosStatsMaxCost = 1200
            self.KhaosStatsScaling = 1.5
            self.KhaosStatsCooldown = 5
            self.KhaosStatsUserCooldown = 6
            self.KhaosStatsStartsOnCooldown = False

            self.KhaosRelicsEnabled = True
            self.KhaosRelicsCost = 1000
            self.KhaosRelicsMaxCost = 8000
            self.KhaosRelicsScaling = 2
            self.KhaosRelicsCooldown = 20
            self.KhaosRelicsUserCooldown = 22
            self.KhaosRelicsStartsOnCooldown = True

            self.PandorasBoxEnabled = True
            self.PandorasBoxCost = 1000
            self.PandorasBoxMaxCost = 15000
            self.PandorasBoxScaling = 2.3
            self.PandorasBoxCooldown = 20
            self.PandorasBoxUserCooldown = 22
            self.PandorasBoxStartsOnCooldown = True

            self.GambleEnabled = True
            self.GambleCost = 200
            self.GambleMaxCost = 3000
            self.GambleScaling = 2
            self.GambleCooldown = 1
            self.GambleUserCooldown = 2
            self.GambleStartsOnCooldown = False

            self.BankruptEnabled = True
            self.BankruptCost = 1000
            self.BankruptMaxCost = 8000
            self.BankruptScaling = 2
            self.BankruptCooldown = 20
            self.BankruptUserCooldown = 22
            self.BankruptStartsOnCooldown = True

            self.WeakenEnabled = True
            self.WeakenCost = 1000
            self.WeakenMaxCost = 15000
            self.WeakenScaling = 2.3
            self.WeakenCooldown = 24
            self.WeakenUserCooldown = 26
            self.WeakenStartsOnCooldown = True

            self.RespawnBossesEnabled = True
            self.RespawnBossesCost = 400
            self.RespawnBossesMaxCost = 1200
            self.RespawnBossesScaling = 1.5
            self.RespawnBossesCooldown = 10
            self.RespawnBossesUserCooldown = 11
            self.RespawnBossesStartsOnCooldown = True

            self.HonestGamerEnabled = True
            self.HonestGamerCost = 300
            self.HonestGamerMaxCost = 1000
            self.HonestGamerScaling = 1.2
            self.HonestGamerCooldown = 4
            self.HonestGamerUserCooldown = 5
            self.HonestGamerStartsOnCooldown = False

            self.SubweaponsOnlyEnabled = True
            self.SubweaponsOnlyCost = 600
            self.SubweaponsOnlyMaxCost = 1300
            self.SubweaponsOnlyScaling = 1.2
            self.SubweaponsOnlyCooldown = 4
            self.SubweaponsOnlyUserCooldown = 5
            self.SubweaponsOnlyStartsOnCooldown = False

            self.CrippleEnabled = True
            self.CrippleCost = 300
            self.CrippleMaxCost = 3000
            self.CrippleScaling = 2
            self.CrippleCooldown = 5
            self.CrippleUserCooldown = 6
            self.CrippleStartsOnCooldown = False

            self.BloodManaEnabled = True
            self.BloodManaCost = 200
            self.BloodManaMaxCost = 1300
            self.BloodManaScaling = 1.5
            self.BloodManaCooldown = 4
            self.BloodManaUserCooldown = 5
            self.BloodManaStartsOnCooldown = False

            self.ThirstEnabled = True
            self.ThirstCost = 500
            self.ThirstMaxCost = 3000
            self.ThirstScaling = 1.5
            self.ThirstCooldown = 4
            self.ThirstUserCooldown = 5
            self.ThirstStartsOnCooldown = True

            self.HordeEnabled = True
            self.HordeCost = 500
            self.HordeMaxCost = 3000
            self.HordeScaling = 2
            self.HordeCooldown = 5
            self.HordeUserCooldown = 6
            self.HordeStartsOnCooldown = False

            self.EnduranceEnabled = True
            self.EnduranceCost = 700
            self.EnduranceMaxCost = 7000
            self.EnduranceScaling = 2
            self.EnduranceCooldown = 4
            self.EnduranceUserCooldown = 5
            self.EnduranceStartsOnCooldown = False

            self.VampireEnabled = True
            self.VampireCost = 100
            self.VampireMaxCost = 400
            self.VampireScaling = 1.3
            self.VampireCooldown = 4
            self.VampireUserCooldown = 5
            self.VampireStartsOnCooldown = False

            self.LightHelpEnabled = True
            self.LightHelpCost = 100
            self.LightHelpMaxCost = 100
            self.LightHelpScaling = 1
            self.LightHelpCooldown = 0
            self.LightHelpUserCooldown = 1
            self.LightHelpStartsOnCooldown = False

            self.MediumHelpEnabled = True
            self.MediumHelpCost = 300
            self.MediumHelpMaxCost = 1000
            self.MediumHelpScaling = 1.5
            self.MediumHelpCooldown = 1
            self.MediumHelpUserCooldown = 2
            self.MediumHelpStartsOnCooldown = False

            self.HeavyHelpEnabled = True
            self.HeavyHelpCost = 500
            self.HeavyHelpMaxCost = 2500
            self.HeavyHelpScaling = 1.5
            self.HeavyHelpCooldown = 4
            self.HeavyHelpUserCooldown = 5
            self.HeavyHelpStartsOnCooldown = True

            self.BattleOrdersEnabled = True
            self.BattleOrdersCost = 200
            self.BattleOrdersMaxCost = 1000
            self.BattleOrdersScaling = 1.5
            self.BattleOrdersCooldown = 3
            self.BattleOrdersUserCooldown = 4
            self.BattleOrdersStartsOnCooldown = False

            self.MagicianEnabled = True
            self.MagicianCost = 300
            self.MagicianMaxCost = 1000
            self.MagicianScaling = 1.5
            self.MagicianCooldown = 4
            self.MagicianUserCooldown = 5
            self.MagicianStartsOnCooldown = True

            self.MeltyBloodEnabled = True
            self.MeltyBloodCost = 500
            self.MeltyBloodMaxCost = 2000
            self.MeltyBloodScaling = 1.5
            self.MeltyBloodCooldown = 4
            self.MeltyBloodUserCooldown = 5
            self.MeltyBloodStartsOnCooldown = False

            self.FourBeastsEnabled = True
            self.FourBeastsCost = 1000
            self.FourBeastsMaxCost = 4000
            self.FourBeastsScaling = 2
            self.FourBeastsCooldown = 4
            self.FourBeastsUserCooldown = 5
            self.FourBeastsStartsOnCooldown = True

            self.ZaWarudoEnabled = True
            self.ZaWarudoCost = 300
            self.ZaWarudoMaxCost = 1500
            self.ZaWarudoScaling = 1.5
            self.ZaWarudoCooldown = 4
            self.ZaWarudoUserCooldown = 5
            self.ZaWarudoStartsOnCooldown = False

            self.HasteEnabled = True
            self.HasteCost = 500
            self.HasteMaxCost = 2000
            self.HasteScaling = 1.5
            self.HasteCooldown = 4
            self.HasteUserCooldown = 5
            self.HasteStartsOnCooldown = False
            Parent.Log(ScriptName, "No settings file found, loading defaults.")

    # Reload settings from Streamlabs user interface by given json data.
    def Reload(self, jsondata):
        self.__dict__ = json.loads(jsondata, encoding='utf-8-sig')

    # Save settings contained within to .json and .js settings files.
    def Save(self, settingsfile):
        try:
            with codecs.open(settingsfile, encoding="utf-8-sig", mode="w+") as f:
                json.dump(self.__dict__, f, encoding="utf-8", ensure_ascii=False)
            with codecs.open(settingsfile.replace("json", "js"), encoding="utf-8-sig", mode="w+") as f:
                f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8', ensure_ascii=False)))
        except ValueError:
            Parent.Log(ScriptName, "Failed to save settings to file.")

class Command:
    def __init__(self, command, index, type, enabled, cost, maxCost, scaling, cooldown, userCooldown, startsOnCooldown):
        self.command = command
        self.index = index
        self.type = type
        self.enabled = enabled
        self.cost = cost
        self.maxCost = maxCost
        self.scaling = scaling
        self.cooldown = cooldown
        self.userCooldown = userCooldown
        self.startsOnCooldown = startsOnCooldown
        return

    # Scale the command cost up to maximum.
    def ScaleCost(self):
        if self.scaling == 1:
            return
        self.cost = round(self.cost * self.scaling)
        if self.cost > self.maxCost:
            self.cost = self.maxCost
        return
    
    # Put the command on cooldown.
    def PutOnCooldown(self):
        if self.cooldown > 0:
            Parent.AddCooldown(ScriptName, self.command, self.cooldown * 60)

    # Put the command on cooldown.
    def PutOnUserCooldown(self, User):
        if self.userCooldown > 0:
            Parent.AddUserCooldown(ScriptName, self.command,User, self.userCooldown * 60)

    # Execute the command.
    def Execute(self, User, UserName):
        if Parent.IsOnCooldown(ScriptName, self.command):
            Parent.SendStreamMessage("{0} is on cooldown for {1} seconds.".format(self.command, Parent.GetCooldownDuration(ScriptName, self.command)))
            return
        elif Parent.IsOnUserCooldown(ScriptName, self.command, User):
            Parent.SendStreamWhisper(User,"You can't use {0} for {1} seconds.".format(self.command, Parent.GetUserCooldownDuration(ScriptName, self.command, User)))
            return
        else:
            if  HasCurrency(User, UserName, self.cost):
                self.PutOnCooldown()
                self.PutOnUserCooldown(User)
                self.ScaleCost()
                Parent.BroadcastWsEvent("EVENT_UPDATE_COMMAND", '{{"command":"{0}", "cost":{1}, "cooldown":{2}}}'.format(self.command, self.cost, self.cooldown))
                Parent.BroadcastWsEvent("EVENT_ADD_ACTION", '{{"Command":"{0}", "UserName":"{1}"}}'.format(self.command, UserName))
                if self.scaling > 1:
                    Parent.SendStreamMessage("New {0} cost: {1} {2}".format(self.command, self.cost, Khaos["currency"]))
                return
            else:
                return

class CommandEncoder(JSONEncoder):
    def default(self, command):
        return command.__dict__

#---------------------------
#   Define Variables
#---------------------------
SettingsFile = os.path.join(os.path.dirname(__file__), "settings.json")
OverlayCommandsFile = os.path.join(os.path.dirname(__file__) + "/Overlays/", "commands.js")

Khaos = {
    "on": False,
    "paused": False,
    "currency": "points"
}
ActionCommands = {}

#---------------------------------------
#   Chatbot Initialize Function
#---------------------------------------
def Init():
    #   Load settings
    global ScriptSettings
    ScriptSettings = Settings(SettingsFile)
    ScriptSettings.Save(SettingsFile)
    Khaos["currency"] = Parent.GetCurrencyName()

    # Load commands
    # Khaotic
    ActionCommands["kstatus"] = Command("kstatus", 0, 0, ScriptSettings.KhaosStatusEnabled, ScriptSettings.KhaosStatusCost, ScriptSettings.KhaosStatusMaxCost, ScriptSettings.KhaosStatusScaling, ScriptSettings.KhaosStatusCooldown, ScriptSettings.KhaosStatusUserCooldown, ScriptSettings.KhaosStatusStartsOnCooldown)
    ActionCommands["kequipment"] = Command("kequipment", 1, 0, ScriptSettings.KhaosEquipmentEnabled, ScriptSettings.KhaosEquipmentCost, ScriptSettings.KhaosEquipmentMaxCost, ScriptSettings.KhaosEquipmentScaling, ScriptSettings.KhaosEquipmentCooldown, ScriptSettings.KhaosEquipmentUserCooldown, ScriptSettings.KhaosEquipmentStartsOnCooldown)
    ActionCommands["kstats"] = Command("kstats", 2, 0, ScriptSettings.KhaosStatsEnabled, ScriptSettings.KhaosStatsCost, ScriptSettings.KhaosStatsMaxCost, ScriptSettings.KhaosStatsScaling, ScriptSettings.KhaosStatsCooldown, ScriptSettings.KhaosStatsUserCooldown, ScriptSettings.KhaosStatsStartsOnCooldown)
    ActionCommands["krelics"] = Command("krelics", 3, 0, ScriptSettings.KhaosRelicsEnabled, ScriptSettings.KhaosRelicsCost, ScriptSettings.KhaosRelicsMaxCost, ScriptSettings.KhaosRelicsScaling, ScriptSettings.KhaosRelicsCooldown, ScriptSettings.KhaosRelicsUserCooldown, ScriptSettings.KhaosRelicsStartsOnCooldown)
    ActionCommands["pandora"] = Command("pandora", 4, 0, ScriptSettings.PandorasBoxEnabled, ScriptSettings.PandorasBoxCost, ScriptSettings.PandorasBoxMaxCost, ScriptSettings.PandorasBoxScaling, ScriptSettings.PandorasBoxCooldown, ScriptSettings.PandorasBoxUserCooldown, ScriptSettings.PandorasBoxStartsOnCooldown)
    ActionCommands["gamble"] = Command("gamble", 5, 0, ScriptSettings.GambleEnabled, ScriptSettings.GambleCost, ScriptSettings.GambleMaxCost, ScriptSettings.GambleScaling, ScriptSettings.GambleCooldown, ScriptSettings.GambleUserCooldown, ScriptSettings.GambleStartsOnCooldown)
    # Debuffs
    ActionCommands["bankrupt"] = Command("bankrupt", 6, 1, ScriptSettings.BankruptEnabled, ScriptSettings.BankruptCost, ScriptSettings.BankruptMaxCost, ScriptSettings.BankruptScaling, ScriptSettings.BankruptCooldown, ScriptSettings.BankruptUserCooldown, ScriptSettings.BankruptStartsOnCooldown)
    ActionCommands["weaken"] = Command("weaken", 7, 1, ScriptSettings.WeakenEnabled, ScriptSettings.WeakenCost, ScriptSettings.WeakenMaxCost, ScriptSettings.WeakenScaling, ScriptSettings.WeakenCooldown, ScriptSettings.WeakenUserCooldown, ScriptSettings.WeakenStartsOnCooldown)
    ActionCommands["respawnbosses"] = Command("respawnbosses", 8, 1, ScriptSettings.RespawnBossesEnabled, ScriptSettings.RespawnBossesCost, ScriptSettings.RespawnBossesMaxCost, ScriptSettings.RespawnBossesScaling, ScriptSettings.RespawnBossesCooldown, ScriptSettings.RespawnBossesUserCooldown, ScriptSettings.RespawnBossesStartsOnCooldown)
    ActionCommands["honest"] = Command("honest", 9, 1, ScriptSettings.HonestGamerEnabled, ScriptSettings.HonestGamerCost, ScriptSettings.HonestGamerMaxCost, ScriptSettings.HonestGamerScaling, ScriptSettings.HonestGamerCooldown, ScriptSettings.HonestGamerUserCooldown, ScriptSettings.HonestGamerStartsOnCooldown)
    ActionCommands["subsonly"] = Command("subsonly", 10, 1, ScriptSettings.SubweaponsOnlyEnabled, ScriptSettings.SubweaponsOnlyCost, ScriptSettings.SubweaponsOnlyMaxCost, ScriptSettings.SubweaponsOnlyScaling, ScriptSettings.SubweaponsOnlyCooldown, ScriptSettings.SubweaponsOnlyUserCooldown, ScriptSettings.SubweaponsOnlyStartsOnCooldown)
    ActionCommands["cripple"] = Command("cripple", 11, 1, ScriptSettings.CrippleEnabled, ScriptSettings.CrippleCost, ScriptSettings.CrippleMaxCost, ScriptSettings.CrippleScaling, ScriptSettings.CrippleCooldown, ScriptSettings.CrippleUserCooldown, ScriptSettings.CrippleStartsOnCooldown)
    ActionCommands["bloodmana"] = Command("bloodmana", 12, 1, ScriptSettings.BloodManaEnabled, ScriptSettings.BloodManaCost, ScriptSettings.BloodManaMaxCost, ScriptSettings.BloodManaScaling, ScriptSettings.BloodManaCooldown, ScriptSettings.BloodManaUserCooldown, ScriptSettings.BloodManaStartsOnCooldown)
    ActionCommands["thirst"] = Command("thirst", 13, 1, ScriptSettings.ThirstEnabled, ScriptSettings.ThirstCost, ScriptSettings.ThirstMaxCost, ScriptSettings.ThirstScaling, ScriptSettings.ThirstCooldown, ScriptSettings.ThirstUserCooldown, ScriptSettings.ThirstStartsOnCooldown)
    ActionCommands["horde"] = Command("horde", 14, 1, ScriptSettings.HordeEnabled, ScriptSettings.HordeCost, ScriptSettings.HordeMaxCost, ScriptSettings.HordeScaling, ScriptSettings.HordeCooldown, ScriptSettings.HordeUserCooldown, ScriptSettings.HordeStartsOnCooldown)
    ActionCommands["endurance"] = Command("endurance", 15, 1, ScriptSettings.EnduranceEnabled, ScriptSettings.EnduranceCost, ScriptSettings.EnduranceMaxCost, ScriptSettings.EnduranceScaling, ScriptSettings.EnduranceCooldown, ScriptSettings.EnduranceUserCooldown, ScriptSettings.EnduranceStartsOnCooldown)
    # Buffs
    ActionCommands["vampire"] = Command("vampire", 16, 2, ScriptSettings.VampireEnabled, ScriptSettings.VampireCost, ScriptSettings.VampireMaxCost, ScriptSettings.VampireScaling, ScriptSettings.VampireCooldown, ScriptSettings.VampireUserCooldown, ScriptSettings.VampireStartsOnCooldown)
    ActionCommands["lighthelp"] = Command("lighthelp", 17, 2, ScriptSettings.LightHelpEnabled, ScriptSettings.LightHelpCost, ScriptSettings.LightHelpMaxCost, ScriptSettings.LightHelpScaling, ScriptSettings.LightHelpCooldown, ScriptSettings.LightHelpUserCooldown, ScriptSettings.LightHelpStartsOnCooldown)
    ActionCommands["mediumhelp"] = Command("mediumhelp", 18, 2, ScriptSettings.MediumHelpEnabled, ScriptSettings.MediumHelpCost, ScriptSettings.MediumHelpMaxCost, ScriptSettings.MediumHelpScaling, ScriptSettings.MediumHelpCooldown, ScriptSettings.MediumHelpUserCooldown, ScriptSettings.MediumHelpStartsOnCooldown)
    ActionCommands["heavyhelp"] = Command("heavyhelp", 19, 2, ScriptSettings.HeavyHelpEnabled, ScriptSettings.HeavyHelpCost, ScriptSettings.HeavyHelpMaxCost, ScriptSettings.HeavyHelpScaling, ScriptSettings.HeavyHelpCooldown, ScriptSettings.HeavyHelpUserCooldown, ScriptSettings.HeavyHelpStartsOnCooldown)
    ActionCommands["battleorders"] = Command("battleorders", 20, 2, ScriptSettings.BattleOrdersEnabled, ScriptSettings.BattleOrdersCost, ScriptSettings.BattleOrdersMaxCost, ScriptSettings.BattleOrdersScaling, ScriptSettings.BattleOrdersCooldown, ScriptSettings.BattleOrdersUserCooldown, ScriptSettings.BattleOrdersStartsOnCooldown)
    ActionCommands["magician"] = Command("magician", 21, 2, ScriptSettings.MagicianEnabled, ScriptSettings.MagicianCost, ScriptSettings.MagicianMaxCost, ScriptSettings.MagicianScaling, ScriptSettings.MagicianCooldown, ScriptSettings.MagicianUserCooldown, ScriptSettings.MagicianStartsOnCooldown)
    ActionCommands["melty"] = Command("melty", 22, 2, ScriptSettings.MeltyBloodEnabled, ScriptSettings.MeltyBloodCost, ScriptSettings.MeltyBloodMaxCost, ScriptSettings.MeltyBloodScaling, ScriptSettings.MeltyBloodCooldown, ScriptSettings.MeltyBloodUserCooldown, ScriptSettings.MeltyBloodStartsOnCooldown)
    ActionCommands["fourbeasts"] = Command("fourbeasts", 23, 2, ScriptSettings.FourBeastsEnabled, ScriptSettings.FourBeastsCost, ScriptSettings.FourBeastsMaxCost, ScriptSettings.FourBeastsScaling, ScriptSettings.FourBeastsCooldown, ScriptSettings.FourBeastsUserCooldown, ScriptSettings.FourBeastsStartsOnCooldown)
    ActionCommands["zawarudo"] = Command("zawarudo", 24, 2, ScriptSettings.ZaWarudoEnabled, ScriptSettings.ZaWarudoCost, ScriptSettings.ZaWarudoMaxCost, ScriptSettings.ZaWarudoScaling, ScriptSettings.ZaWarudoCooldown, ScriptSettings.ZaWarudoUserCooldown, ScriptSettings.ZaWarudoStartsOnCooldown)
    ActionCommands["haste"] = Command("haste", 25, 2, ScriptSettings.HasteEnabled, ScriptSettings.HasteCost, ScriptSettings.HasteMaxCost, ScriptSettings.HasteScaling, ScriptSettings.HasteCooldown, ScriptSettings.HasteUserCooldown, ScriptSettings.HasteStartsOnCooldown)

    # Output commands file for overlay
    with codecs.open(OverlayCommandsFile, encoding="utf-8-sig", mode="w+") as f:
        f.write("var commands = {0};".format(json.dumps(ActionCommands, indent=4, encoding='utf-8', ensure_ascii=False, cls = CommandEncoder)))

    return

#---------------------------
#   Process messages
#---------------------------
def Execute(data):
    if not data.IsChatMessage():
        return

    if not Khaos["on"] and Parent.HasPermission(data.User, "Moderator", "") and data.GetParam(0).lower() == '!startkhaos':
        Khaos["on"] = True
        Parent.SendStreamMessage("Khaos started!")
        # Put commands on starting cooldown
        ActivateStartingCooldowns()
        return
    elif Khaos["on"] and Parent.HasPermission(data.User, "Moderator", "") and data.GetParam(0).lower() == '!stopkhaos':
        Khaos["on"] = False
        Parent.SendStreamMessage("Khaos stopped!")
        return
    elif Khaos["on"] and Parent.HasPermission(data.User, "Moderator", "") and data.GetParam(0).lower() == '!pausekhaos':
        Khaos["paused"] = True
        Parent.SendStreamMessage("Khaos paused!")
        return
    elif Khaos["on"] and Parent.HasPermission(data.User, "Moderator", "") and data.GetParam(0).lower() == '!unpausekhaos':
        Khaos["paused"] = False
        Parent.SendStreamMessage("Khaos unpaused!")
        return

    if not Khaos["on"] or Khaos["paused"]:
        return

    for key in ActionCommands:
        if ActionCommands[key].enabled and data.GetParam(0).lower() == "!" + ActionCommands[key].command:
            ActionCommands[key].Execute(data.User, data.UserName)
            return

    return

#---------------------------------------
#   Helper Functions
#---------------------------------------
def HasCurrency(User, UserName, cost):
    if (cost == 0):
        return true
    elif (Parent.RemovePoints(User, UserName, cost)):
        pointsRemaining = Parent.GetPoints(User)
        Parent.SendStreamWhisper(User,"{0} remaining: {1}".format(Khaos["currency"], pointsRemaining))
        return True
    else:
        currentPoints = Parent.GetPoints(User)
        Parent.SendStreamWhisper(User,"Not enough {0}. Current {0}: {1}".format(Khaos["currency"], currentPoints))
        return False

def ActivateStartingCooldowns():
    Parent.BroadcastWsEvent("EVENT_START", '')
    for key in ActionCommands:
        if  ActionCommands[key].startsOnCooldown:
            ActionCommands[key].PutOnCooldown()
#---------------------------------------
#   Chatbot Tick Function
#---------------------------------------
def Tick():
    return

#---------------------------------------
#   Chatbot Save Settings Function
#---------------------------------------
def ReloadSettings(jsondata):
    ScriptSettings.Reload(jsondata)
    return

#---------------------------
#   Unload
#---------------------------
def Unload():
    return

#---------------------------
#   ScriptToggled
#---------------------------
def ScriptToggled(state):
    return
