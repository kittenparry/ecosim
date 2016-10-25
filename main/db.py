defvalnames = ['year', 'month', 'week', 'money','firsttime']
defvalvals = [1, 1, 1, 10000, False]
defprices = [50, 30, 20, 25, 10, 100, 25, 15]

interface_main_tab = "+-------------------------+-----+"
interface_main_mid = "|{0:2}.{1:22}|{2:^5}|"


locale = "EN"
if locale == "EN":
    products = ["Batteries", "Chocolate", "Coffee", "Ice Cream",
                "Matches", "Painkillers", "Pens", "Tissues"]
    interface_text = ['year', 'month', 'week']
    txt_help = "Type help for commands."
    txt_load_fail = "Loading failed."
    txt_save_fail = "Saving failed."

    cmds_gen = "####COMMANDS####" \
               "#CONSOLE RELATED#" \
               "exit" \
               "help" \
               "#GAME RELATED#" \
               "##IN-GAME##" \
               "#UTIL#" \
               "del_saves" \
               "save"