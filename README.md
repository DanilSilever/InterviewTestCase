На firefox все работает отлично. На хроме не работает только double_click, 
возможно из-за того что 2 клика выполняются почти моментально, 
добавив ожидание(time.sleep(1)) между кликами в файле pointer_actions.py в функции double_click(по пути:selenium/webdriver/common/actions/pointer_actions.py),
все заработало.

Start with addition option for browser:
"--browser_name=chrome" or "--browser_name=firefox"
