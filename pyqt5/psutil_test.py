import psutil

processes = [p for p in psutil.process_iter(['pid', 'name', 'create_time'])]
processes_sorted = sorted(processes, key=lambda x: x.info['create_time'], reverse=True)

for process in processes_sorted:
    print(f"PID: {process.info['pid']} Name: {process.info['name']} Created: {process.create_time()}")

    if process.info['name'] == 'chrome.exe':
        process_id = process.info['pid']
        process = psutil.Process(process_id)
        process.terminate()
    elif process.info['name'] == 'chromedriver.exe':
        process_id = process.info['pid']
        process = psutil.Process(process_id)
        process.terminate()
        break