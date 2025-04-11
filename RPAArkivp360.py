from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()
# Spesifiser en unik brukerdata-katalog for å unngå konflikt
options.add_argument(f"--user-data-dir=C:\\temp\\EdgeProfile_{int(time.time())}")

driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
driver.maximize_window()
driver.get('https://unitest01.public360online.com/GlobalDesktop/Custom/Under%20Arbeid')


# Vente på nettside for å laste.
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))


# Finne elementer og klikke på dem
search_input = driver.find_element(By.ID, 'org_selector_filter')
search_input.click()





# Kilkke på feide innlogging
search_input.send_keys('Universitetet i Agder')

# OK klikke
search_input.send_keys(Keys.RETURN)

# finne elementer med XPATH
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="orglist"]')))

# finne elementer og klikke
search_result = driver.find_element(By.XPATH, '//*[@id="orglist"]')
search_result.click()

# Venter på fortsett knappen og klikker på den
fortsett_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Fortsett")]')))
fortsett_button.click()

# finne microsoft innlogging knappen og klikke på den
microsoft_signin_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="microsoft-signin-button"]')))
microsoft_signin_button.click()

# Gi tid for å laste innloggingssiden
time.sleep(5)


# vente og klikke
tiles_element = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tilesHolder"]/div[1]/div/div/div/div[2]')))
tiles_element.click()

# forsinkelse
time.sleep(2)

#Sidepanel
side_panel_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="si-my-items-side-panel-container"]/div/div[1]/nav/div/div[4]/button')))
driver.execute_script("arguments[0].click();", side_panel_button)

#forsinkelse
time.sleep(2)

final_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="si-my-items-side-panel-container"]/div/div[1]/div/div[2]/div/div/div[1]')))
final_element.click()

# forsinkelse
time.sleep(2)

favorite_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="PlaceHolderMain_MainView_FavoriteListControl_body__BoundColumn_0_anchor_8"]')))
favorite_element.click()

# forsinkelse
time.sleep(2)




# Funksjon for å endre status på siste fire saker i tabell. Jeg jar kopiert HTML elemnter fra nettsiden for å bruke dem i koden. Try-except blokk er brukt for å håndtere feil.

def change_case_status(driver, case_number):
    try:
        case_xpath = f'//*[@id="PlaceHolderMain_MainView_FavoriteCases_body__BoundColumn_2_anchor_{case_number}"]'
        case = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, case_xpath))
        )
        case.click()
        time.sleep(2)

        # Finne status knappen og klikke på den.
        try:
            set_status_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="PlaceHolderMain_MainView_SetStatusButton_DetailFunctionControl"]/span'))
            )
            set_status_button.click()
        except:
            # ststus knappen ikke funnet, gå tilbake til listen
            driver.switch_to.default_content()
            back_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/header/div[2]/nav/ol/li[2]/a'))
            )
            back_button.click()
            time.sleep(2)
            return False

        # Må endre her fra nettside til Iframe for å kunne klikke på status knappen
        iframe = WebDriverWait(driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src*="EditCaseStatus"]'))
        )
        # klikke på dropdown for å velge ny status
        dropdown = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="PlaceHolderMain_MainView_CaseStatusComboControl_div"]'))
        )
        dropdown.click()
        time.sleep(1)
        # Velge ny status
        option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@data-value="6"]'))
        )
        option.click()
        time.sleep(2)
        # OK klikk
        ok_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'PlaceHolderMain_MainView_Finish-Button'))
        )
        ok_button.click()
    

        # endre tilbake til hovedvindu Robot_Avslutt_sak
        driver.switch_to.default_content()
        time.sleep(2)

        # Prøv å klikke på Robot_Avslutt_sak i header
        try:
            avslutt_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href*="Robot_Avslutt_sak"][class*="fui-Button"]'))
            )
            avslutt_link.click()
            time.sleep(2)
        except:
            # If Robot_Avslutt_sak fails, Prøv å klikke på tilbake knappen
            back_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/header/div[2]/nav/ol/li[2]/a'))
            )
            back_button.click()
            time.sleep(2)
            return False

        return True

    except Exception:
        # Altid gå tilbake til listen, ved feil.
        try:
            driver.switch_to.default_content()
            back_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/header/div[2]/nav/ol/li[2]/a'))
            )
            back_button.click()
        except:
            pass
        return False


# loop for å endre status på siste fire saker.
try:
    
    case_elements = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@id, "PlaceHolderMain_MainView_FavoriteCases_body__BoundColumn_2_anchor_")]'))
    )
    total_cases = len(case_elements)
    print(f"Funnet {total_cases} saker.")

    start_index = max(total_cases - 4, 0)
    success_count = 0
    for i in range(start_index, total_cases):
        if change_case_status(driver, i):
            success_count += 1
        time.sleep(2)
    print(f"Endret status til: {success_count} ut av {total_cases}")
except Exception as e:
    print(f"Error in processing cases: {e}")



 
# lukke nettleser
driver.quit()

