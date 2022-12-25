import find_contact
import new_contact
import view
import logger


def run():
    tmp = "1"
    while(tmp == "1"):
        mode = view.choose_mode()
        if mode == '1':
            result = find_contact.find_contact()
            view.show_results(result)
            logger.log_result(result)
            tmp = input("1 - продолжить работу\n2 - закончить")
        if mode == '2':
            result = new_contact.new_contact()
            view.show_results(result)
            logger.log_result(result)
            tmp = input("1 - продолжить работу\n2 - закончить")