import requests
from PyQt5.QtWidgets import *
from mojang import API
from view import *
from exceptions import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        """
        Constructor that initializes the GUI
        and connects the "Search" and "Clear"
        buttons to their respective functions.
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.clearButton.clicked.connect(lambda: self.clear())
        self.searchButton.clicked.connect(lambda: self.search())

    def error_ss(self):
        """
        Function used to change the style sheets for the
        "Username" QLineEdit, "Profile" QLineEdit, and "ProcessDisplay" QTextEntry to indicate an error.
        """
        self.formLayoutWidget.setStyleSheet("QLineEdit {"
                                            "font: 12pt \"Consolas\";"
                                            "color: white;"
                                            "background-color: rgb(96, 96, 96);"
                                            "border-color: rgb(255, 100, 100);"
                                            "border-radius: 12px;"
                                            "border-style: outset;"
                                            "border-width: 2px;}"
                                            "QLineEdit:focus {"
                                            "background-color: teal;}")
        self.processDisplay.setStyleSheet("font: 12pt \"Consolas\";"
                                          "background-color: rgb(96, 96, 96);"
                                          "color: white;"
                                          "border-radius: 16px;"
                                          "border-width: 2px;"
                                          "border-style: solid;"
                                          "border-color: rgb(255, 100, 100);")

    def display(self, skill_data: dict, profile_id: str):
        """
        Function searches through the provided dictionary to locate player statistics including
        "Taming", "Farming", "Mining", "Combat", "Foraging", "Fishing", "Enchanting", "Alchemy",
        "Carpentry", "Runecrafting", and "Social" levels. Additionally, the function sets the value of the corresponding
        QLabel to reflect the data given.
        :param skill_data:
        :param profile_id:
        :return:
        """
        try:
            if profile_id is None:
                raise TypeError
            elif len(profile_id) != 0:
                taming = skill_data['profiles'][profile_id]['data']['levels']['taming']['level']
                farming = skill_data['profiles'][profile_id]['data']['levels']['farming']['level']
                mining = skill_data['profiles'][profile_id]['data']['levels']['mining']['level']
                combat = skill_data['profiles'][profile_id]['data']['levels']['combat']['level']
                foraging = skill_data['profiles'][profile_id]['data']['levels']['foraging']['level']
                fishing = skill_data['profiles'][profile_id]['data']['levels']['fishing']['level']
                enchanting = skill_data['profiles'][profile_id]['data']['levels']['enchanting']['level']
                alchemy = skill_data['profiles'][profile_id]['data']['levels']['alchemy']['level']
                carpentry = skill_data['profiles'][profile_id]['data']['levels']['carpentry']['level']
                runecrafting = skill_data['profiles'][profile_id]['data']['levels']['runecrafting']['level']
                social = skill_data['profiles'][profile_id]['data']['levels']['social']['level']

                if taming == 50:
                    self.tamingLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(224, 85, 85);")
                if farming == 60:
                    self.farmingLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(224, 85, 85);")
                if mining == 60:
                    self.miningLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(224, 85, 85);")
                if combat == 60:
                    self.combatLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(224, 85, 85);")
                if foraging == 50:
                    self.foragingLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(224, 85, 85);")
                if fishing == 50:
                    self.fishingLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(224, 85, 85);")
                if enchanting == 60:
                    self.enchantingLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(224, 85, 85);")
                if alchemy == 50:
                    self.alchemyLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(224, 85, 85);")
                if carpentry == 50:
                    self.carpentryLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(224, 85, 85);")
                if runecrafting == 25:
                    self.runecraftingLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(224, 85, 85);")
                if social == 25:
                    self.socialLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(0, 255, 255);")
                self.tamingLevel.setText(
                    str(skill_data['profiles'][profile_id]['data']['levels']['taming']['level']))
                self.farmingLevel.setText(
                    str(skill_data['profiles'][profile_id]['data']['levels']['farming']['level']))
                self.miningLevel.setText(
                    str(skill_data['profiles'][profile_id]['data']['levels']['mining']['level']))
                self.combatLevel.setText(
                    str(skill_data['profiles'][profile_id]['data']['levels']['combat']['level']))
                self.foragingLevel.setText(
                    str(skill_data['profiles'][profile_id]['data']['levels']['foraging']['level']))
                self.fishingLevel.setText(
                    str(skill_data['profiles'][profile_id]['data']['levels']['fishing']['level']))
                self.enchantingLevel.setText(
                    str(skill_data['profiles'][profile_id]['data']['levels']['enchanting']['level']))
                self.alchemyLevel.setText(
                    str(skill_data['profiles'][profile_id]['data']['levels']['alchemy']['level']))
                self.carpentryLevel.setText(
                    str(skill_data['profiles'][profile_id]['data']['levels']['carpentry']['level']))
                self.runecraftingLevel.setText(
                    str(skill_data['profiles'][profile_id]['data']['levels']['runecrafting']['level']))
                self.socialLevel.setText(
                    str(skill_data['profiles'][profile_id]['data']['levels']['social']['level']))
                self.processDisplay.setPlainText(f"Task succeeded\nRed digits indicate a skill with a maximum level")
            else:
                raise ValueError
        except KeyError:
            self.processDisplay.setPlainText(f'Error: Unable to fetch player statistics')
            self.error_ss()
        except ValueError:
            self.processDisplay.setPlainText(f'Error: No profile input')
            self.error_ss()
        except TypeError:
            out = f'Available profiles: '
            for i in skill_data['profiles']:
                out = out + f"\n{skill_data['profiles'][i]['cute_name']}"
            self.processDisplay.setPlainText(f'Error: Profile does not exist\n{out}')

            self.error_ss()

    def search(self):
        """
        Function bound to the "Search" button used to gather information from the entry fields,
        make a UUID request to the Mojang API, make a request from the SkyCrypt API using the previously requested UUID,
        and store the profile ID associated with the specified profile.
        """
        api = API()
        profile_id = None
        try:
            username = self.usernameInput.text()
            if len(username) == 0:
                raise UsernameError
            profile = self.profileInput.text()
            if len(profile) == 0:
                raise ProfileError
            uuid = api.get_uuid(username)
            if uuid is None:
                raise UUIDError

            skill_data = requests.get(f'https://sky.shiiyu.moe/api/v2/profile/{uuid}').json()

            for i in skill_data:
                if i == 'error':
                    raise ZeroProfile

            for i in skill_data['profiles']:
                if str(skill_data['profiles'][i]['cute_name']) == profile:
                    profile_id = i

            self.display(skill_data, profile_id)
        except UsernameError:
            self.processDisplay.setPlainText(f'Error: No username input')
            self.error_ss()

        except UUIDError:
            self.processDisplay.setPlainText(f'Error: Invalid username input')
            self.error_ss()

        except ZeroProfile:
            self.processDisplay.setPlainText(f'Error: No profiles associated with this account')
            self.error_ss()

        except ProfileError:
            self.processDisplay.setPlainText(f'Error: No profile input')
            self.error_ss()

    def clear(self):
        """
        Function bound to the "Clear" button used to return all respective widgets
        to their initial states by clearing entries and reverting changes made to style sheets.
        """
        self.usernameInput.clear()
        self.profileInput.clear()
        self.processDisplay.clear()

        self.tamingLevel.setText('0')
        self.farmingLevel.setText('0')
        self.miningLevel.setText('0')
        self.combatLevel.setText('0')
        self.foragingLevel.setText('0')
        self.fishingLevel.setText('0')
        self.enchantingLevel.setText('0')
        self.alchemyLevel.setText('0')
        self.carpentryLevel.setText('0')
        self.runecraftingLevel.setText('0')
        self.socialLevel.setText('0')

        self.tamingLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(100, 200, 200);")
        self.farmingLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(100, 200, 200);")
        self.miningLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(100, 200, 200);")
        self.combatLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(100, 200, 200);")
        self.foragingLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(100, 200, 200);")
        self.fishingLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(100, 200, 200);")
        self.enchantingLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(100, 200, 200);")
        self.alchemyLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(100, 200, 200);")
        self.carpentryLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(100, 200, 200);")
        self.runecraftingLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(100, 200, 200);")
        self.socialLevel.setStyleSheet("font: 75 16pt \"Consolas\";\n""color: rgb(100, 200, 200);")

        self.formLayoutWidget.setStyleSheet("QLineEdit {"
                                            "font: 12pt \"Consolas\";"
                                            "color: white;"
                                            "background-color: rgb(96, 96, 96);"
                                            "border-color: white;"
                                            "border-radius: 12px;"
                                            "border-style: outset;"
                                            "border-width: 2px;}"
                                            "QLineEdit:focus {"
                                            "background-color: teal;}")

        self.processDisplay.setStyleSheet("font: 12pt \"Consolas\";"
                                          "background-color: rgb(96, 96, 96);"
                                          "color: white;"
                                          "border-radius: 16px;"
                                          "border-width: 2px;"
                                          "border-style: outset;"
                                          "border-color: white;")
