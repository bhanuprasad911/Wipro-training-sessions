import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15) # Increased timeout slightly

try:
    # 1. SWITCH TO IFRAME AND ENTER TEXT
    print("Navigating to Iframe page...")
    driver.get("https://the-internet.herokuapp.com/iframe")

    # FIX: Wait for the frame to be ready and switch immediately 
    # This replaces the need to 'click' the frame container
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr")))
    print("Switched into iframe.")

    # Target the editable body inside the iframe
    editor_body = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))
    
    # Scroll to it to ensure it's not intercepted by footer/overlays
    driver.execute_script("arguments[0].scrollIntoView(true);", editor_body)
    
    # Use JavaScript to clear and focus if standard clear() is blocked
    driver.execute_script("arguments[0].innerHTML = '';", editor_body)
    editor_body.send_keys("Bhanu - Automation Test Successful with JS Fix!")
    print("Step 1: Text entered in iframe successfully.")

    # 2. SWITCH BACK TO MAIN CONTENT
    driver.switch_to.default_content()
    print("Step 2: Back to main content.")

    # 3. OPEN A NEW TAB
    parent_window = driver.current_window_handle
    driver.execute_script("window.open('https://tutorialsninja.com/demo', '_blank');")
    print("Step 3: New tab opened.")

    # 4. SWITCH BETWEEN WINDOWS AND PRINT TITLES
    wait.until(lambda d: len(d.window_handles) > 1)
    all_windows = driver.window_handles
    
    for handle in all_windows:
        driver.switch_to.window(handle)
        print(f"Window Handle: {handle[:8]}... | Title: {driver.title}")

    # 5. CLOSE CHILD WINDOW AND RETURN TO PARENT
    for handle in all_windows:
        if handle != parent_window:
            driver.switch_to.window(handle)
            driver.close()
            print("Step 5: Closed child window.")

    driver.switch_to.window(parent_window)
    print(f"Final Context: {driver.title}")
    print("\nOverall Status: PASS")

except Exception as e:
    print(f"\nAn error occurred: {e}")

finally:
    time.sleep(3)
    driver.quit()