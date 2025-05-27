
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

ns_random = os.environ.get("NS_RANDOM","false")
cookie = os.environ.get("NS_COOKIE") or os.environ.get("COOKIE")
# 通过环境变量控制是否使用无头模式，默认为 True（无头模式）
headless = os.environ.get("HEADLESS", "true").lower() == "true"

# ... (其他代码保持不变)

randomInputStr = [
    "好帖子，顶！",
    "支持一下！",
    "路过打个酱油！",
    "赞一个！",
    "路过支持！",
    "顶一下！",
    "支持好帖！",
    "路过看看！",
    "点赞支持！",
    "顶个帖！",
    "支持楼主！",
    "路过留个脚印！",
    "赞好内容！",
    "顶起来！",
    "支持大佬！",
    "路过打个招呼！",
    "点赞一下！",
    "顶好帖子！",
    "支持原创！",
    "路过顺便顶！",
    "赞个帖子！",
    "支持一下哈！",
    "路过逛逛！",
    "顶支持！",
    "支持真不错！",
    "路过坐坐！",
    "赞个好帖！",
    "顶楼主！",
    "支持加油！",
    "路过刷刷！",
    "赞好分享！",
    "顶个好帖！",
    "支持兄弟！",
    "路过聊聊！",
    "赞支持！",
    "顶个内容！",
    "支持真棒！",
    "路过转转！",
    "赞个楼主！",
    "顶好帖子啦！",
    "支持一下哦！",
    "路过看看哈！",
    "赞个好内容！",
    "顶支持下！",
    "支持大佬帖！",
    "路过留个影！",
    "赞个好分享！",
    "顶个好帖子哦！",
    "支持朋友！",
    "路过打卡！",
    "赞支持一下！",
    "顶个真不错！",
    "支持楼主啦！",
    "路过逛逛哦！",
    "赞个好帖啦！",
    "顶支持兄弟！",
    "支持真厉害！",
    "路过转一圈！",
    "赞个好内容哦！",
    "顶个好分享！",
    "支持一下兄弟！",
    "路过聊两句！",
    "赞支持楼主！",
    "顶个好帖子哈！",
    "支持大佬哦！",
    "路过留个言！",
    "赞个好帖子啦！",
    "顶支持一下！",
    "支持真给力！",
    "路过刷一刷！",
    "赞个好内容啦！",
    "顶个好分享哦！",
    "支持朋友啦！",
    "路过打个照！",
    "赞支持大佬！",
    "顶个好帖子哦啦！",
    "支持一下哈啦！",
    "路过看看哦！",
    "赞个好帖哈！",
    "顶支持兄弟啦！",
    "支持真不错哦！",
    "路过转转啦！",
    "赞个好内容哈！",
    "顶个好分享啦！",
    "支持楼主哦！",
    "路过聊聊啦！",
    "赞支持一下哦！",
    "顶个好帖子啦啦！",
    "支持大佬哈！",
    "路过留个迹！",
    "赞个好帖子哦哈！",
    "顶支持朋友！",
    "支持真棒啦！",
    "路过逛逛哈！",
    "赞个好内容哦啦！",
    "顶个好分享哈！",
    "支持兄弟哦！",
    "路过打个卡！",
    "赞支持楼主啦！",
    "顶个好帖子哈啦！",
    "不错，点赞！",
    "值得一看！",
    "好内容，顶！",
    "挺有意思！",
    "楼主棒棒的！",
    "很有趣，顶！",
    "好帖，点赞！",
    "不错，支持！",
    "顶一个，加油！",
    "好看，顶！",
    "支持好帖子！",
    "楼主厉害！",
    "支持一下楼主！",
    "感谢好分享！",
    "值得顶！",
    "楼主辛苦，顶！",
    "感谢你的帖子！",
    "好帖，支持！",
    "顶起来，加油！",
    "不错，顶一个！",
    "支持楼主，赞！",
    "顶帖，加油！",
    "好内容，值得顶！",
    "支持一下，赞！",
    "不错，顶起来！",
    "感谢分享，赞！",
    "好帖，顶一个！",
    "支持楼主，加油！",
    "感谢你的内容！",
    "顶一个，好帖！",
    "支持原创内容！",
    "不错，值得点赞！",
    "感谢分享，顶！",
    "好内容，点赞！",
    "支持楼主好帖！",
    "感谢你的发布！",
    "楼主辛苦，赞！",
    "感谢好内容！",
    "好帖，值得支持！",
    "感谢楼主，顶！",
    "不错，加油！",
    "感谢分享内容！",
    "好帖子，顶起来！",
    "感谢你的努力！",
    "好内容，支持！",
    "楼主厉害，点赞！",
    "感谢发布好帖！",
    "好分享，顶！",
    "感谢楼主分享！",
    "不错，值得顶！",
    "支持好内容！",
    "感谢你的好帖！",
    "好分享，顶起来！",
    "支持原创，赞！",
    "感谢你的贡献！"
]
def click_sign_icon(driver):
    """
    尝试点击签到图标和试试手气按钮的通用方法
    """
    try:
        print("开始查找签到图标...")
        # 使用更精确的选择器定位签到图标
        sign_icon = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//span[@title='签到']"))
        )
        print("找到签到图标，准备点击...")
        
        # 确保元素可见和可点击
        driver.execute_script("arguments[0].scrollIntoView(true);", sign_icon)
        time.sleep(0.5)
        
        # 打印元素信息
        print(f"签到图标元素: {sign_icon.get_attribute('outerHTML')}")
        
        # 尝试点击
        try:
            
            
            sign_icon.click()
            print("签到图标点击成功")
        except Exception as click_error:
            print(f"点击失败，尝试使用 JavaScript 点击: {str(click_error)}")
            driver.execute_script("arguments[0].click();", sign_icon)
        
        print("等待页面跳转...")
        time.sleep(5)
        
        # 打印当前URL
        print(f"当前页面URL: {driver.current_url}")
        
        # 点击"试试手气"按钮
        try:
            click_button:None
            
            if ns_random:
                click_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '试试手气')]"))
            )
            else:
                click_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '鸡腿 x 5')]"))
            )
            
            click_button.click()
            print("完成试试手气点击")
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
        
        if headless:
            print("启用无头模式...")
            options.add_argument('--headless')
            # 添加以下参数来绕过 Cloudflare 检测
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')
            # 设置 User-Agent
            options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        print("正在启动Chrome...")
        driver = uc.Chrome(options=options)
        
        if headless:
            # 执行 JavaScript 来修改 webdriver 标记
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            driver.set_window_size(1920, 1080)
        
        print("Chrome启动成功")
        
        print("正在设置cookie...")
        driver.get('https://www.nodeseek.com')
        
        # 等待页面加载完成
        time.sleep(5)
        
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
        
        # 获取帖子列表
        posts = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.post-list-item'))
        )
        print(f"成功获取到 {len(posts)} 个帖子")
        
        # 过滤掉置顶帖
        valid_posts = [post for post in posts if not post.find_elements(By.CSS_SELECTOR, '.pined')]
        
        # 随机选择最多20个帖子
        num_posts = min(20, len(valid_posts))
        selected_posts = random.sample(valid_posts, num_posts)
        
        # 获取帖子URL
        selected_urls = []
        for post in selected_posts:
            try:
                post_link = post.find_element(By.CSS_SELECTOR, '.post-title a')
                selected_urls.append(post_link.get_attribute('href'))
            except:
                continue
        
        # 记录已评论的帖子
        commented_urls = set()
        is_chicken_leg = True
        
        # 处理每个帖子
        for i, post_url in enumerate(selected_urls):
            if post_url in commented_urls:
                print(f"帖子 {post_url} 已评论，跳过")
                continue
                
            try:
                print(f"正在处理第 {i+1} 个帖子: {post_url}")
                driver.get(post_url)
                
                # 处理加鸡腿（假设已有函数）
                if not is_chicken_leg:
                    is_chicken_leg = click_chicken_leg(driver)
                
                # 等待编辑器加载
                editor = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.CodeMirror'))
                )
                
                # 输入随机评论
                editor.click()
                time.sleep(0.5)
                input_text = random.choice(randomInputStr)  # 假设 randomInputStr 已定义
                actions = ActionChains(driver)
                for char in input_text:
                    actions.send_keys(char)
                    actions.pause(random.uniform(0.1, 0.3))
                actions.perform()
                
                # 等待输入完成
                time.sleep(2)
                
                # 提交评论
                submit_button = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'submit') and contains(@class, 'btn') and contains(text(), '发布评论')]"))
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
                time.sleep(0.5)
                submit_button.click()
                
                print(f"已在帖子 {post_url} 中完成评论")
                commented_urls.add(post_url)  # 记录已评论
                
                # 返回交易区
                driver.get(target_url)
                time.sleep(random.uniform(2, 5))
                
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
        
        # 等待确认对话框出现
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.msc-confirm'))
        )
        
        # 检查是否是7天前的帖子
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
            
        # 等待确认对话框消失
        WebDriverWait(driver, 5).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.msc-overlay'))
        )
        time.sleep(1)  # 额外等待以确保对话框完全消失
        
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
    # while True:
    #     time.sleep(1)

