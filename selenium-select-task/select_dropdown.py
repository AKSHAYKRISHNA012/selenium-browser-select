from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# Step 1: Setup and Open Page
driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")
print("🔗 Opened: https://demoqa.com/select-menu")

time.sleep(2)  # Wait for page to load

# Step 2: Browser navigation
driver.back()
print("⬅️ Navigated back")
time.sleep(1)

driver.forward()
print("➡️ Navigated forward")
time.sleep(1)

driver.refresh()
print("🔄 Page refreshed")
time.sleep(1)

# Step 3: Interact with dropdowns using Select class

# Old style dropdown
old_style_dropdown = Select(driver.find_element("id", "oldSelectMenu"))

# Select by visible text
old_style_dropdown.select_by_visible_text("Purple")
print("✅ Selected 'Purple' using select_by_visible_text")

time.sleep(1)

# Select by value
old_style_dropdown.select_by_value("10")  # 10 = Purple
print("✅ Selected value '10' using select_by_value")

time.sleep(1)

# Select by index
old_style_dropdown.select_by_index(4)
print("✅ Selected index 4 using select_by_index")

# Done
time.sleep(2)
driver.quit()
print("🚪 Browser closed")
