from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.temu.com/ul/kuiper/un9.html?subj=goods-un&_bg_fs=1&_p_jump_id=894&_x_vst_scene=adg&goods_id=601099522407628&sku_id=17592241603785&adg_ctx=a-dd189da5~c-e7bb5fe7~f-cd180cc1&_x_ads_sub_channel=shopping&_p_rfs=1&_x_ns_prz_type=3&_x_ns_sku_id=17592241603785&_x_ns_gid=601099522407628&mrk_rec=1&_x_ads_channel=google&_x_gmc_account=5072611099&_x_login_type=Google&_x_ads_account=9704659649&_x_ads_set=21278955567&_x_ads_id=162181349733&_x_ads_creative_id=699377609462&_x_ns_source=g&_x_ns_gclid=Cj0KCQjwtsy1BhD7ARIsAHOi4xZv28MVOH4tPohszQvZxBSZEwGLsSbDyPpMtXG1uLPtTeHbzIId_nMaApzhEALw_wcB&_x_ns_placement=&_x_ns_match_type=&_x_ns_ad_position=&_x_ns_product_id=17592241603785&_x_ns_target=&_x_ns_devicemodel=&_x_ns_wbraid=Cj8KCQjwk8e1BhCzARIuAL5yFq-OlL6nE7zFUQoNC1K6G83EA5utOzpY2AL_YuGyBL6B0vNbZ7J1C36ethoCQKs&_x_ns_gbraid=0AAAAAo4mICE3EbWkBB-3Yx0AjgaNv42BL&_x_ns_targetid=pla-2328106488194&gad_source=1&gclid=Cj0KCQjwtsy1BhD7ARIsAHOi4xZv28MVOH4tPohszQvZxBSZEwGLsSbDyPpMtXG1uLPtTeHbzIId_nMaApzhEALw_wcB")
# price_won = driver.find_element(By.CLASS_NAME, value="salePriceAmount-3hxCi")
# print(f"The price is {price_won.text}")

driver.get(url="https://www.python.org/")
# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
# art_link = driver.find_element(By.XPATH, value='//*[@id="container"]/li[5]/ul/li[1]/a')
# print(art_link.text)
event_date = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_name = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
events = {}
for n in range(5):
    events[n] = {
        'time': event_date[n].text,
        'name': event_name[n].text
    }
print(events)

# driver.close()
driver.quit()
