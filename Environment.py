from Browser import Browser
from Pages.sign_up_page import Sign_up_page
from Pages.sign_in_page import Sign_in_page
from Pages.verify_url_page import Verify_url



def before_all(context):
    #  * beefore_all este o metoda recunoscuta de libraria behave si care se
    #  va executa inainte de toate testele
    #  * context este ca o cutiuta in care vom stoca toate atributele ce pot fi folosite in alte fisiere
    context.browser = Browser()
    context.sign_up_object = Sign_up_page()
    context.sign_in_object = Sign_in_page()
    context.verify_url_object = Verify_url()


def after_all(context):
    # * after_all este o metoda recunoscuta de libraria behave si care se
    #     #  va executa dupa de toate testele
    context.browser.close()