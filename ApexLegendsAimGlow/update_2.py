import re
import colorama
import os
import time

list = []
with open("Program.cs") as file:
    lines = file.readlines()
    for line in lines:
        pattern = r'\bVirtualKeyCode\.([a-zA-Z]+)\b'
        result = re.findall(pattern, line)
        for i in result:
            list.append(i)
    print("List = ", list)
        # if result:
        #     string = str(result)
        #     final = string.split(",")
        #     update = final[0].replace("['", "")
        #     update_2 = update.replace("']", "")
        #     if update_2 != "Delete":
        #         keys = update_2
        #         print(keys)

#
#
# class Main:
#
#     def __init__(self):
#         print(colorama.Fore.WHITE)
#         print("Apex Legends Script", colorama.Fore.GREEN)
#         print("    Made by Python-Cod")
#         print(colorama.Fore.BLUE)
#         print("Released:")
#         print("1. Change Aim Key.")
#         print("2. See current settings.")
#         print()
#         print(colorama.Fore.LIGHTRED_EX)
#         print("In progress, don't use them!:")
#         print("3. Change Fov size.")
#         print("4. Change Aim Spot Key")
#         print("More coming soon")
#         print()
#         print(colorama.Fore.CYAN)
#         option = int(input("Select an option: "))
#         while option != 1 and option != 2:
#             option = int(input("Select an option: "))
#         if option == 1:
#             print(colorama.Fore.MAGENTA)
#             print('''Change aim key to:
#                 1.Right Mouse Button
#                 2.Alt
#                 3.Control
#                 4.Shift
#                 ''')
#             print(colorama.Fore.CYAN)
#             key_choice = int(input("Choose: "))
#             if key_choice == 1:
#                 self.key = "RightMouse"
#             elif key_choice == 2:
#                 self.key = "Alt"
#             elif key_choice == 3:
#                 self.key = "Control"
#             elif key_choice == 4:
#                 self.key = "Shift"
#             with open("Program.cs") as self.file:
#                 self.lines = self.file.readlines()
#                 for self.line in self.lines:
#                     self.pattern = r'(?<=VirtualKeyCode\.).*(?=,)'
#                     self.result = re.findall(self.pattern, self.line)
#                     if self.result is not None:
#                         if self.result:
#                             self.string = str(self.result)
#                             self.final = self.string.split(",")
#                             self.result1 = self.final[0].replace("['", '')
#                             self.result2 = self.result1
#                             if self.result1 != "Delete":
#                                 self.sub = self.result2
#                                 print(colorama.Fore.LIGHTGREEN_EX)
#                                 print("Key setting changing to", self.key, "...")
#                                 print(colorama.Fore.RESET)
#
#             self.version_2 = ""
#             with open("Program.cs") as f:
#                 for i in f:
#                     self.version_2 += i
#             self.sub_change = re.sub(self.sub, self.key, self.version_2)
#             with open("replace.txt", "w") as file:
#                 file.write(self.sub_change)
#             time.sleep(3)
#             print(colorama.Fore.LIGHTGREEN_EX)
#             print("Key setting changed to", self.key, "successfully!!!")
#             print(colorama.Fore.RESET)
#             # Finish
#             os.remove("Program.cs")
#             os.rename("replace.txt", "Program.cs")
#
#             print(colorama.Fore.LIGHTYELLOW_EX)
#             print("Do you want to run again? (Y or N)")
#             again = input()
#             while again != "Y" and again != "N":
#                 again = input()
#             if again == "Y":
#                 run_again = Main()
#             if again == "N":
#                 pass
#
#         if option == 2:
#             with open("Program.cs") as self.file:
#                 self.lines = self.file.readlines()
#                 for self.line in self.lines:
#                     self.pattern = r'(?<="Aimbot HotKey (HOLD)", VirtualKeyCode\.).*(?=,)'
#                     self.result = re.findall(self.pattern, self.line)
#                     if self.result is not None:
#                         if self.result:
#                             self.string = str(self.result)
#                             self.final = self.string.split(",")
#                             self.result1 = self.final[0].replace("['", '')
#                             self.result2 = self.result1
#                             if self.result1 != "Delete":
#                                 self.sub = self.result2
#                                 print(colorama.Fore.LIGHTGREEN_EX)
#                                 print("Current setting is", self.result2)
#                                 print(colorama.Fore.RESET)
#         print(colorama.Fore.LIGHTYELLOW_EX)
#         print("Do you want to run again? (Y or N)")
#         again = input()
#         while again != "Y" and again != "N":
#             again = input()
#         if again == "Y":
#             run_again = Main()
#         if again == "N":
#             pass
#
#
# run = Main()
