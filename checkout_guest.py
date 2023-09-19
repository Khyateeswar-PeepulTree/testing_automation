import json
import profile
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains


#######itention was to use cash on delivery and make an automated purchase

# The webdriver management will be handled by the browserstack-sdk
# so this will be overridden and tests will run browserstack -
# without any changes to the test files!
# options = ChromeOptions()
# options.set_capability('sessionName', 'Dev Peepultree checkout test')
# driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()

# xpath of checkout button - /html/body/div/div/div/main/section[1]/div/div/div[2]/div[1]/div[5]/button
#                          - //button[@class = "btn primary-btn w-full p-[7px] text-[18px] leading-[24px] rounded-[4px]"]
#                          - //button[contains(text(),"Checkout")]
# xpath of filling email in checkout - //input[@type='email']

# xpath of submitting email for cheokout - //button[@type='submit']

# xpath of the email in address input page - //div[@class = 'flex bg-[#fff] rounded px-2 my-5']/input (value contains the email value )

# xpath of the email edit in address input page - //img[@src="/_next/static/media/edit-icon-otp.8108cbad.svg"]

#xpath of the full name in the address input page - //input[@placeholder="Full Name"]

#xpath of the phone in  the address input page - //input[@id="phone"]

#xpath of the pincode in the address input page - //input[@id="zip"]

#xpath of the address in the address input page - //textarea[@id="address1"]

#xpath of the save in the address input page - //button[@type='submit']

#xpath of the exit address in the order summary page - //div[@class="text-[12px] font-bold !text-[#C19426] cursor-pointer hover:underline edit-link"]

#xpath of the email in order summary page is same as the save address page

#xpath of the address in order summary page - //div[@class="select-address bg-[#fff] p-4 rounded"]//div[@class="!text-[#1d1d1d] mt-2 max-w-[400px] "]//p[1]

#xpath of the phone in order summary page - //div[@class="select-address bg-[#fff] p-4 rounded"]//div[@class="!text-[#1d1d1d] mt-2 max-w-[400px] "]//p[3]

#xpath of the pincode in order summary page - //div[@class="text-sm font-semibold text-[#1d1d1d] max-w-[400px]"]

try: 
     mail = "sel12323@gmail.com"
     address = "Madhuram"
     phone = "8688164030"
     first_name = "selen"
     last_name = "pyth"
     pincode = "500001"
     country = "India"
     driver.implicitly_wait(10) 
     start = time.time()

    #  driver.get('https://www.whatismyip.com/')
    #  time.sleep(10)

     driver.get('https://dev.peepultree.world/products/beaded-long-necklace-and-earring-set-enchanted-garden')   
    
    #  time.sleep(1)
     check_button = driver.find_element(By.XPATH,'//button[contains(text(),"Checkout")]' )
     check_button.click()

    #  time.sleep(1)
     t = driver.find_element(By.XPATH,'//div[@class="back-arrow cursor-pointer"]/h1').text
     if t=='Customer Details':
            print("success in reaching the email filling page")
     email_inp = driver.find_element(By.XPATH, "//input[@type='email']")
     email_inp.send_keys(mail)
     sub_email = driver.find_element(By.XPATH,"//button[@type='submit']")
     sub_email.click()
    #  if driver.find_element(By.XPATH,"//div[@class = 'back-arrow cursor-pointer']/h1").text == 'Customer Details':
    #         print("Success in reaching the address filling page")
    

     val_em = driver.find_element(By.XPATH,"//div[@class = 'flex bg-[#fff] rounded px-2 my-5']/input")
     if val_em.get_attribute("value")==mail:
            print("email got succesfully recovered from session")
     name_inp = driver.find_element(By.XPATH,"//input[@placeholder='Full Name']")
     name_inp.send_keys(first_name)
     name_inp.send_keys(" ")
     name_inp.send_keys(last_name)

     
     ph_inp = driver.find_element(By.XPATH,'//input[@id="phone"]')
     ph_inp.send_keys(phone)


     con_men = driver.find_element(By.XPATH,'//div[@class="undefined relative custom-dropdown dropdown-main"]//button')
     con_men.click()
    #  time.sleep(1)

     drop_down =  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//ul')))
     li_elements = drop_down.find_elements(By.TAG_NAME, "li")
     li_elements[0].click()
    #  time.sleep(1)

     try:
         
         inr = driver.find_element(By.XPATH,'//p[contains(text(),"INR")]')
         inr.click()
         time.sleep(2)
         cur = driver.find_element(By.XPATH,'//button[contains(text(),"Continue")]')
         cur.click()
     except:
         print("No need to change currency")

    
    #  time.sleep(1)
    
     pin_inp = driver.find_element(By.XPATH,'//input[@id="zip"]')
     pin_inp.send_keys(pincode)

     pin_val =  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="form-row"]')))

    #  time.sleep(1)   #  try:
    #        con_inp = driver.find_element(By.XPATH,'//input[@placeholder="India"]') 
    #  except:
    #        con_inp = driver.find_element(By.XPATH,'//input[@role="combobox"]')
    #        con_inp.send_keys(country)
     
     add_inp = driver.find_element(By.XPATH,'//textarea[@id="address1"]')
     
    #  action = ActionChains(driver)
    #  action.click(on_element = add_inp)
    #  action.send_keys(address)
    #  action.pause(5)
    #  action.release(on_element = add_inp)
    #  action.perform()
     add_inp.click()
     add_inp.clear()
     add_inp.send_keys(address)
   
    
     name_inp.click()
    #  add_inp.send_keys(" ")
    #  add_inp.send_keys(" kara4kids")


     print(add_inp.text)
     
  

    
    #  sav = driver.find_element(By.XPATH,"//button[@type='submit']")
    #   (10)
    


    #  while   (EC.visibility_of_element_located((By.XPATH,'//p[@class="error-text"]'))):
    #     print("something is not filled")
    #     try:
    #         name_inp = driver.find_element(By.XPATH,"//input[@placeholder='Full Name']")
    #         name_inp.send_keys(first_name)
    #         name_inp.send_keys(" ")
    #         name_inp.send_keys(last_name)

        
    #         ph_inp = driver.find_element(By.XPATH,'//input[@id="phone"]')
    #         ph_inp.send_keys(phone)

    #         time.sleep(2)

    #         con_men = driver.find_element(By.XPATH,'//div[@class="undefined relative custom-dropdown dropdown-main"]//button')
    #         con_men.click()
    #         time.sleep(2)

    #         drop_down =  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//ul')))
    #         li_elements = drop_down.find_elements(By.TAG_NAME, "li")
    #         li_elements[0].click()
    #         time.sleep(2)

    #         try:
    #             cur = driver.find_element(By.XPATH,'//button[contains(text(),"Continue")]')
    #             inr = driver.find_element(By.XPATH,'//p[contains(text(),"INR")]')
    #             inr.click()
    #             cur.click()
    #         except:
    #             print("No need to change currency")

        
    #         time.sleep(2)
        
    #         pin_inp = driver.find_element(By.XPATH,'//input[@id="zip"]')
    #         pin_inp.send_keys(pincode)

    #         pin_val =  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="form-row"]')))

    #         time.sleep(2)
    #         add_inp = driver.find_element(By.XPATH,'//textarea[@id="address1"]')
    #         add_inp.send_keys(address)

    
    #     except:
    #          print("trying to fill the address page after 1 sec")
    #          time.sleep(1)
     
     time.sleep(1) # for the save address button because some validation happens there
     
     for i in range(2):
        try:
              sav = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]")))
              #    print(sav.text)
              sav.click()
              print("tried hitting save")
        except:
              print("not able to hit save")
    #  get_em = driver.find_element(By.XPATH,"//div[@class = 'flex bg-[#fff] rounded px-2 my-5']/input")
    #   (4000)
    #  print(get_em.get_attribute("value"))
    #  get_add = driver.find_element(By.XPATH,'//div[@class="!text-[#1d1d1d] mt-2 max-w-[400px] "]/p[1]')
    #  print(get_add.text)
    #  get_phone = driver.find_element(By.XPATH,'//div[@class="select-address bg-[#fff] p-4 rounded"]//div[@class="!text-[#1d1d1d] mt-2 max-w-[400px] "]//p[3]')
    #   (4000)
    #  time.sleep(2)
     print("got to the order summary page")
    #  driver.refresh()
     time.sleep(1)
    #  print(driver.find_element(By.XPATH,'//h1[1]').text)

    #  print(driver.find_element(By.XPATH,'//div[@class="payment-mode py-4 bg-white-1 mt-5 p-4 rounded"]'))

    #  cod = driver.find_element(By.XPATH,'//div[contains(text(),"Cash On Delivery")]')
     cod = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[contains(text(),"Cash On Delivery")]')))
     cod.click()

     print("changed the payment to cash on delivery")

    #  for i in range(1):
    #        try:
    #              cod = driver.find_element(By.XPATH,'//div[@class="payment-mode py-4 bg-white-1 mt-5 p-4 rounded"]/div[2]')
    #              cod.click()  
    #        except:
    #              print("retrying after 1 second")
    #              time.sleep(1)


    #  coup = driver.find_element(By.XPATH,'//h2[contains(text(),"Got Coupon ?")]')
    #  try:
    #     fo = driver.find_element(By.XPATH,"//form")
    #  except:
    #     coup.click()
    #  fo = driver.find_element(By.XPATH,"//form")
    #  cou_in = driver.find_element(By.XPATH,"//input[@placeholder='Add Coupon']")
    #  cou_in.send_keys("welcome10")
    #  cou_sub = driver.find_element(By.XPATH,'//span[contains(text(),"Apply")]')
    #  cou_sub.click()    
    #  cou_suc = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Coupon applied successfully')]")))


    #  cod = driver.find_element(By.XPATH,'//div[class="bg-[#C19426] w-[18px] h-[18px] rounded-[50%] flex items-center justify-center "]')
    #  cod.click()
    #  print("clicked ")
    #  cod.release()
    #  print("released")
    #  time.sleep(1)
     ord = driver.find_element(By.XPATH,"//span[contains(text(),'Place order')]")
     ord.click()
     print("Order placed")
     end = time.time()
    #  print(" ######time######")
     print(end-start)

    #  time.sleep(1)
     driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "order successfully placed"}}')
     driver.quit()

     
    #  pay = driver.find_element(By.XPATH,"//div[@class='razorpay-backdrop']")
    #  print()
    #  pay.send_keys(phone)
    #  time.sleep(10)


   
    #  get_pin = driver.find_element(By.XPATH,'//div[@class="text-sm font-semibold text-[#1d1d1d] max-w-[400px]"]')
    #  l=get_pin.text.split()
    #  print(get_em.get_attribute("value"))

    #  if get_em.get_attribute("value")==mail and get_add.text == address and get_phone.text==phone and l[len(l)-1]==pincode and l[2]==first_name:
    #         print("successfully order summary summary page got generated")

       
     



     
except:
        print("something went wrong")
        driver.execute_script(
             'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "order not placed"}}')
        driver.quit()

# <button class="!w-full md:w-[60%]"><span class="large-btn !w-full md:w-auto">Place order</span></button>


# <div class="submit-btn mb-5 !rounded md:mb-[100px]"><button type="submit" class="primary-btn large-btn ">Save</button></div>

# <div class="bg-[#C19426] w-[18px] h-[18px] rounded-[50%] flex items-center justify-center "><img alt="Check sign" src="/_next/static/media/checkout_right.9f012ed2.svg" width="13" height="11" decoding="async" data-nimg="1" loading="lazy" style="color: transparent;"></div>

# <div class="flex justify-between items-center cursor-pointer !cursor-default"><div><div class="text-[#1d1d1d] text-[14px] font-[600] ">Cash On Delivery </div></div><div class="bg-[#C19426] w-[18px] h-[18px] rounded-[50%] flex items-center justify-center "><img alt="Check sign" src="/_next/static/media/checkout_right.9f012ed2.svg" width="13" height="11" decoding="async" data-nimg="1" loading="lazy" style="color: transparent;"></div></div>


# <input class=" btn relative w-full text-left cursor-default bg-white" placeholder="India" id="headlessui-combobox-input-:r0:" role="combobox" type="text" aria-expanded="false" data-headlessui-state="">






