
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
    "感谢分享，内容非常实用！",
    "楼主辛苦了，这个帖子质量很高！",
    "学习了，感谢楼主的详细讲解！",
    "支持一下，期待更多这样的好内容！",
    "这个教程太棒了，帮大忙了！",
    "收藏了，回头再仔细研究一下！",
    "楼主的技术真强，学到了不少！",
    "非常有价值的分享，感谢！",
    "这个思路很新颖，值得学习！",
    "感谢楼主无私分享，顶一个！",
    "内容很详细，适合新手入门！",
    "这个资源太实用了，谢谢！",
    "楼主厉害，期待你的更多作品！",
    "看了之后豁然开朗，感谢！",
    "支持原创内容，顶起来！",
    "楼主用心了，内容很棒！",
    "这篇帖子值得一看，推荐！",
    "受益匪浅，感谢楼主的分享！",
    "很棒的教程，学到了新技能！",
    "期待楼主更多干货分享！",
    "感谢解答，问题终于解决了！",
    "这个方法很实用，感谢提供！",
    "楼主的技术水平令人佩服！",
    "非常实用的内容，顶一个！",
    "支持一下，学到了不少新知识！",
    "这帖子质量很高，值得收藏！",
    "感谢楼主无私分享，辛苦了！",
    "思路很清晰，学到了很多！",
    "大佬的经验分享非常宝贵！",
    "收藏了，准备回头再看一遍！",
    "感谢提供这么好的学习资源！",
    "支持楼主，希望你继续加油！",
    "这篇教程讲解得很清晰，顶！",
    "楼主太强了，感谢你的分享！",
    "学到了一些新技巧，谢谢！",
    "这帖子太有用了，必须顶起来！",
    "感谢楼主，帮我解决了大问题！",
    "内容很硬核，支持一下！",
    "非常棒的分享，学到了很多！",
    "楼主用心，内容质量很高！",
    "感谢大佬，期待你的更多分享！",
    "这篇干货值得收藏，谢谢！",
    "支持楼主，内容非常棒！",
    "学到了不少新东西，感谢！",
    "楼主辛苦了，必须顶一个！",
    "这个教程太实用了，感谢分享！",
    "楼主的技术真高超，学到了！",
    "非常有帮助的内容，顶！",
    "感谢楼主，期待你的新作！",
    "这个帖子写得很好，值得推荐！",
    "内容很丰富，学到了不少！",
    "楼主分享的经验很实用，谢谢！",
    "收藏了，准备仔细研究一下！",
    "感谢提供这么好的技术分享！",
    "支持楼主，希望你继续分享！",
    "这篇教程讲解得很透彻，顶！",
    "楼主太厉害了，感谢你的无私分享！",
    "学到了一些新的技术点，谢谢！",
    "这帖子太有价值了，顶起来！",
    "感谢楼主，帮我澄清了很多疑问！",
    "内容很扎实，支持一下！",
    "非常棒的技术分享，学到了！",
    "楼主用心，内容质量很赞！",
    "感谢大佬，期待你的更多干货！",
    "这篇帖子值得反复阅读，谢谢！",
    "支持楼主，内容非常实用！",
    "学到了很多新知识，感谢分享！",
    "楼主辛苦了，帖子写得太好了！",
    "这个教程简单易懂，感谢提供！",
    "楼主的技术实力真强，佩服！",
    "很有启发的内容，顶一个！",
    "感谢楼主，期待你的后续更新！",
    "这个帖子条理清晰，值得学习！",
    "内容很全面，学到了不少东西！",
    "楼主分享的技巧很实用，谢谢！",
    "收藏了，准备好好消化一下！",
    "感谢提供这么优质的学习资料！",
    "支持楼主，希望你保持创作！",
    "这篇教程深入浅出，顶！",
    "楼主真牛，感谢你的慷慨分享！",
    "学到了不少干货，谢谢楼主！",
    "这帖子太给力了，必须支持！",
    "感谢楼主，解决了我的困惑！",
    "内容很硬核，值得点赞！",
    "非常不错的分享，收获颇丰！",
    "楼主用心良苦，内容很精彩！",
    "感谢大佬，期待更多技术干货！",
    "这篇帖子太棒了，值得收藏！",
    "支持楼主，内容质量一流！",
    "学到了很多新思路，感谢！",
    "楼主辛苦了，帖子非常棒！",
    "这个教程实用性很强，谢谢！",
    "楼主的技术功底深厚，学到了！",
    "很有价值的内容，顶起来！",
    "感谢楼主，期待你的更多精彩！",
    "这个帖子写得太好了，推荐！",
    "内容详实，学到了很多东西！",
    "楼主分享的经验太珍贵了，谢谢！",
    "收藏了，准备深入研究一下！",
    "感谢提供这么优秀的技术内容！"
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
        is_chicken_leg = False
        
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

