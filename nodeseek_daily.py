# -- coding: utf-8 --
"""
Copyright (c) 2024 [Hosea]
Licensed under the MIT License.
See LICENSE file in the project root for full license information.
"""
import os
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import traceback
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

ns_random = os.environ.get("NS_RANDOM", "false")
cookie = os.environ.get("NS_COOKIE") or os.environ.get("COOKIE")
# 通过环境变量控制是否使用无头模式，默认为 True（无头模式）
headless = os.environ.get("HEADLESS", "true").lower() == "true"

randomInputStr = [
    "顶飞~",
    "路过打个酱油！",
    "绑定",
    "哎",
    "顶一下！",
    "不能沉",
    "顶",
    "顶个帖！",
    "UP",
    "路过留个大脚印子",
    "人工置顶",
    "助顶~下",
    "滋滋滋",
    "DT",
    "顶楼主",
    "路过顺便顶",
    "飘过",
    "支持一下哈",
    "路过逛逛",
    "顶支持",
    "帮顶下",
    "bd",
    "顶up主",
    "雁过留痕",
    "朕飘过",
    "路过转转！",
    "支持一下",
    "bangding",
    "帮NS坛友顶下",
    "+1:",
    "顶下坛友",
    "路过",
    "(￣▽￣)",
    "o_o ....",
    "支持楼主",
    ":xhj029:",
    "路过留个迹",
    "(ง •_•)ง",
    "O(∩_∩)O",
    "顶一个，加油！",
    "支持一下楼主！",
    "顶一个",
    "B楼主顶下",
    "我想加分，顺便顶下",
]

def click_sign_icon(driver):
    """
    尝试点击签到图标和试试手气按钮的通用方法
    """
    try:
        print("开始查找签到图标...")
        sign_icon = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//span[@title='签到']"))
        )
        print("找到签到图标，准备点击...")
        
        driver.execute_script("arguments[0].scrollIntoView(true);", sign_icon)
        time.sleep(0.5)
        
        print(f"签到图标元素: {sign_icon.get_attribute('outerHTML')}")
        
        try:
            sign_icon.click()
            print("签到图标点击成功")
        except Exception as click_error:
            print(f"点击失败，尝试使用 JavaScript 点击: {str(click_error)}")
            driver.execute_script("arguments[0].click();", sign_icon)
        
        print("等待页面跳转...")
        time.sleep(5)
        
        print(f"当前页面URL: {driver.current_url}")
        
        try:
            click_button = None
            if ns_random.lower() == "true":
                click_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '试试手气')]"))
                )
            else:
                click_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '鸡腿 x 5')]"))
                )
            
            if click_button:
                click_button.click()
                print("完成试试手气点击")
            else:
                print("未找到试试手气按钮")
        except Exception as lucky_error:
            print(f"试试手气按钮点击失败或者签到过了: {str(lucky_error)}")
            
        return True
        
    except Exception as e:
        print(f"签到过程中出错:")
        print(f"错误类型: {type(e).__name__}")
        print(f"错误信息: {str(e)}")
        print(f"当前页面URL: {driver.current_url}")
        print(f"当前页面源码片段: {driver.page_source[:500]}...")
        print("详细错误信息:")
        traceback.print_exc()
        return False

def setup_driver_and_cookies():
    """
    初始化浏览器并设置cookie的通用方法
    返回: 设置好cookie的driver实例
    """
    try:
        cookie = os.environ.get("NS_COOKIE") or os.environ.get("COOKIE")
        headless = os.environ.get("HEADLESS", "true").lower() == "true"
        
        if not cookie:
            print("未找到cookie配置")
            return None
            
        print("开始初始化浏览器...")
        options = uc.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        # 明确指定 Chrome 可执行文件路径
        chrome_binary = os.environ.get("CHROME_BINARY", "/usr/bin/google-chrome")
        options.binary_location = chrome_binary
        print(f"使用 Chrome 可执行文件路径: {chrome_binary}")
        
        if headless:
            print("启用无头模式...")
            options.add_argument('--headless')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')
            options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        print("正在启动Chrome...")
        driver = uc.Chrome(options=options)
        
        if headless:
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            driver.set_window_size(1920, 1080)
        
        print("Chrome启动成功")
        
        print("正在设置cookie...")
        driver.get('https://www.nodeseek.com')
        time.sleep(5)  # 确保页面加载
        
        for cookie_item in cookie.split(';'):
            try:
                name, value = cookie_item.strip().split('=', 1)
                driver.add_cookie({
                    'name': name, 
                    'value': value, 
                    'domain': '.nodeseek.com',
                    'path': '/'
                })
            except Exception as e:
                print(f"设置cookie出错: {str(e)}")
                continue
        
        print("刷新页面...")
        driver.refresh()
        time.sleep(5)  # 增加等待时间
        
        return driver
        
    except Exception as e:
        print(f"设置浏览器和Cookie时出错: {str(e)}")
        print("详细错误信息:")
        print(traceback.format_exc())
        return None
        
def nodeseek_comment(driver):
    try:
        print("正在访问交易区...")
        target_url = 'https://www.nodeseek.com/categories/trade'
        driver.get(target_url)
        print("等待页面加载...")
        
        posts = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.post-list-item'))
        )
        print(f"成功获取到 {len(posts)} 个帖子")
        
        valid_posts = [post for post in posts if not post.find_elements(By.CSS_SELECTOR, '.pined')]
        num_posts = min(20, len(valid_posts))
        selected_posts = random.sample(valid_posts, num_posts)
        
        selected_urls = []
        for post in selected_posts:
            try:
                post_link = post.find_element(By.CSS_SELECTOR, '.post-title a')
                selected_urls.append(post_link.get_attribute('href'))
            except:
                continue
        
        commented_urls = set()
        is_chicken_leg = True
        
        for i, post_url in enumerate(selected_urls):
            if post_url in commented_urls:
                print(f"帖子 {post_url} 已评论，跳过")
                continue
                
            try:
                print(f"正在处理第 {i+1} 个帖子: {post_url}")
                driver.get(post_url)
                
                if not is_chicken_leg:
                    is_chicken_leg = click_chicken_leg(driver)
                
                editor = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.CodeMirror'))
                )
                
                editor.click()
                time.sleep(0.5)
                input_text = random.choice(randomInputStr)
                actions = ActionChains(driver)
                for char in input_text:
                    actions.send_keys(char)
                    actions.pause(random.uniform(0.1, 0.3))
                actions.perform()
                
                time.sleep(2)
                
                submit_button = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'submit') and contains(@class, 'btn') and contains(text(), '发布评论')]"))
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
                time.sleep(0.5)
                submit_button.click()
                
                print(f"已在帖子 {post_url} 中完成评论")
                commented_urls.add(post_url)
                driver.get(target_url)
                time.sleep(random.uniform(5, 15))
                
            except Exception as e:
                print(f"处理帖子 {post_url} 时出错: {str(e)}")
                continue
                
        print("NodeSeek评论任务完成")
                
    except Exception as e:
        print(f"NodeSeek评论出错: {str(e)}")
        print("详细错误信息:")
        print(traceback.format_exc())

def click_chicken_leg(driver):
    try:
        print("尝试点击加鸡腿按钮...")
        chicken_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="nsk-post"]//div[@title="加鸡腿"][1]'))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", chicken_btn)
        time.sleep(0.5)
        chicken_btn.click()
        print("加鸡腿按钮点击成功")
        
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.msc-confirm'))
        )
        
        try:
            error_title = driver.find_element(By.XPATH, "//h3[contains(text(), '该评论创建于7天前')]")
            if error_title:
                print("该帖子超过7天，无法加鸡腿")
                ok_btn = driver.find_element(By.CSS_SELECTOR, '.msc-confirm .msc-ok')
                ok_btn.click()
                return False
        except:
            ok_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.msc-confirm .msc-ok'))
            )
            ok_btn.click()
            print("确认加鸡腿成功")
        
        WebDriverWait(driver, 5).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.msc-overlay'))
        )
        time.sleep(1)
        
        return True
        
    except Exception as e:
        print(f"加鸡腿操作失败: {str(e)}")
        return False

if __name__ == "__main__":
    print("开始执行NodeSeek评论脚本...")
    driver = setup_driver_and_cookies()
    if not driver:
        print("浏览器初始化失败")
        exit(1)
    nodeseek_comment(driver)
    click_sign_icon(driver)
    print("脚本执行完成")
